import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


STRIPE_BASE_URL = "https://api.stripe.com"


def _stripe_headers(stripe_account: Optional[str] = None, idempotency_key: Optional[str] = None) -> Dict[str, str]:
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
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
    """Convert nested dict/list structures into Stripe-style form encoding.

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
        elif isinstance(value, str):
            out[key] = value
        else:
            out[key] = str(value)

    if data is None:
        return out

    if isinstance(data, dict):
        for k, v in data.items():
            new_prefix = f"{prefix}[{k}]" if prefix else str(k)
            out.update(_flatten_params(v, new_prefix))
        return out

    if isinstance(data, list):
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
    data: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    timeout: float = 60.0,
    max_retries: int = 2,
) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    """Return (result, error). Never raises for expected HTTP errors."""

    headers = _stripe_headers(stripe_account=stripe_account, idempotency_key=idempotency_key)
    if not headers:
        return None, {"error": "STRIPE_API_KEY is not set"}

    url = STRIPE_BASE_URL + path
    q = params or {}
    body = _flatten_params(data or {})

    last_err: Optional[Dict[str, Any]] = None
    for attempt in range(max_retries + 1):
        try:
            resp = requests.request(method.upper(), url, headers=headers, params=q, data=body, timeout=timeout)
        except requests.RequestException as e:
            last_err = {"error": str(e)}
            if attempt < max_retries:
                time.sleep(0.5 * (2**attempt))
                continue
            return None, last_err

        ct = resp.headers.get("content-type", "")
        payload: Any
        if "application/json" in ct:
            try:
                payload = resp.json()
            except Exception:
                payload = {"raw": resp.text}
        else:
            payload = {"raw": resp.text}

        if 200 <= resp.status_code < 300:
            if isinstance(payload, dict):
                return payload, None
            return {"data": payload}, None

        # Stripe error format: {"error": {...}}
        if isinstance(payload, dict) and "error" in payload:
            err = payload
        else:
            err = {"error": {"message": resp.text, "status": resp.status_code}}

        err["http_status"] = resp.status_code
        return None, err

    return None, last_err or {"error": "Unknown error"}
