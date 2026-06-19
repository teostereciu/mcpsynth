import os
import time
import base64
from typing import Any, Dict, Optional

import requests


class EbayClient:
    def __init__(self) -> None:
        env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
        self.base_url = "https://api.ebay.com" if env == "PRODUCTION" else "https://api.sandbox.ebay.com"
        self.app_id = os.getenv("EBAY_APP_ID", "")
        self.cert_id = os.getenv("EBAY_CERT_ID", "")
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN", "")
        self._access_token: Optional[str] = None
        self._expires_at = 0.0

    def _token(self) -> str:
        if self._access_token and time.time() < self._expires_at - 60:
            return self._access_token
        if not self.app_id or not self.cert_id or not self.refresh_token:
            raise RuntimeError("Missing EBAY_APP_ID, EBAY_CERT_ID, or EBAY_REFRESH_TOKEN")
        basic = base64.b64encode(f"{self.app_id}:{self.cert_id}".encode()).decode()
        resp = requests.post(
            f"{self.base_url}/identity/v1/oauth2/token",
            headers={
                "Authorization": f"Basic {basic}",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data={
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token,
            },
            timeout=60,
        )
        resp.raise_for_status()
        data = resp.json()
        self._access_token = data["access_token"]
        self._expires_at = time.time() + int(data.get("expires_in", 7200))
        return self._access_token

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
            token = self._token()
            req_headers = {
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
            if headers:
                req_headers.update(headers)
            resp = requests.request(
                method,
                f"{self.base_url}{path}",
                params=params,
                json=json_body,
                headers=req_headers,
                timeout=120,
            )
            if resp.status_code >= 400:
                try:
                    return {"error": f"HTTP {resp.status_code}", "details": resp.json()}
                except Exception:
                    return {"error": f"HTTP {resp.status_code}", "details": resp.text}
            if not resp.text:
                return {"ok": True, "status_code": resp.status_code}
            try:
                return resp.json()
            except Exception:
                return {"text": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}


client = EbayClient()
