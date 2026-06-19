from __future__ import annotations

from typing import Any, Dict, Optional

from .client import EbayClient


_GUEST_ORDER_SCOPE = "https://api.ebay.com/oauth/api_scope/buy.guest.order"


def initiate_guest_checkout_session(
    client: EbayClient,
    *,
    contact_email: str,
    line_item_inputs: list[dict[str, Any]],
    shipping_address: dict[str, Any],
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    payload = {
        "contactEmail": contact_email,
        "lineItemInputs": line_item_inputs,
        "shippingAddress": shipping_address,
    }

    return client.request(
        "POST",
        "/buy/order/v2/guest_checkout_session/initiate",
        headers=headers,
        json=payload,
        scope=_GUEST_ORDER_SCOPE,
    )


def get_guest_checkout_session(
    client: EbayClient,
    *,
    checkout_session_id: str,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request(
        "GET",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}",
        headers=headers,
        scope=_GUEST_ORDER_SCOPE,
    )


def update_guest_quantity(
    client: EbayClient,
    *,
    checkout_session_id: str,
    line_item_id: str,
    quantity: int,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    payload = {"lineItemId": line_item_id, "quantity": quantity}

    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_quantity",
        headers=headers,
        json=payload,
        scope=_GUEST_ORDER_SCOPE,
    )


def update_guest_shipping_address(
    client: EbayClient,
    *,
    checkout_session_id: str,
    shipping_address: dict[str, Any],
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_address",
        headers=headers,
        json=shipping_address,
        scope=_GUEST_ORDER_SCOPE,
    )


def update_guest_shipping_option(
    client: EbayClient,
    *,
    checkout_session_id: str,
    line_item_id: str,
    shipping_option_id: str,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    payload = {"lineItemId": line_item_id, "shippingOptionId": shipping_option_id}

    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_option",
        headers=headers,
        json=payload,
        scope=_GUEST_ORDER_SCOPE,
    )


def apply_guest_coupon(
    client: EbayClient,
    *,
    checkout_session_id: str,
    redemption_code: str,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    payload = {"redemptionCode": redemption_code}

    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/apply_coupon",
        headers=headers,
        json=payload,
        scope=_GUEST_ORDER_SCOPE,
    )


def remove_guest_coupon(
    client: EbayClient,
    *,
    checkout_session_id: str,
    redemption_code: str,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    payload = {"redemptionCode": redemption_code}

    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/remove_coupon",
        headers=headers,
        json=payload,
        scope=_GUEST_ORDER_SCOPE,
    )


def get_guest_purchase_order(
    client: EbayClient,
    *,
    purchase_order_id: str,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request(
        "GET",
        f"/buy/order/v2/guest_purchase_order/{purchase_order_id}",
        headers=headers,
        scope=_GUEST_ORDER_SCOPE,
    )
