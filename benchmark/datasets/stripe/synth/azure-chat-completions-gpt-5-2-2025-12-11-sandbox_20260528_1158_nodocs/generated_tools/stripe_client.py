import os
import time
from typing import Any, Dict, Optional, Tuple, Union

import requests


STRIPE_BASE_URL = "https://api.stripe.com"


def _stripe_headers(stripe_account: Optional[str] = None, idempotency_key: Optional[str] = None) -> Dict[str, str]:
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        # Return empty; caller will handle error
        return {}

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key
    return headers


def _flatten_params(data: Any, prefix: str = "") -> Dict[str, str]:
    """Flatten nested dict/list into Stripe-style form encoding.

    Examples:
      {"metadata": {"a": "b"}} -> {"metadata[a]": "b"}
      {"items": [{"price": "p", "quantity": 1}]} -> {"items[0][price]": "p", "items[0][quantity]": "1"}
    """
    out: Dict[str, str] = {}

    def add(key: str, value: Any):
        if value is None:
            return
        if isinstance(value, bool):
            out[key] = "true" if value else "false"
        elif isinstance(value, (int, float)):
            out[key] = str(value)
        else:
            out[key] = str(value)

    if data is None:
        return out

    if isinstance(data, dict):
        for k, v in data.items():
            new_prefix = f"{prefix}[{k}]" if prefix else str(k)
            out.update(_flatten_params(v, new_prefix))
        return out

    if isinstance(data, (list, tuple)):
        for i, v in enumerate(data):
            new_prefix = f"{prefix}[{i}]"
            out.update(_flatten_params(v, new_prefix))
        return out

    add(prefix, data)
    return out


def stripe_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    timeout: float = 60.0,
) -> Union[Dict[str, Any], Dict[str, str]]:
    """Internal helper. Returns JSON dict or {"error": ...}.

    Not exposed as an MCP tool.
    """
    headers = _stripe_headers(stripe_account=stripe_account, idempotency_key=idempotency_key)
    if not headers:
        return {"error": "STRIPE_API_KEY is not set"}

    url = STRIPE_BASE_URL + path

    try:
        if method.upper() in ("GET", "DELETE"):
            r = requests.request(
                method.upper(),
                url,
                headers=headers,
                params=_flatten_params(params or {}),
                timeout=timeout,
            )
        else:
            r = requests.request(
                method.upper(),
                url,
                headers=headers,
                data=_flatten_params(params or {}),
                timeout=timeout,
            )

        # Stripe returns JSON for both success and error
        try:
            payload = r.json()
        except Exception:
            return {"error": f"Non-JSON response from Stripe (status {r.status_code})"}

        if r.status_code >= 400:
            # Normalize Stripe error shape
            if isinstance(payload, dict) and "error" in payload:
                err = payload.get("error")
                if isinstance(err, dict):
                    msg = err.get("message") or str(err)
                    code = err.get("code")
                    typ = err.get("type")
                    return {"error": msg, "status": r.status_code, "code": code, "type": typ, "raw": payload}
            return {"error": f"Stripe API error (status {r.status_code})", "status": r.status_code, "raw": payload}

        return payload if isinstance(payload, dict) else {"data": payload}

    except requests.RequestException as e:
        return {"error": f"Request failed: {e.__class__.__name__}: {str(e)}"}


def make_idempotency_key(prefix: str = "mcp") -> str:
    return f"{prefix}_{int(time.time() * 1000)}"
