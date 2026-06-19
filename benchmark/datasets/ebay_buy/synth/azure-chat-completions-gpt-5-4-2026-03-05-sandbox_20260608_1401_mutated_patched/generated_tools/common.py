import base64
import os
from typing import Any, Dict, Optional

import requests


class EbayClient:
    def __init__(self) -> None:
        self.app_id = os.getenv("EBAY_APP_ID", "")
        self.cert_id = os.getenv("EBAY_CERT_ID", "")
        self.environment = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
        self.base_url = (
            "https://api.ebay.com" if self.environment == "PRODUCTION" else "https://api.sandbox.ebay.com"
        )
        self._token: Optional[str] = None

    def _token_url(self) -> str:
        return f"{self.base_url}/identity/v1/oauth2/token"

    def get_token(self) -> str:
        if self._token:
            return self._token
        if not self.app_id or not self.cert_id:
            raise ValueError("EBAY_APP_ID and EBAY_CERT_ID must be set")
        creds = base64.b64encode(f"{self.app_id}:{self.cert_id}".encode()).decode()
        response = requests.post(
            self._token_url(),
            headers={
                "Authorization": f"Basic {creds}",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data={
                "grant_type": "client_credentials",
                "scope": "https://api.ebay.com/oauth/api_scope",
            },
            timeout=60,
        )
        response.raise_for_status()
        self._token = response.json().get("access_token")
        if not self._token:
            raise ValueError("Unable to obtain OAuth token")
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
            token = self.get_token()
            merged_headers = {
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
            }
            if headers:
                merged_headers.update({k: v for k, v in headers.items() if v is not None})
            response = requests.request(
                method,
                f"{self.base_url}{path}",
                params={k: v for k, v in (params or {}).items() if v is not None},
                json=json_body,
                headers=merged_headers,
                timeout=90,
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
