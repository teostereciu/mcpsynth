import os
import time
from typing import Any, Dict, Optional, Tuple

import requests

STRIPE_BASE_URL = "https://api.stripe.com"


def _encode_form(prefix: str, value: Any, out: Dict[str, str]) -> None:
    """Flatten nested structures to Stripe-style form encoding.

    Examples:
      {"metadata": {"order_id": "123"}} -> metadata[order_id]=123
      {"items": [{"price": "price_...", "quantity": 1}]} -> items[0][price]=...&items[0][quantity]=1
    """
    if value is None:
        return
    if isinstance(value, bool):
        out[prefix] = "true" if value else "false"
    elif isinstance(value, (int, float)):
        out[prefix] = str(value)
    elif isinstance(value, str):
        out[prefix] = value
    elif isinstance(value, dict):
        for k, v in value.items():
            _encode_form(f"{prefix}[{k}]", v, out)
    elif isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            _encode_form(f"{prefix}[{i}]", v, out)
    else:
        out[prefix] = str(value)


def stripe_form_encode(data: Optional[Dict[str, Any]]) -> Dict[str, str]:
    if not data:
        return {}
    out: Dict[str, str] = {}
    for k, v in data.items():
        _encode_form(k, v, out)
    return out


def stripe_request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None, idempotency_key: Optional[str] = None, timeout: float = 60.0) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    """Internal helper. Returns (result, error_dict)."""
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        return None, {"error": "STRIPE_API_KEY is not set"}

    url = STRIPE_BASE_URL + path
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Stripe-Version": "2024-06-20",
    }
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key

    try:
        resp = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            params=stripe_form_encode(params) if params else None,
            data=stripe_form_encode(data) if data else None,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return None, {"error": f"request_failed: {e}"}

    try:
        payload = resp.json()
    except ValueError:
        payload = {"raw": resp.text}

    if 200 <= resp.status_code < 300:
        return payload, None

    # Stripe error format: {"error": {"message": ..., "type": ..., ...}}
    if isinstance(payload, dict) and "error" in payload:
        err = payload.get("error")
        if isinstance(err, dict):
            return None, {
                "error": err.get("message") or "stripe_error",
                "type": err.get("type"),
                "code": err.get("code"),
                "param": err.get("param"),
                "status": resp.status_code,
                "request_id": resp.headers.get("Request-Id"),
            }
    return None, {"error": "http_error", "status": resp.status_code, "response": payload}


def stripe_poll(path: str, *, params: Optional[Dict[str, Any]] = None, attempts: int = 10, sleep_s: float = 1.0) -> Dict[str, Any]:
    """Poll a GET endpoint until it returns a terminal state if present."""
    last: Optional[Dict[str, Any]] = None
    for _ in range(max(1, attempts)):
        last, err = stripe_request("GET", path, params=params)
        if err:
            return err
        if not isinstance(last, dict):
            return {"result": last}
        status = last.get("status")
        if status in ("succeeded", "canceled", "requires_payment_method", "requires_action", "processing", "requires_confirmation"):
            return last
        time.sleep(sleep_s)
    return last or {"error": "poll_failed"}
