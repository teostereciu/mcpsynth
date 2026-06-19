import os
import time
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://api.stripe.com"


def _flatten_params(prefix: str, value: Any, out: Dict[str, Any]) -> None:
    """Flatten nested dict/list params into Stripe form-encoding style.

    Examples:
      {"metadata": {"order_id": "1"}} -> {"metadata[order_id]": "1"}
      {"items": [{"price": "p", "quantity": 1}]} -> {"items[0][price]": "p", "items[0][quantity]": 1}
    """
    if value is None:
        return
    if isinstance(value, dict):
        for k, v in value.items():
            key = f"{prefix}[{k}]" if prefix else str(k)
            _flatten_params(key, v, out)
        return
    if isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            key = f"{prefix}[{i}]"
            _flatten_params(key, v, out)
        return
    out[prefix] = value


def stripe_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
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

    data: Optional[Dict[str, Any]] = None
    query: Optional[Dict[str, Any]] = None

    flat: Dict[str, Any] = {}
    if params:
        for k, v in params.items():
            _flatten_params(str(k), v, flat)

    if method.upper() in ("GET", "DELETE"):
        query = flat or None
    else:
        data = flat or None

    try:
        resp = requests.request(method.upper(), url, headers=headers, params=query, data=data, timeout=timeout)
    except requests.RequestException as e:
        return {"error": f"request_failed: {type(e).__name__}: {e}"}

    try:
        payload = resp.json()
    except ValueError:
        payload = {"error": "non_json_response", "status": resp.status_code, "text": resp.text}

    if resp.status_code >= 400:
        # Stripe error format: {"error": {...}}
        if isinstance(payload, dict) and "error" in payload:
            return payload
        return {"error": {"message": "http_error", "status": resp.status_code, "body": payload}}

    return payload
