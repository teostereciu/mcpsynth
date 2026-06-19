import base64
import json
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import requests


class EbayApiError(Exception):
    pass


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name)
    return v if v not in (None, "") else default


def get_environment() -> str:
    return (_env("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()


def get_base_url(is_media: bool = False) -> str:
    env = get_environment()
    if env not in ("SANDBOX", "PRODUCTION"):
        env = "SANDBOX"
    if is_media:
        return "https://apim.sandbox.ebay.com" if env == "SANDBOX" else "https://apim.ebay.com"
    return "https://api.sandbox.ebay.com" if env == "SANDBOX" else "https://api.ebay.com"


@dataclass
class Token:
    access_token: str
    expires_at: float

    def is_valid(self, skew_seconds: int = 60) -> bool:
        return time.time() + skew_seconds < self.expires_at


class EbayOAuth:
    def __init__(self):
        self.client_id = _env("EBAY_APP_ID")
        self.client_secret = _env("EBAY_CERT_ID")
        self.refresh_token = _env("EBAY_REFRESH_TOKEN")
        if not self.client_id or not self.client_secret:
            raise EbayApiError("Missing EBAY_APP_ID or EBAY_CERT_ID environment variables")

        self._app_token: Optional[Token] = None
        self._user_token: Optional[Token] = None

    def _basic_auth_header(self) -> str:
        raw = f"{self.client_id}:{self.client_secret}".encode("utf-8")
        return "Basic " + base64.b64encode(raw).decode("ascii")

    def _token_url(self) -> str:
        # OAuth is on api.ebay.com even for media; sandbox uses api.sandbox.ebay.com
        return get_base_url(is_media=False) + "/identity/v1/oauth2/token"

    def get_app_token(self, scope: str) -> str:
        if self._app_token and self._app_token.is_valid():
            return self._app_token.access_token

        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "client_credentials",
            "scope": scope,
        }
        r = requests.post(self._token_url(), headers=headers, data=data, timeout=60)
        if r.status_code >= 400:
            raise EbayApiError(f"OAuth client_credentials failed: {r.status_code} {r.text}")
        payload = r.json()
        expires_in = float(payload.get("expires_in", 0))
        self._app_token = Token(payload["access_token"], time.time() + expires_in)
        return self._app_token.access_token

    def get_user_token(self, scope: str) -> str:
        if not self.refresh_token:
            raise EbayApiError("Missing EBAY_REFRESH_TOKEN environment variable")
        if self._user_token and self._user_token.is_valid():
            return self._user_token.access_token

        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "scope": scope,
        }
        r = requests.post(self._token_url(), headers=headers, data=data, timeout=60)
        if r.status_code >= 400:
            raise EbayApiError(f"OAuth refresh_token failed: {r.status_code} {r.text}")
        payload = r.json()
        expires_in = float(payload.get("expires_in", 0))
        self._user_token = Token(payload["access_token"], time.time() + expires_in)
        return self._user_token.access_token


class EbayClient:
    def __init__(self):
        self.oauth = EbayOAuth()

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        scope: Optional[str] = None,
        user: bool = False,
        is_media: bool = False,
        raw_body: Any = None,
    ) -> Dict[str, Any]:
        url = get_base_url(is_media=is_media) + path
        hdrs: Dict[str, str] = {"Accept": "application/json"}
        if headers:
            hdrs.update({k: v for k, v in headers.items() if v is not None})

        if scope:
            token = self.oauth.get_user_token(scope) if user else self.oauth.get_app_token(scope)
            hdrs["Authorization"] = f"Bearer {token}"

        try:
            r = requests.request(
                method.upper(),
                url,
                params=params,
                json=json_body,
                data=raw_body,
                headers=hdrs,
                timeout=60,
            )
        except requests.RequestException as e:
            return {"error": str(e), "url": url}

        content_type = r.headers.get("Content-Type", "")
        if r.status_code == 204:
            return {"status": 204}

        if "application/json" in content_type:
            try:
                data = r.json()
            except Exception:
                data = {"raw": r.text}
        else:
            data = {"raw": r.text}

        if r.status_code >= 400:
            return {
                "error": "ebay_api_error",
                "status": r.status_code,
                "url": url,
                "response": data,
            }
        return data
