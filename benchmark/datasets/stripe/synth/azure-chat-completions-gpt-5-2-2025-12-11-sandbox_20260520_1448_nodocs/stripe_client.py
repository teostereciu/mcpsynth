import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


STRIPE_BASE_URL = "https://api.stripe.com"


def _encode_form_value(v: Any) -> str:
    if v is None:
        return ""
    if isinstance(v, bool):
        return "true" if v else "false"
    return str(v)


def _flatten_params(prefix: str, value: Any, out: Dict[str, str]) -> None:
    """Flatten nested dict/list into Stripe-style form keys.

    Examples:
      {"metadata": {"a": "b"}} -> metadata[a]=b
      {"items": [{"price": "p", "quantity": 1}]} -> items[0][price]=p, items[0][quantity]=1
    """
    if isinstance(value, dict):
        for k, v in value.items():
            key = f"{prefix}[{k}]" if prefix else str(k)
            _flatten_params(key, v, out)
    elif isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            key = f"{prefix}[{i}]"
            _flatten_params(key, v, out)
    else:
        out[prefix] = _encode_form_value(value)


def to_form(params: Optional[Dict[str, Any]]) -> Dict[str, str]:
    if not params:
        return {}
    out: Dict[str, str] = {}
    for k, v in params.items():
        _flatten_params(str(k), v, out)
    return out


class StripeClient:
    def __init__(self, api_key: Optional[str] = None, base_url: str = STRIPE_BASE_URL, timeout: int = 60):
        self.api_key = api_key or os.getenv("STRIPE_API_KEY", "")
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        idempotency_key: Optional[str] = None,
        stripe_account: Optional[str] = None,
    ) -> Tuple[int, Dict[str, Any]]:
        if not self.api_key:
            return 401, {"error": "Missing STRIPE_API_KEY"}

        url = f"{self.base_url}{path}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        if idempotency_key:
            headers["Idempotency-Key"] = idempotency_key
        if stripe_account:
            headers["Stripe-Account"] = stripe_account

        data = to_form(params)

        try:
            if method.upper() == "GET":
                resp = requests.request(method, url, headers=headers, params=data, timeout=self.timeout)
            else:
                resp = requests.request(method, url, headers=headers, data=data, timeout=self.timeout)
        except requests.RequestException as e:
            return 0, {"error": f"Network error: {e}"}

        try:
            payload = resp.json()
        except ValueError:
            payload = {"error": "Non-JSON response", "status": resp.status_code, "text": resp.text}

        if resp.status_code >= 400:
            # Stripe errors are usually {error: {...}}
            if isinstance(payload, dict) and "error" in payload:
                return resp.status_code, payload
            return resp.status_code, {"error": payload}

        return resp.status_code, payload


def default_idempotency_key(prefix: str = "mcp") -> str:
    return f"{prefix}_{int(time.time() * 1000)}"
