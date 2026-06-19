import os
import time
from typing import Any, Dict, Optional, Tuple

import requests

BASE_URL = "https://api.stripe.com"


def _flatten_params(data: Any, prefix: str = "") -> Dict[str, Any]:
    """Flatten nested dict/list into Stripe form-encoding style keys.

    Examples:
      {"metadata": {"order_id": "1"}} -> {"metadata[order_id]": "1"}
      {"line_items": [{"price": "p", "quantity": 2}]} -> {"line_items[0][price]": "p", "line_items[0][quantity]": 2}
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
            key = f"{prefix}[{i}]" if prefix else str(i)
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
    timeout: int = 60,
) -> Dict[str, Any]:
    api_key = os.environ.get("STRIPE_API_KEY")
    if not api_key:
        return {"error": "STRIPE_API_KEY environment variable is not set"}

    url = BASE_URL + path
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
        resp = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            params=data if method.upper() == "GET" else None,
            data=data if method.upper() != "GET" else None,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": f"request_failed: {e}"}

    try:
        payload = resp.json()
    except ValueError:
        payload = {"error": "non_json_response", "status_code": resp.status_code, "text": resp.text}

    if resp.status_code >= 400:
        # Stripe error format: {"error": {"message": ..., "type": ...}}
        if isinstance(payload, dict) and "error" in payload:
            return {"error": payload.get("error"), "status_code": resp.status_code}
        return {"error": payload, "status_code": resp.status_code}

    return payload
