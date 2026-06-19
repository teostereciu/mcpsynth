import os
import time
from typing import Any, Dict, Optional, Tuple

import requests

STRIPE_BASE_URL = "https://api.stripe.com"


def _encode_form(prefix: str, value: Any, out: Dict[str, str]) -> None:
    """Flatten nested structures into Stripe-style form encoding.

    Examples:
      {"metadata": {"a": "b"}} -> metadata[a]=b
      {"items": [{"price": "p", "quantity": 1}]} -> items[0][price]=p, items[0][quantity]=1
    """
    if value is None:
        return
    if isinstance(value, bool):
        out[prefix] = "true" if value else "false"
    elif isinstance(value, (str, int, float)):
        out[prefix] = str(value)
    elif isinstance(value, dict):
        for k, v in value.items():
            _encode_form(f"{prefix}[{k}]", v, out)
    elif isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            _encode_form(f"{prefix}[{i}]", v, out)
    else:
        out[prefix] = str(value)


def to_form(data: Optional[Dict[str, Any]]) -> Dict[str, str]:
    if not data:
        return {}
    out: Dict[str, str] = {}
    for k, v in data.items():
        _encode_form(k, v, out)
    return out


def stripe_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
    timeout: float = 60.0,
) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        return None, {"error": "STRIPE_API_KEY environment variable is not set"}

    url = STRIPE_BASE_URL + path
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key
    if stripe_account:
        headers["Stripe-Account"] = stripe_account

    try:
        resp = requests.request(
            method.upper(),
            url,
            headers=headers,
            params=to_form(params) if params else None,
            data=to_form(data) if data else None,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return None, {"error": f"Network error: {e}"}

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
            msg = err.get("message") or str(err)
        else:
            msg = str(err)
        return None, {"error": msg, "status": resp.status_code, "stripe_error": payload.get("error")}

    return None, {"error": f"HTTP {resp.status_code}", "status": resp.status_code, "response": payload}


def stripe_get(path: str, *, params: Optional[Dict[str, Any]] = None, **kw):
    return stripe_request("GET", path, params=params, **kw)


def stripe_post(path: str, *, data: Optional[Dict[str, Any]] = None, **kw):
    return stripe_request("POST", path, data=data, **kw)


def stripe_delete(path: str, *, data: Optional[Dict[str, Any]] = None, **kw):
    return stripe_request("DELETE", path, data=data, **kw)
