import base64
import json
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import requests


class EbayApiError(Exception):
    pass


def _env(name: str, default: Optional[str] = None) -> str:
    v = os.getenv(name, default)
    if v is None or v == "":
        raise EbayApiError(f"Missing required environment variable: {name}")
    return v


def _is_sandbox() -> bool:
    return os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper() != "PRODUCTION"


def _base_url(media: bool = False) -> str:
    if _is_sandbox():
        return "https://apim.sandbox.ebay.com" if media else "https://api.sandbox.ebay.com"
    return "https://apim.ebay.com" if media else "https://api.ebay.com"


@dataclass
class _Token:
    access_token: str
    expires_at: float


class EbayClient:
    """Minimal eBay REST client with OAuth token caching.

    Supports:
      - client credentials token (application token)
      - refresh token flow (user token)

    Docs for token endpoints are not included in this workspace; we implement the standard eBay OAuth endpoints.
    """

    def __init__(self) -> None:
        self.app_id = _env("EBAY_APP_ID")
        self.cert_id = _env("EBAY_CERT_ID")
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN")
        self._app_token: Optional[_Token] = None
        self._user_token: Optional[_Token] = None

    def _oauth_base(self) -> str:
        return "https://api.sandbox.ebay.com" if _is_sandbox() else "https://api.ebay.com"

    def _basic_auth_header(self) -> str:
        raw = f"{self.app_id}:{self.cert_id}".encode("utf-8")
        return "Basic " + base64.b64encode(raw).decode("ascii")

    def _token_valid(self, tok: Optional[_Token]) -> bool:
        return tok is not None and (tok.expires_at - time.time()) > 30

    def get_app_token(self, scope: str = "https://api.ebay.com/oauth/api_scope") -> str:
        if self._token_valid(self._app_token):
            return self._app_token.access_token

        url = self._oauth_base() + "/identity/v1/oauth2/token"
        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "client_credentials",
            "scope": scope,
        }
        r = requests.post(url, headers=headers, data=data, timeout=60)
        if r.status_code >= 400:
            return self._as_error(r)
        payload = r.json()
        access_token = payload.get("access_token")
        expires_in = float(payload.get("expires_in", 0))
        if not access_token:
            raise EbayApiError(f"OAuth response missing access_token: {payload}")
        self._app_token = _Token(access_token=access_token, expires_at=time.time() + expires_in)
        return access_token

    def get_user_token(self, scope: str) -> str:
        if self._token_valid(self._user_token):
            return self._user_token.access_token
        if not self.refresh_token:
            raise EbayApiError("Missing EBAY_REFRESH_TOKEN for user-scoped API")

        url = self._oauth_base() + "/identity/v1/oauth2/token"
        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "scope": scope,
        }
        r = requests.post(url, headers=headers, data=data, timeout=60)
        if r.status_code >= 400:
            return self._as_error(r)
        payload = r.json()
        access_token = payload.get("access_token")
        expires_in = float(payload.get("expires_in", 0))
        if not access_token:
            raise EbayApiError(f"OAuth response missing access_token: {payload}")
        self._user_token = _Token(access_token=access_token, expires_at=time.time() + expires_in)
        return access_token

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        marketplace_id: Optional[str] = None,
        media: bool = False,
        user_scope: Optional[str] = None,
        raw_body: Any = None,
        content_type: Optional[str] = None,
    ) -> Any:
        url = _base_url(media=media) + path

        hdrs: Dict[str, str] = {"Accept": "application/json"}
        if headers:
            hdrs.update(headers)
        if marketplace_id:
            hdrs["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

        if user_scope:
            token = self.get_user_token(user_scope)
        else:
            # default app scope works for many endpoints; specific scopes are passed by tools when needed
            token = self.get_app_token()
        if isinstance(token, dict):
            return token
        hdrs["Authorization"] = f"Bearer {token}"

        data = None
        json_payload = None
        if raw_body is not None:
            data = raw_body
            if content_type:
                hdrs["Content-Type"] = content_type
        elif json_body is not None:
            json_payload = json_body
            hdrs.setdefault("Content-Type", "application/json")

        r = requests.request(method, url, params=params, json=json_payload, data=data, headers=hdrs, timeout=120)
        if r.status_code >= 400:
            return self._as_error(r)
        if r.status_code == 204:
            return {"status": 204}
        ctype = r.headers.get("Content-Type", "")
        if "application/json" in ctype:
            return r.json()
        # fallback
        return {"status": r.status_code, "content_type": ctype, "text": r.text}

    def _as_error(self, r: requests.Response) -> Dict[str, Any]:
        try:
            payload = r.json()
        except Exception:
            payload = {"message": r.text}
        return {
            "error": {
                "status": r.status_code,
                "reason": r.reason,
                "url": r.url,
                "details": payload,
            }
        }
