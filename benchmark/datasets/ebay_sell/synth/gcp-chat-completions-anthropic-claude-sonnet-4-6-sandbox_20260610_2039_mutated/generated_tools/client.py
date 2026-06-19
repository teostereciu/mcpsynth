"""Shared HTTP client for eBay Sell API with OAuth 2.0 token management."""
import os
import time
import requests
from typing import Any, Optional


class EbayClient:
    """HTTP client that handles OAuth token refresh and request execution."""

    SANDBOX_BASE = "https://api.sandbox.ebay.com"
    PRODUCTION_BASE = "https://api.ebay.com"
    TOKEN_URL_SANDBOX = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
    TOKEN_URL_PRODUCTION = "https://api.ebay.com/identity/v1/oauth2/token"

    def __init__(self):
        self.app_id = os.environ.get("EBAY_APP_ID", "")
        self.cert_id = os.environ.get("EBAY_CERT_ID", "")
        self.refresh_token = os.environ.get("EBAY_REFRESH_TOKEN", "")
        env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
        if env == "PRODUCTION":
            self.base_url = self.PRODUCTION_BASE
            self.token_url = self.TOKEN_URL_PRODUCTION
        else:
            self.base_url = self.SANDBOX_BASE
            self.token_url = self.TOKEN_URL_SANDBOX

        self._access_token: Optional[str] = None
        self._token_expiry: float = 0.0

    def _get_access_token(self) -> str:
        """Obtain a fresh access token using the refresh token grant."""
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
        resp.raise_for_status()
        data = resp.json()
        self._access_token = data["access_token"]
        self._token_expiry = time.time() + data.get("expires_in", 7200)
        return self._access_token

    def request(
        self,
        method: str,
        path: str,
        params: Optional[dict] = None,
        json: Optional[dict] = None,
        headers: Optional[dict] = None,
        files: Optional[dict] = None,
    ) -> Any:
        """Execute an authenticated HTTP request and return parsed JSON or error dict."""
        try:
            token = self._get_access_token()
        except Exception as e:
            return {"error": f"Failed to obtain access token: {str(e)}"}

        url = self.base_url + path
        req_headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }
        if json is not None and files is None:
            req_headers["Content-Type"] = "application/json"
        if headers:
            req_headers.update(headers)

        try:
            response = requests.request(
                method=method,
                url=url,
                params=params,
                json=json,
                headers=req_headers,
                files=files,
                timeout=60,
            )
        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {str(e)}"}

        # Handle empty responses (204 No Content, etc.)
        if response.status_code in (204, 202) and not response.content:
            return {"status": response.status_code, "message": "Success (no content)"}

        # Try to parse JSON
        try:
            result = response.json()
        except ValueError:
            if response.ok:
                return {"status": response.status_code, "content": response.text[:2000]}
            return {"error": f"HTTP {response.status_code}: {response.text[:500]}"}

        if not response.ok:
            return {"error": f"HTTP {response.status_code}", "details": result}

        return result


# Module-level singleton
_client: Optional[EbayClient] = None


def get_client() -> EbayClient:
    """Return the shared EbayClient singleton."""
    global _client
    if _client is None:
        _client = EbayClient()
    return _client
