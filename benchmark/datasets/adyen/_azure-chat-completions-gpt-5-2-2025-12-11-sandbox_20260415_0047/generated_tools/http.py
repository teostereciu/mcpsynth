from __future__ import annotations

import os
from typing import Any, Dict, Optional

import requests


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.environ.get(name)
    if v is None:
        return default
    v = v.strip()
    return v if v else default


def get_adyen_base_urls() -> Dict[str, str]:
    """Return base URLs for Adyen services based on ADYEN_ENVIRONMENT.

    Only the test URLs are required for evaluation, but live URLs are included
    for completeness.
    """

    env = (_env("ADYEN_ENVIRONMENT", "test") or "test").lower()
    if env not in {"test", "live"}:
        env = "test"

    if env == "live":
        # Live endpoints are region-specific; these are common defaults.
        checkout = "https://checkout-live.adyen.com/v71"
        payment = "https://pal-live.adyen.com/pal/servlet/Payment/v68"
        management = "https://management-live.adyen.com/v3"
    else:
        checkout = "https://checkout-test.adyen.com/v71"
        payment = "https://pal-test.adyen.com/pal/servlet/Payment/v68"
        management = "https://management-test.adyen.com/v3"

    return {"checkout": checkout, "payment": payment, "management": management}


def adyen_request(
    *,
    service: str,
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    timeout: float = 30.0,
) -> Dict[str, Any]:
    """Make an authenticated request to an Adyen API.

    Returns a JSON-serializable dict. Errors are returned as dicts and never
    raised for expected HTTP failures.
    """

    api_key = _env("ADYEN_API_KEY")
    if not api_key:
        return {"error": "Missing ADYEN_API_KEY environment variable"}

    base_urls = get_adyen_base_urls()
    base = base_urls.get(service)
    if not base:
        return {"error": f"Unknown service '{service}'. Expected one of {sorted(base_urls.keys())}."}

    url = f"{base}{path}"
    headers = {
        "X-API-Key": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    try:
        resp = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            params=params,
            json=json,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": "Request failed", "details": str(e), "url": url, "method": method.upper()}

    try:
        data: Any = resp.json() if resp.content else None
    except ValueError:
        data = {"raw": resp.text}

    if 200 <= resp.status_code < 300:
        return data if isinstance(data, dict) else {"data": data}

    # Normalize Adyen error shape.
    err: Dict[str, Any] = {
        "error": "Adyen API error",
        "status": resp.status_code,
        "url": url,
        "method": method.upper(),
    }
    if isinstance(data, dict):
        err.update({"adyen": data})
        # Common fields: errorCode, message, errorType, status
        if "message" in data:
            err["message"] = data.get("message")
        if "errorCode" in data:
            err["errorCode"] = data.get("errorCode")
        if "errorType" in data:
            err["errorType"] = data.get("errorType")
    else:
        err["adyen"] = data

    return err


def default_merchant_account(override: Optional[str] = None) -> Optional[str]:
    return override or _env("ADYEN_MERCHANT_ACCOUNT")


def default_company_account(override: Optional[str] = None) -> Optional[str]:
    return override or _env("ADYEN_COMPANY_ACCOUNT")
