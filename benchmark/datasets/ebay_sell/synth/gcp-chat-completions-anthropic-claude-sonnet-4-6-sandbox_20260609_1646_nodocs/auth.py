"""
eBay OAuth2 token management.
Fetches and caches a user access token using the refresh token grant.
"""

import os
import time
import base64
import requests

_token_cache: dict = {"access_token": None, "expires_at": 0}

SANDBOX_BASE = "https://api.sandbox.ebay.com"
PRODUCTION_BASE = "https://api.ebay.com"


def get_base_url() -> str:
    env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return PRODUCTION_BASE if env == "PRODUCTION" else SANDBOX_BASE


def get_access_token() -> str:
    """Return a valid access token, refreshing if necessary."""
    now = time.time()
    if _token_cache["access_token"] and now < _token_cache["expires_at"] - 60:
        return _token_cache["access_token"]

    app_id = os.getenv("EBAY_APP_ID", "")
    cert_id = os.getenv("EBAY_CERT_ID", "")
    refresh_token = os.getenv("EBAY_REFRESH_TOKEN", "")

    credentials = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
    base_url = get_base_url()

    resp = requests.post(
        f"{base_url}/identity/v1/oauth2/token",
        headers={
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        },
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    _token_cache["access_token"] = data["access_token"]
    _token_cache["expires_at"] = now + data.get("expires_in", 7200)
    return _token_cache["access_token"]


def auth_headers(extra: dict | None = None) -> dict:
    """Return Authorization + JSON content-type headers."""
    headers = {
        "Authorization": f"Bearer {get_access_token()}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if extra:
        headers.update(extra)
    return headers


def api_get(path: str, params: dict | None = None) -> dict:
    url = f"{get_base_url()}{path}"
    try:
        r = requests.get(url, headers=auth_headers(), params=params, timeout=30)
        if r.status_code == 204:
            return {"success": True}
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json() if r.text else {"success": True}
    except Exception as e:
        return {"error": str(e)}


def api_post(path: str, body: dict | None = None, params: dict | None = None) -> dict:
    url = f"{get_base_url()}{path}"
    try:
        r = requests.post(url, headers=auth_headers(), json=body, params=params, timeout=30)
        if r.status_code in (200, 201, 204):
            return r.json() if r.text else {"success": True}
        return {"error": r.text, "status_code": r.status_code}
    except Exception as e:
        return {"error": str(e)}


def api_put(path: str, body: dict | None = None, params: dict | None = None) -> dict:
    url = f"{get_base_url()}{path}"
    try:
        r = requests.put(url, headers=auth_headers(), json=body, params=params, timeout=30)
        if r.status_code in (200, 201, 204):
            return r.json() if r.text else {"success": True}
        return {"error": r.text, "status_code": r.status_code}
    except Exception as e:
        return {"error": str(e)}


def api_delete(path: str, params: dict | None = None) -> dict:
    url = f"{get_base_url()}{path}"
    try:
        r = requests.delete(url, headers=auth_headers(), params=params, timeout=30)
        if r.status_code in (200, 204):
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}
    except Exception as e:
        return {"error": str(e)}


def api_patch(path: str, body: dict | None = None, params: dict | None = None) -> dict:
    url = f"{get_base_url()}{path}"
    try:
        r = requests.patch(url, headers=auth_headers(), json=body, params=params, timeout=30)
        if r.status_code in (200, 201, 204):
            return r.json() if r.text else {"success": True}
        return {"error": r.text, "status_code": r.status_code}
    except Exception as e:
        return {"error": str(e)}
