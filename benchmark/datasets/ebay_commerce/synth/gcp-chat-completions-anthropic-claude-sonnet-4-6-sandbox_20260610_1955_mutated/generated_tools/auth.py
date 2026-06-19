"""
eBay OAuth token management.
Provides app tokens (client_credentials) and user tokens (refresh_token).
"""
import os
import time
import base64
import requests

_token_cache: dict = {}

EBAY_ENV = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()

if EBAY_ENV == "PRODUCTION":
    BASE_URL = "https://api.ebay.com"
    MEDIA_BASE_URL = "https://apim.ebay.com"
else:
    BASE_URL = "https://api.sandbox.ebay.com"
    MEDIA_BASE_URL = "https://apim.sandbox.ebay.com"

TOKEN_URL = f"{BASE_URL}/identity/v1/oauth2/token"


def _basic_auth() -> str:
    app_id = os.environ.get("EBAY_APP_ID", "")
    cert_id = os.environ.get("EBAY_CERT_ID", "")
    creds = f"{app_id}:{cert_id}"
    return base64.b64encode(creds.encode()).decode()


def get_app_token() -> str:
    """Obtain/cache an application-level OAuth token (client_credentials)."""
    cache_key = "app_token"
    cached = _token_cache.get(cache_key)
    if cached and cached["expires_at"] > time.time() + 60:
        return cached["token"]

    resp = requests.post(
        TOKEN_URL,
        headers={
            "Authorization": f"Basic {_basic_auth()}",
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
    """Obtain/cache a user-level OAuth token (refresh_token grant)."""
    cache_key = "user_token"
    cached = _token_cache.get(cache_key)
    if cached and cached["expires_at"] > time.time() + 60:
        return cached["token"]

    refresh_token = os.environ.get("EBAY_REFRESH_TOKEN", "")
    resp = requests.post(
        TOKEN_URL,
        headers={
            "Authorization": f"Basic {_basic_auth()}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "scope": "https://api.ebay.com/oauth/api_scope/sell.inventory "
                     "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly",
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


def app_headers(marketplace_id: str = "EBAY_US") -> dict:
    return {
        "Authorization": f"Bearer {get_app_token()}",
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }


def user_headers(marketplace_id: str = "EBAY_US") -> dict:
    return {
        "Authorization": f"Bearer {get_user_token()}",
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }


def safe_json(resp: requests.Response) -> dict:
    """Return JSON or an error dict."""
    try:
        return resp.json()
    except Exception:
        return {"error": resp.text, "status_code": resp.status_code}
