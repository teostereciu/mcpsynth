"""Shared HTTP utilities for Adyen MCP tools."""

from __future__ import annotations

import os
from typing import Any, Dict, Optional

import requests


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.environ.get(name)
    return v if v not in (None, "") else default


def get_adyen_base_urls() -> Dict[str, str]:
    """Return base URLs for the configured environment.

    Environment variable:
      - ADYEN_ENVIRONMENT: 'test' or 'live' (default: 'test')

    Note: Live URLs often require a prefix; this implementation focuses on test usage.
    """

    env = (_env("ADYEN_ENVIRONMENT", "test") or "test").lower()
    if env not in {"test", "live"}:
        env = "test"

    if env == "test":
        return {
            "checkout": "https://checkout-test.adyen.com/v71",
            "payment": "https://pal-test.adyen.com/pal/servlet/Payment/v68",
            "management": "https://management-test.adyen.com/v3",
        }

    # Live: best-effort defaults; many accounts require a live prefix.
    return {
        "checkout": "https://checkout-live.adyen.com/v71",
        "payment": "https://pal-live.adyen.com/pal/servlet/Payment/v68",
        "management": "https://management-live.adyen.com/v3",
    }


def adyen_request(
    service: str,
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    timeout: int = 30,
) -> Dict[str, Any]:
    """Make an authenticated request to an Adyen API.

    Returns a JSON-serializable dict. Errors are returned as:
      {"error": {"message": str, "status": int|None, "details": any}}
    """

    api_key = _env("ADYEN_API_KEY")
    if not api_key:
        return {"error": {"message": "Missing ADYEN_API_KEY env var", "status": None}}

    base_urls = get_adyen_base_urls()
    base = base_urls.get(service)
    if not base:
        return {"error": {"message": f"Unknown service '{service}'", "status": None}}

    url = f"{base}{path}"
    headers = {
        "X-API-Key": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    try:
        resp = requests.request(method.upper(), url, headers=headers, params=params, json=json, timeout=timeout)
        content_type = resp.headers.get("Content-Type", "")
        data: Any
        if "application/json" in content_type:
            data = resp.json()
        else:
            data = {"raw": resp.text}

        if resp.status_code >= 400:
            return {
                "error": {
                    "message": (data.get("message") if isinstance(data, dict) else None) or resp.reason,
                    "status": resp.status_code,
                    "details": data,
                }
            }
        return data if isinstance(data, dict) else {"data": data}
    except requests.RequestException as e:
        return {"error": {"message": str(e), "status": None}}
