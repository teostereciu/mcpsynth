import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


class EbayOAuthError(Exception):
    pass


class EbayClient:
    """Minimal eBay REST client with refresh-token OAuth for Sell APIs."""

    def __init__(
        self,
        app_id: Optional[str] = None,
        cert_id: Optional[str] = None,
        refresh_token: Optional[str] = None,
        environment: Optional[str] = None,
        timeout: float = 30.0,
    ):
        self.app_id = app_id or os.getenv("EBAY_APP_ID")
        self.cert_id = cert_id or os.getenv("EBAY_CERT_ID")
        self.refresh_token = refresh_token or os.getenv("EBAY_REFRESH_TOKEN")
        self.environment = (environment or os.getenv("EBAY_ENVIRONMENT") or "SANDBOX").upper()
        self.timeout = timeout

        if not self.app_id or not self.cert_id or not self.refresh_token:
            raise EbayOAuthError(
                "Missing EBAY_APP_ID, EBAY_CERT_ID, or EBAY_REFRESH_TOKEN environment variables"
            )

        self.base_url = (
            "https://api.sandbox.ebay.com" if self.environment == "SANDBOX" else "https://api.ebay.com"
        )
        self._access_token: Optional[str] = None
        self._access_token_exp: float = 0.0

    def _token_endpoint(self) -> str:
        return f"{self.base_url}/identity/v1/oauth2/token"

    def _get_access_token(self) -> str:
        now = time.time()
        if self._access_token and now < (self._access_token_exp - 30):
            return self._access_token

        auth = requests.auth.HTTPBasicAuth(self.app_id, self.cert_id)
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        resp = requests.post(self._token_endpoint(), auth=auth, data=data, headers=headers, timeout=self.timeout)
        if resp.status_code >= 400:
            raise EbayOAuthError(f"Token refresh failed: {resp.status_code} {resp.text}")
        payload = resp.json()
        token = payload.get("access_token")
        expires_in = payload.get("expires_in", 0)
        if not token:
            raise EbayOAuthError(f"Token refresh response missing access_token: {payload}")
        self._access_token = token
        self._access_token_exp = now + float(expires_in)
        return token

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Any = None,
        headers: Optional[Dict[str, str]] = None,
        accept: str = "application/json",
        content_type: Optional[str] = None,
    ) -> Tuple[int, Dict[str, Any] | list | str | None, Dict[str, str]]:
        url = f"{self.base_url}{path}"
        h = {"Authorization": f"Bearer {self._get_access_token()}", "Accept": accept}
        if headers:
            h.update({k: v for k, v in headers.items() if v is not None})
        if content_type:
            h["Content-Type"] = content_type

        resp = requests.request(
            method.upper(),
            url,
            params=params,
            json=json,
            headers=h,
            timeout=self.timeout,
        )

        resp_headers = {k.lower(): v for k, v in resp.headers.items()}
        if resp.status_code == 204:
            return resp.status_code, None, resp_headers

        ctype = resp.headers.get("Content-Type", "")
        if "application/json" in ctype:
            try:
                body = resp.json()
            except Exception:
                body = resp.text
        else:
            body = resp.text

        return resp.status_code, body, resp_headers

    def ok_or_error(self, status: int, body: Any, headers: Dict[str, str]) -> Any:
        if 200 <= status < 300:
            # include location header when present (common for task creation)
            if isinstance(body, dict) and "location" in headers:
                body = {**body, "location": headers.get("location")}
            elif body is None and "location" in headers:
                body = {"location": headers.get("location")}
            return body
        return {"error": body, "status": status}
