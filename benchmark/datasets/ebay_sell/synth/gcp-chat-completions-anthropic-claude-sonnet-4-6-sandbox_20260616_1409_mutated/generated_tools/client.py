"""Shared HTTP client for eBay Sell API with OAuth 2.0 token management."""
import os
import time
import threading
from typing import Any, Optional
import requests


class EbayClient:
    """Thread-safe eBay API client with automatic token refresh."""

    TOKEN_URL = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
    PROD_TOKEN_URL = "https://api.ebay.com/identity/v1/oauth2/token"

    def __init__(self):
        self.app_id = os.environ.get("EBAY_APP_ID", "")
        self.cert_id = os.environ.get("EBAY_CERT_ID", "")
        self.refresh_token = os.environ.get("EBAY_REFRESH_TOKEN", "")
        env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
        if env == "PRODUCTION":
            self.base_url = "https://api.ebay.com"
            self.token_url = self.PROD_TOKEN_URL
        else:
            self.base_url = "https://api.sandbox.ebay.com"
            self.token_url = self.TOKEN_URL

        self._access_token: Optional[str] = None
        self._token_expiry: float = 0.0
        self._lock = threading.Lock()

    def _get_access_token(self) -> str:
        """Obtain or refresh the OAuth access token."""
        with self._lock:
            if self._access_token and time.time() < self._token_expiry - 60:
                return self._access_token

            resp = requests.post(
                self.token_url,
                auth=(self.app_id, self.cert_id),
                data={
                    "grant_type": "refresh_token",
                    "refresh_token": self.refresh_token,
                },
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=30,
            )
            if not resp.ok:
                raise RuntimeError(f"Token refresh failed: {resp.status_code} {resp.text}")
            data = resp.json()
            self._access_token = data["access_token"]
            self._token_expiry = time.time() + data.get("expires_in", 7200)
            return self._access_token

    def request(self, method: str, path: str, params: Optional[dict] = None,
                json: Optional[dict] = None, extra_headers: Optional[dict] = None,
                files: Optional[dict] = None) -> Any:
        """Make an authenticated request to the eBay API."""
        try:
            token = self._get_access_token()
        except Exception as e:
            return {"error": f"Authentication failed: {str(e)}"}

        url = self.base_url + path
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }
        if json is not None and files is None:
            headers["Content-Type"] = "application/json"
        if extra_headers:
            headers.update(extra_headers)

        try:
            resp = requests.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json,
                files=files,
                timeout=60,
            )
        except requests.RequestException as e:
            return {"error": f"Request failed: {str(e)}"}

        # Handle no-content responses
        if resp.status_code in (204, 202) and not resp.content:
            return {"status": resp.status_code, "message": "Success (no content)"}

        # Try to parse JSON
        try:
            return resp.json()
        except ValueError:
            if resp.ok:
                return {"status": resp.status_code, "content": resp.text[:2000]}
            return {"error": f"HTTP {resp.status_code}", "detail": resp.text[:2000]}


_client_instance: Optional[EbayClient] = None


def get_client() -> EbayClient:
    """Return the singleton EbayClient instance."""
    global _client_instance
    if _client_instance is None:
        _client_instance = EbayClient()
    return _client_instance
