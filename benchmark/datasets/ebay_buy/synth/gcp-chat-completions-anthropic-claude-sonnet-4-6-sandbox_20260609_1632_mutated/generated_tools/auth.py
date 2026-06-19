"""
eBay OAuth 2.0 Client Credentials authentication helper.
Manages token acquisition and caching for the Buy API.
"""

from __future__ import annotations
import os
import time
import base64
import requests

_token_cache: dict = {"access_token": None, "expires_at": 0}


def get_base_url() -> str:
    """Return the correct eBay API base URL based on EBAY_ENVIRONMENT."""
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    if env == "PRODUCTION":
        return "https://api.ebay.com"
    return "https://api.sandbox.ebay.com"


def get_order_base_url() -> str:
    """Return the correct eBay Order API base URL (uses apix subdomain)."""
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    if env == "PRODUCTION":
        return "https://apix.ebay.com"
    return "https://apix.sandbox.ebay.com"


def _fetch_token() -> str:
    """Fetch a new OAuth application token using client credentials grant."""
    app_id = os.environ.get("EBAY_APP_ID", "")
    cert_id = os.environ.get("EBAY_CERT_ID", "")
    if not app_id or not cert_id:
        raise ValueError(
            "EBAY_APP_ID and EBAY_CERT_ID environment variables must be set."
        )

    credentials = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    if env == "PRODUCTION":
        token_url = "https://api.ebay.com/identity/v1/oauth2/token"
    else:
        token_url = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"

    headers = {
        "Authorization": f"Basic {credentials}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "client_credentials",
        "scope": (
            "https://api.ebay.com/oauth/api_scope "
            "https://api.ebay.com/oauth/api_scope/buy.item.feed "
            "https://api.ebay.com/oauth/api_scope/buy.marketing "
            "https://api.ebay.com/oauth/api_scope/buy.deal "
            "https://api.ebay.com/oauth/api_scope/buy.guest.order "
            "https://api.ebay.com/oauth/api_scope/buy.item.bulk"
        ),
    }

    resp = requests.post(token_url, headers=headers, data=data, timeout=30)
    resp.raise_for_status()
    token_data = resp.json()
    return token_data["access_token"], int(token_data.get("expires_in", 7200))


def get_access_token() -> str:
    """Return a valid access token, refreshing if expired."""
    global _token_cache
    now = time.time()
    if _token_cache["access_token"] and now < _token_cache["expires_at"] - 60:
        return _token_cache["access_token"]

    token, expires_in = _fetch_token()
    _token_cache["access_token"] = token
    _token_cache["expires_at"] = now + expires_in
    return token


def get_auth_header() -> dict:
    """Return the Authorization header dict with a valid Bearer token."""
    return {"Authorization": f"Bearer {get_access_token()}"}
