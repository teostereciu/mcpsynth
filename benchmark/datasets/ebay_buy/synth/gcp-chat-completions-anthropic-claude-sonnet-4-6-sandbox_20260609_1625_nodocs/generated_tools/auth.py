"""
eBay OAuth 2.0 Client Credentials token management.
Handles token acquisition and caching for application-level access.
"""

import os
import time
import base64
import requests

_token_cache: dict = {"access_token": None, "expires_at": 0.0}

SANDBOX_BASE = "https://api.sandbox.ebay.com"
PRODUCTION_BASE = "https://api.ebay.com"

SANDBOX_AUTH = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
PRODUCTION_AUTH = "https://api.ebay.com/identity/v1/oauth2/token"


def get_base_url() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return PRODUCTION_BASE if env == "PRODUCTION" else SANDBOX_BASE


def get_auth_url() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return PRODUCTION_AUTH if env == "PRODUCTION" else SANDBOX_AUTH


def get_access_token() -> str:
    """Return a valid OAuth application access token, refreshing if needed."""
    now = time.time()
    if _token_cache["access_token"] and now < _token_cache["expires_at"] - 60:
        return _token_cache["access_token"]

    app_id = os.environ.get("EBAY_APP_ID", "")
    cert_id = os.environ.get("EBAY_CERT_ID", "")
    if not app_id or not cert_id:
        raise RuntimeError(
            "EBAY_APP_ID and EBAY_CERT_ID environment variables must be set."
        )

    credentials = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
    headers = {
        "Authorization": f"Basic {credentials}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope",
    }

    resp = requests.post(get_auth_url(), headers=headers, data=data, timeout=30)
    resp.raise_for_status()
    payload = resp.json()

    _token_cache["access_token"] = payload["access_token"]
    _token_cache["expires_at"] = now + int(payload.get("expires_in", 7200))
    return _token_cache["access_token"]


def auth_headers(extra: dict | None = None) -> dict:
    """Return HTTP headers with Bearer token for eBay API calls."""
    token = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-EBAY-C-MARKETPLACE-ID": os.environ.get(
            "EBAY_MARKETPLACE_ID", "EBAY_US"
        ),
    }
    if extra:
        headers.update(extra)
    return headers


def api_get(path: str, params: dict | None = None) -> dict:
    """Perform an authenticated GET against the eBay API."""
    url = get_base_url() + path
    try:
        resp = requests.get(url, headers=auth_headers(), params=params, timeout=30)
        if not resp.ok:
            return {"error": resp.text, "status_code": resp.status_code}
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}


def api_post(path: str, body: dict | None = None, params: dict | None = None) -> dict:
    """Perform an authenticated POST against the eBay API."""
    url = get_base_url() + path
    try:
        resp = requests.post(
            url, headers=auth_headers(), json=body, params=params, timeout=30
        )
        if not resp.ok:
            return {"error": resp.text, "status_code": resp.status_code}
        if resp.status_code == 204 or not resp.content:
            return {"success": True}
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}


def api_put(path: str, body: dict | None = None, params: dict | None = None) -> dict:
    """Perform an authenticated PUT against the eBay API."""
    url = get_base_url() + path
    try:
        resp = requests.put(
            url, headers=auth_headers(), json=body, params=params, timeout=30
        )
        if not resp.ok:
            return {"error": resp.text, "status_code": resp.status_code}
        if resp.status_code == 204 or not resp.content:
            return {"success": True}
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}


def api_delete(path: str, params: dict | None = None) -> dict:
    """Perform an authenticated DELETE against the eBay API."""
    url = get_base_url() + path
    try:
        resp = requests.delete(
            url, headers=auth_headers(), params=params, timeout=30
        )
        if not resp.ok:
            return {"error": resp.text, "status_code": resp.status_code}
        if resp.status_code == 204 or not resp.content:
            return {"success": True}
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}
