import os
import time
from typing import Any, Dict, Optional

import requests


class EbayOAuthError(Exception):
    pass


class EbayClient:
    """Minimal eBay REST client with refresh-token OAuth for Sell APIs."""

    def __init__(
        self,
        app_id: Optional[str] = None,
        cert_id: Optional[str] = None,
        refresh_token: Optional[str] = None,
        environment: Optional[str] = None,
        timeout_s: int = 60,
    ):
        self.app_id = app_id or os.getenv("EBAY_APP_ID")
        self.cert_id = cert_id or os.getenv("EBAY_CERT_ID")
        self.refresh_token = refresh_token or os.getenv("EBAY_REFRESH_TOKEN")
        self.environment = (environment or os.getenv("EBAY_ENVIRONMENT") or "SANDBOX").upper()
        self.timeout_s = timeout_s

        if not self.app_id or not self.cert_id or not self.refresh_token:
            raise EbayOAuthError(
                "Missing EBAY_APP_ID, EBAY_CERT_ID, or EBAY_REFRESH_TOKEN environment variables"
            )

        self.base_url = (
            "https://api.sandbox.ebay.com" if self.environment == "SANDBOX" else "https://api.ebay.com"
        )

        self._access_token: Optional[str] = None
        self._access_token_expiry: float = 0.0

    def _token_endpoint(self) -> str:
        # eBay OAuth token endpoint is the same for sandbox/prod domains.
        return f"{self.base_url}/identity/v1/oauth2/token"

    def _basic_auth_header(self) -> str:
        import base64

        raw = f"{self.app_id}:{self.cert_id}".encode("utf-8")
        return "Basic " + base64.b64encode(raw).decode("ascii")

    def get_access_token(self, force_refresh: bool = False) -> str:
        now = time.time()
        if not force_refresh and self._access_token and now < (self._access_token_expiry - 30):
            return self._access_token

        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            # Scope is optional for refresh flow if token already has scopes.
            # We omit to avoid mismatches across Sell APIs.
        }
        resp = requests.post(self._token_endpoint(), headers=headers, data=data, timeout=self.timeout_s)
        if resp.status_code >= 400:
            raise EbayOAuthError(f"OAuth token error {resp.status_code}: {resp.text}")
        payload = resp.json()
        self._access_token = payload.get("access_token")
        expires_in = payload.get("expires_in", 7200)
        self._access_token_expiry = now + float(expires_in)
        if not self._access_token:
            raise EbayOAuthError(f"OAuth token response missing access_token: {payload}")
        return self._access_token

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Any = None,
        headers: Optional[Dict[str, str]] = None,
        accept: str = "application/json",
        content_language: Optional[str] = None,
    ) -> Dict[str, Any]:
        url = self.base_url + path
        token = self.get_access_token()
        req_headers: Dict[str, str] = {
            "Authorization": f"Bearer {token}",
            "Accept": accept,
        }
        if json is not None:
            req_headers.setdefault("Content-Type", "application/json")
        if content_language:
            req_headers["Content-Language"] = content_language
        if headers:
            req_headers.update(headers)

        resp = requests.request(
            method.upper(),
            url,
            params=params,
            json=json,
            headers=req_headers,
            timeout=self.timeout_s,
        )

        # eBay often returns empty body for 204
        if resp.status_code == 204:
            return {"status": 204}

        ctype = resp.headers.get("Content-Type", "")
        body: Any
        if "application/json" in ctype:
            try:
                body = resp.json()
            except Exception:
                body = {"raw": resp.text}
        else:
            body = {"raw": resp.text}

        if resp.status_code >= 400:
            return {
                "error": True,
                "status": resp.status_code,
                "body": body,
            }
        return body if isinstance(body, dict) else {"data": body}
