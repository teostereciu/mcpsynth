import os
import time
from typing import Any, Dict, Optional, Tuple

import requests

STRIPE_BASE_URL = "https://api.stripe.com"


def _flatten_params(prefix: str, value: Any, out: Dict[str, str]) -> None:
    """Flatten nested dict/list params into Stripe form-encoding style.

    Examples:
      {"metadata": {"a": "b"}} -> metadata[a]=b
      {"items": [{"price": "p", "quantity": 1}]} -> items[0][price]=p, items[0][quantity]=1
    """
    if value is None:
        return
    if isinstance(value, dict):
        for k, v in value.items():
            key = f"{prefix}[{k}]" if prefix else str(k)
            _flatten_params(key, v, out)
    elif isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            key = f"{prefix}[{i}]"
            _flatten_params(key, v, out)
    else:
        out[prefix] = str(value)


def stripe_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
    api_version: Optional[str] = None,
    timeout: float = 60.0,
    max_retries: int = 2,
) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    """Internal helper. Returns (data, error)."""
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        return None, {"error": "STRIPE_API_KEY is not set"}

    url = STRIPE_BASE_URL + path
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    if api_version:
        headers["Stripe-Version"] = api_version

    data = None
    query = None
    if params:
        flat: Dict[str, str] = {}
        _flatten_params("", params, flat)
        if method.upper() in ("GET", "DELETE"):
            query = flat
        else:
            data = flat

    last_err: Optional[Dict[str, Any]] = None
    for attempt in range(max_retries + 1):
        try:
            resp = requests.request(method.upper(), url, headers=headers, params=query, data=data, timeout=timeout)
            ct = resp.headers.get("content-type", "")
            payload: Any
            if "application/json" in ct:
                payload = resp.json()
            else:
                payload = {"raw": resp.text}

            if 200 <= resp.status_code < 300:
                if isinstance(payload, dict):
                    return payload, None
                return {"data": payload}, None

            # Stripe error format: {"error": {...}}
            if isinstance(payload, dict) and "error" in payload:
                err = payload["error"]
                last_err = {
                    "error": err.get("message") if isinstance(err, dict) else str(err),
                    "type": err.get("type") if isinstance(err, dict) else None,
                    "code": err.get("code") if isinstance(err, dict) else None,
                    "param": err.get("param") if isinstance(err, dict) else None,
                    "status": resp.status_code,
                }
            else:
                last_err = {"error": "Stripe API error", "status": resp.status_code, "body": payload}

            # Retry on rate limit / transient
            if resp.status_code in (429, 500, 502, 503, 504) and attempt < max_retries:
                time.sleep(0.5 * (2**attempt))
                continue
            return None, last_err
        except requests.RequestException as e:
            last_err = {"error": str(e)}
            if attempt < max_retries:
                time.sleep(0.5 * (2**attempt))
                continue
            return None, last_err

    return None, last_err or {"error": "Unknown error"}
