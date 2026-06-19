import os
import time
from typing import Any, Dict, Optional, Tuple

import requests

BASE_URL = "https://api.stripe.com"


def _flatten_params(data: Any, prefix: str = "") -> Dict[str, Any]:
    """Flatten nested dict/list into Stripe-style form encoding.

    Examples:
      {"metadata": {"order_id": "123"}} -> {"metadata[order_id]": "123"}
      {"items": [{"price": "price_...", "quantity": 1}]} -> {"items[0][price]": "price_...", "items[0][quantity]": 1}
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
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
    timeout: int = 60,
) -> Tuple[int, Dict[str, Any]]:
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        return 401, {"error": "STRIPE_API_KEY is not set"}

    url = BASE_URL + path
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key
    if stripe_account:
        headers["Stripe-Account"] = stripe_account

    flat = _flatten_params(params or {})

    try:
        resp = requests.request(
            method.upper(),
            url,
            headers=headers,
            params=flat if method.upper() == "GET" else None,
            data=flat if method.upper() != "GET" else None,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return 0, {"error": str(e)}

    try:
        payload = resp.json()
    except ValueError:
        payload = {"error": resp.text}

    if resp.status_code >= 400:
        err = payload.get("error") if isinstance(payload, dict) else None
        if isinstance(err, dict):
            msg = err.get("message") or str(err)
        else:
            msg = str(payload)
        return resp.status_code, {"error": msg, "details": payload}

    return resp.status_code, payload


def maybe_retryable(status_code: int) -> bool:
    return status_code in (409, 429, 500, 502, 503, 504)


def stripe_request_with_retries(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
    timeout: int = 60,
    max_retries: int = 2,
) -> Dict[str, Any]:
    attempt = 0
    backoff = 0.5
    while True:
        status, payload = stripe_request(
            method,
            path,
            params=params,
            idempotency_key=idempotency_key,
            stripe_account=stripe_account,
            timeout=timeout,
        )
        if status and status < 400:
            return payload
        if attempt >= max_retries or not maybe_retryable(status):
            return payload
        time.sleep(backoff)
        backoff *= 2
        attempt += 1
