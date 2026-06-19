import base64
import os
import time
from typing import Any, Dict, Optional

import requests


class EbayClient:
    def __init__(self) -> None:
        self.app_id = os.getenv("EBAY_APP_ID", "")
        self.cert_id = os.getenv("EBAY_CERT_ID", "")
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN", "")
        self.environment = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
        self._access_token: Optional[str] = None
        self._token_expiry = 0.0

    @property
    def base_url(self) -> str:
        if self.environment == "PRODUCTION":
            return "https://api.ebay.com"
        return "https://api.sandbox.ebay.com"

    def _token_url(self) -> str:
        return f"{self.base_url}/identity/v1/oauth2/token"

    def get_access_token(self) -> str:
        if self._access_token and time.time() < self._token_expiry - 60:
            return self._access_token
        if not self.app_id or not self.cert_id or not self.refresh_token:
            raise RuntimeError("Missing one or more required environment variables: EBAY_APP_ID, EBAY_CERT_ID, EBAY_REFRESH_TOKEN")
        creds = base64.b64encode(f"{self.app_id}:{self.cert_id}".encode()).decode()
        response = requests.post(
            self._token_url(),
            headers={
                "Authorization": f"Basic {creds}",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data={
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token,
            },
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()
        self._access_token = data["access_token"]
        self._token_expiry = time.time() + int(data.get("expires_in", 7200))
        return self._access_token

    def request(
        self,
        method: str,
        api_path: str,
        *,
        api_group: str,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Any] = None,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[Any] = None,
    ) -> Any:
        token = self.get_access_token()
        merged_headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }
        if headers:
            merged_headers.update({k: v for k, v in headers.items() if v is not None})
        url = f"{self.base_url}/sell/{api_group}/v1{api_path}"
        response = requests.request(
            method=method,
            url=url,
            params={k: v for k, v in (params or {}).items() if v is not None},
            json=json_body,
            headers=merged_headers,
            data=data,
            timeout=120,
        )
        if response.status_code == 204:
            return {"status": 204, "success": True}
        content_type = response.headers.get("Content-Type", "")
        if response.ok:
            if "application/json" in content_type:
                return response.json()
            return {"status": response.status_code, "content": response.text}
        try:
            err = response.json()
        except Exception:
            err = {"message": response.text}
        return {"error": True, "status": response.status_code, "details": err}


client = EbayClient()
