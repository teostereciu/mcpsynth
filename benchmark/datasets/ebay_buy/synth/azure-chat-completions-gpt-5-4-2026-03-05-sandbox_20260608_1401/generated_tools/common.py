import base64
import os
import time
from typing import Any, Dict, Optional

import requests


class EbayClient:
    def __init__(self) -> None:
        env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
        self.base_url = "https://api.sandbox.ebay.com" if env == "SANDBOX" else "https://api.ebay.com"
        self._token: Optional[str] = None
        self._token_expiry = 0.0

    def _get_token(self) -> str:
        if self._token and time.time() < self._token_expiry - 60:
            return self._token

        app_id = os.getenv("EBAY_APP_ID")
        cert_id = os.getenv("EBAY_CERT_ID")
        if not app_id or not cert_id:
            raise RuntimeError("EBAY_APP_ID and EBAY_CERT_ID environment variables are required")

        creds = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
        response = requests.post(
            f"{self.base_url}/identity/v1/oauth2/token",
            headers={
                "Authorization": f"Basic {creds}",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data={
                "grant_type": "client_credentials",
                "scope": "https://api.ebay.com/oauth/api_scope",
            },
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()
        self._token = data["access_token"]
        self._token_expiry = time.time() + int(data.get("expires_in", 7200))
        return self._token

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        try:
            token = self._get_token()
            req_headers = {
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
            if headers:
                req_headers.update({k: v for k, v in headers.items() if v is not None})
            response = requests.request(
                method,
                f"{self.base_url}{path}",
                params={k: v for k, v in (params or {}).items() if v is not None},
                json=json_body,
                headers=req_headers,
                timeout=60,
            )
            if response.status_code >= 400:
                try:
                    return {"error": response.json(), "status_code": response.status_code}
                except Exception:
                    return {"error": response.text, "status_code": response.status_code}
            if not response.text:
                return {"status_code": response.status_code}
            try:
                return response.json()
            except Exception:
                return {"text": response.text, "status_code": response.status_code}
        except Exception as e:
            return {"error": str(e)}


client = EbayClient()
