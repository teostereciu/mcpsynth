from typing import Any, Dict, Optional

from .client import EbayBuyApiClient


ORDER_SCOPE = "https://api.ebay.com/oauth/api_scope/buy.order"


def initiate_checkout_session(
    client: EbayBuyApiClient,
    *,
    payload: Dict[str, Any],
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    return client.request(
        "POST",
        "/buy/order/v1/guest_checkout_session/initiate",
        scope=ORDER_SCOPE,
        json=payload,
        headers=headers,
    )


def get_checkout_session(client: EbayBuyApiClient, *, checkout_session_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/order/v1/guest_checkout_session/{checkout_session_id}", scope=ORDER_SCOPE)


def update_shipping_address(
    client: EbayBuyApiClient,
    *,
    checkout_session_id: str,
    payload: Dict[str, Any],
) -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_shipping_address",
        scope=ORDER_SCOPE,
        json=payload,
    )


def update_quantity(
    client: EbayBuyApiClient,
    *,
    checkout_session_id: str,
    line_item_id: str,
    quantity: int,
) -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_quantity",
        scope=ORDER_SCOPE,
        json={"lineItemId": line_item_id, "quantity": quantity},
    )


def apply_coupon(
    client: EbayBuyApiClient,
    *,
    checkout_session_id: str,
    coupon_code: str,
) -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/apply_coupon",
        scope=ORDER_SCOPE,
        json={"couponCode": coupon_code},
    )


def remove_coupon(client: EbayBuyApiClient, *, checkout_session_id: str) -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/remove_coupon",
        scope=ORDER_SCOPE,
    )


def place_order(
    client: EbayBuyApiClient,
    *,
    checkout_session_id: str,
    payload: Dict[str, Any],
) -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/place_order",
        scope=ORDER_SCOPE,
        json=payload,
    )
