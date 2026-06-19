"""HTTP utilities for Shopify Admin REST API (2026-01)."""

from __future__ import annotations

import os
from typing import Any, Dict, Optional

import requests


API_VERSION = "2026-01"


def _base_url() -> str:
    store_url = os.environ.get("SHOPIFY_STORE_URL")
    if not store_url:
        raise RuntimeError("Missing env var SHOPIFY_STORE_URL")
    return f"https://{store_url}/admin/api/{API_VERSION}"


def shopify_request(
    method: str,
    endpoint: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    body: Optional[Dict[str, Any]] = None,
    timeout: float = 60.0,
) -> Dict[str, Any]:
    """Make an authenticated request to Shopify Admin REST API.

    Returns a JSON dict. On HTTP errors, returns {"error": ..., "status_code": ...}.
    """

    access_token = os.environ.get("SHOPIFY_ACCESS_TOKEN")
    if not access_token:
        return {"error": "Missing env var SHOPIFY_ACCESS_TOKEN", "status_code": 401}

    if not endpoint.startswith("/"):
        endpoint = "/" + endpoint

    url = _base_url() + endpoint
    headers = {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    try:
        resp = requests.request(
            method.upper(),
            url,
            headers=headers,
            params=params,
            json=body,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": f"Request failed: {e.__class__.__name__}: {e}", "status_code": 0}

    if not resp.ok:
        # Shopify often returns JSON error bodies; keep raw text for clarity.
        return {"error": resp.text, "status_code": resp.status_code}

    if resp.status_code == 204:
        return {"ok": True}

    try:
        return resp.json()
    except ValueError:
        return {"error": "Non-JSON response from Shopify", "status_code": resp.status_code, "text": resp.text}


def unwrap_envelope(data: Dict[str, Any]) -> Any:
    """Unwrap Shopify REST envelope when response is {"resource": ...}.

    If the dict has exactly one top-level key, returns its value.
    Otherwise returns the original dict.
    """

    if isinstance(data, dict) and len(data) == 1:
        return next(iter(data.values()))
    return data
