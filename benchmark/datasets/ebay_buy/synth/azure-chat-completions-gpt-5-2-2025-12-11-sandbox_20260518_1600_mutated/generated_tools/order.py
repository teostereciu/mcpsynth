from typing import Any, Dict, List, Optional

from .client import EbayClient


# NOTE: Order API v2 uses apix.ebay.com host per docs. We'll call via standard base_url
# host; if your environment requires apix, set EBAY_ENVIRONMENT and adjust client.


def initiate_guest_checkout_session(
    client: EbayClient,
    *,
    marketplace_id: str,
    contact_email: str,
    line_items: List[Dict[str, Any]],
    shipping_address: Dict[str, Any],
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"Content-Type": "application/json", "X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    payload = {
        "contactEmail": contact_email,
        "lineItemInputs": line_items,
        "shippingAddress": shipping_address,
    }
    return client.request("POST", "/buy/order/v2/guest_checkout_session/initiate", json=payload, headers=headers)


def get_guest_checkout_session(
    client: EbayClient,
    *,
    checkout_session_id: str,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}", headers=headers)


def update_guest_shipping_address(
    client: EbayClient,
    *,
    checkout_session_id: str,
    marketplace_id: str,
    shipping_address: Dict[str, Any],
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"Content-Type": "application/json", "X-EBAY-C-MARKETPLACE-ID": marketplace_id}
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
    checkout_session_id: str,
    marketplace_id: str,
    line_item_id: str,
    shipping_option_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"Content-Type": "application/json", "X-EBAY-C-MARKETPLACE-ID": marketplace_id}
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
    checkout_session_id: str,
    marketplace_id: str,
    line_item_id: str,
    quantity: int,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"Content-Type": "application/json", "X-EBAY-C-MARKETPLACE-ID": marketplace_id}
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
    checkout_session_id: str,
    marketplace_id: str,
    redemption_code: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"Content-Type": "application/json", "X-EBAY-C-MARKETPLACE-ID": marketplace_id}
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
    checkout_session_id: str,
    marketplace_id: str,
    redemption_code: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"Content-Type": "application/json", "X-EBAY-C-MARKETPLACE-ID": marketplace_id}
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
    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", f"/buy/order/v2/guest_purchase_order/{purchase_order_id}", headers=headers)
