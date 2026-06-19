"""
eBay OAuth 2.0 authentication helpers.
Provides app token (client_credentials) and user token (refresh_token) flows.
Tokens are cached in-process for their lifetime.
"""

import os
import time
import base64
import requests

_token_cache: dict = {}

def _base_url() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    if env == "PRODUCTION":
        return "https://api.ebay.com"
    return "https://api.sandbox.ebay.com"

def _media_base_url() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    if env == "PRODUCTION":
        return "https://apim.ebay.com"
    return "https://apim.sandbox.ebay.com"

def _get_credentials() -> tuple[str, str]:
    app_id = os.environ.get("EBAY_APP_ID", "")
    cert_id = os.environ.get("EBAY_CERT_ID", "")
    return app_id, cert_id

def get_app_token() -> str:
    """Obtain (or return cached) an application-level OAuth token via client_credentials grant."""
    cache_key = "app_token"
    cached = _token_cache.get(cache_key)
    if cached and cached["expires_at"] > time.time() + 60:
        return cached["token"]

    app_id, cert_id = _get_credentials()
    credentials = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
    token_url = f"{_base_url()}/identity/v1/oauth2/token"
    resp = requests.post(
        token_url,
        headers={
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope",
        },
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    _token_cache[cache_key] = {
        "token": data["access_token"],
        "expires_at": time.time() + int(data.get("expires_in", 7200)),
    }
    return data["access_token"]


def get_user_token() -> str:
    """Obtain (or return cached) a user-level OAuth token via refresh_token grant."""
    cache_key = "user_token"
    cached = _token_cache.get(cache_key)
    if cached and cached["expires_at"] > time.time() + 60:
        return cached["token"]

    app_id, cert_id = _get_credentials()
    refresh_token = os.environ.get("EBAY_REFRESH_TOKEN", "")
    credentials = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
    token_url = f"{_base_url()}/identity/v1/oauth2/token"
    resp = requests.post(
        token_url,
        headers={
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "scope": "https://api.ebay.com/oauth/api_scope/sell.inventory "
                     "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly "
                     "https://api.ebay.com/oauth/api_scope/commerce.identity.readonly",
        },
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    _token_cache[cache_key] = {
        "token": data["access_token"],
        "expires_at": time.time() + int(data.get("expires_in", 7200)),
    }
    return data["access_token"]


def app_headers(marketplace_id: str | None = None) -> dict:
    """Return headers for app-token endpoints (Taxonomy, Catalog, Charity)."""
    h = {"Authorization": f"Bearer {get_app_token()}"}
    if marketplace_id:
        h["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    return h


def user_headers(marketplace_id: str | None = None, content_type: str = "application/json") -> dict:
    """Return headers for user-token endpoints (Identity, Media, Notification)."""
    h = {
        "Authorization": f"Bearer {get_user_token()}",
        "Content-Type": content_type,
    }
    if marketplace_id:
        h["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    return h
