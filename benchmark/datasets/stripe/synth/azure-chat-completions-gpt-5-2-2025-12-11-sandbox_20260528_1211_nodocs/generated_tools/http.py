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
    """Flatten nested dict/list into Stripe-style form encoding keys.

    Examples:
      {"metadata": {"a": "b"}} -> {"metadata[a]": "b"}
      {"items": [{"price": "p", "quantity": 1}]} -> {"items[0][price]": "p", "items[0][quantity]": "1"}
    """
    out: Dict[str, str] = {}

    if data is None:
        return out

    if isinstance(data, (str, int, float, bool)):
        if prefix:
            out[prefix] = str(data).lower() if isinstance(data, bool) else str(data)
        return out

    if isinstance(data, dict):
        for k, v in data.items():
            key = f"{prefix}[{k}]" if prefix else str(k)
            out.update(_flatten_params(v, key))
        return out

    if isinstance(data, (list, tuple)):
        for i, v in enumerate(data):
            key = f"{prefix}[{i}]" if prefix else str(i)
            out.update(_flatten_params(v, key))
        return out

    # Fallback: stringify
    if prefix:
        out[prefix] = str(data)
    return out


def stripe_request(
    method: str,
    path: str,
    *,
    query: Optional[Dict[str, Any]] = None,
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
    params = query or None
    form = _flatten_params(data or {}) if data is not None else None

    last_err: Optional[Dict[str, Any]] = None
    for attempt in range(max_retries + 1):
        try:
            resp = requests.request(
                method=method.upper(),
                url=url,
                headers=headers,
                params=params,
                data=form,
                timeout=timeout,
            )
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
            return {"result": payload}, None

        # Stripe error format: {"error": {...}}
        if isinstance(payload, dict) and "error" in payload:
            err = payload["error"]
            if isinstance(err, dict):
                return None, {
                    "error": err.get("message") or "Stripe API error",
                    "type": err.get("type"),
                    "code": err.get("code"),
                    "param": err.get("param"),
                    "status": resp.status_code,
                    "request_id": resp.headers.get("request-id"),
                    "raw": payload,
                }

        return None, {
            "error": f"HTTP {resp.status_code}",
            "status": resp.status_code,
            "request_id": resp.headers.get("request-id"),
            "raw": payload,
        }

    return None, last_err or {"error": "Unknown error"}
