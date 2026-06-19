"""
eBay Sell Fulfillment API tools.
Covers: orders, shipping fulfillments, payment disputes.
"""

from typing import Optional
from auth import api_get, api_post, api_put


# ---------------------------------------------------------------------------
# Orders
# ---------------------------------------------------------------------------

def get_orders(
    filter: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
    order_ids: Optional[str] = None,
    field_groups: Optional[str] = None,
) -> dict:
    """
    Get a list of orders.

    filter: eBay filter string, e.g. "orderfulfillmentstatus:{NOT_STARTED|IN_PROGRESS}"
    order_ids: comma-separated list of order IDs
    field_groups: e.g. "TAX_BREAKDOWN"
    """
    params: dict = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if order_ids:
        params["orderIds"] = order_ids
    if field_groups:
        params["fieldGroups"] = field_groups
    return api_get("/sell/fulfillment/v1/order", params=params)


def get_order(order_id: str, field_groups: Optional[str] = None) -> dict:
    """Get a single order by order ID."""
    params = {}
    if field_groups:
        params["fieldGroups"] = field_groups
    return api_get(f"/sell/fulfillment/v1/order/{order_id}", params=params or None)


# ---------------------------------------------------------------------------
# Shipping Fulfillments
# ---------------------------------------------------------------------------

def get_shipping_fulfillments(order_id: str) -> dict:
    """Get all shipping fulfillments for an order."""
    return api_get(f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment")


def get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> dict:
    """Get a specific shipping fulfillment."""
    return api_get(f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment/{fulfillment_id}")


def create_shipping_fulfillment(order_id: str, body: dict) -> dict:
    """
    Create a shipping fulfillment for an order.

    body fields:
      lineItems: list of dicts with lineItemId and quantity
      shippedDate: ISO 8601 date string
      shippingCarrierCode: str (e.g. "USPS", "UPS", "FEDEX")
      trackingNumber: str
    """
    return api_post(f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment", body=body)


# ---------------------------------------------------------------------------
# Payment Disputes
# ---------------------------------------------------------------------------

def get_payment_disputes(
    order_id: Optional[str] = None,
    buyer_username: Optional[str] = None,
    open_date_from: Optional[str] = None,
    open_date_to: Optional[str] = None,
    payment_dispute_status: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
) -> dict:
    """Get a list of payment disputes."""
    params: dict = {"limit": limit, "offset": offset}
    if order_id:
        params["order_id"] = order_id
    if buyer_username:
        params["buyer_username"] = buyer_username
    if open_date_from:
        params["open_date_from"] = open_date_from
    if open_date_to:
        params["open_date_to"] = open_date_to
    if payment_dispute_status:
        params["payment_dispute_status"] = payment_dispute_status
    return api_get("/sell/fulfillment/v1/payment_dispute", params=params)


def get_payment_dispute(payment_dispute_id: str) -> dict:
    """Get a specific payment dispute by ID."""
    return api_get(f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}")


def accept_payment_dispute(payment_dispute_id: str, return_address: Optional[dict] = None,
                            revision: Optional[int] = None) -> dict:
    """Accept a payment dispute."""
    body: dict = {}
    if return_address:
        body["returnAddress"] = return_address
    if revision is not None:
        body["revision"] = revision
    return api_post(f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/accept", body=body)


def contest_payment_dispute(payment_dispute_id: str, body: dict) -> dict:
    """
    Contest a payment dispute.

    body fields:
      note: str
      returnAddress: dict
      revision: int
    """
    return api_post(f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/contest",
                    body=body)


def add_evidence_to_payment_dispute(payment_dispute_id: str, body: dict) -> dict:
    """
    Add evidence to a payment dispute.

    body fields:
      evidenceType: str (e.g. "PROOF_OF_SHIPPING")
      files: list of dicts with fileId
      lineItems: list of dicts
    """
    return api_post(
        f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/add_evidence",
        body=body,
    )


def update_evidence_for_payment_dispute(payment_dispute_id: str, body: dict) -> dict:
    """Update evidence for a payment dispute."""
    return api_put(
        f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/update_evidence",
        body=body,
    )


def upload_evidence_file_for_payment_dispute(payment_dispute_id: str) -> dict:
    """
    Initiate an evidence file upload for a payment dispute.
    Returns upload URL/token details.
    """
    return api_post(
        f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/upload_evidence_file"
    )


def get_activities_for_payment_dispute(payment_dispute_id: str) -> dict:
    """Get the activity history for a payment dispute."""
    return api_get(
        f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/activity"
    )


# ---------------------------------------------------------------------------
# Issue Refund
# ---------------------------------------------------------------------------

def issue_refund(order_id: str, body: dict) -> dict:
    """
    Issue a refund for an order.

    body fields:
      comments: dict with content and contentType
      refundItems: list of dicts with lineItemId, legacyReference, refundAmount
      orderLevelRefundAmount: dict with value and currency
    """
    return api_post(f"/sell/fulfillment/v1/order/{order_id}/issue_refund", body=body)
