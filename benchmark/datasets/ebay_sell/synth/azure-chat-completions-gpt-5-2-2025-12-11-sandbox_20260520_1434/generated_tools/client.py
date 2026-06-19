import os
import time
from typing import Any, Dict, Optional

import requests


class EbayOAuthClient:
    def __init__(self):
        self.app_id = os.getenv("EBAY_APP_ID", "").strip()
        self.cert_id = os.getenv("EBAY_CERT_ID", "").strip()
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN", "").strip()
        self.environment = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").strip().upper() or "SANDBOX"

        if self.environment not in {"SANDBOX", "PRODUCTION"}:
            self.environment = "SANDBOX"

        self.base_url = "https://api.sandbox.ebay.com" if self.environment == "SANDBOX" else "https://api.ebay.com"

        self._access_token: Optional[str] = None
        self._access_token_expiry: float = 0.0

    def _token_url(self) -> str:
        return f"{self.base_url}/identity/v1/oauth2/token"

    def _basic_auth_header(self) -> str:
        import base64

        raw = f"{self.app_id}:{self.cert_id}".encode("utf-8")
        return "Basic " + base64.b64encode(raw).decode("ascii")

    def get_access_token(self) -> str:
        now = time.time()
        if self._access_token and now < (self._access_token_expiry - 30):
            return self._access_token

        if not (self.app_id and self.cert_id and self.refresh_token):
            raise RuntimeError("Missing EBAY_APP_ID, EBAY_CERT_ID, or EBAY_REFRESH_TOKEN")

        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
        }
        resp = requests.post(self._token_url(), headers=headers, data=data, timeout=30)
        if resp.status_code >= 400:
            raise RuntimeError(f"OAuth token error {resp.status_code}: {resp.text}")
        payload = resp.json()
        self._access_token = payload.get("access_token")
        expires_in = float(payload.get("expires_in", 0) or 0)
        self._access_token_expiry = now + expires_in
        if not self._access_token:
            raise RuntimeError(f"OAuth token response missing access_token: {payload}")
        return self._access_token


class EbaySellClient:
    def __init__(self, oauth: Optional[EbayOAuthClient] = None):
        self.oauth = oauth or EbayOAuthClient()

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Any = None,
        headers: Optional[Dict[str, str]] = None,
        accept: str = "application/json",
    ) -> Dict[str, Any]:
        url = self.oauth.base_url + path
        try:
            token = self.oauth.get_access_token()
        except Exception as e:
            return {"error": str(e)}

        req_headers = {
            "Authorization": f"Bearer {token}",
            "Accept": accept,
        }
        if headers:
            req_headers.update({k: v for k, v in headers.items() if v is not None})

        try:
            resp = requests.request(method, url, params=params, json=json, headers=req_headers, timeout=60)
        except Exception as e:
            return {"error": f"Request failed: {e}"}

        if resp.status_code == 204:
            return {"status": 204}

        content_type = resp.headers.get("Content-Type", "")
        body: Any
        if "application/json" in content_type:
            try:
                body = resp.json()
            except Exception:
                body = {"raw": resp.text}
        else:
            body = {"raw": resp.text}

        if resp.status_code >= 400:
            return {
                "error": "HTTP error",
                "status": resp.status_code,
                "body": body,
                "headers": dict(resp.headers),
            }

        return body if isinstance(body, (dict, list)) else {"result": body}
