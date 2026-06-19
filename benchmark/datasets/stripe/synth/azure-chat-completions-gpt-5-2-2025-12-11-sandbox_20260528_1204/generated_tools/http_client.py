import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


STRIPE_BASE_URL = "https://api.stripe.com"


def _flatten(prefix: str, value: Any, out: Dict[str, Any]) -> None:
    """Flatten nested dict/list into Stripe form-encoding style keys.

    Examples:
      {"metadata": {"a": "b"}} -> {"metadata[a]": "b"}
      {"items": [{"price": "p"}]} -> {"items[0][price]": "p"}
    """
    if value is None:
        return
    if isinstance(value, dict):
        for k, v in value.items():
            key = f"{prefix}[{k}]" if prefix else str(k)
            _flatten(key, v, out)
        return
    if isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            key = f"{prefix}[{i}]"
            _flatten(key, v, out)
        return
    out[prefix] = value


def stripe_form_encode(data: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if not data:
        return {}
    out: Dict[str, Any] = {}
    for k, v in data.items():
        _flatten(str(k), v, out)
    return out


def stripe_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    timeout: int = 60,
) -> Dict[str, Any]:
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        return {"error": "STRIPE_API_KEY environment variable is not set"}

    url = STRIPE_BASE_URL + path
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Stripe-Version": "2024-06-20",
    }
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key

    method_u = method.upper()
    try:
        if method_u in ("GET", "DELETE"):
            resp = requests.request(method_u, url, headers=headers, params=stripe_form_encode(params), timeout=timeout)
        else:
            resp = requests.request(
                method_u,
                url,
                headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
                data=stripe_form_encode(params),
                timeout=timeout,
            )

        # Stripe returns JSON for both success and error.
        try:
            payload = resp.json()
        except Exception:
            payload = {"error": f"Non-JSON response from Stripe", "status": resp.status_code, "text": resp.text}

        if resp.status_code >= 400:
            # Normalize Stripe error shape.
            if isinstance(payload, dict) and "error" in payload:
                err = payload.get("error")
                return {
                    "error": err.get("message") if isinstance(err, dict) else str(err),
                    "type": err.get("type") if isinstance(err, dict) else None,
                    "code": err.get("code") if isinstance(err, dict) else None,
                    "param": err.get("param") if isinstance(err, dict) else None,
                    "status": resp.status_code,
                    "raw": payload,
                }
            return {"error": "Stripe API error", "status": resp.status_code, "raw": payload}

        return payload
    except requests.RequestException as e:
        return {"error": f"Request failed: {e.__class__.__name__}: {str(e)}"}
