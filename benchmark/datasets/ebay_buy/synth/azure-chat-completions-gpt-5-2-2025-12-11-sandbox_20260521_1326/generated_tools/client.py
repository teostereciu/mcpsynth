import os
import time
from typing import Any, Dict, Optional

import requests


class EbayApiClient:
    """Minimal eBay Buy API client with OAuth2 client-credentials token caching."""

    def __init__(self):
        self.app_id = os.getenv("EBAY_APP_ID")
        self.cert_id = os.getenv("EBAY_CERT_ID")
        self.environment = (os.getenv("EBAY_ENVIRONMENT") or "SANDBOX").upper()
        if self.environment not in {"SANDBOX", "PRODUCTION"}:
            self.environment = "SANDBOX"

        self.base_url = (
            "https://api.sandbox.ebay.com" if self.environment == "SANDBOX" else "https://api.ebay.com"
        )
        self._token: Optional[str] = None
        self._token_exp: float = 0.0

    def _token_url(self) -> str:
        return f"{self.base_url}/identity/v1/oauth2/token"

    def _get_token(self) -> str:
        if self._token and time.time() < (self._token_exp - 30):
            return self._token

        if not self.app_id or not self.cert_id:
            raise RuntimeError("Missing EBAY_APP_ID or EBAY_CERT_ID")

        data = {
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope",
        }
        resp = requests.post(
            self._token_url(),
            data=data,
            auth=(self.app_id, self.cert_id),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=30,
        )
        if resp.status_code >= 400:
            raise RuntimeError(f"Token request failed: {resp.status_code} {resp.text}")
        payload = resp.json()
        self._token = payload.get("access_token")
        expires_in = float(payload.get("expires_in") or 0)
        self._token_exp = time.time() + expires_in
        if not self._token:
            raise RuntimeError("Token response missing access_token")
        return self._token

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        try:
            token = self._get_token()
        except Exception as e:
            return {"error": str(e)}

        h = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }
        if headers:
            h.update({k: v for k, v in headers.items() if v is not None})

        try:
            resp = requests.request(method, url, params=params, json=json, headers=h, timeout=30)
        except Exception as e:
            return {"error": str(e)}

        content_type = resp.headers.get("Content-Type", "")
        if resp.status_code >= 400:
            # Try to parse JSON error
            if "application/json" in content_type:
                try:
                    return {"error": resp.json(), "status": resp.status_code}
                except Exception:
                    return {"error": resp.text, "status": resp.status_code}
            return {"error": resp.text, "status": resp.status_code}

        if resp.status_code == 204:
            return {"status": 204}

        if "application/json" in content_type:
            try:
                return resp.json()
            except Exception:
                return {"error": "Failed to parse JSON response", "status": resp.status_code, "text": resp.text}

        return {"status": resp.status_code, "text": resp.text}
