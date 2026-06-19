"""Shared HTTP utilities for HubSpot API calls."""

from __future__ import annotations

import os
from typing import Any, Dict, Optional

import requests

HUBSPOT_BASE = "https://api.hubapi.com"


def _get_headers() -> Dict[str, str]:
    token = os.environ.get("HUBSPOT_ACCESS_TOKEN")
    if not token:
        # Return a sentinel header; callers will get 401 from HubSpot if used.
        # But we prefer a local error.
        raise RuntimeError("Missing environment variable HUBSPOT_ACCESS_TOKEN")
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }


def _handle_response(resp: requests.Response) -> Dict[str, Any]:
    try:
        data = resp.json() if resp.text else {}
    except Exception:
        data = {"raw": resp.text}

    if resp.ok:
        return data if isinstance(data, dict) else {"data": data}

    # Normalize error shape.
    err: Dict[str, Any] = {
        "error": data.get("message") if isinstance(data, dict) else resp.text,
        "status": resp.status_code,
    }
    if isinstance(data, dict):
        err["details"] = data
    return err


def hubspot_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    timeout: int = 30,
) -> Dict[str, Any]:
    """Make an authenticated request to HubSpot.

    Returns a JSON-serializable dict. Errors are returned as dicts with `error` and `status`.
    """

    url = f"{HUBSPOT_BASE}{path}"
    try:
        headers = _get_headers()
    except RuntimeError as e:
        return {"error": str(e), "status": 0}

    try:
        resp = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            params=params or {},
            json=json,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": str(e), "status": 0}

    return _handle_response(resp)
