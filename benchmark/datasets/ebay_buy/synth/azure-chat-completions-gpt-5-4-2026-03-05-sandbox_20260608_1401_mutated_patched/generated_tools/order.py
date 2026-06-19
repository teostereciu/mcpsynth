from typing import Any, Dict, List, Optional

from .common import client


def initiate_guest_checkout_session(
    contact_email: str,
    line_item_inputs: List[Dict[str, Any]],
    shipping_address: Dict[str, Any],
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {
        "Content-Type": "application/json",
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "X-EBAY-C-ENDUSERCTX": enduserctx,
    }
    return client.request(
        "POST",
        "/buy/order/v2/guest_checkout_session/initiate",
        json_body={
            "contactEmail": contact_email,
            "lineItemInputs": line_item_inputs,
            "shippingAddress": shipping_address,
        },
        headers=headers,
    )


def get_guest_checkout_session(
    checkout_session_id: str,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}",
        headers={
            "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
            "X-EBAY-C-ENDUSERCTX": enduserctx,
        },
    )


def apply_guest_coupon(
    checkout_session_id: str,
    redemption_code: str,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/apply_coupon",
        json_body={"redemptionCode": redemption_code},
        headers={
            "Content-Type": "application/json",
            "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
            "X-EBAY-C-ENDUSERCTX": enduserctx,
        },
    )


def update_guest_shipping_option(
    checkout_session_id: str,
    line_item_id: str,
    shipping_option_id: str,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_option",
        json_body={"lineItemId": line_item_id, "shippingOptionId": shipping_option_id},
        headers={
            "Content-Type": "application/json",
            "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
            "X-EBAY-C-ENDUSERCTX": enduserctx,
        },
    )


def update_guest_shipping_address(
    checkout_session_id: str,
    shipping_address: Dict[str, Any],
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_address",
        json_body=shipping_address,
        headers={
            "Content-Type": "application/json",
            "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
            "X-EBAY-C-ENDUSERCTX": enduserctx,
        },
    )


def remove_guest_coupon(
    checkout_session_id: str,
    redemption_code: str,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/remove_coupon",
        json_body={"redemptionCode": redemption_code},
        headers={
            "Content-Type": "application/json",
            "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
            "X-EBAY-C-ENDUSERCTX": enduserctx,
        },
    )


def update_guest_quantity(
    checkout_session_id: str,
    line_item_id: str,
    quantity: int,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_quantity",
        json_body={"lineItemId": line_item_id, "quantity": quantity},
        headers={
            "Content-Type": "application/json",
            "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
            "X-EBAY-C-ENDUSERCTX": enduserctx,
        },
    )
