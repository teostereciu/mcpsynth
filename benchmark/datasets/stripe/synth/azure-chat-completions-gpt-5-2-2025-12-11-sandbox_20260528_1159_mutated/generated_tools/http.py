import os
import time
from typing import Any, Dict, List, Optional, Tuple, Union

import requests


STRIPE_BASE_URL = "https://api.stripe.com"


def _flatten_params(prefix: str, value: Any, out: List[Tuple[str, str]]) -> None:
    """Flatten nested structures into Stripe form-encoding style.

    Examples:
      {"metadata": {"a": "b"}} -> metadata[a]=b
      {"items": [{"price": "p", "quantity": 1}]} -> items[0][price]=p, items[0][quantity]=1
    """
    if value is None:
        return
    if isinstance(value, (str, int, float, bool)):
        out.append((prefix, str(value).lower() if isinstance(value, bool) else str(value)))
        return
    if isinstance(value, dict):
        for k, v in value.items():
            _flatten_params(f"{prefix}[{k}]", v, out)
        return
    if isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            _flatten_params(f"{prefix}[{i}]", v, out)
        return
    out.append((prefix, str(value)))


def encode_form(params: Optional[Dict[str, Any]]) -> List[Tuple[str, str]]:
    if not params:
        return []
    out: List[Tuple[str, str]] = []
    for k, v in params.items():
        _flatten_params(k, v, out)
    return out


def stripe_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    timeout: float = 60.0,
) -> Union[Dict[str, Any], List[Any]]:
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        return {"error": "STRIPE_API_KEY is not set"}

    url = STRIPE_BASE_URL + path
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key

    data = encode_form(params)

    try:
        resp = requests.request(method.upper(), url, headers=headers, data=data, timeout=timeout)
    except requests.RequestException as e:
        return {"error": f"request_failed: {e}"}

    try:
        payload = resp.json()
    except ValueError:
        payload = {"error": "non_json_response", "status_code": resp.status_code, "text": resp.text}

    if resp.status_code >= 400:
        # Stripe error format: {"error": {"message": ..., "type": ...}}
        return {
            "error": "stripe_error",
            "status_code": resp.status_code,
            "details": payload,
        }

    return payload
