"""
eBay Buy Order API tools — Guest Checkout flow.
Covers: initiateGuestCheckoutSession, getGuestCheckoutSession,
        updateGuestCheckoutSession, initiateGuestPayment,
        getGuestPurchaseOrder, placeGuestOrder.
"""

from mcp.server.fastmcp import FastMCP
from .auth import api_get, api_post, api_put

mcp = FastMCP("ebay-order")

ORDER_BASE = "/buy/order/v2"


# ---------------------------------------------------------------------------
# Guest Checkout Session
# ---------------------------------------------------------------------------

@mcp.tool()
def initiate_guest_checkout_session(
    line_items: list[dict],
    shipping_address: dict | None = None,
    credit_card: dict | None = None,
    contact_email: str = "",
    marketing_terms_accepted: bool = False,
) -> dict:
    """
    Initiate a guest checkout session for one or more eBay items.

    Args:
        line_items: List of line item dicts. Each must contain:
            - itemId (str): eBay item ID (e.g. 'v1|123456789|0')
            - quantity (int): Number of units to purchase
            - (optional) itemAspects: list of aspect name/value dicts for variations
        shipping_address: Shipping address dict with fields:
            - addressLine1, addressLine2 (optional), city, stateOrProvince,
              postalCode, countryCode, fullName, phoneNumber
        credit_card: Credit card dict with fields:
            - accountHolderName, cardNumber, cvvNumber, expireMonth, expireYear,
              billingAddress (same structure as shipping_address)
        contact_email: Buyer's email address for order confirmation.
        marketing_terms_accepted: Whether buyer accepts marketing terms.
    Returns:
        dict with checkoutSessionId and session details.
    """
    body: dict = {"lineItemInputs": line_items}
    if shipping_address:
        body["shippingAddress"] = shipping_address
    if credit_card:
        body["creditCard"] = credit_card
    if contact_email:
        body["contactEmail"] = contact_email
    if marketing_terms_accepted:
        body["marketingTermsAccepted"] = marketing_terms_accepted
    return api_post(f"{ORDER_BASE}/guest_checkout_session/initiate", body=body)


@mcp.tool()
def get_guest_checkout_session(checkout_session_id: str) -> dict:
    """
    Retrieve the current state of a guest checkout session.

    Args:
        checkout_session_id: The checkout session ID returned by initiate_guest_checkout_session.
    Returns:
        dict with full session details including line items, pricing, and shipping options.
    """
    return api_get(f"{ORDER_BASE}/guest_checkout_session/{checkout_session_id}")


@mcp.tool()
def update_guest_checkout_session(
    checkout_session_id: str,
    shipping_address: dict | None = None,
    credit_card: dict | None = None,
    contact_email: str = "",
    shipping_option: dict | None = None,
    coupon_code: str = "",
) -> dict:
    """
    Update an existing guest checkout session (address, payment, shipping option, coupon).

    Args:
        checkout_session_id: The checkout session ID to update.
        shipping_address: Updated shipping address dict.
        credit_card: Updated credit card dict.
        contact_email: Updated buyer email address.
        shipping_option: Selected shipping option dict with:
            - shippingOptionId (str): ID from the session's available shipping options
        coupon_code: Promotional coupon code to apply.
    Returns:
        dict with updated session details.
    """
    body: dict = {}
    if shipping_address:
        body["shippingAddress"] = shipping_address
    if credit_card:
        body["creditCard"] = credit_card
    if contact_email:
        body["contactEmail"] = contact_email
    if shipping_option:
        body["shippingOption"] = shipping_option
    if coupon_code:
        body["couponCode"] = coupon_code
    return api_put(
        f"{ORDER_BASE}/guest_checkout_session/{checkout_session_id}/update", body=body
    )


@mcp.tool()
def apply_guest_coupon(
    checkout_session_id: str,
    coupon_code: str,
) -> dict:
    """
    Apply a coupon/promotional code to a guest checkout session.

    Args:
        checkout_session_id: The checkout session ID.
        coupon_code: The coupon or promotional code to apply.
    Returns:
        dict with updated session details including adjusted pricing.
    """
    body = {"couponCode": coupon_code}
    return api_post(
        f"{ORDER_BASE}/guest_checkout_session/{checkout_session_id}/apply_coupon",
        body=body,
    )


@mcp.tool()
def remove_guest_coupon(checkout_session_id: str, coupon_code: str) -> dict:
    """
    Remove a previously applied coupon from a guest checkout session.

    Args:
        checkout_session_id: The checkout session ID.
        coupon_code: The coupon code to remove.
    Returns:
        dict with updated session details.
    """
    body = {"couponCode": coupon_code}
    return api_post(
        f"{ORDER_BASE}/guest_checkout_session/{checkout_session_id}/remove_coupon",
        body=body,
    )


@mcp.tool()
def update_guest_quantity(
    checkout_session_id: str,
    line_item_id: str,
    quantity: int,
) -> dict:
    """
    Update the quantity of a line item in a guest checkout session.

    Args:
        checkout_session_id: The checkout session ID.
        line_item_id: The line item ID within the session.
        quantity: New quantity (must be >= 1).
    Returns:
        dict with updated session details.
    """
    body = {"lineItemId": line_item_id, "quantity": quantity}
    return api_post(
        f"{ORDER_BASE}/guest_checkout_session/{checkout_session_id}/update_quantity",
        body=body,
    )


@mcp.tool()
def update_guest_shipping_option(
    checkout_session_id: str,
    line_item_id: str,
    shipping_option_id: str,
) -> dict:
    """
    Select a shipping option for a line item in a guest checkout session.

    Args:
        checkout_session_id: The checkout session ID.
        line_item_id: The line item ID within the session.
        shipping_option_id: The shipping option ID to select (from available options).
    Returns:
        dict with updated session details.
    """
    body = {
        "lineItemId": line_item_id,
        "shippingOption": {"shippingOptionId": shipping_option_id},
    }
    return api_post(
        f"{ORDER_BASE}/guest_checkout_session/{checkout_session_id}/update_shipping_option",
        body=body,
    )


# ---------------------------------------------------------------------------
# Place Order / Payment
# ---------------------------------------------------------------------------

@mcp.tool()
def initiate_guest_payment(checkout_session_id: str) -> dict:
    """
    Initiate payment for a guest checkout session (triggers the payment process).

    This is the penultimate step before placing the order. Call this after
    all session details (address, payment, shipping) are confirmed.

    Args:
        checkout_session_id: The checkout session ID ready for payment.
    Returns:
        dict with payment initiation result.
    """
    return api_post(
        f"{ORDER_BASE}/guest_checkout_session/{checkout_session_id}/initiate_payment"
    )


@mcp.tool()
def place_guest_order(checkout_session_id: str) -> dict:
    """
    Place the final guest order, completing the checkout flow.

    Call this after initiate_guest_payment succeeds.

    Args:
        checkout_session_id: The checkout session ID with completed payment.
    Returns:
        dict with purchaseOrderId and order confirmation details.
    """
    body = {"checkoutSessionId": checkout_session_id}
    return api_post(f"{ORDER_BASE}/guest_purchase_order", body=body)


# ---------------------------------------------------------------------------
# Purchase Order Retrieval
# ---------------------------------------------------------------------------

@mcp.tool()
def get_guest_purchase_order(purchase_order_id: str) -> dict:
    """
    Retrieve details of a completed guest purchase order.

    Args:
        purchase_order_id: The purchase order ID returned by place_guest_order.
    Returns:
        dict with full order details including line items, pricing, and status.
    """
    return api_get(f"{ORDER_BASE}/guest_purchase_order/{purchase_order_id}")
