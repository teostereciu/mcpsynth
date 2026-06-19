"""Shared HTTP utilities for Stripe API tools."""

from __future__ import annotations

import os
import time
from typing import Any, Dict, Optional, Tuple, Union

import requests

STRIPE_API_BASE = "https://api.stripe.com"


def _stripe_headers(api_key: Optional[str] = None) -> Dict[str, str]:
    key = api_key or os.environ.get("STRIPE_API_KEY")
    if not key:
        # Return empty; caller will handle error.
        return {}
    return {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Stripe-Version": os.environ.get("STRIPE_API_VERSION", "2024-06-20"),
    }


def _flatten(prefix: str, value: Any, out: Dict[str, Any]) -> None:
    """Flatten nested dict/list into Stripe form-encoding style keys.

    Examples:
      {"invoice_settings": {"default_payment_method": "pm_..."}}
        -> invoice_settings[default_payment_method]=...
      {"items": [{"price": "price_...", "quantity": 2}]}
        -> items[0][price]=..., items[0][quantity]=2
    """

    if value is None:
        return
    if isinstance(value, dict):
        for k, v in value.items():
            _flatten(f"{prefix}[{k}]" if prefix else str(k), v, out)
        return
    if isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            _flatten(f"{prefix}[{i}]", v, out)
        return
    out[prefix] = value


def encode_form(data: Optional[Dict[str, Any]]) -> Dict[str, Any]:
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
    query: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    api_key: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
    timeout: float = 60.0,
) -> Dict[str, Any]:
    """Perform a Stripe API request.

    Returns JSON dict on success; on error returns {"error": ..., "status": ...}.
    """

    headers = _stripe_headers(api_key)
    if not headers:
        return {"error": "Missing STRIPE_API_KEY environment variable", "status": 401}

    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key
    if stripe_account:
        headers["Stripe-Account"] = stripe_account

    url = STRIPE_API_BASE + path

    try:
        resp = requests.request(
            method.upper(),
            url,
            headers=headers,
            params=query or None,
            data=encode_form(data),
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": f"Network error calling Stripe: {e}", "status": 503}

    try:
        payload = resp.json()
    except ValueError:
        payload = {"raw": resp.text}

    if 200 <= resp.status_code < 300:
        return payload

    # Stripe error format: {"error": {"message": ..., "type": ..., ...}}
    err = payload.get("error") if isinstance(payload, dict) else None
    message = None
    if isinstance(err, dict):
        message = err.get("message")
    if not message:
        message = payload.get("message") if isinstance(payload, dict) else None
    if not message:
        message = resp.text

    return {
        "error": message,
        "status": resp.status_code,
        "stripe_error": err,
        "response": payload,
    }


def unix_timestamp_now() -> int:
    return int(time.time())
