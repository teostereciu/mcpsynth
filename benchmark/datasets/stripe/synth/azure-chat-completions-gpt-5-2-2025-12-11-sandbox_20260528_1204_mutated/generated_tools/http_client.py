import os
import time
from typing import Any, Dict, Optional, Tuple

import requests

BASE_URL = "https://api.stripe.com"


def _flatten(prefix: str, value: Any, out: Dict[str, Any]) -> None:
    """Flatten nested dict/list into Stripe form-encoding style keys.

    Examples:
      {"metadata": {"order_id": "123"}} -> {"metadata[order_id]": "123"}
      {"items": [{"price": "price_...", "quantity": 1}]} -> {"items[0][price]": "price_...", "items[0][quantity]": 1}
    """
    if value is None:
        return
    if isinstance(value, dict):
        for k, v in value.items():
            key = f"{prefix}[{k}]" if prefix else str(k)
            _flatten(key, v, out)
        return
    if isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            key = f"{prefix}[{i}]"
            _flatten(key, v, out)
        return
    out[prefix] = value


def stripe_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_version: Optional[str] = None,
    timeout: int = 60,
) -> Dict[str, Any]:
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        return {"error": "STRIPE_API_KEY environment variable is not set"}

    url = BASE_URL + path
    headers: Dict[str, str] = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key
    if stripe_version:
        headers["Stripe-Version"] = stripe_version

    data: Optional[Dict[str, Any]] = None
    query: Optional[Dict[str, Any]] = None

    flat: Dict[str, Any] = {}
    if params:
        _flatten("", params, flat)

    m = method.upper()
    if m in ("GET", "DELETE"):
        query = flat
    else:
        data = flat

    try:
        resp = requests.request(m, url, headers=headers, params=query, data=data, timeout=timeout)
    except requests.RequestException as e:
        return {"error": f"request_failed: {str(e)}"}

    try:
        payload = resp.json()
    except ValueError:
        payload = {"raw": resp.text}

    if resp.status_code >= 400:
        # Stripe error format: {"error": {"message": ..., "type": ..., ...}}
        if isinstance(payload, dict) and "error" in payload:
            return {"error": payload.get("error"), "status_code": resp.status_code}
        return {"error": payload, "status_code": resp.status_code}

    return payload
