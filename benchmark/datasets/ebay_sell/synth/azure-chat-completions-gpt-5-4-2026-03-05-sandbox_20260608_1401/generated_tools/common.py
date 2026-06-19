import base64
import json
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

    def _oauth_token(self) -> str:
        if self._token and time.time() < self._token_expiry - 60:
            return self._token
        app_id = os.getenv("EBAY_APP_ID")
        cert_id = os.getenv("EBAY_CERT_ID")
        refresh_token = os.getenv("EBAY_REFRESH_TOKEN")
        if not app_id or not cert_id or not refresh_token:
            raise RuntimeError("Missing one or more required environment variables: EBAY_APP_ID, EBAY_CERT_ID, EBAY_REFRESH_TOKEN")
        auth = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
        response = requests.post(
            f"{self.base_url}/identity/v1/oauth2/token",
            headers={
                "Authorization": f"Basic {auth}",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data={
                "grant_type": "refresh_token",
                "refresh_token": refresh_token,
                "scope": "https://api.ebay.com/oauth/api_scope",
            },
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()
        self._token = data["access_token"]
        self._token_expiry = time.time() + int(data.get("expires_in", 7200))
        return self._token

    def request(
        self,
        api_path: str,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Any = None,
        headers: Optional[Dict[str, str]] = None,
        allow_no_content: bool = True,
    ) -> Any:
        try:
            token = self._oauth_token()
            req_headers = {
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
            }
            if headers:
                req_headers.update({k: v for k, v in headers.items() if v is not None})
            url = f"{self.base_url}{api_path}{path}"
            response = requests.request(
                method,
                url,
                params={k: v for k, v in (params or {}).items() if v is not None},
                json=json_body,
                headers=req_headers,
                timeout=120,
            )
            if response.status_code == 204 and allow_no_content:
                return {"status": 204, "ok": True}
            content_type = response.headers.get("Content-Type", "")
            if response.ok:
                if "application/json" in content_type:
                    return response.json()
                text = response.text
                return {"status": response.status_code, "content": text}
            error_body: Any
            if "application/json" in content_type:
                try:
                    error_body = response.json()
                except Exception:
                    error_body = response.text
            else:
                error_body = response.text
            return {"error": f"HTTP {response.status_code}", "details": error_body}
        except requests.HTTPError as exc:
            return {"error": str(exc)}
        except Exception as exc:
            return {"error": str(exc)}


client = EbayClient()
