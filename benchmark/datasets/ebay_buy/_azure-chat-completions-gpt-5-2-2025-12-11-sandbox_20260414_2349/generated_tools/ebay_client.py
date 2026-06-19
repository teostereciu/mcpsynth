"""Shared eBay Buy API client utilities (OAuth + request helpers)."""

from __future__ import annotations

import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests


class EbayApiError(Exception):
    """Internal exception used for control flow; tools should catch and return dict errors."""


def _base_url() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return "https://api.sandbox.ebay.com" if env == "SANDBOX" else "https://api.ebay.com"


def _token_url() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return (
        "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
        if env == "SANDBOX"
        else "https://api.ebay.com/identity/v1/oauth2/token"
    )


@dataclass
class _TokenCache:
    access_token: Optional[str] = None
    expires_at: float = 0.0


_TOKEN_CACHE = _TokenCache()


def get_application_token(scope: str = "https://api.ebay.com/oauth/api_scope") -> str:
    """Get OAuth application token for eBay Buy APIs (client credentials).

    Uses a simple in-process cache to avoid requesting a token for every tool call.
    """

    now = time.time()
    if _TOKEN_CACHE.access_token and now < (_TOKEN_CACHE.expires_at - 30):
        return _TOKEN_CACHE.access_token

    app_id = os.environ.get("EBAY_APP_ID")
    cert_id = os.environ.get("EBAY_CERT_ID")
    if not app_id or not cert_id:
        raise EbayApiError("Missing EBAY_APP_ID or EBAY_CERT_ID environment variables")

    resp = requests.post(
        _token_url(),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        auth=(app_id, cert_id),
        data={"grant_type": "client_credentials", "scope": scope},
        timeout=30,
    )
    if not resp.ok:
        raise EbayApiError(f"OAuth token request failed: {resp.status_code} {resp.text}")

    data = resp.json()
    _TOKEN_CACHE.access_token = data.get("access_token")
    expires_in = float(data.get("expires_in", 0))
    _TOKEN_CACHE.expires_at = now + expires_in
    if not _TOKEN_CACHE.access_token:
        raise EbayApiError("OAuth token response missing access_token")
    return _TOKEN_CACHE.access_token


def make_buy_api_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    marketplace_id: str = "EBAY_US",
    extra_headers: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Make an authenticated request to an eBay Buy API endpoint.

    Returns parsed JSON dict. Raises EbayApiError for non-2xx responses.
    """

    token = get_application_token()
    headers: Dict[str, str] = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
    }
    if extra_headers:
        headers.update(extra_headers)

    url = f"{_base_url()}{path}"
    try:
        resp = requests.request(
            method.upper(),
            url,
            headers=headers,
            params=params,
            json=json,
            timeout=30,
        )
    except requests.RequestException as e:
        raise EbayApiError(f"Network error calling eBay API: {e}") from e

    if not resp.ok:
        # Try to parse eBay error payload
        try:
            err = resp.json()
        except Exception:
            err = {"message": resp.text}
        raise EbayApiError(
            f"eBay API error {resp.status_code} for {method.upper()} {path}",
        )

    if resp.status_code == 204:
        return {"status": 204}

    try:
        return resp.json()
    except Exception as e:
        raise EbayApiError(f"Failed to parse JSON response: {e}") from e


def tool_error(message: str, *, details: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    out: Dict[str, Any] = {"error": message}
    if details:
        out["details"] = details
    return out
