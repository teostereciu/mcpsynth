import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


STRIPE_BASE_URL = "https://api.stripe.com"


def _stripe_api_key() -> Optional[str]:
    return os.environ.get("STRIPE_API_KEY")


def _flatten_params(data: Any, prefix: str = "") -> Dict[str, str]:
    """Flatten nested dict/list into Stripe form-encoding style.

    Examples:
      {"metadata": {"a": "b"}} -> {"metadata[a]": "b"}
      {"items": [{"price": "p", "quantity": 1}]} -> {"items[0][price]": "p", "items[0][quantity]": "1"}
    """
    out: Dict[str, str] = {}

    def keyjoin(p: str, k: str) -> str:
        if not p:
            return k
        return f"{p}[{k}]"

    if data is None:
        return out

    if isinstance(data, (str, int, float, bool)):
        out[prefix] = str(data).lower() if isinstance(data, bool) else str(data)
        return out

    if isinstance(data, dict):
        for k, v in data.items():
            if v is None:
                continue
            out.update(_flatten_params(v, keyjoin(prefix, str(k)) if prefix else str(k)))
        return out

    if isinstance(data, (list, tuple)):
        for i, v in enumerate(data):
            if v is None:
                continue
            out.update(_flatten_params(v, keyjoin(prefix, str(i))))
        return out

    # Fallback
    out[prefix] = str(data)
    return out


def stripe_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
    timeout_s: int = 60,
) -> Dict[str, Any]:
    """Make a Stripe API request.

    Returns JSON dict on success; on error returns {"error": ..., "status": ..., "details": ...}.
    """
    api_key = _stripe_api_key()
    if not api_key:
        return {"error": "STRIPE_API_KEY environment variable is not set"}

    url = STRIPE_BASE_URL + path
    headers = {
        "Authorization": f"Bearer {api_key}",
        "User-Agent": "mcp-stripe-server/1.0",
    }
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key
    if stripe_account:
        headers["Stripe-Account"] = stripe_account

    method_u = method.upper()
    data = None
    query = None
    if params:
        if method_u in ("GET", "DELETE"):
            query = _flatten_params(params)
        else:
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            data = _flatten_params(params)

    # Simple retry for 429/5xx
    for attempt in range(3):
        try:
            resp = requests.request(
                method_u,
                url,
                headers=headers,
                params=query,
                data=data,
                timeout=timeout_s,
            )
        except requests.RequestException as e:
            return {"error": "request_failed", "details": str(e)}

        if resp.status_code in (429, 500, 502, 503, 504) and attempt < 2:
            time.sleep(0.5 * (2**attempt))
            continue

        try:
            payload = resp.json()
        except ValueError:
            payload = {"raw": resp.text}

        if 200 <= resp.status_code < 300:
            return payload

        return {
            "error": payload.get("error", payload),
            "status": resp.status_code,
        }

    return {"error": "request_failed", "details": "max retries exceeded"}
