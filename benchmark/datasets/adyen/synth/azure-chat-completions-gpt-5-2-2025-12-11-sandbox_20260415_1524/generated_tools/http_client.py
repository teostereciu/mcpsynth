import os
import json
from typing import Any, Dict, Optional

import requests


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name)
    return v if v not in (None, "") else default


def adyen_base_urls() -> Dict[str, str]:
    env = (_env("ADYEN_ENVIRONMENT", "test") or "test").lower()
    if env not in ("test", "live"):
        env = "test"

    if env == "live":
        # Live base URLs vary by region/account; allow overrides.
        return {
            "checkout": _env("ADYEN_CHECKOUT_BASE_URL", "https://checkout-live.adyen.com/v71"),
            "payment": _env("ADYEN_PAYMENT_BASE_URL", "https://pal-live.adyen.com/pal/servlet/Payment/v68"),
            "management": _env("ADYEN_MANAGEMENT_BASE_URL", "https://management-live.adyen.com/v3"),
        }

    return {
        "checkout": _env("ADYEN_CHECKOUT_BASE_URL", "https://checkout-test.adyen.com/v71"),
        "payment": _env("ADYEN_PAYMENT_BASE_URL", "https://pal-test.adyen.com/pal/servlet/Payment/v68"),
        "management": _env("ADYEN_MANAGEMENT_BASE_URL", "https://management-test.adyen.com/v3"),
    }


def _headers(extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    api_key = _env("ADYEN_API_KEY")
    h = {
        "Content-Type": "application/json",
    }
    if api_key:
        h["X-API-Key"] = api_key
    if extra:
        h.update({k: v for k, v in extra.items() if v is not None})
    return h


def request_json(
    method: str,
    url: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    timeout: int = 60,
) -> Dict[str, Any]:
    try:
        resp = requests.request(
            method=method.upper(),
            url=url,
            headers=_headers(),
            params=params,
            json=json_body,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": str(e), "url": url}

    content_type = resp.headers.get("Content-Type", "")
    if resp.status_code >= 400:
        # Try to parse Adyen error payload.
        try:
            data = resp.json() if "json" in content_type else {"message": resp.text}
        except Exception:
            data = {"message": resp.text}
        return {
            "error": "http_error",
            "status": resp.status_code,
            "url": url,
            "details": data,
        }

    if resp.status_code == 204:
        return {"status": 204}

    if "json" in content_type:
        try:
            return resp.json()
        except Exception:
            return {"error": "invalid_json", "status": resp.status_code, "url": url, "raw": resp.text}

    # Fallback
    return {"status": resp.status_code, "raw": resp.text}


def with_merchant_account(payload: Dict[str, Any]) -> Dict[str, Any]:
    ma = _env("ADYEN_MERCHANT_ACCOUNT")
    if ma and "merchantAccount" not in payload:
        payload = dict(payload)
        payload["merchantAccount"] = ma
    return payload
