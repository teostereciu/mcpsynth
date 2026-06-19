"""
eBay OAuth2 authentication helper.
Handles token acquisition and caching using the refresh token flow.
"""

import os
import time
import base64
import requests

_token_cache: dict = {"access_token": None, "expires_at": 0}

SANDBOX_BASE = "https://api.sandbox.ebay.com"
PRODUCTION_BASE = "https://api.ebay.com"


def get_base_url() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return PRODUCTION_BASE if env == "PRODUCTION" else SANDBOX_BASE


def get_access_token() -> str:
    """Return a valid access token, refreshing if necessary."""
    now = time.time()
    if _token_cache["access_token"] and now < _token_cache["expires_at"] - 60:
        return _token_cache["access_token"]

    app_id = os.environ.get("EBAY_APP_ID", "")
    cert_id = os.environ.get("EBAY_CERT_ID", "")
    refresh_token = os.environ.get("EBAY_REFRESH_TOKEN", "")

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
    _token_cache["expires_at"] = now + int(data.get("expires_in", 7200))
    return _token_cache["access_token"]


def ebay_request(
    method: str,
    path: str,
    *,
    params: dict | None = None,
    json: dict | None = None,
    data: str | None = None,
    extra_headers: dict | None = None,
) -> dict | list | str:
    """
    Internal HTTP helper — NOT exposed as an MCP tool.
    Makes an authenticated request to the eBay API and returns parsed JSON
    or an error dict.
    """
    token = get_access_token()
    base_url = get_base_url()
    url = f"{base_url}{path}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if extra_headers:
        headers.update(extra_headers)

    try:
        resp = requests.request(
            method,
            url,
            headers=headers,
            params=params,
            json=json,
            data=data,
            timeout=60,
        )
        if resp.status_code == 204 or not resp.content:
            return {"status": "success", "http_status": resp.status_code}
        try:
            return resp.json()
        except Exception:
            return {"status": "success", "body": resp.text, "http_status": resp.status_code}
    except requests.exceptions.RequestException as exc:
        return {"error": str(exc)}
