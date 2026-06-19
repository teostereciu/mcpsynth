import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


STRIPE_BASE_URL = "https://api.stripe.com"


def _encode_form(data: Any, prefix: str = "") -> Dict[str, Any]:
    """Flatten nested dict/list structures into Stripe-style form fields.

    Examples:
      {"metadata": {"a": "b"}} -> {"metadata[a]": "b"}
      {"items": [{"price": "p", "quantity": 1}]} -> {"items[0][price]": "p", "items[0][quantity]": 1}
    """
    out: Dict[str, Any] = {}
    if data is None:
        return out

    if isinstance(data, dict):
        for k, v in data.items():
            key = f"{prefix}[{k}]" if prefix else str(k)
            out.update(_encode_form(v, key))
        return out

    if isinstance(data, (list, tuple)):
        for i, v in enumerate(data):
            key = f"{prefix}[{i}]"
            out.update(_encode_form(v, key))
        return out

    out[prefix] = data
    return out


def stripe_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    account: Optional[str] = None,
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
        "Stripe-Version": os.getenv("STRIPE_API_VERSION", "2024-06-20"),
    }
    if account:
        headers["Stripe-Account"] = account
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key

    data = _encode_form(params or {})

    try:
        resp = requests.request(method.upper(), url, headers=headers, data=data, timeout=timeout)
    except requests.RequestException as e:
        return {"error": str(e)}

    try:
        payload = resp.json()
    except ValueError:
        payload = {"error": f"Non-JSON response (status {resp.status_code})", "text": resp.text}

    if resp.status_code >= 400:
        # Stripe errors are usually {"error": {...}}
        if isinstance(payload, dict) and "error" in payload:
            return payload
        return {"error": payload, "status": resp.status_code}

    return payload


def stripe_list_all(
    path: str,
    params: Optional[Dict[str, Any]] = None,
    account: Optional[str] = None,
    limit: int = 100,
    max_pages: int = 10,
) -> Dict[str, Any]:
    """Auto-paginate list endpoints that return {data: [...], has_more: bool}.

    Returns {"data": [...], "has_more": bool, "pages": n}
    """
    params = dict(params or {})
    params.setdefault("limit", limit)

    all_data = []
    starting_after = None
    pages = 0

    while True:
        if starting_after:
            params["starting_after"] = starting_after
        res = stripe_request("GET", path, params=params, account=account)
        if isinstance(res, dict) and res.get("error"):
            return res
        data = res.get("data", []) if isinstance(res, dict) else []
        all_data.extend(data)
        pages += 1
        if not res.get("has_more") or not data or pages >= max_pages:
            return {"data": all_data, "has_more": bool(res.get("has_more")), "pages": pages}
        starting_after = data[-1].get("id")
        time.sleep(0.05)
