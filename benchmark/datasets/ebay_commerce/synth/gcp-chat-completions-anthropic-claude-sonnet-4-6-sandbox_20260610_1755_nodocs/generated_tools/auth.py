"""
eBay OAuth 2.0 authentication helpers.
Provides app token (client_credentials) and user token (refresh_token) flows.
Tokens are cached in-memory for their lifetime.
"""

import os
import time
import base64
import requests

# ── Environment ──────────────────────────────────────────────────────────────
EBAY_APP_ID      = os.environ.get("EBAY_APP_ID", "")
EBAY_CERT_ID     = os.environ.get("EBAY_CERT_ID", "")
EBAY_REFRESH_TOKEN = os.environ.get("EBAY_REFRESH_TOKEN", "")
EBAY_ENVIRONMENT = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()

# Base URLs
if EBAY_ENVIRONMENT == "PRODUCTION":
    BASE_URL  = "https://api.ebay.com"
    MEDIA_URL = "https://apim.ebay.com"
else:
    BASE_URL  = "https://api.sandbox.ebay.com"
    MEDIA_URL = "https://apim.sandbox.ebay.com"

TOKEN_URL = f"{BASE_URL}/identity/v1/oauth2/token"

# ── Token cache ───────────────────────────────────────────────────────────────
_app_token_cache: dict = {}   # {"token": str, "expires_at": float}
_user_token_cache: dict = {}  # {"token": str, "expires_at": float}


def _basic_auth_header() -> str:
    """Return the Basic auth header value for client credentials."""
    creds = f"{EBAY_APP_ID}:{EBAY_CERT_ID}"
    encoded = base64.b64encode(creds.encode()).decode()
    return f"Basic {encoded}"


def get_app_token() -> str:
    """
    Obtain (or return cached) an application-level OAuth token via
    client_credentials grant.  Used for Taxonomy and Catalog APIs.
    """
    now = time.time()
    if _app_token_cache.get("token") and _app_token_cache.get("expires_at", 0) > now + 60:
        return _app_token_cache["token"]

    resp = requests.post(
        TOKEN_URL,
        headers={
            "Authorization": _basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope",
        },
        timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()
    _app_token_cache["token"] = data["access_token"]
    _app_token_cache["expires_at"] = now + int(data.get("expires_in", 7200))
    return _app_token_cache["token"]


def get_user_token() -> str:
    """
    Obtain (or return cached) a user-level OAuth token via refresh_token grant.
    Used for Identity, Media, and Notification APIs.
    """
    now = time.time()
    if _user_token_cache.get("token") and _user_token_cache.get("expires_at", 0) > now + 60:
        return _user_token_cache["token"]

    resp = requests.post(
        TOKEN_URL,
        headers={
            "Authorization": _basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "refresh_token",
            "refresh_token": EBAY_REFRESH_TOKEN,
        },
        timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()
    _user_token_cache["token"] = data["access_token"]
    _user_token_cache["expires_at"] = now + int(data.get("expires_in", 7200))
    return _user_token_cache["token"]


def app_headers() -> dict:
    """Return request headers using the app token."""
    return {
        "Authorization": f"Bearer {get_app_token()}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def user_headers() -> dict:
    """Return request headers using the user token."""
    return {
        "Authorization": f"Bearer {get_user_token()}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def safe_json(resp: requests.Response) -> dict:
    """Return JSON body or an error dict."""
    try:
        return resp.json()
    except Exception:
        return {"error": resp.text or f"HTTP {resp.status_code}"}
