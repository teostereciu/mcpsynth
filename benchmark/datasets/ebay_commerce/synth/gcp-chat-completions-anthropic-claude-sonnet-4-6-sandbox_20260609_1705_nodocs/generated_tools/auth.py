"""
eBay OAuth 2.0 authentication helpers.
Provides app-token (client_credentials) and user-token (refresh_token) flows.
Tokens are cached in-process until they expire.
"""

import os
import time
import base64
import requests

# ── environment ──────────────────────────────────────────────────────────────
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

# ── token cache ───────────────────────────────────────────────────────────────
_app_token_cache: dict = {}
_user_token_cache: dict = {}


def _basic_auth_header() -> str:
    credentials = f"{EBAY_APP_ID}:{EBAY_CERT_ID}"
    encoded = base64.b64encode(credentials.encode()).decode()
    return f"Basic {encoded}"


def get_app_token() -> str:
    """Return a valid app-level OAuth token (client_credentials grant)."""
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
    """Return a valid user-level OAuth token (refresh_token grant)."""
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
            "scope": (
                "https://api.ebay.com/oauth/api_scope "
                "https://api.ebay.com/oauth/api_scope/commerce.identity.readonly "
                "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription "
                "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription.readonly"
            ),
        },
        timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()
    _user_token_cache["token"] = data["access_token"]
    _user_token_cache["expires_at"] = now + int(data.get("expires_in", 7200))
    return _user_token_cache["token"]


def app_headers() -> dict:
    return {"Authorization": f"Bearer {get_app_token()}", "Content-Type": "application/json"}


def user_headers() -> dict:
    return {"Authorization": f"Bearer {get_user_token()}", "Content-Type": "application/json"}


def safe_json(resp: requests.Response) -> dict | list:
    """Return parsed JSON or an error dict."""
    try:
        resp.raise_for_status()
        if resp.status_code == 204 or not resp.content:
            return {"status": "success", "http_status": resp.status_code}
        return resp.json()
    except requests.HTTPError as exc:
        try:
            detail = resp.json()
        except Exception:
            detail = resp.text
        return {"error": str(exc), "detail": detail}
    except Exception as exc:
        return {"error": str(exc)}
