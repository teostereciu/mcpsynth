import os
import time
from typing import Any, Dict, Optional, Tuple

import requests

BASE_URL = "https://api.stripe.com"


def _flatten(prefix: str, value: Any, out: Dict[str, Any]) -> None:
    """Flatten nested dict/list into Stripe form-encoding keys.

    Examples:
      {"metadata": {"order_id": "123"}} -> metadata[order_id]=123
      {"items": [{"price": "price_...", "quantity": 1}]} -> items[0][price]=...
    """
    if value is None:
        return
    if isinstance(value, dict):
        for k, v in value.items():
            key = f"{prefix}[{k}]" if prefix else str(k)
            _flatten(key, v, out)
    elif isinstance(value, list):
        for i, v in enumerate(value):
            key = f"{prefix}[{i}]"
            _flatten(key, v, out)
    else:
        out[prefix] = value


def form_encode(data: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if not data:
        return {}
    out: Dict[str, Any] = {}
    for k, v in data.items():
        _flatten(str(k), v, out)
    return out


def stripe_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    timeout: float = 60.0,
) -> Tuple[int, Dict[str, Any]]:
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        return 401, {"error": "STRIPE_API_KEY is not set"}

    url = BASE_URL + path
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Stripe-Version": "2024-06-20",
        "User-Agent": "mcp-stripe-server/1.0",
    }
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key

    data = form_encode(params)

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
        return 599, {"error": str(e)}

    try:
        payload = resp.json()
    except ValueError:
        payload = {"raw": resp.text}

    if resp.status_code >= 400:
        # Stripe error format: {"error": {...}}
        if isinstance(payload, dict) and "error" in payload:
            return resp.status_code, payload
        return resp.status_code, {"error": payload}

    return resp.status_code, payload
