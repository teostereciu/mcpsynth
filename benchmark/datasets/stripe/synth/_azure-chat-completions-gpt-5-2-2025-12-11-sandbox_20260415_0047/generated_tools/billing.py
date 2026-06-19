"""Billing domain: Products, Prices, Subscriptions, Subscription Items/Schedules, Invoices, Invoice Items, Coupons/Promotion Codes."""

from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import stripe_request


# Products
@mcp.tool()
def products_create(
    *,
    name: str,
    description: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create a product (/v1/products)."""

    data: Dict[str, Any] = {"name": name}
    if description is not None:
        data["description"] = description
    if active is not None:
        data["active"] = active
    if metadata is not None:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/products", data=data)


# Prices
@mcp.tool()
def prices_create(
    *,
    unit_amount: int,
    currency: str,
    product: str,
    recurring: Optional[Dict[str, Any]] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create a price (/v1/prices)."""

    data: Dict[str, Any] = {
        "unit_amount": unit_amount,
        "currency": currency,
        "product": product,
    }
    if recurring is not None:
        data["recurring"] = recurring
    if nickname is not None:
        data["nickname"] = nickname
    if metadata is not None:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/prices", data=data)


# Subscriptions
@mcp.tool()
def subscriptions_create(
    *,
    customer: str,
    items: list[Dict[str, Any]],
    default_payment_method: Optional[str] = None,
    payment_behavior: Optional[str] = None,
    proration_behavior: Optional[str] = None,
    trial_end: Optional[int] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    promotion_code: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create a subscription (/v1/subscriptions)."""

    data: Dict[str, Any] = {"customer": customer, "items": items}
    if default_payment_method is not None:
        data["default_payment_method"] = default_payment_method
    if payment_behavior is not None:
        data["payment_behavior"] = payment_behavior
    if proration_behavior is not None:
        data["proration_behavior"] = proration_behavior
    if trial_end is not None:
        data["trial_end"] = trial_end
    if discounts is not None:
        data["discounts"] = discounts
    if promotion_code is not None:
        data["promotion_code"] = promotion_code
    if metadata is not None:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/subscriptions", data=data)


@mcp.tool()
def subscriptions_cancel(subscription_id: str, *, invoice_now: Optional[bool] = None, prorate: Optional[bool] = None) -> Dict[str, Any]:
    """Cancel a subscription immediately (/v1/subscriptions/{id})."""

    data: Dict[str, Any] = {}
    if invoice_now is not None:
        data["invoice_now"] = invoice_now
    if prorate is not None:
        data["prorate"] = prorate
    return stripe_request("DELETE", f"/v1/subscriptions/{subscription_id}", data=data)


@mcp.tool()
def subscriptions_retrieve(subscription_id: str) -> Dict[str, Any]:
    """Retrieve a subscription (/v1/subscriptions/{id})."""

    return stripe_request("GET", f"/v1/subscriptions/{subscription_id}")


# Subscription Items
@mcp.tool()
def subscription_items_update(
    subscription_item_id: str,
    *,
    quantity: Optional[int] = None,
    proration_behavior: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a subscription item (/v1/subscription_items/{id})."""

    data: Dict[str, Any] = {}
    if quantity is not None:
        data["quantity"] = quantity
    if proration_behavior is not None:
        data["proration_behavior"] = proration_behavior
    return stripe_request("POST", f"/v1/subscription_items/{subscription_item_id}", data=data)


# Metered usage records (legacy endpoint)
@mcp.tool()
def subscription_items_create_usage_record(
    subscription_item_id: str,
    *,
    quantity: int,
    timestamp: Optional[int] = None,
    action: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a usage record (/v1/subscription_items/{id}/usage_records)."""

    data: Dict[str, Any] = {"quantity": quantity}
    if timestamp is not None:
        data["timestamp"] = timestamp
    if action is not None:
        data["action"] = action
    return stripe_request("POST", f"/v1/subscription_items/{subscription_item_id}/usage_records", data=data)


# Subscription Schedules
@mcp.tool()
def subscription_schedules_create(
    *,
    from_subscription: Optional[str] = None,
    phases: Optional[list[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """Create a subscription schedule (/v1/subscription_schedules)."""

    data: Dict[str, Any] = {}
    if from_subscription is not None:
        data["from_subscription"] = from_subscription
    if phases is not None:
        data["phases"] = phases
    return stripe_request("POST", "/v1/subscription_schedules", data=data)


# Invoice Items
@mcp.tool()
def invoiceitems_create(
    *,
    customer: str,
    amount: int,
    currency: str,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """Create an invoice item (/v1/invoiceitems)."""

    data: Dict[str, Any] = {"customer": customer, "amount": amount, "currency": currency}
    if description is not None:
        data["description"] = description
    return stripe_request("POST", "/v1/invoiceitems", data=data)


# Invoices
@mcp.tool()
def invoices_create(
    *,
    customer: str,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
) -> Dict[str, Any]:
    """Create an invoice (/v1/invoices)."""

    data: Dict[str, Any] = {"customer": customer}
    if auto_advance is not None:
        data["auto_advance"] = auto_advance
    if collection_method is not None:
        data["collection_method"] = collection_method
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    return stripe_request("POST", "/v1/invoices", data=data)


@mcp.tool()
def invoices_finalize(invoice_id: str, *, auto_advance: Optional[bool] = None) -> Dict[str, Any]:
    """Finalize an invoice (/v1/invoices/{id}/finalize)."""

    data: Dict[str, Any] = {}
    if auto_advance is not None:
        data["auto_advance"] = auto_advance
    return stripe_request("POST", f"/v1/invoices/{invoice_id}/finalize", data=data)


@mcp.tool()
def invoices_send(invoice_id: str) -> Dict[str, Any]:
    """Send an invoice (/v1/invoices/{id}/send)."""

    return stripe_request("POST", f"/v1/invoices/{invoice_id}/send")


@mcp.tool()
def invoices_void(invoice_id: str) -> Dict[str, Any]:
    """Void an invoice (/v1/invoices/{id}/void)."""

    return stripe_request("POST", f"/v1/invoices/{invoice_id}/void")


# Coupons & Promotion Codes
@mcp.tool()
def coupons_create(
    *,
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    duration: str = "once",
    name: Optional[str] = None,
    id: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a coupon (/v1/coupons)."""

    data: Dict[str, Any] = {"duration": duration}
    if percent_off is not None:
        data["percent_off"] = percent_off
    if amount_off is not None:
        data["amount_off"] = amount_off
    if currency is not None:
        data["currency"] = currency
    if name is not None:
        data["name"] = name
    if id is not None:
        data["id"] = id
    return stripe_request("POST", "/v1/coupons", data=data)


@mcp.tool()
def promotion_codes_create(
    *,
    coupon: str,
    code: str,
    active: Optional[bool] = None,
    max_redemptions: Optional[int] = None,
) -> Dict[str, Any]:
    """Create a promotion code (/v1/promotion_codes)."""

    data: Dict[str, Any] = {"coupon": coupon, "code": code}
    if active is not None:
        data["active"] = active
    if max_redemptions is not None:
        data["max_redemptions"] = max_redemptions
    return stripe_request("POST", "/v1/promotion_codes", data=data)
