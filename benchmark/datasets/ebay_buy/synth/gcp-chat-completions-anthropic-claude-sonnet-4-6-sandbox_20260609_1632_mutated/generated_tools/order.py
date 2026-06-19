"""
eBay Buy Order API tools (v2) — Guest Checkout Flow.
Covers: initiate session, get session, update quantity/shipping/address,
apply/remove coupon, get purchase order.

Note: Order API uses apix.ebay.com (not api.ebay.com).
All methods require buy.guest.order OAuth scope.
Limited Release: only available to select developers approved by business units.
"""

from __future__ import annotations
from typing import Optional, List, Dict
from .auth import get_auth_header, get_order_base_url


def initiate_guest_checkout_session(
    contact_email: str,
    line_items: List[Dict],
    shipping_address: Dict,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Create an eBay guest checkout session. This is the first step in the
    guest checkout flow. Returns a checkoutSessionId for subsequent calls.

    Args:
        contact_email: The buyer's email address.
        line_items: List of dicts with 'itemId' (RESTful item ID) and 'quantity'.
            Example: [{'itemId': 'v1|123|0', 'quantity': 1}]
            Maximum: 10 line items per session.
        shipping_address: Dict with shipping address fields:
            Required: addressLine1, city, country, phoneNumber, recipient
                (recipient has firstName and lastName)
            Optional: addressLine2, county, postalCode, stateOrProvince
            Example: {
                'addressLine1': '123 Main St',
                'city': 'San Jose',
                'country': 'US',
                'phoneNumber': '+14085551234',
                'postalCode': '95125',
                'stateOrProvince': 'CA',
                'recipient': {'firstName': 'John', 'lastName': 'Doe'}
            }
        marketplace_id: eBay marketplace ID (default EBAY_US).

    Returns:
        Dict with checkoutSessionId, lineItems, pricingSummary, shippingAddress.
    """
    import requests
    url = f"{get_order_base_url()}/buy/order/v2/guest_checkout_session/initiate"
    headers = get_auth_header()
    headers["Content-Type"] = "application/json"
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    body = {
        "contactEmail": contact_email,
        "lineItemInputs": line_items,
        "shippingAddress": shipping_address,
    }
    try:
        resp = requests.post(url, headers=headers, json=body, timeout=30)
        if resp.status_code in (200, 201):
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_guest_checkout_session(
    checkout_session_id: str,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Retrieve the details of an existing eBay guest checkout session.

    Args:
        checkout_session_id: The eBay-assigned checkout session ID returned
            by initiateGuestCheckoutSession.
        marketplace_id: eBay marketplace ID — must match the one used when
            the session was created (default EBAY_US).

    Returns:
        Dict with checkoutSessionId, lineItems, pricingSummary, shippingAddress,
        and any applied coupons.
    """
    import requests
    url = f"{get_order_base_url()}/buy/order/v2/guest_checkout_session/{checkout_session_id}"
    headers = get_auth_header()
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    try:
        resp = requests.get(url, headers=headers, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def update_guest_quantity(
    checkout_session_id: str,
    line_item_id: str,
    quantity: int,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Update the quantity of a specific line item in a guest checkout session.

    Args:
        checkout_session_id: The eBay-assigned checkout session ID.
        line_item_id: The eBay-assigned line item ID within the session.
        quantity: The new quantity for the line item.
        marketplace_id: eBay marketplace ID (default EBAY_US).

    Returns:
        Updated checkout session dict.
    """
    import requests
    url = f"{get_order_base_url()}/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_quantity"
    headers = get_auth_header()
    headers["Content-Type"] = "application/json"
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    body = {"lineItemId": line_item_id, "quantity": quantity}
    try:
        resp = requests.post(url, headers=headers, json=body, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def update_guest_shipping_address(
    checkout_session_id: str,
    shipping_address: Dict,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Update the shipping address for all line items in a guest checkout session.
    All line items in an order must be shipped to the same address.

    Args:
        checkout_session_id: The eBay-assigned checkout session ID.
        shipping_address: Dict with shipping address fields:
            Required: addressLine1, city, country, phoneNumber, recipient
                (recipient has firstName and lastName)
            Optional: addressLine2, county, postalCode, stateOrProvince
        marketplace_id: eBay marketplace ID (default EBAY_US).

    Returns:
        Updated checkout session dict.
    """
    import requests
    url = f"{get_order_base_url()}/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_address"
    headers = get_auth_header()
    headers["Content-Type"] = "application/json"
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    try:
        resp = requests.post(url, headers=headers, json=shipping_address, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def update_guest_shipping_option(
    checkout_session_id: str,
    line_item_id: str,
    shipping_option_id: str,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Update the shipping method/option for a specific line item in a guest
    checkout session. Each line item can have its own shipping option.

    Args:
        checkout_session_id: The eBay-assigned checkout session ID.
        line_item_id: The eBay-assigned line item ID within the session.
        shipping_option_id: The unique ID of the shipping option to select.
            Available shipping option IDs are returned in the lineItems.shippingOptions
            array from getGuestCheckoutSession.
        marketplace_id: eBay marketplace ID (default EBAY_US).

    Returns:
        Updated checkout session dict.
    """
    import requests
    url = f"{get_order_base_url()}/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_option"
    headers = get_auth_header()
    headers["Content-Type"] = "application/json"
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    body = {"lineItemId": line_item_id, "shippingOptionId": shipping_option_id}
    try:
        resp = requests.post(url, headers=headers, json=body, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def apply_guest_coupon(
    checkout_session_id: str,
    redemption_code: str,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Apply a coupon to a guest checkout session. The coupon is applied to all
    eligible items in the order. Maximum one coupon per order.

    Args:
        checkout_session_id: The eBay-assigned checkout session ID.
        redemption_code: The coupon redemption code to apply.
        marketplace_id: eBay marketplace ID (default EBAY_US).

    Returns:
        Updated checkout session dict with appliedCoupons and promotions.
    """
    import requests
    url = f"{get_order_base_url()}/buy/order/v2/guest_checkout_session/{checkout_session_id}/apply_coupon"
    headers = get_auth_header()
    headers["Content-Type"] = "application/json"
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    body = {"redemptionCode": redemption_code}
    try:
        resp = requests.post(url, headers=headers, json=body, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def remove_guest_coupon(
    checkout_session_id: str,
    redemption_code: str,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Remove a coupon from a guest checkout session.

    Args:
        checkout_session_id: The eBay-assigned checkout session ID.
        redemption_code: The coupon redemption code to remove.
        marketplace_id: eBay marketplace ID (default EBAY_US).

    Returns:
        Updated checkout session dict.
    """
    import requests
    url = f"{get_order_base_url()}/buy/order/v2/guest_checkout_session/{checkout_session_id}/remove_coupon"
    headers = get_auth_header()
    headers["Content-Type"] = "application/json"
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    body = {"redemptionCode": redemption_code}
    try:
        resp = requests.post(url, headers=headers, json=body, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_guest_purchase_order(
    purchase_order_id: str,
    marketplace_id: Optional[str] = None,
) -> dict:
    """
    Retrieve the details of a completed guest purchase order.
    Use this to check payment status (purchaseOrderPaymentStatus=PAID)
    and fulfillment status of the order.

    Args:
        purchase_order_id: The unique purchase order ID returned in the
            callback URL from the eBay pay widget after checkout completes.
        marketplace_id: eBay marketplace ID (optional, must match the one
            used when the checkout session was created).

    Returns:
        Dict with lineItems, pricingSummary, purchaseOrderPaymentStatus,
        purchaseOrderStatus, and creation date.
    """
    import requests
    url = f"{get_order_base_url()}/buy/order/v2/guest_purchase_order/{purchase_order_id}"
    headers = get_auth_header()
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    try:
        resp = requests.get(url, headers=headers, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
