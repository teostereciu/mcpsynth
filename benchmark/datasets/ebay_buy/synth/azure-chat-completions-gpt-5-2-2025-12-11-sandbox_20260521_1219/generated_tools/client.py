import os
import time
from typing import Any, Dict, Optional

import requests


class EbayClient:
    """Minimal eBay Buy API client using OAuth2 client-credentials (application token)."""

    def __init__(self):
        self.app_id = os.getenv("EBAY_APP_ID")
        self.cert_id = os.getenv("EBAY_CERT_ID")
        self.environment = (os.getenv("EBAY_ENVIRONMENT") or "SANDBOX").upper()
        if not self.app_id or not self.cert_id:
            raise RuntimeError("EBAY_APP_ID and EBAY_CERT_ID must be set")

        self.base_url = (
            "https://api.ebay.com" if self.environment == "PRODUCTION" else "https://api.sandbox.ebay.com"
        )
        self._token: Optional[str] = None
        self._token_exp: float = 0.0

    def _get_token(self) -> str:
        now = time.time()
        if self._token and now < self._token_exp - 30:
            return self._token

        url = f"{self.base_url}/identity/v1/oauth2/token"
        data = {
            "grant_type": "client_credentials",
            # Browse/Deal/Feed/Order all accept api_scope for app tokens.
            "scope": "https://api.ebay.com/oauth/api_scope",
        }
        resp = requests.post(url, data=data, auth=(self.app_id, self.cert_id), timeout=30)
        if resp.status_code >= 400:
            return ""
        payload = resp.json()
        self._token = payload.get("access_token")
        expires_in = payload.get("expires_in", 0)
        self._token_exp = now + float(expires_in)
        return self._token or ""

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json: Any = None,
    ) -> Dict[str, Any]:
        token = self._get_token()
        if not token:
            return {"error": "Failed to obtain OAuth token"}

        url = f"{self.base_url}{path}"
        h = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
        if headers:
            h.update({k: v for k, v in headers.items() if v is not None})

        try:
            resp = requests.request(method, url, params=params, headers=h, json=json, timeout=30)
        except requests.RequestException as e:
            return {"error": str(e)}

        content_type = resp.headers.get("content-type", "")
        if resp.status_code >= 400:
            try:
                err = resp.json() if "json" in content_type else {"message": resp.text}
            except Exception:
                err = {"message": resp.text}
            return {"error": "HTTP error", "status": resp.status_code, "details": err}

        if resp.status_code == 204:
            return {"status": 204}

        if "json" in content_type:
            try:
                return resp.json()
            except Exception:
                return {"error": "Invalid JSON response", "status": resp.status_code, "text": resp.text}

        return {"status": resp.status_code, "text": resp.text}
