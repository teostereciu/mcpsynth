import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


class EbayOAuthError(Exception):
    pass


class EbayClient:
    """Minimal eBay REST client for Sell APIs using refresh-token OAuth.

    Tools should call request_json() with a concrete method/path.
    """

    def __init__(
        self,
        app_id: Optional[str] = None,
        cert_id: Optional[str] = None,
        refresh_token: Optional[str] = None,
        environment: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self.app_id = app_id or os.getenv("EBAY_APP_ID", "")
        self.cert_id = cert_id or os.getenv("EBAY_CERT_ID", "")
        self.refresh_token = refresh_token or os.getenv("EBAY_REFRESH_TOKEN", "")
        self.environment = (environment or os.getenv("EBAY_ENVIRONMENT", "SANDBOX")).upper()
        self.timeout = timeout

        self._access_token: Optional[str] = None
        self._access_token_exp: float = 0.0

    @property
    def base_url(self) -> str:
        return "https://api.sandbox.ebay.com" if self.environment != "PRODUCTION" else "https://api.ebay.com"

    @property
    def oauth_base_url(self) -> str:
        return "https://api.sandbox.ebay.com" if self.environment != "PRODUCTION" else "https://api.ebay.com"

    def _basic_auth_header(self) -> str:
        if not self.app_id or not self.cert_id:
            raise EbayOAuthError("Missing EBAY_APP_ID or EBAY_CERT_ID")
        import base64

        token = base64.b64encode(f"{self.app_id}:{self.cert_id}".encode("utf-8")).decode("ascii")
        return f"Basic {token}"

    def get_access_token(self, force: bool = False) -> str:
        now = time.time()
        if not force and self._access_token and now < (self._access_token_exp - 30):
            return self._access_token

        if not self.refresh_token:
            raise EbayOAuthError("Missing EBAY_REFRESH_TOKEN")

        url = f"{self.oauth_base_url}/identity/v1/oauth2/token"
        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            # Scope is optional for refresh-token grant; if omitted, eBay returns token with original scopes.
        }
        resp = requests.post(url, headers=headers, data=data, timeout=self.timeout)
        if resp.status_code >= 400:
            return self._as_error(resp, prefix="oauth")  # type: ignore[return-value]

        payload = resp.json()
        token = payload.get("access_token")
        expires_in = payload.get("expires_in", 0)
        if not token:
            raise EbayOAuthError(f"OAuth response missing access_token: {payload}")
        self._access_token = token
        self._access_token_exp = now + float(expires_in or 0)
        return token

    def _as_error(self, resp: requests.Response, prefix: str = "request") -> Dict[str, Any]:
        try:
            body = resp.json()
        except Exception:
            body = resp.text
        return {
            "error": f"{prefix}_failed",
            "status": resp.status_code,
            "body": body,
            "headers": dict(resp.headers),
        }

    def request_json(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        accept: str = "application/json",
        content_language: Optional[str] = None,
        content_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        token = self.get_access_token()
        url = f"{self.base_url}{path}"
        h: Dict[str, str] = {
            "Authorization": f"Bearer {token}",
            "Accept": accept,
        }
        if content_language:
            h["Content-Language"] = content_language
        if content_type:
            h["Content-Type"] = content_type
        if headers:
            h.update(headers)

        resp = requests.request(method.upper(), url, params=params, json=json, headers=h, timeout=self.timeout)

        if resp.status_code == 204:
            return {"status": 204, "body": None}
        if resp.status_code >= 400:
            return self._as_error(resp)
        try:
            return resp.json()
        except Exception:
            return {"status": resp.status_code, "body": resp.text}
