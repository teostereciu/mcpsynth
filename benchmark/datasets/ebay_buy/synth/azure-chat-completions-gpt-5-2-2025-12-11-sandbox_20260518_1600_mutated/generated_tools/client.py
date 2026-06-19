import base64
import os
import time
from typing import Any, Dict, Optional

import requests


class EbayClient:
    """Minimal eBay Buy API client using OAuth2 client-credentials (application token)."""

    def __init__(
        self,
        app_id: Optional[str] = None,
        cert_id: Optional[str] = None,
        environment: Optional[str] = None,
        timeout_s: int = 30,
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
        # Standard eBay OAuth token endpoint
        return f"{self.base_url}/identity/v1/oauth2/token"

    def _get_token(self) -> str:
        now = time.time()
        if self._token and now < (self._token_expiry - 30):
            return self._token

        basic = base64.b64encode(f"{self.app_id}:{self.cert_id}".encode("utf-8")).decode("ascii")
        headers = {
            "Authorization": f"Basic {basic}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope",
        }
        resp = requests.post(self._token_url(), headers=headers, data=data, timeout=self.timeout_s)
        if resp.status_code >= 400:
            return ""  # handled by caller
        payload = resp.json()
        self._token = payload.get("access_token")
        expires_in = payload.get("expires_in", 0)
        self._token_expiry = now + float(expires_in)
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
            return {"error": "Failed to obtain OAuth token. Check EBAY_APP_ID/EBAY_CERT_ID and environment."}

        url = f"{self.base_url}{path}"
        req_headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }
        if headers:
            req_headers.update(headers)

        try:
            resp = requests.request(
                method.upper(),
                url,
                params=params,
                json=json,
                headers=req_headers,
                timeout=self.timeout_s,
            )
        except requests.RequestException as e:
            return {"error": f"Network error calling eBay: {e}"}

        content_type = resp.headers.get("Content-Type", "")
        if resp.status_code >= 400:
            err: Dict[str, Any] = {"error": f"HTTP {resp.status_code}", "status_code": resp.status_code}
            if "application/json" in content_type:
                try:
                    err["details"] = resp.json()
                except Exception:
                    err["details"] = resp.text
            else:
                err["details"] = resp.text
            return err

        if "application/json" in content_type:
            try:
                return resp.json()
            except Exception:
                return {"error": "Failed to parse JSON response", "raw": resp.text}

        return {"raw": resp.text, "content_type": content_type}
