"""
eBay Sell Fulfillment API tools.
Covers: orders, shipping fulfillments, payment disputes.
"""

from mcp.server.fastmcp import FastMCP
from .auth import api_get, api_post, api_put, api_patch

mcp = FastMCP("ebay-fulfillment")


# ── Orders ───────────────────────────────────────────────────────────────────

@mcp.tool()
def get_orders(filter: str | None = None,
               limit: int = 50,
               offset: int = 0,
               order_ids: str | None = None,
               field_groups: str | None = None) -> dict:
    """
    Retrieve a list of orders.

    Args:
        filter: Filter string, e.g. 'orderfulfillmentstatus:{NOT_STARTED|IN_PROGRESS}'.
        limit: Number of orders per page (max 200).
        offset: Pagination offset.
        order_ids: Comma-separated list of order IDs to retrieve.
        field_groups: Additional field groups to include (e.g. TAX_BREAKDOWN).
    """
    params: dict = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if order_ids:
        params["orderIds"] = order_ids
    if field_groups:
        params["fieldGroups"] = field_groups
    return api_get("/sell/fulfillment/v1/order", params=params)


@mcp.tool()
def get_order(order_id: str, field_groups: str | None = None) -> dict:
    """
    Retrieve a single order by order ID.

    Args:
        order_id: The eBay order ID.
        field_groups: Optional additional field groups.
    """
    params = {}
    if field_groups:
        params["fieldGroups"] = field_groups
    return api_get(f"/sell/fulfillment/v1/order/{order_id}", params=params or None)


@mcp.tool()
def issue_order_refund(order_id: str, reason_for_refund: str,
                       comment: str | None = None,
                       refund_items: list[dict] | None = None) -> dict:
    """
    Issue a refund for an order.

    Args:
        order_id: The eBay order ID.
        reason_for_refund: Reason code (e.g. BUYER_CANCEL, ITEM_NOT_RECEIVED).
        comment: Optional comment for the refund.
        refund_items: Optional list of line items with refund amounts.
    """
    body: dict = {"reasonForRefund": reason_for_refund}
    if comment:
        body["comment"] = comment
    if refund_items:
        body["refundItems"] = refund_items
    return api_post(f"/sell/fulfillment/v1/order/{order_id}/issue_refund", body=body)


# ── Shipping Fulfillments ────────────────────────────────────────────────────

@mcp.tool()
def get_shipping_fulfillments(order_id: str) -> dict:
    """
    Retrieve all shipping fulfillments for an order.

    Args:
        order_id: The eBay order ID.
    """
    return api_get(f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment")


@mcp.tool()
def get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> dict:
    """
    Retrieve a single shipping fulfillment.

    Args:
        order_id: The eBay order ID.
        fulfillment_id: The fulfillment ID.
    """
    return api_get(f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment/{fulfillment_id}")


@mcp.tool()
def create_shipping_fulfillment(order_id: str, tracking_number: str,
                                 shipping_carrier_code: str,
                                 line_items: list[dict],
                                 shipped_date: str | None = None) -> dict:
    """
    Create a shipping fulfillment (mark items as shipped with tracking).

    Args:
        order_id: The eBay order ID.
        tracking_number: Carrier tracking number.
        shipping_carrier_code: Carrier code (e.g. USPS, UPS, FEDEX).
        line_items: List of line item references being fulfilled.
        shipped_date: ISO 8601 date/time of shipment (defaults to now).
    """
    body: dict = {
        "trackingNumber": tracking_number,
        "shippingCarrierCode": shipping_carrier_code,
        "lineItems": line_items,
    }
    if shipped_date:
        body["shippedDate"] = shipped_date
    return api_post(f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment", body=body)


# ── Payment Disputes ─────────────────────────────────────────────────────────

@mcp.tool()
def get_payment_disputes(order_id: str | None = None,
                          buyer_username: str | None = None,
                          open_date_from: str | None = None,
                          open_date_to: str | None = None,
                          payment_dispute_status: str | None = None,
                          limit: int = 50,
                          offset: int = 0) -> dict:
    """
    Retrieve payment disputes (chargebacks/INR claims).

    Args:
        order_id: Filter by order ID.
        buyer_username: Filter by buyer username.
        open_date_from: ISO 8601 start date filter.
        open_date_to: ISO 8601 end date filter.
        payment_dispute_status: Status filter (e.g. OPEN, CLOSED).
        limit: Results per page.
        offset: Pagination offset.
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
    if payment_dispute_status:
        params["payment_dispute_status"] = payment_dispute_status
    return api_get("/sell/fulfillment/v1/payment_dispute", params=params)


@mcp.tool()
def get_payment_dispute(payment_dispute_id: str) -> dict:
    """
    Retrieve a single payment dispute by ID.

    Args:
        payment_dispute_id: The payment dispute ID.
    """
    return api_get(f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}")


@mcp.tool()
def accept_payment_dispute(payment_dispute_id: str,
                            return_address: dict | None = None) -> dict:
    """
    Accept a payment dispute (concede the claim).

    Args:
        payment_dispute_id: The payment dispute ID.
        return_address: Optional return address if buyer must return item.
    """
    body: dict = {}
    if return_address:
        body["returnAddress"] = return_address
    return api_post(f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/accept", body=body)


@mcp.tool()
def contest_payment_dispute(payment_dispute_id: str,
                             revision: int,
                             note: str | None = None) -> dict:
    """
    Contest a payment dispute by providing evidence.

    Args:
        payment_dispute_id: The payment dispute ID.
        revision: Current revision number of the dispute.
        note: Optional note to include with the contest.
    """
    body: dict = {"revision": revision}
    if note:
        body["note"] = note
    return api_post(f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/contest", body=body)


@mcp.tool()
def add_evidence_to_payment_dispute(payment_dispute_id: str,
                                     evidence_type: str,
                                     files: list[dict],
                                     line_items: list[dict] | None = None) -> dict:
    """
    Add evidence files to a payment dispute.

    Args:
        payment_dispute_id: The payment dispute ID.
        evidence_type: Type of evidence (e.g. PROOF_OF_SHIPPING, PROOF_OF_DELIVERY).
        files: List of file reference objects (fileId).
        line_items: Optional list of line items the evidence relates to.
    """
    body: dict = {"evidenceType": evidence_type, "files": files}
    if line_items:
        body["lineItems"] = line_items
    return api_post(f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/add_evidence",
                    body=body)


@mcp.tool()
def get_payment_dispute_activities(payment_dispute_id: str) -> dict:
    """
    Retrieve the activity history for a payment dispute.

    Args:
        payment_dispute_id: The payment dispute ID.
    """
    return api_get(f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/activity")


@mcp.tool()
def get_payment_dispute_evidence(payment_dispute_id: str) -> dict:
    """
    Retrieve evidence documents associated with a payment dispute.

    Args:
        payment_dispute_id: The payment dispute ID.
    """
    return api_get(f"/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/fetch_evidence_content")
