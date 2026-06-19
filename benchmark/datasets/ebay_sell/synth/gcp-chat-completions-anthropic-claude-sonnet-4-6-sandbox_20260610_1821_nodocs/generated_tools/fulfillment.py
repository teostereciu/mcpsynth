"""
eBay Sell Fulfillment API tools.
Covers: orders, shipping fulfillments, payment disputes.
"""

from mcp.server.fastmcp import FastMCP
from .auth import ebay_request

mcp = FastMCP("ebay-fulfillment")

# ---------------------------------------------------------------------------
# Orders
# ---------------------------------------------------------------------------

@mcp.tool()
def get_orders(
    filter: str | None = None,
    order_ids: str | None = None,
    limit: int = 50,
    offset: int = 0,
    field_groups: str | None = None,
) -> dict:
    """
    Retrieve a list of orders for the seller.

    Args:
        filter: Filter string, e.g. 'orderfulfillmentstatus:{NOT_STARTED|IN_PROGRESS}'
                or 'creationdate:[2024-01-01T00:00:00.000Z..]'.
        order_ids: Comma-separated list of specific order IDs to retrieve.
        limit: Number of orders to return (default 50, max 200).
        offset: Pagination offset (default 0).
        field_groups: Additional fields to include, e.g. 'TAX_BREAKDOWN'.
    """
    params: dict = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if order_ids:
        params["orderIds"] = order_ids
    if field_groups:
        params["fieldgroups"] = field_groups
    return ebay_request("GET", "/sell/fulfillment/v1/order", params=params)


@mcp.tool()
def get_order(order_id: str, field_groups: str | None = None) -> dict:
    """
    Retrieve a single order by its order ID.

    Args:
        order_id: The unique identifier of the order.
        field_groups: Additional fields to include, e.g. 'TAX_BREAKDOWN'.
    """
    params: dict = {}
    if field_groups:
        params["fieldgroups"] = field_groups
    return ebay_request(
        "GET", f"/sell/fulfillment/v1/order/{order_id}", params=params or None
    )


@mcp.tool()
def issue_order_refund(order_id: str, refund_detail: dict) -> dict:
    """
    Issue a refund for an order.

    Args:
        order_id: The unique identifier of the order.
        refund_detail: Refund object with 'reasonForRefund', 'comment',
                       and 'refundItems' (list of line items with amounts).
    """
    return ebay_request(
        "POST",
        f"/sell/fulfillment/v1/order/{order_id}/issue_refund",
        json=refund_detail,
    )


# ---------------------------------------------------------------------------
# Shipping Fulfillments
# ---------------------------------------------------------------------------

@mcp.tool()
def get_shipping_fulfillments(order_id: str) -> dict:
    """
    Retrieve all shipping fulfillments for an order.

    Args:
        order_id: The unique identifier of the order.
    """
    return ebay_request(
        "GET",
        f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment",
    )


@mcp.tool()
def get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> dict:
    """
    Retrieve a specific shipping fulfillment for an order.

    Args:
        order_id: The unique identifier of the order.
        fulfillment_id: The unique identifier of the shipping fulfillment.
    """
    return ebay_request(
        "GET",
        f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment/{fulfillment_id}",
    )


@mcp.tool()
def create_shipping_fulfillment(order_id: str, fulfillment: dict) -> dict:
    """
    Create a shipping fulfillment (mark items as shipped) for an order.

    Args:
        order_id: The unique identifier of the order.
        fulfillment: Fulfillment object with 'lineItems', 'shippedDate',
                     'shippingCarrierCode', 'trackingNumber'.
                     Example: {
                       "lineItems": [{"lineItemId": "...", "quantity": 1}],
                       "shippedDate": "2024-06-01T12:00:00.000Z",
                       "shippingCarrierCode": "USPS",
                       "trackingNumber": "9400111899223397987318"
                     }
    """
    return ebay_request(
        "POST",
        f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment",
        json=fulfillment,
    )


@mcp.tool()
def delete_shipping_fulfillment(order_id: str, fulfillment_id: str) -> dict:
    """
    Delete a shipping fulfillment record from an order.

    Args:
        order_id: The unique identifier of the order.
        fulfillment_id: The unique identifier of the shipping fulfillment.
    """
    return ebay_request(
        "DELETE",
        f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment/{fulfillment_id}",
    )


