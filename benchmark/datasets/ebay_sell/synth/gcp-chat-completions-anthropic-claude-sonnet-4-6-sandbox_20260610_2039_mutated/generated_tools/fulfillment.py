"""eBay Sell Fulfillment API tools."""
from typing import Any, Optional
from .client import get_client


# --- Orders ---

def get_order(order_id: str, field_groups: Optional[str] = None) -> dict:
    """Retrieve the contents of an order by its unique identifier."""
    client = get_client()
    params = {}
    if field_groups is not None:
        params["fieldGroups"] = field_groups
    return client.request("GET", f"/sell/fulfillment/v1/order/{order_id}", params=params)


def get_orders(
    filter: Optional[str] = None,
    order_ids: Optional[str] = None,
    field_groups: Optional[str] = None,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
) -> dict:
    """Search for and retrieve one or more orders based on filters."""
    client = get_client()
    params = {}
    if filter is not None:
        params["filter"] = filter
    if order_ids is not None:
        params["orderIds"] = order_ids
    if field_groups is not None:
        params["fieldGroups"] = field_groups
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return client.request("GET", "/sell/fulfillment/v1/order", params=params)


def issue_refund(order_id: str, body: dict) -> dict:
    """Issue a full or partial refund to a buyer for an order."""
    client = get_client()
    return client.request("POST", f"/sell/fulfillment/v1/order/{order_id}/issue_refund", json=body)


# --- Shipping Fulfillments ---

def create_shipping_fulfillment(order_id: str, body: dict) -> dict:
    """Create a shipping fulfillment for a package within an order."""
    client = get_client()
    return client.request("POST", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment", json=body)


def get_shipping_fulfillments(order_id: str) -> dict:
    """Retrieve all shipping fulfillments for a specified order."""
    client = get_client()
    return client.request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment")


def get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> dict:
    """Retrieve a specific shipping fulfillment by order ID and fulfillment ID."""
    client = get_client()
    return client.request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment/{fulfillment_id}")


# --- Payment Disputes ---

def get_payment_dispute_summaries(
    order_id: Optional[str] = None,
    buyer_username: Optional[str] = None,
    open_date_from: Optional[str] = None,
    open_date_to: Optional[str] = None,
    payment_dispute_status: Optional[str] = None,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
) -> dict:
    """Retrieve payment disputes filed against the seller with optional filters."""
    client = get_client()
    params = {}
    if order_id is not None:
        params["order_id"] = order_id
    if buyer_username is not None:
        params["buyer_username"] = buyer_username
    if open_date_from is not None:
        params["open_date_from"] = open_date_from
    if open_date_to is not None:
        params["open_date_to"] = open_date_to
    if payment_dispute_status is not None:
        params["payment_dispute_status"] = payment_dispute_status
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return client.request("GET", "/sell/fulfillment/v1/payment_dispute_summary", params=params)


def get_payment_dispute(payment_dispute_id: str) -> dict:
    """Retrieve detailed information on a specific payment dispute."""
    client = get_client()
    return client.request("GET", f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}")


def accept_payment_dispute(payment_dispute_id: str, body: dict) -> dict:
    """Accept a payment dispute filed by a buyer."""
    client = get_client()
    return client.request("POST", f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/accept", json=body)


def contest_payment_dispute(payment_dispute_id: str, body: dict) -> dict:
    """Contest a payment dispute initiated by the buyer."""
    client = get_client()
    return client.request("POST", f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/contest", json=body)


def add_evidence(payment_dispute_id: str, body: dict) -> dict:
    """Add an evidence file to a payment dispute."""
    client = get_client()
    return client.request("POST", f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/add_evidence", json=body)


def update_evidence(payment_dispute_id: str, body: dict) -> dict:
    """Update evidence for a payment dispute."""
    client = get_client()
    return client.request("POST", f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/update_evidence", json=body)


def get_payment_dispute_activities(payment_dispute_id: str) -> dict:
    """Retrieve the activity history for a payment dispute."""
    client = get_client()
    return client.request("GET", f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/activity")
