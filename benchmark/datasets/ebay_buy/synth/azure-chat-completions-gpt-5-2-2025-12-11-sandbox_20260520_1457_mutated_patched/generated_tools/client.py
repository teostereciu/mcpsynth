import base64
import os
import time
from typing import Any, Dict, Optional

import requests


class EbayClient:
    """Minimal eBay REST client with OAuth2 client-credentials token caching."""

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
            raise ValueError("EBAY_APP_ID and EBAY_CERT_ID must be set")

        self.base_url = (
            "https://api.ebay.com" if self.environment == "PRODUCTION" else "https://api.sandbox.ebay.com"
        )
        self._token: Optional[str] = None
        self._token_expiry: float = 0.0

    def _token_url(self) -> str:
        # eBay OAuth token endpoint (common across environments)
        return f"{self.base_url}/identity/v1/oauth2/token"

    def _get_app_token(self, scope: str = "https://api.ebay.com/oauth/api_scope") -> str:
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
            "scope": scope,
        }
        resp = requests.post(self._token_url(), headers=headers, data=data, timeout=self.timeout)
        if resp.status_code >= 400:
            return ""  # handled by caller
        payload = resp.json()
        token = payload.get("access_token")
        expires_in = float(payload.get("expires_in", 0))
        if not token:
            return ""
        self._token = token
        self._token_expiry = now + expires_in
        return token

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        scope: str = "https://api.ebay.com/oauth/api_scope",
        raw: bool = False,
    ) -> Dict[str, Any]:
        token = self._get_app_token(scope=scope)
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
                method,
                url,
                params=params,
                json=json,
                headers=req_headers,
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            return {"error": f"Network error: {e}"}

        if raw:
            body = resp.text
        else:
            content_type = resp.headers.get("content-type", "")
            if "application/json" in content_type:
                body: Any = resp.json()
            else:
                body = resp.text

        if resp.status_code >= 400:
            return {
                "error": "eBay API error",
                "status": resp.status_code,
                "body": body,
            }

        return {"status": resp.status_code, "body": body, "headers": dict(resp.headers)}
