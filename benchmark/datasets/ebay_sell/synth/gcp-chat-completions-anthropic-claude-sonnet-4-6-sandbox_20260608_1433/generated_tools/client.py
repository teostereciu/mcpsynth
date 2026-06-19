"""Shared HTTP client for eBay Sell API with OAuth 2.0 authentication."""
import os
import time
import requests

_token_cache = {"access_token": None, "expires_at": 0}


def _get_base_url() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    if env == "PRODUCTION":
        return "https://api.ebay.com"
    return "https://api.sandbox.ebay.com"


def _get_access_token() -> str:
    """Obtain a user access token using the refresh token grant."""
    now = time.time()
    if _token_cache["access_token"] and now < _token_cache["expires_at"] - 60:
        return _token_cache["access_token"]

    app_id = os.environ["EBAY_APP_ID"]
    cert_id = os.environ["EBAY_CERT_ID"]
    refresh_token = os.environ["EBAY_REFRESH_TOKEN"]
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()

    token_url = (
        "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
        if env != "PRODUCTION"
        else "https://api.ebay.com/identity/v1/oauth2/token"
    )

    resp = requests.post(
        token_url,
        auth=(app_id, cert_id),
        data={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "scope": (
                "https://api.ebay.com/oauth/api_scope/sell.inventory "
                "https://api.ebay.com/oauth/api_scope/sell.account "
                "https://api.ebay.com/oauth/api_scope/sell.fulfillment "
                "https://api.ebay.com/oauth/api_scope/sell.marketing "
                "https://api.ebay.com/oauth/api_scope/sell.finances "
                "https://api.ebay.com/oauth/api_scope/sell.analytics.readonly "
                "https://api.ebay.com/oauth/api_scope/sell.feed "
                "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription"
            ),
        },
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    _token_cache["access_token"] = data["access_token"]
    _token_cache["expires_at"] = now + data.get("expires_in", 7200)
    return _token_cache["access_token"]


class EbayClient:
    def __init__(self):
        self.base_url = _get_base_url()
        self.session = requests.Session()

    def request(self, method: str, path: str, **kwargs) -> dict:
        token = _get_access_token()
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {token}"
        headers["Accept"] = "application/json"
        if method in ("POST", "PUT", "PATCH") and "json" in kwargs:
            headers["Content-Type"] = "application/json"

        url = self.base_url + path
        try:
            resp = self.session.request(method, url, headers=headers, timeout=30, **kwargs)
            if resp.status_code == 204:
                return {"status": "success", "http_status": 204}
            if not resp.content:
                return {"status": "success", "http_status": resp.status_code}
            try:
                data = resp.json()
            except Exception:
                data = {"raw": resp.text}
            if not resp.ok:
                return {"error": data, "http_status": resp.status_code}
            return data
        except requests.RequestException as e:
            return {"error": str(e)}


_client_instance = None


def get_client() -> EbayClient:
    global _client_instance
    if _client_instance is None:
        _client_instance = EbayClient()
    return _client_instance
