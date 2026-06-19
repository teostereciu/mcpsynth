import os
import time
from typing import Any, Dict, Optional

import requests


class EbayClient:
    def __init__(self):
        self.app_id = os.getenv("EBAY_APP_ID")
        self.cert_id = os.getenv("EBAY_CERT_ID")
        self.environment = (os.getenv("EBAY_ENVIRONMENT") or "SANDBOX").upper()
        self.base_url = (
            "https://api.sandbox.ebay.com" if self.environment == "SANDBOX" else "https://api.ebay.com"
        )
        self._token: Optional[str] = None
        self._token_expiry: float = 0.0

    def _token_url(self) -> str:
        return f"{self.base_url}/identity/v1/oauth2/token"

    def _get_token(self, scope: str = "https://api.ebay.com/oauth/api_scope") -> str:
        if self._token and time.time() < (self._token_expiry - 30):
            return self._token
        if not self.app_id or not self.cert_id:
            raise RuntimeError("Missing EBAY_APP_ID or EBAY_CERT_ID")

        auth = requests.auth.HTTPBasicAuth(self.app_id, self.cert_id)
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"grant_type": "client_credentials", "scope": scope}
        r = requests.post(self._token_url(), headers=headers, data=data, auth=auth, timeout=30)
        if r.status_code >= 400:
            raise RuntimeError(f"OAuth token error {r.status_code}: {r.text}")
        j = r.json()
        self._token = j.get("access_token")
        expires_in = float(j.get("expires_in", 7200))
        self._token_expiry = time.time() + expires_in
        return self._token

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        scope: str = "https://api.ebay.com/oauth/api_scope",
    ) -> Dict[str, Any]:
        token = self._get_token(scope=scope)
        url = f"{self.base_url}{path}"
        h = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
        if headers:
            h.update(headers)
        r = requests.request(method, url, params=params, json=json, headers=h, timeout=60)
        ct = r.headers.get("content-type", "")
        if r.status_code >= 400:
            return {"error": "request_failed", "status": r.status_code, "body": r.text}
        if "application/json" in ct:
            return r.json()
        return {"status": r.status_code, "body": r.text}
