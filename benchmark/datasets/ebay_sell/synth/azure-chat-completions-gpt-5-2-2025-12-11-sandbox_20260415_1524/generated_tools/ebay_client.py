import os
import time
from typing import Any, Dict, Optional

import requests


class EbayClient:
    """Minimal eBay REST client with OAuth refresh-token flow for Sell APIs."""

    def __init__(self):
        self.app_id = os.getenv("EBAY_APP_ID")
        self.cert_id = os.getenv("EBAY_CERT_ID")
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN")
        self.environment = (os.getenv("EBAY_ENVIRONMENT") or "SANDBOX").upper()

        if self.environment not in ("SANDBOX", "PRODUCTION"):
            self.environment = "SANDBOX"

        self.base_url = (
            "https://api.sandbox.ebay.com" if self.environment == "SANDBOX" else "https://api.ebay.com"
        )

        self._access_token: Optional[str] = None
        self._access_token_expiry: float = 0.0

    def _token_endpoint(self) -> str:
        return f"{self.base_url}/identity/v1/oauth2/token"

    def _basic_auth_header(self) -> str:
        # eBay expects HTTP Basic with base64(client_id:client_secret)
        import base64

        if not self.app_id or not self.cert_id:
            raise ValueError("Missing EBAY_APP_ID or EBAY_CERT_ID")
        raw = f"{self.app_id}:{self.cert_id}".encode("utf-8")
        return "Basic " + base64.b64encode(raw).decode("ascii")

    def get_access_token(self, force_refresh: bool = False) -> str:
        now = time.time()
        if not force_refresh and self._access_token and now < (self._access_token_expiry - 30):
            return self._access_token

        if not self.refresh_token:
            raise ValueError("Missing EBAY_REFRESH_TOKEN")

        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            # Scope is optional for refresh; omit to use token's granted scopes.
        }
        resp = requests.post(self._token_endpoint(), headers=headers, data=data, timeout=60)
        if resp.status_code >= 400:
            try:
                return_error = resp.json()
            except Exception:
                return_error = {"error": resp.text}
            raise RuntimeError(f"OAuth token error {resp.status_code}: {return_error}")

        payload = resp.json()
        self._access_token = payload.get("access_token")
        expires_in = payload.get("expires_in") or 0
        self._access_token_expiry = now + float(expires_in)
        if not self._access_token:
            raise RuntimeError(f"OAuth token response missing access_token: {payload}")
        return self._access_token

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Any = None,
        headers: Optional[Dict[str, str]] = None,
        accept: str = "application/json",
        content_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Perform an authenticated request.

        Returns JSON dict when possible; otherwise returns {"status_code":..., "text":...}.
        For expected errors, returns {"error":..., "status_code":..., "details":...}.
        """
        url = self.base_url + path
        try:
            token = self.get_access_token()
        except Exception as e:
            return {"error": "auth_error", "details": str(e)}

        req_headers: Dict[str, str] = {
            "Authorization": f"Bearer {token}",
            "Accept": accept,
        }
        if content_type:
            req_headers["Content-Type"] = content_type
        if headers:
            req_headers.update({k: v for k, v in headers.items() if v is not None})

        try:
            resp = requests.request(
                method,
                url,
                params=params,
                json=json,
                data=data,
                headers=req_headers,
                timeout=60,
            )
        except Exception as e:
            return {"error": "request_failed", "details": str(e)}

        if resp.status_code == 204:
            return {"status_code": 204}

        # Try JSON
        try:
            body = resp.json()
        except Exception:
            body = {"text": resp.text}

        if resp.status_code >= 400:
            return {"error": "http_error", "status_code": resp.status_code, "details": body}

        if isinstance(body, dict):
            body.setdefault("status_code", resp.status_code)
            return body
        return {"status_code": resp.status_code, "data": body}
