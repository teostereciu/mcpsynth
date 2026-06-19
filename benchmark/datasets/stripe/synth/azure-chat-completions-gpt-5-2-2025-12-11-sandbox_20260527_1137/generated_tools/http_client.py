import os
import time
from typing import Any, Dict, Optional, Tuple

import requests

BASE_URL = "https://api.stripe.com"


def _flatten(prefix: str, value: Any, out: Dict[str, Any]) -> None:
    """Flatten nested dict/list into Stripe form-encoding style keys.

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

    if method.upper() in ("GET", "DELETE"):
        query = params or None
    else:
        flat: Dict[str, Any] = {}
        _flatten("", params or {}, flat)
        data = flat or None

    try:
        resp = requests.request(method.upper(), url, headers=headers, params=query, data=data, timeout=timeout)
        try:
            payload = resp.json()
        except Exception:
            payload = {"raw": resp.text}

        if resp.status_code >= 400:
            # Stripe errors are usually {"error": {...}}
            return {
                "error": payload.get("error") if isinstance(payload, dict) else payload,
                "status_code": resp.status_code,
            }
        return payload if isinstance(payload, dict) else {"data": payload}
    except requests.RequestException as e:
        return {"error": str(e)}


def _maybe_expand(params: Optional[Dict[str, Any]], expand: Optional[list]) -> Dict[str, Any]:
    out = dict(params or {})
    if expand:
        out["expand"] = expand
    return out
