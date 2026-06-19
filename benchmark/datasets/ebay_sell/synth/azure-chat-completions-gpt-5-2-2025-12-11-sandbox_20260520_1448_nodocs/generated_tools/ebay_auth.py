import os
import time
import base64
from typing import Dict, Any, Optional

import requests


TOKEN_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com/identity/v1/oauth2/token",
    "PRODUCTION": "https://api.ebay.com/identity/v1/oauth2/token",
}


class EbayAuth:
    def __init__(self):
        self.client_id = os.getenv("EBAY_APP_ID", "")
        self.client_secret = os.getenv("EBAY_CERT_ID", "")
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN", "")
        self.environment = (os.getenv("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()

        self._access_token: Optional[str] = None
        self._expires_at: float = 0.0

    def _basic_auth_header(self) -> str:
        raw = f"{self.client_id}:{self.client_secret}".encode("utf-8")
        return "Basic " + base64.b64encode(raw).decode("ascii")

    def get_access_token(self, scope: Optional[str] = None) -> Dict[str, Any]:
        if not self.client_id or not self.client_secret or not self.refresh_token:
            return {
                "error": "Missing EBAY_APP_ID/EBAY_CERT_ID/EBAY_REFRESH_TOKEN environment variables",
            }

        now = time.time()
        if self._access_token and now < (self._expires_at - 60):
            return {"access_token": self._access_token, "expires_at": self._expires_at}

        url = TOKEN_URLS.get(self.environment, TOKEN_URLS["SANDBOX"])
        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
        }
        if scope:
            data["scope"] = scope

        try:
            resp = requests.post(url, headers=headers, data=data, timeout=30)
        except Exception as e:
            return {"error": f"Token request failed: {e}"}

        if resp.status_code >= 400:
            return {"error": "Token request error", "status": resp.status_code, "body": _safe_json(resp)}

        js = _safe_json(resp)
        token = js.get("access_token")
        expires_in = js.get("expires_in", 0)
        if not token:
            return {"error": "Token response missing access_token", "body": js}

        self._access_token = token
        self._expires_at = time.time() + int(expires_in)
        return {"access_token": token, "expires_at": self._expires_at}


def _safe_json(resp: requests.Response):
    try:
        return resp.json()
    except Exception:
        return {"text": resp.text}
