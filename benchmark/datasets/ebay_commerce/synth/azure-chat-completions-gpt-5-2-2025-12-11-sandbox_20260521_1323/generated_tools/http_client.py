import base64
import json
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import requests


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name)
    return v if v not in (None, "") else default


def _is_sandbox() -> bool:
    return (_env("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper() != "PRODUCTION"


def ebay_api_base_url(is_media: bool = False) -> str:
    if is_media:
        return "https://apim.sandbox.ebay.com" if _is_sandbox() else "https://apim.ebay.com"
    return "https://api.sandbox.ebay.com" if _is_sandbox() else "https://api.ebay.com"


@dataclass
class Token:
    access_token: str
    expires_at: float

    def valid(self) -> bool:
        return time.time() < self.expires_at - 30


class EbayOAuth:
    def __init__(self) -> None:
        self.app_id = _env("EBAY_APP_ID")
        self.cert_id = _env("EBAY_CERT_ID")
        self.refresh_token = _env("EBAY_REFRESH_TOKEN")
        self._app_token: Optional[Token] = None
        self._user_token: Optional[Token] = None

    def _basic_auth_header(self) -> str:
        if not self.app_id or not self.cert_id:
            raise ValueError("Missing EBAY_APP_ID or EBAY_CERT_ID")
        raw = f"{self.app_id}:{self.cert_id}".encode("utf-8")
        return "Basic " + base64.b64encode(raw).decode("ascii")

    def _token_url(self) -> str:
        # OAuth is on api.ebay.com even for sandbox; sandbox uses api.sandbox.ebay.com
        base = "https://api.sandbox.ebay.com" if _is_sandbox() else "https://api.ebay.com"
        return base + "/identity/v1/oauth2/token"

    def get_app_token(self, scope: Optional[str] = None) -> str:
        if self._app_token and self._app_token.valid():
            return self._app_token.access_token
        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "client_credentials",
        }
        if scope:
            data["scope"] = scope
        r = requests.post(self._token_url(), headers=headers, data=data, timeout=60)
        if r.status_code >= 400:
            return self._raise_or_error("oauth_app_token", r)
        payload = r.json()
        access_token = payload.get("access_token")
        expires_in = float(payload.get("expires_in", 0))
        if not access_token:
            raise ValueError(f"OAuth response missing access_token: {payload}")
        self._app_token = Token(access_token=access_token, expires_at=time.time() + expires_in)
        return access_token

    def get_user_token(self, scope: Optional[str] = None) -> str:
        if self._user_token and self._user_token.valid():
            return self._user_token.access_token
        if not self.refresh_token:
            raise ValueError("Missing EBAY_REFRESH_TOKEN")
        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
        }
        if scope:
            data["scope"] = scope
        r = requests.post(self._token_url(), headers=headers, data=data, timeout=60)
        if r.status_code >= 400:
            return self._raise_or_error("oauth_user_token", r)
        payload = r.json()
        access_token = payload.get("access_token")
        expires_in = float(payload.get("expires_in", 0))
        if not access_token:
            raise ValueError(f"OAuth response missing access_token: {payload}")
        self._user_token = Token(access_token=access_token, expires_at=time.time() + expires_in)
        return access_token

    @staticmethod
    def _raise_or_error(context: str, r: requests.Response) -> str:
        try:
            body = r.json()
        except Exception:
            body = r.text
        raise RuntimeError(f"{context} failed: HTTP {r.status_code}: {body}")


class EbayClient:
    def __init__(self) -> None:
        self.oauth = EbayOAuth()

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        is_media: bool = False,
        marketplace_id: Optional[str] = None,
        scope: Optional[str] = None,
        user_token: bool = False,
        raw_body: Any = None,
        content_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        url = ebay_api_base_url(is_media=is_media) + path
        h: Dict[str, str] = {"Accept": "application/json"}
        if headers:
            h.update({k: v for k, v in headers.items() if v is not None})
        if marketplace_id:
            h.setdefault("X-EBAY-C-MARKETPLACE-ID", marketplace_id)

        try:
            token = self.oauth.get_user_token(scope) if user_token else self.oauth.get_app_token(scope)
        except Exception as e:
            return {"error": str(e)}
        h["Authorization"] = f"Bearer {token}"

        data = None
        json_payload = None
        if raw_body is not None:
            data = raw_body
            if content_type:
                h["Content-Type"] = content_type
        elif json_body is not None:
            json_payload = json_body
            h.setdefault("Content-Type", "application/json")

        try:
            r = requests.request(method, url, params=params, json=json_payload, data=data, headers=h, timeout=90)
        except Exception as e:
            return {"error": f"request_failed: {e}", "url": url}

        if r.status_code == 204:
            return {"status": 204}

        ct = (r.headers.get("Content-Type") or "").lower()
        parsed: Any
        if "application/json" in ct:
            try:
                parsed = r.json()
            except Exception:
                parsed = {"raw": r.text}
        else:
            parsed = {"raw": r.text}

        if r.status_code >= 400:
            return {
                "error": "http_error",
                "status": r.status_code,
                "url": url,
                "response": parsed,
            }
        if isinstance(parsed, dict):
            parsed.setdefault("_http", {"status": r.status_code})
            return parsed
        return {"data": parsed, "_http": {"status": r.status_code}}
