from __future__ import annotations

from typing import Any, Dict, Optional

from .ebay_client import EbayClient

ORDER_SCOPE = "https://api.ebay.com/oauth/api_scope/buy.guest.order"


def initiate_checkout_session(
    payload: Dict[str, Any],
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """POST /buy/order/v1/guest_checkout_session/initiate"""
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return EbayClient().request(
        "POST",
        "/buy/order/v1/guest_checkout_session/initiate",
        scope=ORDER_SCOPE,
        json=payload,
        headers=headers,
    )


def get_checkout_session(
    checkout_session_id: str,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """GET /buy/order/v1/guest_checkout_session/{checkoutSessionId}"""
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return EbayClient().request(
        "GET",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}",
        scope=ORDER_SCOPE,
        headers=headers,
    )


def update_shipping_address(
    checkout_session_id: str,
    payload: Dict[str, Any],
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """POST /buy/order/v1/guest_checkout_session/{checkoutSessionId}/update_shipping_address"""
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return EbayClient().request(
        "POST",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_shipping_address",
        scope=ORDER_SCOPE,
        json=payload,
        headers=headers,
    )


def update_quantity(
    checkout_session_id: str,
    payload: Dict[str, Any],
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """POST /buy/order/v1/guest_checkout_session/{checkoutSessionId}/update_quantity"""
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return EbayClient().request(
        "POST",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_quantity",
        scope=ORDER_SCOPE,
        json=payload,
        headers=headers,
    )


def apply_coupon(
    checkout_session_id: str,
    payload: Dict[str, Any],
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """POST /buy/order/v1/guest_checkout_session/{checkoutSessionId}/apply_coupon"""
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return EbayClient().request(
        "POST",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/apply_coupon",
        scope=ORDER_SCOPE,
        json=payload,
        headers=headers,
    )


def remove_coupon(
    checkout_session_id: str,
    payload: Dict[str, Any],
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """POST /buy/order/v1/guest_checkout_session/{checkoutSessionId}/remove_coupon"""
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return EbayClient().request(
        "POST",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/remove_coupon",
        scope=ORDER_SCOPE,
        json=payload,
        headers=headers,
    )


def place_order(
    checkout_session_id: str,
    payload: Dict[str, Any],
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """POST /buy/order/v1/guest_checkout_session/{checkoutSessionId}/place_order"""
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return EbayClient().request(
        "POST",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/place_order",
        scope=ORDER_SCOPE,
        json=payload,
        headers=headers,
    )
