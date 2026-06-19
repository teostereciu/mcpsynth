"""Shared HTTP + OAuth helpers for eBay Buy APIs."""

from __future__ import annotations

import base64
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests


class EbayApiError(Exception):
    """Internal exception used for control flow; tools must catch and return errors."""


def _env(name: str, default: Optional[str] = None) -> str:
    val = os.environ.get(name, default)
    if val is None or val == "":
        raise EbayApiError(f"Missing required environment variable: {name}")
    return val


def get_base_url() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return "https://api.sandbox.ebay.com" if env == "SANDBOX" else "https://api.ebay.com"


@dataclass
class OAuthToken:
    access_token: str
    expires_at: float


_TOKEN_CACHE: Optional[OAuthToken] = None


def get_application_token(scope: str = "https://api.ebay.com/oauth/api_scope") -> str:
    """Get OAuth application token for Buy APIs (client credentials). Cached in-process."""
    global _TOKEN_CACHE

    now = time.time()
    if _TOKEN_CACHE and _TOKEN_CACHE.expires_at - 30 > now:
        return _TOKEN_CACHE.access_token

    app_id = _env("EBAY_APP_ID")
    cert_id = _env("EBAY_CERT_ID")

    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    token_url = (
        "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
        if env == "SANDBOX"
        else "https://api.ebay.com/identity/v1/oauth2/token"
    )

    basic = base64.b64encode(f"{app_id}:{cert_id}".encode("utf-8")).decode("ascii")

    resp = requests.post(
        token_url,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {basic}",
        },
        data={"grant_type": "client_credentials", "scope": scope},
        timeout=30,
    )

    if resp.status_code >= 400:
        raise EbayApiError(_format_http_error(resp))

    data = resp.json()
    access_token = data.get("access_token")
    expires_in = float(data.get("expires_in", 0))
    if not access_token:
        raise EbayApiError("OAuth token response missing access_token")

    _TOKEN_CACHE = OAuthToken(access_token=access_token, expires_at=now + expires_in)
    return access_token


def _format_http_error(resp: requests.Response) -> str:
    try:
        payload = resp.json()
    except Exception:
        payload = resp.text
    return f"HTTP {resp.status_code}: {payload}"


def request_json(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    marketplace_id: str = "EBAY_US",
    extra_headers: Optional[Dict[str, str]] = None,
    scope: str = "https://api.ebay.com/oauth/api_scope",
) -> Dict[str, Any]:
    """Make an authenticated request to an eBay Buy API endpoint.

    Returns parsed JSON dict. Raises EbayApiError on HTTP errors.
    """

    token = get_application_token(scope=scope)
    url = f"{get_base_url()}{path}"

    headers: Dict[str, str] = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
    }
    if extra_headers:
        headers.update({k: v for k, v in extra_headers.items() if v is not None})

    resp = requests.request(
        method.upper(),
        url,
        headers=headers,
        params=params,
        json=json_body,
        timeout=30,
    )

    if resp.status_code >= 400:
        raise EbayApiError(_format_http_error(resp))

    if resp.status_code == 204:
        return {"status": 204}

    return resp.json()


def safe_tool_call(fn, *args, **kwargs):
    """Run a tool implementation and convert expected errors to JSON-serializable dicts."""
    try:
        return fn(*args, **kwargs)
    except EbayApiError as e:
        return {"error": str(e)}
    except requests.RequestException as e:
        return {"error": f"Network error: {e}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}
