import os
import time
from typing import Any, Dict, Optional

import requests


class EbayClient:
    def __init__(
        self,
        app_id: Optional[str] = None,
        cert_id: Optional[str] = None,
        refresh_token: Optional[str] = None,
        environment: Optional[str] = None,
    ):
        self.app_id = app_id or os.getenv("EBAY_APP_ID")
        self.cert_id = cert_id or os.getenv("EBAY_CERT_ID")
        self.refresh_token = refresh_token or os.getenv("EBAY_REFRESH_TOKEN")
        self.environment = (environment or os.getenv("EBAY_ENVIRONMENT") or "SANDBOX").upper()

        if self.environment not in ("SANDBOX", "PRODUCTION"):
            self.environment = "SANDBOX"

        self.base_url = "https://api.sandbox.ebay.com" if self.environment == "SANDBOX" else "https://api.ebay.com"

        self._access_token: Optional[str] = None
        self._access_token_exp: float = 0.0

    def _token_endpoint(self) -> str:
        return f"{self.base_url}/identity/v1/oauth2/token"

    def _basic_auth_header(self) -> str:
        # eBay expects HTTP Basic with base64(client_id:client_secret)
        import base64

        if not self.app_id or not self.cert_id:
            raise ValueError("Missing EBAY_APP_ID or EBAY_CERT_ID")
        raw = f"{self.app_id}:{self.cert_id}".encode("utf-8")
        return "Basic " + base64.b64encode(raw).decode("ascii")

    def get_access_token(self, force: bool = False) -> str:
        now = time.time()
        if not force and self._access_token and now < (self._access_token_exp - 30):
            return self._access_token

        if not self.refresh_token:
            raise ValueError("Missing EBAY_REFRESH_TOKEN")

        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            # scope is optional for refresh_token grant; omit to use token's granted scopes
        }
        resp = requests.post(self._token_endpoint(), headers=headers, data=data, timeout=60)
        if resp.status_code >= 400:
            raise RuntimeError(f"Token request failed: {resp.status_code} {resp.text}")
        payload = resp.json()
        self._access_token = payload.get("access_token")
        expires_in = payload.get("expires_in", 7200)
        self._access_token_exp = now + float(expires_in)
        if not self._access_token:
            raise RuntimeError("Token response missing access_token")
        return self._access_token

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        accept: str = "application/json",
        content_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        url = self.base_url + path
        token = self.get_access_token()
        h = {
            "Authorization": f"Bearer {token}",
            "Accept": accept,
        }
        if content_type:
            h["Content-Type"] = content_type
        if headers:
            h.update(headers)

        resp = requests.request(method.upper(), url, params=params, json=json, headers=h, timeout=90)
        if resp.status_code == 204:
            return {"status": 204}

        # Try JSON; fall back to text
        try:
            body: Any = resp.json()
        except Exception:
            body = {"text": resp.text}

        if resp.status_code >= 400:
            return {
                "error": True,
                "status": resp.status_code,
                "body": body,
                "url": url,
                "method": method.upper(),
            }
        if isinstance(body, dict):
            body.setdefault("_status", resp.status_code)
            return body
        return {"_status": resp.status_code, "data": body}
