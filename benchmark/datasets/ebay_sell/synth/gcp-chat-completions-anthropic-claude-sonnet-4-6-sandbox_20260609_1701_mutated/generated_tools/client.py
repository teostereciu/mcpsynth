"""Shared HTTP client for eBay Sell API with OAuth 2.0 token management."""
import os
import time
import requests
from typing import Optional


class EbayClient:
    """HTTP client that handles OAuth token refresh and API requests."""

    TOKEN_URL = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
    PROD_TOKEN_URL = "https://api.ebay.com/identity/v1/oauth2/token"

    def __init__(self):
        self.app_id = os.environ.get("EBAY_APP_ID", "")
        self.cert_id = os.environ.get("EBAY_CERT_ID", "")
        self.refresh_token = os.environ.get("EBAY_REFRESH_TOKEN", "")
        self.environment = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()

        if self.environment == "PRODUCTION":
            self.base_url = "https://api.ebay.com"
            self.token_url = self.PROD_TOKEN_URL
        else:
            self.base_url = "https://api.sandbox.ebay.com"
            self.token_url = self.TOKEN_URL

        self._access_token: Optional[str] = None
        self._token_expiry: float = 0.0

    def _get_access_token(self) -> str:
        """Obtain or refresh the OAuth access token."""
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
                json: Optional[dict] = None, extra_headers: Optional[dict] = None) -> dict:
        """Make an authenticated API request and return the JSON response."""
        try:
            token = self._get_access_token()
        except Exception as e:
            return {"error": f"Authentication failed: {str(e)}"}

        url = self.base_url + path
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        if extra_headers:
            headers.update(extra_headers)

        try:
            resp = requests.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json,
                timeout=30,
            )
        except requests.RequestException as e:
            return {"error": f"Request failed: {str(e)}"}

        # Handle empty responses (204 No Content, etc.)
        if resp.status_code in (204, 202) or not resp.content:
            return {"status": resp.status_code, "message": "Success (no content)"}

        try:
            result = resp.json()
        except ValueError:
            # Non-JSON response (e.g., binary file download)
            return {"status": resp.status_code, "content_type": resp.headers.get("Content-Type", ""), "size": len(resp.content)}

        if not resp.ok:
            return {"error": result, "status_code": resp.status_code}

        return result


_client_instance: Optional[EbayClient] = None


def get_client() -> EbayClient:
    """Return the singleton EbayClient instance."""
    global _client_instance
    if _client_instance is None:
        _client_instance = EbayClient()
    return _client_instance
