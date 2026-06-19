import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


STRIPE_BASE_URL = "https://api.stripe.com"


def _flatten_params(data: Any, prefix: str = "") -> Dict[str, Any]:
    """Flatten nested dict/list into Stripe form-encoding style keys.

    Examples:
      {"metadata": {"order_id": "1"}} -> {"metadata[order_id]": "1"}
      {"line_items": [{"price": "p", "quantity": 1}]} -> {"line_items[0][price]": "p", ...}
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
            key = f"{prefix}[{i}]"
            out.update(_flatten_params(v, key))
        return out

    out[prefix] = data
    return out


def stripe_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    timeout: int = 60,
) -> Dict[str, Any]:
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        return {"error": "STRIPE_API_KEY environment variable is not set"}

    url = STRIPE_BASE_URL + path
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Stripe-Version": "2024-06-20",
    }
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key

    try:
        resp = requests.request(
            method.upper(),
            url,
            headers=headers,
            params=_flatten_params(params) if params else None,
            data=_flatten_params(data) if data else None,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": str(e)}

    try:
        payload = resp.json()
    except ValueError:
        payload = {"raw": resp.text}

    if resp.status_code >= 400:
        # Stripe errors are typically {"error": {...}}
        if isinstance(payload, dict) and "error" in payload:
            return {"error": payload.get("error"), "status_code": resp.status_code}
        return {"error": payload, "status_code": resp.status_code}

    return payload


def stripe_list(
    path: str,
    *,
    query: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request("GET", path, params=query, stripe_account=stripe_account)


def now_unix() -> int:
    return int(time.time())
