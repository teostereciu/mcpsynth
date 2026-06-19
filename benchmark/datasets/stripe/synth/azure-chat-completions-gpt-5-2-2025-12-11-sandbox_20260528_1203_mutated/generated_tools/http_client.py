import os
import time
from typing import Any, Dict, Optional, Tuple

import requests

BASE_URL = "https://api.stripe.com"


def _flatten(prefix: str, value: Any, out: Dict[str, Any]) -> None:
    """Flatten nested dict/list into Stripe-style form encoding.

    Examples:
      {"metadata": {"a": "b"}} -> {"metadata[a]": "b"}
      {"items": [{"price": "p", "quantity": 1}]} -> {"items[0][price]": "p", "items[0][quantity]": 1}
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
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    timeout: int = 60,
) -> Dict[str, Any]:
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        return {"error": "STRIPE_API_KEY environment variable is not set"}

    url = BASE_URL + path
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Stripe-Version": "2024-06-20",
    }
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key

    data: Dict[str, Any] = {}
    if params:
        _flatten("", params, data)

    try:
        resp = requests.request(method.upper(), url, headers=headers, data=data, timeout=timeout)
    except requests.RequestException as e:
        return {"error": str(e)}

    try:
        payload = resp.json()
    except ValueError:
        payload = {"raw": resp.text}

    if resp.status_code >= 400:
        # Stripe error format: {"error": {...}}
        if isinstance(payload, dict) and "error" in payload:
            return payload
        return {"error": payload, "status_code": resp.status_code}

    return payload
