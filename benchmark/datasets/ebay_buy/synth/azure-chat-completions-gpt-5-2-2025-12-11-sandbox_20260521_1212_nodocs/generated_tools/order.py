from typing import Any, Dict, Optional

from .ebay_client import EbayClient


ORDER_SCOPE = "https://api.ebay.com/oauth/api_scope/buy.order"


def initiate_checkout_session(
    client: EbayClient,
    *,
    body: Dict[str, Any],
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request(
        "POST",
        "/buy/order/v1/guest_checkout_session/initiate",
        json=body,
        headers=headers,
        scope=ORDER_SCOPE,
    )


def get_checkout_session(
    client: EbayClient,
    checkout_session_id: str,
    *,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request(
        "GET",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}",
        headers=headers,
        scope=ORDER_SCOPE,
    )


def update_shipping_address(
    client: EbayClient,
    checkout_session_id: str,
    *,
    body: Dict[str, Any],
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request(
        "POST",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_shipping_address",
        json=body,
        headers=headers,
        scope=ORDER_SCOPE,
    )


def update_quantity(
    client: EbayClient,
    checkout_session_id: str,
    line_item_id: str,
    *,
    body: Dict[str, Any],
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request(
        "POST",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_quantity",
        json={**body, "lineItemId": line_item_id},
        headers=headers,
        scope=ORDER_SCOPE,
    )


def apply_coupon(
    client: EbayClient,
    checkout_session_id: str,
    *,
    body: Dict[str, Any],
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request(
        "POST",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/apply_coupon",
        json=body,
        headers=headers,
        scope=ORDER_SCOPE,
    )


def remove_coupon(
    client: EbayClient,
    checkout_session_id: str,
    *,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request(
        "POST",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/remove_coupon",
        headers=headers,
        scope=ORDER_SCOPE,
    )


def place_order(
    client: EbayClient,
    checkout_session_id: str,
    *,
    body: Dict[str, Any],
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request(
        "POST",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/place_order",
        json=body,
        headers=headers,
        scope=ORDER_SCOPE,
    )
