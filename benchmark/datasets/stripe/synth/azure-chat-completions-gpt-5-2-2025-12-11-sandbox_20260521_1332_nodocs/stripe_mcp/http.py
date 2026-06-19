import os
import time
from typing import Any, Dict, Optional, Tuple

import requests

BASE_URL = "https://api.stripe.com"


def _encode_form(data: Dict[str, Any], prefix: str = "") -> Dict[str, Any]:
    """Flatten nested dict/list into Stripe-style form encoding.

    Examples:
      {"metadata": {"a": "b"}} -> {"metadata[a]": "b"}
      {"items": [{"price": "p", "quantity": 1}]} -> {"items[0][price]": "p", "items[0][quantity]": 1}
    """
    out: Dict[str, Any] = {}
    for k, v in (data or {}).items():
        key = f"{prefix}{k}" if not prefix else f"{prefix}[{k}]"
        if v is None:
            continue
        if isinstance(v, dict):
            out.update(_encode_form(v, key))
        elif isinstance(v, (list, tuple)):
            for i, item in enumerate(v):
                ikey = f"{key}[{i}]"
                if isinstance(item, dict):
                    out.update(_encode_form(item, ikey))
                else:
                    out[ikey] = item
        else:
            out[key] = v
    return out


def stripe_request(
    method: str,
    path: str,
    *,
    query: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
    timeout: float = 60.0,
) -> Tuple[Optional[Any], Optional[Dict[str, Any]]]:
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        return None, {"error": "STRIPE_API_KEY is not set"}

    url = f"{BASE_URL}{path}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Stripe-Version": os.getenv("STRIPE_API_VERSION", "2024-06-20"),
    }
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key
    if stripe_account:
        headers["Stripe-Account"] = stripe_account

    params = query or None
    form = _encode_form(data or {}) if data else None

    # Basic retry for rate limits / transient errors
    for attempt in range(4):
        try:
            resp = requests.request(method, url, headers=headers, params=params, data=form, timeout=timeout)
        except requests.RequestException as e:
            return None, {"error": str(e)}

        if resp.status_code in (429, 500, 502, 503, 504) and attempt < 3:
            retry_after = resp.headers.get("Retry-After")
            sleep_s = float(retry_after) if retry_after else (0.5 * (2**attempt))
            time.sleep(min(8.0, sleep_s))
            continue

        try:
            payload = resp.json()
        except ValueError:
            payload = {"raw": resp.text}

        if 200 <= resp.status_code < 300:
            return payload, None

        # Stripe error format: {"error": {"message":..., "type":..., ...}}
        if isinstance(payload, dict) and "error" in payload:
            err = payload["error"]
            if isinstance(err, dict):
                return None, {
                    "error": err.get("message") or "Stripe API error",
                    "type": err.get("type"),
                    "code": err.get("code"),
                    "param": err.get("param"),
                    "status": resp.status_code,
                }
        return None, {"error": "Stripe API error", "status": resp.status_code, "details": payload}

    return None, {"error": "Stripe API error: retries exhausted"}
