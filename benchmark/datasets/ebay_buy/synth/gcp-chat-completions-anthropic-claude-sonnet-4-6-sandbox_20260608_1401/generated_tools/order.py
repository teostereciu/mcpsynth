"""
eBay Buy Order API tools (v2).
Covers: guest checkout session (initiate, get, update, coupon management)
        and guest purchase order retrieval.

Note: The Order API v2 only supports guest payment/checkout flow.
      Base URL uses apix.ebay.com (not api.ebay.com) for checkout session endpoints.
      This is a Limited Release API available only to select developers.
"""
from typing import Optional, List
from . import _client as client


def initiate_guest_checkout_session(
    contact_email: str,
    line_items: List[dict],
    shipping_address: dict,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """Create a new eBay guest checkout session (first step in guest checkout flow).

    Returns a checkoutSessionId needed for all subsequent checkout operations.

    Args:
        contact_email: The buyer's email address.
        line_items: List of dicts with 'itemId' (RESTful item ID) and 'quantity' (int).
            Example: [{'itemId': 'v1|123|0', 'quantity': 1}]
            Maximum 10 line items per session.
        shipping_address: Dict with shipping address fields:
            - addressLine1 (required): First line of street address.
            - addressLine2 (optional): Second line (apt, suite, etc.).
            - city (required): City name.
            - country (required): 2-letter ISO country code (e.g. 'US').
            - county (optional): County name.
            - phoneNumber (required): Phone number with country code (e.g. '+14155551234').
            - postalCode (conditional): Postal/zip code.
            - recipient (required): Dict with 'firstName' and 'lastName'.
            - stateOrProvince (conditional): State/province code (e.g. 'CA').
        marketplace_id: eBay marketplace ID (e.g. 'EBAY_US').
    """
    headers = {
        "Content-Type": "application/json",
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
    }

    body = {
        "contactEmail": contact_email,
        "lineItemInputs": line_items,
        "shippingAddress": shipping_address,
    }

    return client.post(
        "/buy/order/v2/guest_checkout_session/initiate",
        json=body,
        extra_headers=headers,
        use_order_host=True,
    )


def get_guest_checkout_session(
    checkout_session_id: str,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """Retrieve the details of an existing guest checkout session.

    Args:
        checkout_session_id: The eBay-assigned checkout session ID returned by
            initiate_guest_checkout_session.
        marketplace_id: eBay marketplace ID (must match the one used when the
            session was created).
    """
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.get(
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}",
        extra_headers=headers,
        use_order_host=True,
    )


def apply_guest_coupon(
    checkout_session_id: str,
    redemption_code: str,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """Apply a coupon to a guest checkout session.

    Applies the coupon to all eligible items in the order.

    Args:
        checkout_session_id: The eBay-assigned checkout session ID.
        redemption_code: The coupon redemption code to apply.
            Maximum one redemption code per order.
        marketplace_id: eBay marketplace ID (must match session's marketplace).
    """
    headers = {
        "Content-Type": "application/json",
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
    }
    body = {"redemptionCode": redemption_code}

    return client.post(
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/apply_coupon",
        json=body,
        extra_headers=headers,
        use_order_host=True,
    )


def remove_guest_coupon(
    checkout_session_id: str,
    redemption_code: str,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """Remove a coupon from a guest checkout session.

    Args:
        checkout_session_id: The eBay-assigned checkout session ID.
        redemption_code: The coupon redemption code to remove.
        marketplace_id: eBay marketplace ID (must match session's marketplace).
    """
    headers = {
        "Content-Type": "application/json",
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
    }
    body = {"redemptionCode": redemption_code}

    return client.post(
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/remove_coupon",
        json=body,
        extra_headers=headers,
        use_order_host=True,
    )


def update_guest_quantity(
    checkout_session_id: str,
    line_item_id: str,
    quantity: int,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """Update the quantity of a line item in a guest checkout session.

    Args:
        checkout_session_id: The eBay-assigned checkout session ID.
        line_item_id: The eBay-assigned line item ID within the checkout session.
        quantity: The new quantity for the line item.
        marketplace_id: eBay marketplace ID (must match session's marketplace).
    """
    headers = {
        "Content-Type": "application/json",
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
    }
    body = {
        "lineItemId": line_item_id,
        "quantity": quantity,
    }

    return client.post(
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_quantity",
        json=body,
        extra_headers=headers,
        use_order_host=True,
    )


def update_guest_shipping_address(
    checkout_session_id: str,
    address_line1: str,
    city: str,
    country: str,
    phone_number: str,
    recipient_first_name: str,
    recipient_last_name: str,
    address_line2: Optional[str] = None,
    county: Optional[str] = None,
    postal_code: Optional[str] = None,
    state_or_province: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """Update the shipping address for a guest checkout session.

    All line items in the order are shipped to the same address.

    Args:
        checkout_session_id: The eBay-assigned checkout session ID.
        address_line1: First line of the street address.
        city: City name.
        country: 2-letter ISO country code (e.g. 'US').
        phone_number: Phone number with country code (e.g. '+14155551234').
        recipient_first_name: First name of the recipient.
        recipient_last_name: Last name of the recipient.
        address_line2: Second line of address (apt, suite, etc.).
        county: County name.
        postal_code: Postal/zip code.
        state_or_province: State or province code (e.g. 'CA' for US).
        marketplace_id: eBay marketplace ID (must match session's marketplace).
    """
    headers = {
        "Content-Type": "application/json",
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
    }

    body = {
        "addressLine1": address_line1,
        "city": city,
        "country": country,
        "phoneNumber": phone_number,
        "recipient": {
            "firstName": recipient_first_name,
            "lastName": recipient_last_name,
        },
    }
    if address_line2 is not None:
        body["addressLine2"] = address_line2
    if county is not None:
        body["county"] = county
    if postal_code is not None:
        body["postalCode"] = postal_code
    if state_or_province is not None:
        body["stateOrProvince"] = state_or_province

    return client.post(
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_address",
        json=body,
        extra_headers=headers,
        use_order_host=True,
    )


def update_guest_shipping_option(
    checkout_session_id: str,
    line_item_id: str,
    shipping_option_id: str,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """Update the shipping method/option for a specific line item in a guest checkout session.

    Each line item can have its own shipping option.

    Args:
        checkout_session_id: The eBay-assigned checkout session ID.
        line_item_id: The eBay-assigned line item ID within the checkout session.
        shipping_option_id: The unique ID of the shipping option to select.
            Available shipping option IDs are returned in the lineItems.shippingOptions
            array from get_guest_checkout_session or initiate_guest_checkout_session.
        marketplace_id: eBay marketplace ID (must match session's marketplace).
    """
    headers = {
        "Content-Type": "application/json",
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
    }
    body = {
        "lineItemId": line_item_id,
        "shippingOptionId": shipping_option_id,
    }

    return client.post(
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_option",
        json=body,
        extra_headers=headers,
        use_order_host=True,
    )


def get_guest_purchase_order(
    purchase_order_id: str,
    marketplace_id: Optional[str] = None,
) -> dict:
    """Retrieve the details of a completed guest purchase order.

    Returns line items, payment status, fulfillment status, shipping info,
    and pricing summary. Check purchaseOrderPaymentStatus for 'PAID' status.

    Args:
        purchase_order_id: The unique purchase order ID returned in the eBay
            pay widget callback URL after checkout completion.
        marketplace_id: eBay marketplace ID (optional, should match the session's).
    """
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    return client.get(
        f"/buy/order/v2/guest_purchase_order/{purchase_order_id}",
        extra_headers=headers,
    )
