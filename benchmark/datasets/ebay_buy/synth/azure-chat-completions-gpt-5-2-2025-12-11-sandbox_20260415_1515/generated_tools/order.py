from typing import Any, Dict, List, Optional

from .http_client import EbayClient


client = EbayClient()


def order_initiate_guest_checkout_session(
    *,
    marketplace_id: str,
    contact_email: str,
    line_items: List[Dict[str, Any]],
    shipping_address: Dict[str, Any],
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a guest checkout session.

    line_items: list of {"itemId": str, "quantity": int}
    shipping_address: dict per API (shippingAddress)
    """
    headers: Dict[str, str] = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    payload = {
        "contactEmail": contact_email,
        "lineItemInputs": line_items,
        "shippingAddress": shipping_address,
    }
    return client.request("POST", "/buy/order/v2/guest_checkout_session/initiate", json=payload, headers=headers)


def order_get_guest_checkout_session(
    checkout_session_id: str,
    *,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request("GET", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}", headers=headers)


def order_apply_guest_coupon(
    checkout_session_id: str,
    *,
    marketplace_id: str,
    coupon_code: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Content-Type": "application/json"}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    payload = {"couponCode": coupon_code}
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/apply_coupon",
        json=payload,
        headers=headers,
    )


def order_remove_guest_coupon(
    checkout_session_id: str,
    *,
    marketplace_id: str,
    coupon_code: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Content-Type": "application/json"}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    payload = {"couponCode": coupon_code}
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/remove_coupon",
        json=payload,
        headers=headers,
    )


def order_update_guest_quantity(
    checkout_session_id: str,
    *,
    marketplace_id: str,
    line_item_id: str,
    quantity: int,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Content-Type": "application/json"}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    payload = {"lineItemId": line_item_id, "quantity": int(quantity)}
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_quantity",
        json=payload,
        headers=headers,
    )


def order_update_guest_shipping_address(
    checkout_session_id: str,
    *,
    marketplace_id: str,
    shipping_address: Dict[str, Any],
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Content-Type": "application/json"}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    payload = {"shippingAddress": shipping_address}
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_address",
        json=payload,
        headers=headers,
    )


def order_update_guest_shipping_option(
    checkout_session_id: str,
    *,
    marketplace_id: str,
    line_item_id: str,
    shipping_option_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Content-Type": "application/json"}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    payload = {"lineItemId": line_item_id, "shippingOptionId": shipping_option_id}
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_option",
        json=payload,
        headers=headers,
    )


def order_get_guest_purchase_order(
    purchase_order_id: str,
    *,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request("GET", f"/buy/order/v2/guest_purchase_order/{purchase_order_id}", headers=headers)
