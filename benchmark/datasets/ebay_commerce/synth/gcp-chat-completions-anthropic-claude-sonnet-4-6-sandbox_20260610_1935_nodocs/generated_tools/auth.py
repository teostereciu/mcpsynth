"""
eBay OAuth 2.0 authentication helpers.
Provides app-token (client_credentials) and user-token (refresh_token) flows.
Tokens are cached in-process to avoid redundant round-trips.
"""

import os
import time
import base64
import requests

# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------

def _base_url() -> str:
    env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
    if env == "PRODUCTION":
        return "https://api.ebay.com"
    return "https://api.sandbox.ebay.com"


def _media_base_url() -> str:
    env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
    if env == "PRODUCTION":
        return "https://apim.ebay.com"
    return "https://apim.sandbox.ebay.com"


# ---------------------------------------------------------------------------
# Token cache
# ---------------------------------------------------------------------------

_app_token_cache: dict = {}   # {"token": str, "expires_at": float}
_user_token_cache: dict = {}  # {"token": str, "expires_at": float}


def _basic_auth_header() -> str:
    app_id = os.getenv("EBAY_APP_ID", "")
    cert_id = os.getenv("EBAY_CERT_ID", "")
    creds = f"{app_id}:{cert_id}"
    encoded = base64.b64encode(creds.encode()).decode()
    return f"Basic {encoded}"


def get_app_token() -> str:
    """Return a valid app-level OAuth token (client_credentials grant)."""
    now = time.time()
    if _app_token_cache.get("token") and _app_token_cache.get("expires_at", 0) > now + 60:
        return _app_token_cache["token"]

    url = f"{_base_url()}/identity/v1/oauth2/token"
    headers = {
        "Authorization": _basic_auth_header(),
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope",
    }
    resp = requests.post(url, headers=headers, data=data, timeout=30)
    resp.raise_for_status()
    payload = resp.json()
    _app_token_cache["token"] = payload["access_token"]
    _app_token_cache["expires_at"] = now + int(payload.get("expires_in", 7200))
    return _app_token_cache["token"]


def get_user_token() -> str:
    """Return a valid user-level OAuth token (refresh_token grant)."""
    now = time.time()
    if _user_token_cache.get("token") and _user_token_cache.get("expires_at", 0) > now + 60:
        return _user_token_cache["token"]

    refresh_token = os.getenv("EBAY_REFRESH_TOKEN", "")
    url = f"{_base_url()}/identity/v1/oauth2/token"
    headers = {
        "Authorization": _basic_auth_header(),
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
    }
    resp = requests.post(url, headers=headers, data=data, timeout=30)
    resp.raise_for_status()
    payload = resp.json()
    _user_token_cache["token"] = payload["access_token"]
    _user_token_cache["expires_at"] = now + int(payload.get("expires_in", 7200))
    return _user_token_cache["token"]


# ---------------------------------------------------------------------------
# Convenience request helpers
# ---------------------------------------------------------------------------

def app_get(path: str, params: dict | None = None) -> dict:
    token = get_app_token()
    url = f"{_base_url()}{path}"
    resp = requests.get(url, headers={"Authorization": f"Bearer {token}"}, params=params, timeout=30)
    if not resp.ok:
        return {"error": resp.text, "status_code": resp.status_code}
    return resp.json() if resp.content else {}


def app_post(path: str, json_body: dict | None = None, params: dict | None = None) -> dict:
    token = get_app_token()
    url = f"{_base_url()}{path}"
    resp = requests.post(url, headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
                         json=json_body, params=params, timeout=30)
    if not resp.ok:
        return {"error": resp.text, "status_code": resp.status_code}
    return resp.json() if resp.content else {}


def user_get(path: str, params: dict | None = None, media: bool = False) -> dict:
    token = get_user_token()
    base = _media_base_url() if media else _base_url()
    url = f"{base}{path}"
    resp = requests.get(url, headers={"Authorization": f"Bearer {token}"}, params=params, timeout=30)
    if not resp.ok:
        return {"error": resp.text, "status_code": resp.status_code}
    return resp.json() if resp.content else {}


def user_post(path: str, json_body: dict | None = None, params: dict | None = None, media: bool = False) -> dict:
    token = get_user_token()
    base = _media_base_url() if media else _base_url()
    url = f"{base}{path}"
    resp = requests.post(url, headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
                         json=json_body, params=params, timeout=30)
    if not resp.ok:
        return {"error": resp.text, "status_code": resp.status_code}
    return resp.json() if resp.content else {}


def user_put(path: str, json_body: dict | None = None, params: dict | None = None, media: bool = False) -> dict:
    token = get_user_token()
    base = _media_base_url() if media else _base_url()
    url = f"{base}{path}"
    resp = requests.put(url, headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
                        json=json_body, params=params, timeout=30)
    if not resp.ok:
        return {"error": resp.text, "status_code": resp.status_code}
    return resp.json() if resp.content else {}


def user_delete(path: str, params: dict | None = None, media: bool = False) -> dict:
    token = get_user_token()
    base = _media_base_url() if media else _base_url()
    url = f"{base}{path}"
    resp = requests.delete(url, headers={"Authorization": f"Bearer {token}"}, params=params, timeout=30)
    if not resp.ok:
        return {"error": resp.text, "status_code": resp.status_code}
    return {"deleted": True} if resp.status_code in (200, 204) else resp.json()


def user_patch(path: str, json_body: dict | None = None, params: dict | None = None, media: bool = False) -> dict:
    token = get_user_token()
    base = _media_base_url() if media else _base_url()
    url = f"{base}{path}"
    resp = requests.patch(url, headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
                          json=json_body, params=params, timeout=30)
    if not resp.ok:
        return {"error": resp.text, "status_code": resp.status_code}
    return resp.json() if resp.content else {}
