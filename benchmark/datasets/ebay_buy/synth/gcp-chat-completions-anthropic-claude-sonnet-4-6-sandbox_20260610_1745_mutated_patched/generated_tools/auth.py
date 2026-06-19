"""
eBay OAuth 2.0 Client Credentials authentication helper.
Fetches and caches application access tokens.
"""

import os
import time
import base64
import requests

_token_cache: dict = {"token": None, "expires_at": 0}

SANDBOX_BASE = "https://api.sandbox.ebay.com"
PRODUCTION_BASE = "https://api.ebay.com"

SANDBOX_AUTH_URL = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
PRODUCTION_AUTH_URL = "https://api.ebay.com/identity/v1/oauth2/token"


def get_base_url() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return PRODUCTION_BASE if env == "PRODUCTION" else SANDBOX_BASE


def _get_auth_url() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return PRODUCTION_AUTH_URL if env == "PRODUCTION" else SANDBOX_AUTH_URL


def _fetch_token() -> str:
    app_id = os.environ.get("EBAY_APP_ID", "")
    cert_id = os.environ.get("EBAY_CERT_ID", "")
    if not app_id or not cert_id:
        raise ValueError("EBAY_APP_ID and EBAY_CERT_ID environment variables must be set.")

    credentials = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
    resp = requests.post(
        _get_auth_url(),
        headers={
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "client_credentials",
            "scope": (
                "https://api.ebay.com/oauth/api_scope "
                "https://api.ebay.com/oauth/api_scope/buy.deal "
                "https://api.ebay.com/oauth/api_scope/buy.item.bulk "
                "https://api.ebay.com/oauth/api_scope/buy.offer.auction "
                "https://api.ebay.com/oauth/api_scope/buy.order.readonly "
                "https://api.ebay.com/oauth/api_scope/buy.guest.order"
            ),
        },
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["access_token"], int(data.get("expires_in", 7200))


def get_access_token() -> str:
    """Return a valid OAuth access token, refreshing if expired."""
    now = time.time()
    if _token_cache["token"] and now < _token_cache["expires_at"] - 60:
        return _token_cache["token"]
    token, expires_in = _fetch_token()
    _token_cache["token"] = token
    _token_cache["expires_at"] = now + expires_in
    return token


def get_auth_headers() -> dict:
    """Return Authorization header dict with a valid Bearer token."""
    return {"Authorization": f"Bearer {get_access_token()}"}
