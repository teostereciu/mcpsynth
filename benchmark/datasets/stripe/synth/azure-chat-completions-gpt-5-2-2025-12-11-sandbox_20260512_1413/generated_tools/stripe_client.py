import os
import time
from typing import Any, Dict, List, Optional, Tuple, Union

import requests

BASE_URL = "https://api.stripe.com"


def _stripe_key() -> Optional[str]:
    return os.getenv("STRIPE_API_KEY")


def _encode_form(data: Any, prefix: str = "") -> List[Tuple[str, str]]:
    """Flatten nested dict/list into Stripe-style form fields.

    Examples:
      {"metadata": {"order_id": "123"}} -> [("metadata[order_id]", "123")]
      {"items": [{"price": "price_...", "quantity": 1}]} ->
          [("items[0][price]", "price_..."), ("items[0][quantity]", "1")]
    """
    out: List[Tuple[str, str]] = []

    if data is None:
        return out

    if isinstance(data, (str, int, float, bool)):
        if prefix == "":
            raise ValueError("Top-level scalar not allowed")
        out.append((prefix, "true" if data is True else "false" if data is False else str(data)))
        return out

    if isinstance(data, dict):
        for k, v in data.items():
            if v is None:
                continue
            key = f"{prefix}[{k}]" if prefix else str(k)
            out.extend(_encode_form(v, key))
        return out

    if isinstance(data, (list, tuple)):
        for i, v in enumerate(data):
            key = f"{prefix}[{i}]" if prefix else str(i)
            out.extend(_encode_form(v, key))
        return out

    # Fallback
    if prefix == "":
        raise ValueError("Unsupported top-level type")
    out.append((prefix, str(data)))
    return out


def stripe_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    timeout: int = 60,
) -> Dict[str, Any]:
    key = _stripe_key()
    if not key:
        return {"error": "STRIPE_API_KEY is not set"}

    url = BASE_URL + path
    headers = {
        "Authorization": f"Bearer {key}",
        "User-Agent": "mcp-stripe-server/1.0",
    }
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key

    try:
        method_u = method.upper()
        if method_u in ("GET", "DELETE"):
            resp = requests.request(method_u, url, headers=headers, params=params or {}, timeout=timeout)
        else:
            form = _encode_form(params or {})
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            resp = requests.request(method_u, url, headers=headers, data=form, timeout=timeout)

        try:
            data = resp.json()
        except Exception:
            return {"error": f"Non-JSON response from Stripe (status {resp.status_code})", "text": resp.text}

        if resp.status_code >= 400:
            # Stripe error format: {"error": {...}}
            return {"error": data.get("error", data), "status": resp.status_code}
        return data
    except requests.RequestException as e:
        return {"error": str(e)}


def stripe_list_all(
    path: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    limit: int = 100,
    max_pages: int = 10,
) -> Dict[str, Any]:
    """Auto-paginate list endpoints that return {object:'list', data:[...], has_more:bool}.

    Returns: {"data": [...], "has_more": bool, "pages": int}
    """
    collected: List[Any] = []
    starting_after: Optional[str] = None
    pages = 0

    while True:
        pages += 1
        if pages > max_pages:
            return {"data": collected, "has_more": True, "pages": pages - 1, "error": "max_pages reached"}

        p = dict(params or {})
        p.setdefault("limit", limit)
        if starting_after:
            p["starting_after"] = starting_after

        res = stripe_request("GET", path, p, stripe_account=stripe_account)
        if "error" in res:
            return {"error": res["error"], "status": res.get("status"), "data": collected, "pages": pages - 1}

        data = res.get("data", [])
        collected.extend(data)
        has_more = bool(res.get("has_more"))
        if not has_more or not data:
            return {"data": collected, "has_more": has_more, "pages": pages}

        starting_after = data[-1].get("id")
        if not starting_after:
            return {"data": collected, "has_more": has_more, "pages": pages, "error": "missing last id for pagination"}
