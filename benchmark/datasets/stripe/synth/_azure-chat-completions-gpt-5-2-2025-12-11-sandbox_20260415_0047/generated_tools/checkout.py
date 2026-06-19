"""Checkout & Payment Links & Billing Portal."""

from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import stripe_request


@mcp.tool()
def checkout_sessions_create(
    *,
    mode: str,
    success_url: str,
    cancel_url: str,
    line_items: list[Dict[str, Any]],
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
) -> Dict[str, Any]:
    """Create a Checkout Session (/v1/checkout/sessions)."""

    data: Dict[str, Any] = {
        "mode": mode,
        "success_url": success_url,
        "cancel_url": cancel_url,
        "line_items": line_items,
    }
    if customer is not None:
        data["customer"] = customer
    if customer_email is not None:
        data["customer_email"] = customer_email
    if metadata is not None:
        data["metadata"] = metadata
    if allow_promotion_codes is not None:
        data["allow_promotion_codes"] = allow_promotion_codes
    return stripe_request("POST", "/v1/checkout/sessions", data=data)


@mcp.tool()
def payment_links_create(
    *,
    line_items: list[Dict[str, Any]],
    active: Optional[bool] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create a Payment Link (/v1/payment_links)."""

    data: Dict[str, Any] = {"line_items": line_items}
    if active is not None:
        data["active"] = active
    if after_completion is not None:
        data["after_completion"] = after_completion
    if metadata is not None:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/payment_links", data=data)


@mcp.tool()
def billing_portal_sessions_create(*, customer: str, return_url: str) -> Dict[str, Any]:
    """Create a Billing Portal session (/v1/billing_portal/sessions)."""

    return stripe_request(
        "POST",
        "/v1/billing_portal/sessions",
        data={"customer": customer, "return_url": return_url},
    )
