from typing import Any, Dict, Optional

from .ebay_client import EbayClient


class OrderTools:
    def __init__(self, client: Optional[EbayClient] = None):
        self.client = client or EbayClient()

    def initiate_guest_checkout_session(
        self,
        *,
        payload: Dict[str, Any],
        marketplace_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        headers: Dict[str, str] = {"Content-Type": "application/json"}
        if marketplace_id:
            headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
        return self.client.request(
            "POST",
            "/buy/order/v1/guest_checkout_session/initiate",
            json=payload,
            headers=headers,
            scope="https://api.ebay.com/oauth/api_scope/buy.guest.order",
        )

    def get_guest_checkout_session(
        self,
        checkout_session_id: str,
        *,
        marketplace_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        headers: Dict[str, str] = {}
        if marketplace_id:
            headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
        return self.client.request(
            "GET",
            f"/buy/order/v1/guest_checkout_session/{checkout_session_id}",
            headers=headers,
            scope="https://api.ebay.com/oauth/api_scope/buy.guest.order",
        )

    def update_guest_quantity(
        self,
        checkout_session_id: str,
        line_item_id: str,
        quantity: int,
        *,
        marketplace_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        headers: Dict[str, str] = {"Content-Type": "application/json"}
        if marketplace_id:
            headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
        payload = {"lineItemId": line_item_id, "quantity": int(quantity)}
        return self.client.request(
            "POST",
            f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_quantity",
            json=payload,
            headers=headers,
            scope="https://api.ebay.com/oauth/api_scope/buy.guest.order",
        )

    def update_guest_shipping_address(
        self,
        checkout_session_id: str,
        shipping_address: Dict[str, Any],
        *,
        marketplace_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        headers: Dict[str, str] = {"Content-Type": "application/json"}
        if marketplace_id:
            headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
        payload = {"shippingAddress": shipping_address}
        return self.client.request(
            "POST",
            f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_shipping_address",
            json=payload,
            headers=headers,
            scope="https://api.ebay.com/oauth/api_scope/buy.guest.order",
        )

    def update_guest_shipping_option(
        self,
        checkout_session_id: str,
        shipping_option_id: str,
        *,
        marketplace_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        headers: Dict[str, str] = {"Content-Type": "application/json"}
        if marketplace_id:
            headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
        payload = {"shippingOptionId": shipping_option_id}
        return self.client.request(
            "POST",
            f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_shipping_option",
            json=payload,
            headers=headers,
            scope="https://api.ebay.com/oauth/api_scope/buy.guest.order",
        )

    def apply_guest_coupon(
        self,
        checkout_session_id: str,
        coupon_code: str,
        *,
        marketplace_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        headers: Dict[str, str] = {"Content-Type": "application/json"}
        if marketplace_id:
            headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
        payload = {"couponCode": coupon_code}
        return self.client.request(
            "POST",
            f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/apply_coupon",
            json=payload,
            headers=headers,
            scope="https://api.ebay.com/oauth/api_scope/buy.guest.order",
        )

    def remove_guest_coupon(
        self,
        checkout_session_id: str,
        coupon_code: str,
        *,
        marketplace_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        headers: Dict[str, str] = {"Content-Type": "application/json"}
        if marketplace_id:
            headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
        payload = {"couponCode": coupon_code}
        return self.client.request(
            "POST",
            f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/remove_coupon",
            json=payload,
            headers=headers,
            scope="https://api.ebay.com/oauth/api_scope/buy.guest.order",
        )

    def get_guest_purchase_order(
        self,
        purchase_order_id: str,
        *,
        marketplace_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        headers: Dict[str, str] = {}
        if marketplace_id:
            headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
        return self.client.request(
            "GET",
            f"/buy/order/v1/guest_purchase_order/{purchase_order_id}",
            headers=headers,
            scope="https://api.ebay.com/oauth/api_scope/buy.guest.order",
        )
