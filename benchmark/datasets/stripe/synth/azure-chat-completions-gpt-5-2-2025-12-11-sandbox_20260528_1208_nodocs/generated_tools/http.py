import os
import time
from typing import Any, Dict, Optional, Tuple

import requests

STRIPE_BASE_URL = "https://api.stripe.com"


def _stripe_headers(stripe_account: Optional[str] = None, idempotency_key: Optional[str] = None) -> Dict[str, str]:
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        raise RuntimeError("STRIPE_API_KEY environment variable is not set")

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
    """Flatten nested dict/list into Stripe form-encoding style keys.

    Examples:
      {"metadata": {"a": "b"}} -> {"metadata[a]": "b"}
      {"items": [{"price": "p", "quantity": 1}]} -> {"items[0][price]": "p", "items[0][quantity]": "1"}
    """
    out: Dict[str, str] = {}

    if data is None:
        return out

    if isinstance(data, (str, int, float, bool)):
        out[prefix] = "true" if data is True else "false" if data is False else str(data)
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

    # Fallback
    out[prefix] = str(data)
    return out


def stripe_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    timeout: float = 60.0,
    max_retries: int = 2,
) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    """Make a Stripe API request.

    Returns (result, error). Exactly one is non-None.
    """
    url = STRIPE_BASE_URL + path
    headers = _stripe_headers(stripe_account=stripe_account, idempotency_key=idempotency_key)

    req_kwargs: Dict[str, Any] = {
        "headers": headers,
        "timeout": timeout,
    }

    if params:
        req_kwargs["params"] = _flatten_params(params)
    if data:
        req_kwargs["data"] = _flatten_params(data)

    last_err: Optional[Dict[str, Any]] = None

    for attempt in range(max_retries + 1):
        try:
            resp = requests.request(method.upper(), url, **req_kwargs)
        except requests.RequestException as e:
            last_err = {"error": str(e)}
            if attempt < max_retries:
                time.sleep(0.5 * (2**attempt))
                continue
            return None, last_err

        content_type = resp.headers.get("Content-Type", "")
        is_json = "application/json" in content_type
        payload: Any
        if is_json:
            try:
                payload = resp.json()
            except Exception:
                payload = {"raw": resp.text}
        else:
            payload = {"raw": resp.text}

        if 200 <= resp.status_code < 300:
            if isinstance(payload, dict):
                return payload, None
            return {"result": payload}, None

        # Stripe error format typically: {"error": {"message": ..., "type": ...}}
        if isinstance(payload, dict) and "error" in payload:
            err_obj = payload.get("error")
            if isinstance(err_obj, dict):
                last_err = {
                    "error": err_obj.get("message") or "Stripe API error",
                    "type": err_obj.get("type"),
                    "code": err_obj.get("code"),
                    "param": err_obj.get("param"),
                    "status": resp.status_code,
                }
            else:
                last_err = {"error": str(err_obj), "status": resp.status_code}
        else:
            last_err = {"error": "Stripe API error", "status": resp.status_code, "details": payload}

        # Retry on rate limit / transient server errors
        if resp.status_code in (429, 500, 502, 503, 504) and attempt < max_retries:
            time.sleep(0.5 * (2**attempt))
            continue

        return None, last_err

    return None, last_err or {"error": "Unknown error"}
