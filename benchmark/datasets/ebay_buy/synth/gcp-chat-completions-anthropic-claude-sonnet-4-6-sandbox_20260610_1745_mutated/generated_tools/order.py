"""
eBay Buy Order API tools.
Covers: guest checkout session (initiate, get, update, coupon management)
and guest purchase order retrieval.

Note: The Order API uses apix.ebay.com (not api.ebay.com) for production
and apix.sandbox.ebay.com for sandbox.
"""

import os
from typing import Optional, List, Dict
from mcp.server.fastmcp import FastMCP
from .auth import get_auth_headers


def _get_order_base_url() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    if env == "PRODUCTION":
        return "https://apix.ebay.com"
    return "https://apix.sandbox.ebay.com"


def _order_headers(marketplace_id: str, device_id: Optional[str] = None) -> dict:
    headers = {
        **get_auth_headers(),
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }
    if device_id:
        headers["X-EBAY-C-ENDUSERCTX"] = device_id
    return headers


def register_order_tools(mcp: FastMCP) -> None:

    @mcp.tool()
    def initiate_guest_checkout_session(
        contact_email: str,
        line_items: List[Dict],
        shipping_address: Dict,
        marketplace_id: str = "EBAY_US",
        device_id: Optional[str] = None,
    ) -> dict:
        """Start a new eBay guest checkout session (first step in guest checkout flow).
        Returns a checkoutSessionId needed for all subsequent checkout operations.

        Args:
            contact_email: Buyer's email address.
            line_items: List of dicts with 'itemId' (RESTful item ID) and 'quantity'.
                        Example: [{'itemId': 'v1|123|0', 'quantity': 1}]. Max 10 items.
            shipping_address: Dict with shipping address fields:
                - addressLine1 (required): Street address line 1.
                - addressLine2 (optional): Street address line 2.
                - city (required): City name.
                - country (required): 2-letter ISO country code (e.g. 'US').
                - postalCode (conditional): Postal/zip code.
                - stateOrProvince (conditional): State/province (2-char for US).
                - phoneNumber (required): Recipient phone number.
                - recipient (required): Dict with 'firstName' and 'lastName'.
                - county (optional): County name.
            marketplace_id: eBay marketplace ID (default EBAY_US).
            device_id: Optional device ID for payment gateway tracking.
        """
        import requests
        url = f"{_get_order_base_url()}/buy/order/v2/guest_checkout_session/initiate"
        payload = {
            "contactEmail": contact_email,
            "lineItemInputs": line_items,
            "shippingAddress": shipping_address,
        }
        try:
            resp = requests.post(
                url,
                json=payload,
                headers=_order_headers(marketplace_id, device_id),
                timeout=30,
            )
            if resp.status_code in (200, 201):
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_guest_checkout_session(
        checkout_session_id: str,
        marketplace_id: str = "EBAY_US",
        device_id: Optional[str] = None,
    ) -> dict:
        """Retrieve the details of an existing eBay guest checkout session.
        Returns line items, shipping options, pricing summary, and applied coupons.

        Args:
            checkout_session_id: The checkout session ID from initiate_guest_checkout_session.
            marketplace_id: eBay marketplace ID (must match the one used at session creation).
            device_id: Optional device ID for payment gateway tracking.
        """
        import requests
        url = f"{_get_order_base_url()}/buy/order/v2/guest_checkout_session/{checkout_session_id}"
        try:
            resp = requests.get(
                url,
                headers=_order_headers(marketplace_id, device_id),
                timeout=30,
            )
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def apply_guest_coupon(
        checkout_session_id: str,
        redemption_code: str,
        marketplace_id: str = "EBAY_US",
        device_id: Optional[str] = None,
    ) -> dict:
        """Apply a coupon to an eBay guest checkout session.
        The coupon is applied to all eligible items in the order.

        Args:
            checkout_session_id: The checkout session ID.
            redemption_code: The coupon redemption code to apply.
            marketplace_id: eBay marketplace ID (must match session's marketplace).
            device_id: Optional device ID for payment gateway tracking.
        """
        import requests
        url = (
            f"{_get_order_base_url()}/buy/order/v2/guest_checkout_session"
            f"/{checkout_session_id}/apply_coupon"
        )
        payload = {"redemptionCode": redemption_code}
        try:
            resp = requests.post(
                url,
                json=payload,
                headers=_order_headers(marketplace_id, device_id),
                timeout=30,
            )
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def remove_guest_coupon(
        checkout_session_id: str,
        redemption_code: str,
        marketplace_id: str = "EBAY_US",
        device_id: Optional[str] = None,
    ) -> dict:
        """Remove a coupon from an eBay guest checkout session.

        Args:
            checkout_session_id: The checkout session ID.
            redemption_code: The coupon redemption code to remove.
            marketplace_id: eBay marketplace ID (must match session's marketplace).
            device_id: Optional device ID for payment gateway tracking.
        """
        import requests
        url = (
            f"{_get_order_base_url()}/buy/order/v2/guest_checkout_session"
            f"/{checkout_session_id}/remove_coupon"
        )
        payload = {"redemptionCode": redemption_code}
        try:
            resp = requests.post(
                url,
                json=payload,
                headers=_order_headers(marketplace_id, device_id),
                timeout=30,
            )
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_guest_quantity(
        checkout_session_id: str,
        line_item_id: str,
        quantity: int,
        marketplace_id: str = "EBAY_US",
        device_id: Optional[str] = None,
    ) -> dict:
        """Update the quantity of a line item in an eBay guest checkout session.

        Args:
            checkout_session_id: The checkout session ID.
            line_item_id: The eBay-assigned line item ID to update.
            quantity: The new quantity for the line item.
            marketplace_id: eBay marketplace ID (must match session's marketplace).
            device_id: Optional device ID for payment gateway tracking.
        """
        import requests
        url = (
            f"{_get_order_base_url()}/buy/order/v2/guest_checkout_session"
            f"/{checkout_session_id}/update_quantity"
        )
        payload = {"lineItemId": line_item_id, "quantity": quantity}
        try:
            resp = requests.post(
                url,
                json=payload,
                headers=_order_headers(marketplace_id, device_id),
                timeout=30,
            )
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_guest_shipping_address(
        checkout_session_id: str,
        address_line1: str,
        city: str,
        country: str,
        phone_number: str,
        recipient_first_name: str,
        recipient_last_name: str,
        address_line2: Optional[str] = None,
        postal_code: Optional[str] = None,
        state_or_province: Optional[str] = None,
        county: Optional[str] = None,
        marketplace_id: str = "EBAY_US",
        device_id: Optional[str] = None,
    ) -> dict:
        """Update the shipping address for an eBay guest checkout session.
        All line items in the order are shipped to the same address.

        Args:
            checkout_session_id: The checkout session ID.
            address_line1: First line of the street address.
            city: City name.
            country: 2-letter ISO country code (e.g. 'US', 'GB').
            phone_number: Recipient phone number (include country code, e.g. '+14155551234').
            recipient_first_name: First name of the recipient.
            recipient_last_name: Last name of the recipient.
            address_line2: Optional second line of the street address.
            postal_code: Postal/zip code.
            state_or_province: State or province (2-char for US).
            county: Optional county name.
            marketplace_id: eBay marketplace ID (must match session's marketplace).
            device_id: Optional device ID for payment gateway tracking.
        """
        import requests
        url = (
            f"{_get_order_base_url()}/buy/order/v2/guest_checkout_session"
            f"/{checkout_session_id}/update_shipping_address"
        )
        payload = {
            "addressLine1": address_line1,
            "city": city,
            "country": country,
            "phoneNumber": phone_number,
            "recipient": {
                "firstName": recipient_first_name,
                "lastName": recipient_last_name,
            },
        }
        if address_line2:
            payload["addressLine2"] = address_line2
        if postal_code:
            payload["postalCode"] = postal_code
        if state_or_province:
            payload["stateOrProvince"] = state_or_province
        if county:
            payload["county"] = county

        try:
            resp = requests.post(
                url,
                json=payload,
                headers=_order_headers(marketplace_id, device_id),
                timeout=30,
            )
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_guest_shipping_option(
        checkout_session_id: str,
        line_item_id: str,
        shipping_option_id: str,
        marketplace_id: str = "EBAY_US",
        device_id: Optional[str] = None,
    ) -> dict:
        """Update the shipping method/option for a specific line item in a guest checkout session.
        Each line item can have its own shipping option.

        Args:
            checkout_session_id: The checkout session ID.
            line_item_id: The eBay-assigned line item ID to update shipping for.
            shipping_option_id: The unique ID of the shipping option to select
                                (from the shippingOptions array in the session).
            marketplace_id: eBay marketplace ID (must match session's marketplace).
            device_id: Optional device ID for payment gateway tracking.
        """
        import requests
        url = (
            f"{_get_order_base_url()}/buy/order/v2/guest_checkout_session"
            f"/{checkout_session_id}/update_shipping_option"
        )
        payload = {
            "lineItemId": line_item_id,
            "shippingOptionId": shipping_option_id,
        }
        try:
            resp = requests.post(
                url,
                json=payload,
                headers=_order_headers(marketplace_id, device_id),
                timeout=30,
            )
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_guest_purchase_order(
        purchase_order_id: str,
        marketplace_id: str = "EBAY_US",
        device_id: Optional[str] = None,
    ) -> dict:
        """Retrieve details of a completed eBay guest purchase order.
        Returns line items, payment status, fulfillment status, shipping info,
        and pricing summary. Check purchaseOrderPaymentStatus for 'PAID' status.

        Args:
            purchase_order_id: The purchase order ID (returned in the eBay pay widget callback URL).
            marketplace_id: eBay marketplace ID.
            device_id: Optional device ID for payment gateway tracking.
        """
        import requests
        # getGuestPurchaseOrder uses api.ebay.com (not apix)
        env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
        if env == "PRODUCTION":
            base = "https://api.ebay.com"
        else:
            base = "https://api.sandbox.ebay.com"

        url = f"{base}/buy/order/v2/guest_purchase_order/{purchase_order_id}"
        headers = {**get_auth_headers()}
        if marketplace_id:
            headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
        if device_id:
            headers["X-EBAY-C-ENDUSERCTX"] = device_id

        try:
            resp = requests.get(url, headers=headers, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}
