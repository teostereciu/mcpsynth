from typing import Any, Dict, Optional

from .client import EbayClient


def initiate_guest_checkout_session(
    client: EbayClient,
    *,
    marketplace_id: str,
    contact_email: str,
    line_item_inputs: list[dict[str, Any]],
    shipping_address: dict[str, Any],
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /buy/order/v2/guest_checkout_session/initiate"""
    headers: Dict[str, str] = {
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

    return client.request("POST", "/buy/order/v2/guest_checkout_session/initiate", json=payload, headers=headers)


def get_guest_checkout_session(
    client: EbayClient,
    *,
    marketplace_id: str,
    checkout_session_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/order/v2/guest_checkout_session/{checkoutSessionId}"""
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request(
        "GET",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}",
        headers=headers,
    )


def update_guest_shipping_address(
    client: EbayClient,
    *,
    marketplace_id: str,
    checkout_session_id: str,
    shipping_address: dict[str, Any],
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /buy/order/v2/guest_checkout_session/{checkoutSessionId}/update_shipping_address"""
    headers: Dict[str, str] = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_address",
        json=shipping_address,
        headers=headers,
    )


def update_guest_shipping_option(
    client: EbayClient,
    *,
    marketplace_id: str,
    checkout_session_id: str,
    line_item_id: str,
    shipping_option_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /buy/order/v2/guest_checkout_session/{checkoutSessionId}/update_shipping_option"""
    headers: Dict[str, str] = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    payload = {"lineItemId": line_item_id, "shippingOptionId": shipping_option_id}

    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_option",
        json=payload,
        headers=headers,
    )


def update_guest_quantity(
    client: EbayClient,
    *,
    marketplace_id: str,
    checkout_session_id: str,
    line_item_id: str,
    quantity: int,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /buy/order/v2/guest_checkout_session/{checkoutSessionId}/update_quantity"""
    headers: Dict[str, str] = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    payload = {"lineItemId": line_item_id, "quantity": quantity}

    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_quantity",
        json=payload,
        headers=headers,
    )


def apply_guest_coupon(
    client: EbayClient,
    *,
    marketplace_id: str,
    checkout_session_id: str,
    redemption_code: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /buy/order/v2/guest_checkout_session/{checkoutSessionId}/apply_coupon"""
    headers: Dict[str, str] = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    payload = {"redemptionCode": redemption_code}

    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/apply_coupon",
        json=payload,
        headers=headers,
    )


def remove_guest_coupon(
    client: EbayClient,
    *,
    marketplace_id: str,
    checkout_session_id: str,
    redemption_code: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /buy/order/v2/guest_checkout_session/{checkoutSessionId}/remove_coupon"""
    headers: Dict[str, str] = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    payload = {"redemptionCode": redemption_code}

    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/remove_coupon",
        json=payload,
        headers=headers,
    )


def get_guest_purchase_order(
    client: EbayClient,
    *,
    purchase_order_id: str,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/order/v2/guest_purchase_order/{purchaseOrderId}"""
    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request(
        "GET",
        f"/buy/order/v2/guest_purchase_order/{purchase_order_id}",
        headers=headers,
    )
