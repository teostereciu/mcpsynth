import os
import time
from typing import Any, Dict, Optional, Tuple

import requests

STRIPE_BASE_URL = "https://api.stripe.com"


def _flatten_params(data: Any, prefix: str = "") -> Dict[str, Any]:
    """Flatten nested dict/list into Stripe-style form-encoded keys.

    Examples:
      {"metadata": {"order_id": "123"}} -> {"metadata[order_id]": "123"}
      {"items": [{"price": "price_...", "quantity": 1}]} -> {"items[0][price]": "price_...", "items[0][quantity]": 1}
    """
    out: Dict[str, Any] = {}

    if data is None:
        return out

    if isinstance(data, dict):
        for k, v in data.items():
            key = f"{prefix}[{k}]" if prefix else str(k)
            out.update(_flatten_params(v, key))
        return out

    if isinstance(data, (list, tuple)):
        for i, v in enumerate(data):
            key = f"{prefix}[{i}]"
            out.update(_flatten_params(v, key))
        return out

    out[prefix] = data
    return out


def stripe_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    timeout: float = 60.0,
) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    """Make a Stripe API request.

    Returns (data, error). error is JSON-serializable.
    """
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        return None, {"error": "STRIPE_API_KEY environment variable is not set"}

    url = STRIPE_BASE_URL + path
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key

    data = _flatten_params(params or {})

    try:
        resp = requests.request(method.upper(), url, headers=headers, data=data, timeout=timeout)
    except requests.RequestException as e:
        return None, {"error": "request_failed", "message": str(e)}

    try:
        payload = resp.json()
    except ValueError:
        payload = {"raw": resp.text}

    if 200 <= resp.status_code < 300:
        return payload, None

    # Stripe error format: {"error": {"type":..., "message":..., ...}}
    err_obj = payload.get("error") if isinstance(payload, dict) else None
    if isinstance(err_obj, dict):
        return None, {
            "error": err_obj.get("type") or "stripe_error",
            "message": err_obj.get("message") or "Unknown Stripe error",
            "status": resp.status_code,
            "code": err_obj.get("code"),
            "param": err_obj.get("param"),
            "request_log_url": err_obj.get("request_log_url"),
        }

    return None, {"error": "http_error", "status": resp.status_code, "body": payload, "ts": int(time.time())}
