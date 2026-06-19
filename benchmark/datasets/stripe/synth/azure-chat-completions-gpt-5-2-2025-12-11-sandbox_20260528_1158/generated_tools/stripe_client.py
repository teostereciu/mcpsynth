import os
import json
from typing import Any, Dict, List, Optional, Tuple, Union

import requests

BASE_URL = "https://api.stripe.com"

Json = Union[Dict[str, Any], List[Any], str, int, float, bool, None]


def _flatten_params(prefix: str, value: Any, out: List[Tuple[str, str]]) -> None:
    """Flatten nested dict/list params into Stripe-style form encoding.

    Examples:
      {"metadata": {"order_id": "123"}} -> metadata[order_id]=123
      {"items": [{"price": "price_...", "quantity": 1}]} -> items[0][price]=...&items[0][quantity]=1
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
    if isinstance(value, bool):
        out.append((prefix, "true" if value else "false"))
        return
    out.append((prefix, str(value)))


def encode_form(params: Optional[Dict[str, Any]]) -> List[Tuple[str, str]]:
    out: List[Tuple[str, str]] = []
    if not params:
        return out
    for k, v in params.items():
        _flatten_params(str(k), v, out)
    return out


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
    headers: Dict[str, str] = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key

    try:
        if method.upper() == "GET":
            resp = requests.request(
                method.upper(),
                url,
                headers=headers,
                params=params or {},
                timeout=timeout,
            )
        else:
            resp = requests.request(
                method.upper(),
                url,
                headers=headers,
                data=encode_form(params),
                timeout=timeout,
            )
    except requests.RequestException as e:
        return {"error": f"request_failed: {e}"}

    content_type = resp.headers.get("content-type", "")
    data: Any
    if "application/json" in content_type:
        try:
            data = resp.json()
        except Exception:
            data = {"raw": resp.text}
    else:
        data = {"raw": resp.text}

    if resp.status_code >= 400:
        # Stripe error format: {"error": {...}}
        if isinstance(data, dict) and "error" in data:
            err = data.get("error")
            if isinstance(err, dict):
                msg = err.get("message") or "Stripe API error"
                return {"error": msg, "stripe_error": err, "status": resp.status_code}
        return {"error": f"HTTP {resp.status_code}", "details": data}

    if isinstance(data, dict):
        return data
    return {"data": data}
