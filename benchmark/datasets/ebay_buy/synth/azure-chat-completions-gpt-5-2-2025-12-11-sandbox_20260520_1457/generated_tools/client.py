import os
import time
from typing import Any, Dict, Optional

import requests


EBAY_OAUTH_TOKEN_URL = {
    "SANDBOX": "https://api.sandbox.ebay.com/identity/v1/oauth2/token",
    "PRODUCTION": "https://api.ebay.com/identity/v1/oauth2/token",
}

EBAY_API_BASE_URL = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}

EBAY_APIX_BASE_URL = {
    "SANDBOX": "https://apix.sandbox.ebay.com",
    "PRODUCTION": "https://apix.ebay.com",
}


class EbayClient:
    def __init__(self):
        self.app_id = os.getenv("EBAY_APP_ID")
        self.cert_id = os.getenv("EBAY_CERT_ID")
        self.environment = (os.getenv("EBAY_ENVIRONMENT") or "SANDBOX").upper()
        if self.environment not in ("SANDBOX", "PRODUCTION"):
            self.environment = "SANDBOX"

        self._token: Optional[str] = None
        self._token_expiry: float = 0.0

    @property
    def base_url(self) -> str:
        return EBAY_API_BASE_URL[self.environment]

    def _get_token(self) -> str:
        if self._token and time.time() < self._token_expiry - 30:
            return self._token

        if not self.app_id or not self.cert_id:
            raise RuntimeError("Missing EBAY_APP_ID or EBAY_CERT_ID environment variables")

        url = EBAY_OAUTH_TOKEN_URL[self.environment]
        data = {
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope",
        }
        resp = requests.post(url, data=data, auth=(self.app_id, self.cert_id), timeout=30)
        if resp.status_code >= 400:
            raise RuntimeError(f"OAuth token request failed: {resp.status_code} {resp.text}")
        payload = resp.json()
        self._token = payload.get("access_token")
        expires_in = float(payload.get("expires_in", 0))
        self._token_expiry = time.time() + expires_in
        if not self._token:
            raise RuntimeError(f"OAuth token response missing access_token: {payload}")
        return self._token

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        use_apix: bool = False,
    ) -> Dict[str, Any]:
        base = EBAY_APIX_BASE_URL[self.environment] if use_apix else self.base_url
        url = base + path
        token = self._get_token()
        req_headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }
        if json is not None:
            req_headers["Content-Type"] = "application/json"
        if headers:
            req_headers.update({k: v for k, v in headers.items() if v is not None})

        resp = requests.request(method, url, params=params, json=json, headers=req_headers, timeout=60)
        if resp.status_code == 204:
            return {"status": 204}
        content_type = resp.headers.get("content-type", "")
        body: Any
        if "application/json" in content_type:
            body = resp.json()
        else:
            body = resp.text

        if resp.status_code >= 400:
            return {
                "error": "ebay_api_error",
                "status": resp.status_code,
                "body": body,
            }
        return body if isinstance(body, dict) else {"body": body}
