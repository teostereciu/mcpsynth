import os
import time
from typing import Any, Dict, Optional, Tuple, Union

import requests

BASE_URL = "https://api.stripe.com"


def _flatten_params(prefix: str, value: Any, out: Dict[str, Any]) -> None:
    """Flatten nested dict/list params into Stripe form-encoding style.

    Examples:
      {"metadata": {"order_id": "123"}} -> {"metadata[order_id]": "123"}
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


def encode_params(params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if not params:
        return {}
    out: Dict[str, Any] = {}
    for k, v in params.items():
        _flatten_params(str(k), v, out)
    return out


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
        return {"error": "STRIPE_API_KEY is not set"}

    url = BASE_URL + path
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Stripe-Version": "2024-06-20",
        "User-Agent": "mcp-stripe-server/1.0",
    }
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key

    data = encode_params(params)

    try:
        resp = requests.request(
            method.upper(),
            url,
            headers=headers,
            params=data if method.upper() == "GET" else None,
            data=data if method.upper() != "GET" else None,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": str(e)}

    try:
        payload: Union[Dict[str, Any], Any] = resp.json()
    except ValueError:
        payload = {"raw": resp.text}

    if resp.status_code >= 400:
        # Stripe errors are usually {"error": {...}}
        if isinstance(payload, dict) and "error" in payload:
            return {"error": payload.get("error"), "status": resp.status_code}
        return {"error": payload, "status": resp.status_code}

    if isinstance(payload, dict):
        return payload
    return {"data": payload}
