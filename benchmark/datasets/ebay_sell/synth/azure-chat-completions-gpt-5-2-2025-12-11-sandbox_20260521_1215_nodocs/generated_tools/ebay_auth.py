import os
import time
import requests


class EbayAuth:
    """OAuth2 refresh-token flow for eBay Sell APIs."""

    def __init__(self):
        self.app_id = os.getenv("EBAY_APP_ID", "")
        self.cert_id = os.getenv("EBAY_CERT_ID", "")
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN", "")
        self.environment = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
        self._access_token = None
        self._expires_at = 0

    @property
    def base_url(self) -> str:
        return "https://api.ebay.com" if self.environment == "PRODUCTION" else "https://api.sandbox.ebay.com"

    @property
    def oauth_url(self) -> str:
        # OAuth token endpoint is the same for sandbox/prod in practice, but keep consistent with environment.
        return "https://api.ebay.com/identity/v1/oauth2/token" if self.environment == "PRODUCTION" else "https://api.sandbox.ebay.com/identity/v1/oauth2/token"

    def _basic_auth_header(self) -> str:
        import base64

        token = base64.b64encode(f"{self.app_id}:{self.cert_id}".encode("utf-8")).decode("ascii")
        return f"Basic {token}"

    def get_access_token(self) -> str:
        now = int(time.time())
        if self._access_token and now < self._expires_at - 30:
            return self._access_token

        if not (self.app_id and self.cert_id and self.refresh_token):
            raise RuntimeError("Missing EBAY_APP_ID/EBAY_CERT_ID/EBAY_REFRESH_TOKEN env vars")

        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            # Broad scopes for Sell APIs; eBay accepts space-delimited scopes.
            "scope": " ".join(
                [
                    "https://api.ebay.com/oauth/api_scope",
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
                    "https://api.ebay.com/oauth/api_scope/sell.account",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                    "https://api.ebay.com/oauth/api_scope/sell.finances",
                    "https://api.ebay.com/oauth/api_scope/sell.feed",
                ]
            ),
        }
        resp = requests.post(self.oauth_url, headers=headers, data=data, timeout=30)
        if resp.status_code >= 400:
            raise RuntimeError(f"OAuth token error {resp.status_code}: {resp.text}")
        payload = resp.json()
        self._access_token = payload.get("access_token")
        expires_in = int(payload.get("expires_in", 7200))
        self._expires_at = now + expires_in
        return self._access_token
