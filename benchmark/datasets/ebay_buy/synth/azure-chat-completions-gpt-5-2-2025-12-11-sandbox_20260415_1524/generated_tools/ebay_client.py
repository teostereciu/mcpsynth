import os
import time
from typing import Any, Dict, Optional

import requests


class EbayClient:
    """Minimal eBay REST client with application OAuth token caching."""

    def __init__(
        self,
        app_id: Optional[str] = None,
        cert_id: Optional[str] = None,
        environment: Optional[str] = None,
        timeout: float = 30.0,
    ):
        self.app_id = app_id or os.getenv("EBAY_APP_ID")
        self.cert_id = cert_id or os.getenv("EBAY_CERT_ID")
        self.environment = (environment or os.getenv("EBAY_ENVIRONMENT") or "SANDBOX").upper()
        self.timeout = timeout

        if not self.app_id or not self.cert_id:
            raise ValueError("Missing EBAY_APP_ID or EBAY_CERT_ID")

        self.base_url = "https://api.sandbox.ebay.com" if self.environment != "PRODUCTION" else "https://api.ebay.com"
        self._token: Optional[str] = None
        self._token_exp: float = 0.0

    def _token_url(self) -> str:
        return f"{self.base_url}/identity/v1/oauth2/token"

    def _get_token(self) -> str:
        now = time.time()
        if self._token and now < (self._token_exp - 30):
            return self._token

        data = {
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope",
        }
        r = requests.post(
            self._token_url(),
            data=data,
            auth=(self.app_id, self.cert_id),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=self.timeout,
        )
        if r.status_code >= 400:
            return ""
        payload = r.json()
        self._token = payload.get("access_token")
        expires_in = float(payload.get("expires_in") or 0)
        self._token_exp = now + expires_in
        return self._token or ""

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        token = self._get_token()
        if not token:
            return {"error": "oauth_token_error", "details": "Failed to obtain OAuth token"}

        url = f"{self.base_url}{path}"
        h = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }
        if headers:
            h.update({k: v for k, v in headers.items() if v is not None})

        try:
            r = requests.request(method, url, params=params, json=json, headers=h, timeout=self.timeout)
        except requests.RequestException as e:
            return {"error": "request_error", "details": str(e)}

        content_type = (r.headers.get("Content-Type") or "").lower()
        if "application/json" in content_type:
            body: Any = r.json()
        else:
            body = r.text

        if r.status_code >= 400:
            return {"error": "http_error", "status": r.status_code, "body": body}
        return {"status": r.status_code, "body": body, "headers": dict(r.headers)}
