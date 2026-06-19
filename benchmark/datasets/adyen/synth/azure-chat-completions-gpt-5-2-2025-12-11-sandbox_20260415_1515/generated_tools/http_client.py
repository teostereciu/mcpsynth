import json
import os
from typing import Any, Dict, Optional, Tuple

import requests


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name)
    return v if v not in (None, "") else default


def adyen_environment() -> str:
    return (_env("ADYEN_ENVIRONMENT", "test") or "test").lower()


def base_urls() -> Dict[str, str]:
    env = adyen_environment()
    if env == "live":
        # Live URLs require a company-specific prefix for Checkout/Payments.
        # We keep Management API as documented.
        prefix = _env("ADYEN_LIVE_URL_PREFIX")
        checkout = f"https://{prefix}-checkout-live.adyenpayments.com/checkout"
        pal = f"https://{prefix}-pal-live.adyenpayments.com/pal/servlet/Payment"
        management = "https://management-live.adyen.com"
    else:
        checkout = "https://checkout-test.adyen.com"
        pal = "https://pal-test.adyen.com/pal/servlet/Payment"
        management = "https://management-test.adyen.com"
    return {"checkout": checkout, "pal": pal, "management": management}


def default_headers(extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    api_key = _env("ADYEN_API_KEY")
    headers = {
        "Content-Type": "application/json",
    }
    if api_key:
        headers["X-API-Key"] = api_key
    if extra:
        headers.update({k: v for k, v in extra.items() if v is not None})
    return headers


def request_json(
    method: str,
    url: str,
    *,
    headers: Optional[Dict[str, str]] = None,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    timeout: int = 60,
) -> Dict[str, Any]:
    try:
        resp = requests.request(
            method=method.upper(),
            url=url,
            headers=headers or default_headers(),
            params=params,
            json=json_body,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": str(e), "url": url}

    content_type = resp.headers.get("Content-Type", "")
    if "application/json" in content_type:
        try:
            data: Any = resp.json()
        except Exception:
            data = {"raw": resp.text}
    else:
        data = {"raw": resp.text}

    if 200 <= resp.status_code < 300:
        return {"status": resp.status_code, "data": data}

    # Expected errors should be returned, not raised.
    return {
        "error": "Adyen API request failed",
        "status": resp.status_code,
        "data": data,
        "url": url,
    }


def checkout_url(path: str, version: str = "v71") -> str:
    return base_urls()["checkout"].rstrip("/") + f"/{version}" + (path if path.startswith("/") else f"/{path}")


def pal_url(path: str, version: str = "v68") -> str:
    return base_urls()["pal"].rstrip("/") + f"/{version}" + (path if path.startswith("/") else f"/{path}")


def management_url(path: str, version: str = "v3") -> str:
    return base_urls()["management"].rstrip("/") + f"/{version}" + (path if path.startswith("/") else f"/{path}")


def merchant_account(default: Optional[str] = None) -> Optional[str]:
    return _env("ADYEN_MERCHANT_ACCOUNT", default)


def company_account(default: Optional[str] = None) -> Optional[str]:
    return _env("ADYEN_COMPANY_ACCOUNT", default)
