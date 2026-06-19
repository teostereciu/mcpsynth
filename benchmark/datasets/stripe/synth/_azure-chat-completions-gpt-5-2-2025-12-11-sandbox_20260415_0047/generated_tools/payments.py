"""Payments domain: PaymentIntents, Charges, Refunds, Disputes, SetupIntents."""

from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import stripe_request


# Payment Intents
@mcp.tool()
def payment_intents_create(
    amount: int,
    currency: str,
    *,
    confirm: bool = False,
    payment_method: Optional[str] = None,
    customer: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    off_session: Optional[Any] = None,
    error_on_requires_action: Optional[bool] = None,
) -> Dict[str, Any]:
    """Create a PaymentIntent (/v1/payment_intents)."""

    data: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "confirm": confirm,
    }
    if payment_method is not None:
        data["payment_method"] = payment_method
    if customer is not None:
        data["customer"] = customer
    if setup_future_usage is not None:
        data["setup_future_usage"] = setup_future_usage
    if description is not None:
        data["description"] = description
    if receipt_email is not None:
        data["receipt_email"] = receipt_email
    if metadata is not None:
        data["metadata"] = metadata
    if shipping is not None:
        data["shipping"] = shipping
    if automatic_payment_methods is not None:
        data["automatic_payment_methods"] = automatic_payment_methods
    if off_session is not None:
        data["off_session"] = off_session
    if error_on_requires_action is not None:
        data["error_on_requires_action"] = error_on_requires_action

    return stripe_request("POST", "/v1/payment_intents", data=data)


@mcp.tool()
def payment_intents_retrieve(payment_intent_id: str) -> Dict[str, Any]:
    """Retrieve a PaymentIntent (/v1/payment_intents/{id})."""

    return stripe_request("GET", f"/v1/payment_intents/{payment_intent_id}")


@mcp.tool()
def payment_intents_confirm(
    payment_intent_id: str,
    *,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    off_session: Optional[Any] = None,
) -> Dict[str, Any]:
    """Confirm a PaymentIntent (/v1/payment_intents/{id}/confirm)."""

    data: Dict[str, Any] = {}
    if payment_method is not None:
        data["payment_method"] = payment_method
    if return_url is not None:
        data["return_url"] = return_url
    if off_session is not None:
        data["off_session"] = off_session
    return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/confirm", data=data)


# Refunds
@mcp.tool()
def refunds_create(
    *,
    payment_intent: Optional[str] = None,
    charge: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create a refund (/v1/refunds)."""

    data: Dict[str, Any] = {}
    if payment_intent is not None:
        data["payment_intent"] = payment_intent
    if charge is not None:
        data["charge"] = charge
    if amount is not None:
        data["amount"] = amount
    if reason is not None:
        data["reason"] = reason
    if metadata is not None:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/refunds", data=data)


@mcp.tool()
def refunds_retrieve(refund_id: str) -> Dict[str, Any]:
    """Retrieve a refund (/v1/refunds/{id})."""

    return stripe_request("GET", f"/v1/refunds/{refund_id}")


# Disputes
@mcp.tool()
def disputes_list(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    limit: int = 10,
) -> Dict[str, Any]:
    """List disputes (/v1/disputes)."""

    query: Dict[str, Any] = {"limit": limit}
    if charge is not None:
        query["charge"] = charge
    if payment_intent is not None:
        query["payment_intent"] = payment_intent
    return stripe_request("GET", "/v1/disputes", query=query)


@mcp.tool()
def disputes_retrieve(dispute_id: str) -> Dict[str, Any]:
    """Retrieve a dispute (/v1/disputes/{id})."""

    return stripe_request("GET", f"/v1/disputes/{dispute_id}")


# Setup Intents
@mcp.tool()
def setup_intents_create(
    *,
    customer: Optional[str] = None,
    payment_method_types: Optional[list[str]] = None,
    usage: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create a SetupIntent (/v1/setup_intents)."""

    data: Dict[str, Any] = {}
    if customer is not None:
        data["customer"] = customer
    if payment_method_types is not None:
        data["payment_method_types"] = payment_method_types
    if usage is not None:
        data["usage"] = usage
    if metadata is not None:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/setup_intents", data=data)


@mcp.tool()
def setup_intents_confirm(
    setup_intent_id: str,
    *,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
) -> Dict[str, Any]:
    """Confirm a SetupIntent (/v1/setup_intents/{id}/confirm)."""

    data: Dict[str, Any] = {}
    if payment_method is not None:
        data["payment_method"] = payment_method
    if return_url is not None:
        data["return_url"] = return_url
    return stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/confirm", data=data)