# ---------------------------------------------------------------------------
# Payment Disputes
# ---------------------------------------------------------------------------

@mcp.tool()
def get_payment_disputes(
    order_id: str | None = None,
    buyer_username: str | None = None,
    open_date_from: str | None = None,
    open_date_to: str | None = None,
    dispute_state: str | None = None,
    limit: int = 50,
    offset: int = 0,
) -> dict:
    """
    Retrieve payment disputes (chargebacks/INADs) for the seller.

    Args:
        order_id: Filter by order ID (optional).
        buyer_username: Filter by buyer username (optional).
        open_date_from: ISO 8601 start date filter (optional).
        open_date_to: ISO 8601 end date filter (optional).
        dispute_state: Filter by state, e.g. 'OPEN', 'CLOSED' (optional).
        limit: Number of disputes to return (default 50).
        offset: Pagination offset (default 0).
    """
    params: dict = {"limit": limit, "offset": offset}
    if order_id:
        params["order_id"] = order_id
    if buyer_username:
        params["buyer_username"] = buyer_username
    if open_date_from:
        params["open_date_from"] = open_date_from
    if open_date_to:
        params["open_date_to"] = open_date_to
    if dispute_state:
        params["dispute_state"] = dispute_state
    return ebay_request(
        "GET", "/sell/fulfillment/v1/payment_dispute", params=params
    )


@mcp.tool()
def get_payment_dispute(payment_dispute_id: str) -> dict:
    """
    Retrieve a specific payment dispute by its ID.

    Args:
        payment_dispute_id: The unique identifier of the payment dispute.
    """
    return ebay_request(
        "GET",
        f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}",
    )


@mcp.tool()
def accept_payment_dispute(payment_dispute_id: str, return_address: dict | None = None) -> dict:
    """
    Accept a payment dispute (concede the chargeback).

    Args:
        payment_dispute_id: The unique identifier of the payment dispute.
        return_address: Optional return address object if a return is required.
    """
    body: dict = {}
    if return_address:
        body["returnAddress"] = return_address
    return ebay_request(
        "POST",
        f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/accept",
        json=body,
    )


@mcp.tool()
def contest_payment_dispute(payment_dispute_id: str, contest_detail: dict) -> dict:
    """
    Contest a payment dispute by providing evidence.

    Args:
        payment_dispute_id: The unique identifier of the payment dispute.
        contest_detail: Object with 'returnAddress' and/or 'revision' fields.
    """
    return ebay_request(
        "POST",
        f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/contest",
        json=contest_detail,
    )


@mcp.tool()
def add_evidence_to_payment_dispute(
    payment_dispute_id: str, evidence: dict
) -> dict:
    """
    Add evidence (documents) to a payment dispute.

    Args:
        payment_dispute_id: The unique identifier of the payment dispute.
        evidence: Evidence object with 'evidenceType' and 'files' (list of
                  file IDs uploaded via upload_evidence_file).
    """
    return ebay_request(
        "POST",
        f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/add_evidence",
        json=evidence,
    )


@mcp.tool()
def get_payment_dispute_activities(payment_dispute_id: str) -> dict:
    """
    Retrieve the activity history for a payment dispute.

    Args:
        payment_dispute_id: The unique identifier of the payment dispute.
    """
    return ebay_request(
        "GET",
        f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/activity",
    )


@mcp.tool()
def get_payment_dispute_summaries(
    order_id: str | None = None,
    dispute_state: str | None = None,
    limit: int = 50,
    offset: int = 0,
) -> dict:
    """
    Retrieve summary information for payment disputes.

    Args:
        order_id: Filter by order ID (optional).
        dispute_state: Filter by state, e.g. 'OPEN', 'CLOSED' (optional).
        limit: Number of summaries to return (default 50).
        offset: Pagination offset (default 0).
    """
    params: dict = {"limit": limit, "offset": offset}
    if order_id:
        params["order_id"] = order_id
    if dispute_state:
        params["dispute_state"] = dispute_state
    return ebay_request(
        "GET",
        "/sell/fulfillment/v1/payment_dispute/get_payment_dispute_summaries",
        params=params,
    )
