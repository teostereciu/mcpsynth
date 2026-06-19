"""Shared HTTP utilities for Adyen API calls.

All tool functions should call `adyen_request` and return JSON-serializable dict/list.
"""

from __future__ import annotations

import os
from typing import Any, Dict, Optional

import requests


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.environ.get(name)
    return v if v not in (None, "") else default


def adyen_base_urls() -> Dict[str, str]:
    """Return base URLs for the configured environment."""
    env = (_env("ADYEN_ENVIRONMENT", "test") or "test").lower()
    if env not in {"test", "live"}:
        env = "test"

    if env == "live":
        # Live URLs vary by region; allow override via env vars.
        return {
            "checkout": _env("ADYEN_CHECKOUT_BASE_URL", "https://checkout-live.adyenpayments.com/v71") or "",
            "payment": _env("ADYEN_PAYMENT_BASE_URL", "https://pal-live.adyen.com/pal/servlet/Payment/v68") or "",
            "management": _env("ADYEN_MANAGEMENT_BASE_URL", "https://management-live.adyen.com/v3") or "",
            "balanceplatform": _env("ADYEN_BALANCEPLATFORM_BASE_URL", "https://balanceplatform-api-live.adyen.com/bcl/v2")
            or "",
            "transfers": _env("ADYEN_TRANSFERS_BASE_URL", "https://balanceplatform-api-live.adyen.com/transfers/v4")
            or "",
            "legalentity": _env("ADYEN_LEGALENTITY_BASE_URL", "https://balanceplatform-api-live.adyen.com/legalentity/v4")
            or "",
            "capital": _env("ADYEN_CAPITAL_BASE_URL", "https://balanceplatform-api-live.adyen.com/capital/v1") or "",
            "foreignexchange": _env(
                "ADYEN_FOREIGNEXCHANGE_BASE_URL", "https://balanceplatform-api-live.adyen.com/foreignexchange/v1"
            )
            or "",
        }

    return {
        "checkout": "https://checkout-test.adyen.com/v71",
        "payment": "https://pal-test.adyen.com/pal/servlet/Payment/v68",
        "management": "https://management-test.adyen.com/v3",
        "balanceplatform": "https://balanceplatform-api-test.adyen.com/bcl/v2",
        "transfers": "https://balanceplatform-api-test.adyen.com/transfers/v4",
        "legalentity": "https://balanceplatform-api-test.adyen.com/legalentity/v4",
        "capital": "https://balanceplatform-api-test.adyen.com/capital/v1",
        "foreignexchange": "https://balanceplatform-api-test.adyen.com/foreignexchange/v1",
    }


def adyen_request(
    *,
    method: str,
    base_url: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    timeout: float = 30.0,
) -> Dict[str, Any]:
    """Make an authenticated request to an Adyen API.

    Returns either the parsed JSON response, or a dict with `error` fields.
    """
    api_key = _env("ADYEN_API_KEY")
    if not api_key:
        return {"error": "Missing ADYEN_API_KEY environment variable"}

    url = f"{base_url}{path}"
    headers = {
        "X-API-Key": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    try:
        resp = requests.request(method=method.upper(), url=url, headers=headers, params=params, json=json, timeout=timeout)
    except requests.RequestException as e:
        return {"error": "request_failed", "message": str(e), "url": url}

    content_type = (resp.headers.get("Content-Type") or "").lower()
    data: Any
    if "application/json" in content_type:
        try:
            data = resp.json()
        except ValueError:
            data = {"raw": resp.text}
    else:
        data = {"raw": resp.text}

    if 200 <= resp.status_code < 300:
        return data if isinstance(data, dict) else {"data": data}

    # Normalize error shape.
    err: Dict[str, Any] = {
        "error": "adyen_api_error",
        "status": resp.status_code,
        "url": url,
    }
    if isinstance(data, dict):
        err.update({k: v for k, v in data.items() if k not in {"status"}})
        err.setdefault("message", data.get("message") or data.get("errorMessage") or resp.reason)
        err.setdefault("errorCode", data.get("errorCode") or data.get("code"))
    else:
        err["message"] = resp.text
    return err
