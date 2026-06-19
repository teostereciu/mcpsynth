"""Webhook utilities.

Stripe webhook signature verification requires the raw request body and the
Stripe-Signature header. This module provides a lightweight verifier using
Stripe's documented HMAC scheme.

Note: This is not a full replacement for stripe-python's Webhook utility, but
is sufficient for test-mode parsing/verification in many cases.
"""

from __future__ import annotations

import hmac
import hashlib
import json
from typing import Any, Dict, Optional

from . import mcp


def _parse_sig_header(sig_header: str) -> Dict[str, str]:
    parts = [p.strip() for p in sig_header.split(",") if p.strip()]
    out: Dict[str, str] = {}
    for p in parts:
        if "=" in p:
            k, v = p.split("=", 1)
            out[k] = v
    return out


def _compute_signature(secret: str, timestamp: str, payload: str) -> str:
    signed_payload = f"{timestamp}.{payload}".encode("utf-8")
    mac = hmac.new(secret.encode("utf-8"), signed_payload, hashlib.sha256)
    return mac.hexdigest()


@mcp.tool()
def webhook_construct_event(
    payload: str,
    sig_header: Optional[str] = None,
    secret: Optional[str] = None,
    tolerance: int = 300,
) -> Dict[str, Any]:
    """Parse (and optionally verify) a Stripe webhook event.

    Args:
      payload: Raw JSON string body.
      sig_header: Value of Stripe-Signature header.
      secret: Webhook signing secret (whsec_...). If provided with sig_header,
        verification is performed.
      tolerance: Allowed timestamp drift in seconds.

    Returns:
      Parsed event dict, or {"error": ...}.
    """

    try:
        event = json.loads(payload)
    except Exception as e:
        return {"error": f"Invalid JSON payload: {e}"}

    if secret and sig_header:
        sig = _parse_sig_header(sig_header)
        t = sig.get("t")
        v1 = sig.get("v1")
        if not t or not v1:
            return {"error": "Invalid Stripe-Signature header"}

        # Verify timestamp tolerance
        try:
            ts = int(t)
        except ValueError:
            return {"error": "Invalid timestamp in Stripe-Signature header"}

        import time

        now = int(time.time())
        if abs(now - ts) > tolerance:
            return {"error": "Webhook timestamp outside tolerance"}

        expected = _compute_signature(secret, t, payload)
        if not hmac.compare_digest(expected, v1):
            return {"error": "Invalid webhook signature"}

    return event
