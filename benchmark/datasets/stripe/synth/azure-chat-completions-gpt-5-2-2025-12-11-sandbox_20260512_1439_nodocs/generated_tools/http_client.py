import os
import time
from typing import Any, Dict, Optional

import requests


STRIPE_BASE_URL = "https://api.stripe.com"


def _encode_form(data: Any, prefix: str = ""):
    """Encode nested dict/list into Stripe-style form fields.

    Examples:
      {"metadata": {"order_id": "123"}} -> {"metadata[order_id]": "123"}
      {"items": [{"price": "p", "quantity": 1}]} -> {"items[0][price]": "p", "items[0][quantity]": 1}
    """
    out = {}

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


def stripe_request(method: str, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        return {"error": "STRIPE_API_KEY environment variable is not set"}

    url = STRIPE_BASE_URL + path
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Stripe-Version": os.getenv("STRIPE_API_VERSION", "2024-06-20"),
    }

    try:
        if method.upper() in ("POST", "DELETE"):
            data = _encode_form(params or {})
            resp = requests.request(method.upper(), url, headers=headers, data=data, timeout=60)
        else:
            resp = requests.request(method.upper(), url, headers=headers, params=params or {}, timeout=60)

        # Stripe returns JSON for both success and error
        try:
            payload = resp.json()
        except Exception:
            payload = {"error": f"Non-JSON response from Stripe", "status": resp.status_code, "text": resp.text}

        if resp.status_code >= 400:
            # Normalize error
            if isinstance(payload, dict) and "error" in payload:
                err = payload.get("error")
                if isinstance(err, dict):
                    return {
                        "error": err.get("message") or "Stripe API error",
                        "type": err.get("type"),
                        "code": err.get("code"),
                        "param": err.get("param"),
                        "status": resp.status_code,
                        "raw": payload,
                    }
            return {"error": "Stripe API error", "status": resp.status_code, "raw": payload}

        return payload
    except requests.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


def stripe_list_all(path: str, params: Optional[Dict[str, Any]] = None, limit: int = 100) -> Dict[str, Any]:
    """Auto-paginate list endpoints that return {object:'list', data:[...], has_more:bool}.

    Returns: {"data": [...], "has_more": bool, "url": path}
    """
    params = dict(params or {})
    params.setdefault("limit", min(max(int(limit), 1), 100))

    all_data = []
    starting_after = None

    while True:
        if starting_after:
            params["starting_after"] = starting_after
        page = stripe_request("GET", path, params)
        if isinstance(page, dict) and page.get("error"):
            return page
        data = page.get("data", []) if isinstance(page, dict) else []
        all_data.extend(data)
        if not page.get("has_more"):
            return {"object": "list", "data": all_data, "has_more": False, "url": path}
        if not data:
            return {"object": "list", "data": all_data, "has_more": True, "url": path}
        starting_after = data[-1].get("id")
        time.sleep(0.05)
