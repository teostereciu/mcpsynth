import os
import time
from typing import Any, Dict, Optional

import requests


class EbayBuyApiClient:
    """Minimal eBay Buy API client using OAuth2 client-credentials."""

    def __init__(
        self,
        app_id: Optional[str] = None,
        cert_id: Optional[str] = None,
        environment: Optional[str] = None,
        timeout_s: float = 30.0,
    ):
        self.app_id = app_id or os.getenv("EBAY_APP_ID")
        self.cert_id = cert_id or os.getenv("EBAY_CERT_ID")
        self.environment = (environment or os.getenv("EBAY_ENVIRONMENT") or "SANDBOX").upper()
        self.timeout_s = timeout_s

        if not self.app_id or not self.cert_id:
            raise ValueError("EBAY_APP_ID and EBAY_CERT_ID must be set")

        self.base_url = "https://api.sandbox.ebay.com" if self.environment == "SANDBOX" else "https://api.ebay.com"
        self._token: Optional[str] = None
        self._token_expiry: float = 0.0

    def _token_url(self) -> str:
        return f"{self.base_url}/identity/v1/oauth2/token"

    def _get_token(self, scope: str) -> str:
        now = time.time()
        if self._token and now < (self._token_expiry - 30):
            return self._token

        data = {
            "grant_type": "client_credentials",
            "scope": scope,
        }
        resp = requests.post(
            self._token_url(),
            data=data,
            auth=(self.app_id, self.cert_id),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=self.timeout_s,
        )
        if resp.status_code >= 400:
            return ""
        payload = resp.json()
        self._token = payload.get("access_token")
        expires_in = float(payload.get("expires_in") or 0)
        self._token_expiry = now + expires_in
        return self._token or ""

    def request(
        self,
        method: str,
        path: str,
        *,
        scope: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        token = self._get_token(scope)
        if not token:
            return {"error": "Failed to obtain OAuth token. Check EBAY_APP_ID/EBAY_CERT_ID and environment."}

        url = f"{self.base_url}{path}"
        h = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }
        if headers:
            h.update(headers)

        resp = requests.request(
            method.upper(),
            url,
            params=params,
            json=json,
            headers=h,
            timeout=self.timeout_s,
        )

        if resp.status_code == 204:
            return {"status": 204}

        content_type = resp.headers.get("content-type", "")
        body: Any
        if "application/json" in content_type:
            try:
                body = resp.json()
            except Exception:
                body = {"raw": resp.text}
        else:
            body = {"raw": resp.text}

        if resp.status_code >= 400:
            return {
                "error": "API request failed",
                "status": resp.status_code,
                "body": body,
                "url": url,
            }
        return body
