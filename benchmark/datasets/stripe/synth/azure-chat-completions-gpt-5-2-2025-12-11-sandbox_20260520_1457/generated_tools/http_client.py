import os
import time
from typing import Any, Dict, Optional, Tuple

import requests

BASE_URL = "https://api.stripe.com"


def _flatten(prefix: str, value: Any, out: Dict[str, Any]) -> None:
    """Flatten nested dict/list into Stripe form-encoding style keys.

    Examples:
      {"metadata": {"order_id": "1"}} -> metadata[order_id]=1
      {"items": [{"price": "p", "quantity": 1}]} -> items[0][price]=p, items[0][quantity]=1
    """
    if value is None:
        return
    if isinstance(value, dict):
        for k, v in value.items():
            key = f"{prefix}[{k}]" if prefix else str(k)
            _flatten(key, v, out)
    elif isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            key = f"{prefix}[{i}]"
            _flatten(key, v, out)
    else:
        out[prefix] = value


def encode_params(params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if not params:
        return {}
    out: Dict[str, Any] = {}
    for k, v in params.items():
        _flatten(str(k), v, out)
    return out


def stripe_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
    timeout: int = 60,
) -> Tuple[int, Any]:
    api_key = os.environ.get("STRIPE_API_KEY")
    if not api_key:
        return 401, {"error": "Missing STRIPE_API_KEY env var"}

    url = BASE_URL + path
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Stripe-Version": "2024-06-20",
        "User-Agent": "mcp-stripe-server/1.0",
    }
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key
    if stripe_account:
        headers["Stripe-Account"] = stripe_account

    data = encode_params(params)

    try:
        resp = requests.request(method.upper(), url, headers=headers, data=data, timeout=timeout)
    except requests.RequestException as e:
        return 599, {"error": f"Network error: {e}"}

    try:
        payload = resp.json()
    except ValueError:
        payload = resp.text

    return resp.status_code, payload


def ok_or_error(status: int, payload: Any) -> Any:
    if 200 <= status < 300:
        return payload
    # Stripe errors are usually {"error": {...}}
    if isinstance(payload, dict) and "error" in payload:
        return {"error": payload.get("error")}
    return {"error": {"status": status, "message": payload}}
