import os
import time
from typing import Any, Dict, Optional

import requests


class EbayClient:
    def __init__(self) -> None:
        self.app_id = os.getenv("EBAY_APP_ID", "")
        self.cert_id = os.getenv("EBAY_CERT_ID", "")
        self.environment = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
        self.base_url = "https://api.ebay.com" if self.environment == "PRODUCTION" else "https://api.sandbox.ebay.com"
        self._token: Optional[str] = None
        self._token_expiry: float = 0.0

    def _token_url(self) -> str:
        return f"{self.base_url}/identity/v1/oauth2/token"

    def get_access_token(self, scope: str = "https://api.ebay.com/oauth/api_scope") -> str:
        now = time.time()
        if self._token and now < self._token_expiry - 60:
            return self._token

        if not self.app_id or not self.cert_id:
            raise ValueError("Missing EBAY_APP_ID or EBAY_CERT_ID environment variables")

        response = requests.post(
            self._token_url(),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            auth=(self.app_id, self.cert_id),
            data={
                "grant_type": "client_credentials",
                "scope": scope,
            },
            timeout=30,
        )
        response.raise_for_status()
        payload = response.json()
        self._token = payload.get("access_token")
        self._token_expiry = now + int(payload.get("expires_in", 7200))
        return self._token or ""

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        scope: str = "https://api.ebay.com/oauth/api_scope",
    ) -> Dict[str, Any]:
        try:
            token = self.get_access_token(scope=scope)
            request_headers = {
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
            if headers:
                request_headers.update(headers)
            response = requests.request(
                method=method,
                url=f"{self.base_url}{path}",
                params=params,
                json=json_body,
                headers=request_headers,
                timeout=60,
            )
            if response.status_code >= 400:
                try:
                    return {"error": response.json(), "status_code": response.status_code}
                except Exception:
                    return {"error": response.text, "status_code": response.status_code}
            if not response.text:
                return {"status": "ok", "status_code": response.status_code}
            try:
                return response.json()
            except Exception:
                return {"text": response.text, "status_code": response.status_code}
        except Exception as exc:
            return {"error": str(exc)}


client = EbayClient()
