import os
import time
from typing import Any, Dict, Optional, Tuple

import requests

BASE_URL = "https://api.stripe.com"


def _encode_form_value(v: Any) -> str:
    if v is None:
        return ""
    if isinstance(v, bool):
        return "true" if v else "false"
    return str(v)


def _flatten_params(prefix: str, value: Any, out: Dict[str, str]) -> None:
    """Flatten nested dict/list into Stripe-style form encoding keys.

    Examples:
      {"metadata": {"a": "b"}} -> metadata[a]=b
      {"items": [{"price": "p", "quantity": 1}]} -> items[0][price]=p, items[0][quantity]=1
    """
    if value is None:
        return
    if isinstance(value, dict):
        for k, v in value.items():
            key = f"{prefix}[{k}]" if prefix else str(k)
            _flatten_params(key, v, out)
    elif isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            key = f"{prefix}[{i}]"
            _flatten_params(key, v, out)
    else:
        out[prefix] = _encode_form_value(value)


def form_encode(params: Optional[Dict[str, Any]]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    if not params:
        return out
    for k, v in params.items():
        _flatten_params(str(k), v, out)
    return out


def stripe_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
    api_version: Optional[str] = None,
    timeout: float = 60.0,
) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        return None, {"error": "STRIPE_API_KEY environment variable is not set"}

    url = BASE_URL + path
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    if api_version:
        headers["Stripe-Version"] = api_version

    data = None
    query = None
    if method.upper() in ("GET", "DELETE"):
        query = form_encode(params)
    else:
        data = form_encode(params)

    try:
        resp = requests.request(method.upper(), url, headers=headers, params=query, data=data, timeout=timeout)
    except requests.RequestException as e:
        return None, {"error": f"request_failed: {str(e)}"}

    try:
        payload = resp.json()
    except ValueError:
        payload = {"raw": resp.text}

    if resp.status_code >= 400:
        # Stripe error format: {"error": {"message": ..., "type": ..., ...}}
        if isinstance(payload, dict) and "error" in payload:
            return None, payload
        return None, {"error": {"message": "http_error", "status": resp.status_code, "body": payload}}

    return payload if isinstance(payload, dict) else {"data": payload}, None


def now_unix() -> int:
    return int(time.time())
