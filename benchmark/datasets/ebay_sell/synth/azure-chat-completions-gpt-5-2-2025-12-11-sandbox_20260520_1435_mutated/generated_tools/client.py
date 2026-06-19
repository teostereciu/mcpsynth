import os
import time
from typing import Any, Dict, Optional

import requests


class EbayOAuthError(Exception):
    pass


class EbayClient:
    def __init__(self):
        self.app_id = os.getenv("EBAY_APP_ID", "").strip()
        self.cert_id = os.getenv("EBAY_CERT_ID", "").strip()
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN", "").strip()
        self.environment = (os.getenv("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").strip().upper()

        if not self.app_id or not self.cert_id or not self.refresh_token:
            raise EbayOAuthError(
                "Missing EBAY_APP_ID, EBAY_CERT_ID, or EBAY_REFRESH_TOKEN environment variables"
            )

        self.base_url = "https://api.sandbox.ebay.com" if self.environment != "PRODUCTION" else "https://api.ebay.com"
        self._access_token: Optional[str] = None
        self._access_token_expiry: float = 0.0

    def _token_url(self) -> str:
        # eBay OAuth token endpoint
        return (
            "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
            if self.environment != "PRODUCTION"
            else "https://api.ebay.com/identity/v1/oauth2/token"
        )

    def _get_access_token(self) -> str:
        now = time.time()
        if self._access_token and now < (self._access_token_expiry - 30):
            return self._access_token

        auth = requests.auth.HTTPBasicAuth(self.app_id, self.cert_id)
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            # scope is optional for refresh token grant; omit to use token's granted scopes
        }
        resp = requests.post(self._token_url(), headers=headers, data=data, auth=auth, timeout=60)
        if resp.status_code >= 400:
            return f"ERROR: OAuth token request failed ({resp.status_code}): {resp.text}"
        payload = resp.json()
        token = payload.get("access_token")
        expires_in = payload.get("expires_in", 0)
        if not token:
            return f"ERROR: OAuth token response missing access_token: {payload}"
        self._access_token = token
        self._access_token_expiry = now + float(expires_in or 0)
        return token

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
    ) -> Any:
        token = self._get_access_token()
        if isinstance(token, str) and token.startswith("ERROR:"):
            return {"error": token}

        url = self.base_url + path
        req_headers: Dict[str, str] = {
            "Authorization": f"Bearer {token}",
            "Accept": accept,
        }
        if content_type:
            req_headers["Content-Type"] = content_type
        if headers:
            req_headers.update({k: v for k, v in headers.items() if v is not None})

        try:
            resp = requests.request(
                method.upper(),
                url,
                params=params,
                json=json,
                headers=req_headers,
                timeout=60,
            )
        except requests.RequestException as e:
            return {"error": f"Request failed: {e}"}

        if resp.status_code == 204:
            return {"status": 204}

        # Try JSON first
        try:
            data = resp.json()
        except ValueError:
            data = resp.text

        if resp.status_code >= 400:
            return {
                "error": "HTTP error",
                "status": resp.status_code,
                "body": data,
            }
        return data
