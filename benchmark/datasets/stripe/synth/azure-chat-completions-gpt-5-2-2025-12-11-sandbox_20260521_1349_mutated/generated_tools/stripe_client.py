import os
import time
from typing import Any, Dict, Optional, Tuple

import requests

BASE_URL = "https://api.stripe.com"


def _flatten_params(prefix: str, value: Any, out: Dict[str, str]) -> None:
    """Flatten nested dict/list params into Stripe form-encoding style.

    Examples:
      {"metadata": {"order_id": "123"}} -> metadata[order_id]=123
      {"items": [{"price": "price_...", "quantity": 1}]} -> items[0][price]=..., items[0][quantity]=1
    """
    if value is None:
        return
    if isinstance(value, (str, int, float, bool)):
        out[prefix] = "true" if value is True else "false" if value is False else str(value)
        return
    if isinstance(value, dict):
        for k, v in value.items():
            _flatten_params(f"{prefix}[{k}]", v, out)
        return
    if isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            _flatten_params(f"{prefix}[{i}]", v, out)
        return
    out[prefix] = str(value)


def encode_params(params: Optional[Dict[str, Any]]) -> Dict[str, str]:
    if not params:
        return {}
    out: Dict[str, str] = {}
    for k, v in params.items():
        _flatten_params(k, v, out)
    return out


def stripe_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    timeout: float = 60.0,
) -> Dict[str, Any]:
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        return {"error": "STRIPE_API_KEY environment variable is not set"}

    url = f"{BASE_URL}{path}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Stripe-Version": "2024-06-20",
    }
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key

    data = encode_params(params)

    try:
        resp = requests.request(method.upper(), url, headers=headers, data=data, timeout=timeout)
    except requests.RequestException as e:
        return {"error": f"request_failed: {e.__class__.__name__}: {str(e)}"}

    try:
        payload = resp.json()
    except ValueError:
        payload = {"raw": resp.text}

    if 200 <= resp.status_code < 300:
        return payload

    # Stripe error format typically: {"error": {"message": ..., "type": ..., ...}}
    return {
        "error": {
            "status_code": resp.status_code,
            "response": payload,
        }
    }
