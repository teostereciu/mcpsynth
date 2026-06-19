from typing import Any, Dict, List, Optional

from .client import EbayApiClient


def get_guest_checkout_session(
    checkout_session_id: str,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/order/v2/guest_checkout_session/{checkoutSessionId}"""
    client = EbayApiClient()
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request(
        "GET",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}",
        headers=headers,
    )


def apply_guest_coupon(
    checkout_session_id: str,
    marketplace_id: str,
    redemption_code: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /buy/order/v2/guest_checkout_session/{checkoutSessionId}/apply_coupon"""
    client = EbayApiClient()
    headers: Dict[str, str] = {"Content-Type": "application/json", "X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    body = {"redemptionCode": redemption_code}
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/apply_coupon",
        json=body,
        headers=headers,
    )


def initiate_guest_checkout_session(
    contact_email: str,
    line_item_inputs: List[Dict[str, Any]],
    shipping_address: Dict[str, Any],
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /buy/order/v2/guest_checkout_session/initiate"""
    client = EbayApiClient()
    headers: Dict[str, str] = {
        "Content-Type": "application/json",
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
    }
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    body = {
        "contactEmail": contact_email,
        "lineItemInputs": line_item_inputs,
        "shippingAddress": shipping_address,
    }
    return client.request("POST", "/buy/order/v2/guest_checkout_session/initiate", json=body, headers=headers)
