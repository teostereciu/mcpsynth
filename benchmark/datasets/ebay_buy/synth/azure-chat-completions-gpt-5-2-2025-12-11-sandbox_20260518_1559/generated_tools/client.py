import base64
import os
import time
from typing import Any, Dict, Optional

import requests


class EbayClient:
    def __init__(self):
        self.app_id = os.getenv("EBAY_APP_ID")
        self.cert_id = os.getenv("EBAY_CERT_ID")
        self.environment = (os.getenv("EBAY_ENVIRONMENT") or "SANDBOX").upper()
        if self.environment not in {"SANDBOX", "PRODUCTION"}:
            self.environment = "SANDBOX"

        self.base_url = (
            "https://api.sandbox.ebay.com" if self.environment == "SANDBOX" else "https://api.ebay.com"
        )
        # Order API docs sometimes show apix.ebay.com; api.ebay.com works for production.
        self._token: Optional[str] = None
        self._token_expiry: float = 0.0

    def _token_url(self) -> str:
        return f"{self.base_url}/identity/v1/oauth2/token"

    def _get_token(self) -> str:
        if self._token and time.time() < self._token_expiry - 30:
            return self._token

        if not self.app_id or not self.cert_id:
            raise RuntimeError("Missing EBAY_APP_ID or EBAY_CERT_ID")

        basic = base64.b64encode(f"{self.app_id}:{self.cert_id}".encode("utf-8")).decode("ascii")
        headers = {
            "Authorization": f"Basic {basic}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "client_credentials",
            # Use the broadest application scope; some endpoints may require additional scopes.
            "scope": "https://api.ebay.com/oauth/api_scope",
        }
        resp = requests.post(self._token_url(), headers=headers, data=data, timeout=30)
        if resp.status_code >= 400:
            return_error = {
                "error": "oauth_token_error",
                "status": resp.status_code,
                "body": _safe_json(resp),
            }
            raise RuntimeError(str(return_error))
        payload = resp.json()
        self._token = payload.get("access_token")
        expires_in = float(payload.get("expires_in") or 0)
        self._token_expiry = time.time() + expires_in
        return self._token or ""

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        try:
            token = self._get_token()
        except Exception as e:
            return {"error": "auth_error", "message": str(e)}

        req_headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }
        if headers:
            req_headers.update(headers)

        try:
            resp = requests.request(
                method.upper(),
                url,
                params=params,
                json=json,
                headers=req_headers,
                timeout=60,
            )
        except Exception as e:
            return {"error": "request_failed", "message": str(e)}

        if resp.status_code >= 400:
            return {
                "error": "http_error",
                "status": resp.status_code,
                "url": url,
                "body": _safe_json(resp),
            }

        return _safe_json(resp)


def _safe_json(resp: requests.Response) -> Dict[str, Any]:
    try:
        return resp.json()
    except Exception:
        return {"text": resp.text}
