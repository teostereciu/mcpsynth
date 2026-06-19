from typing import Any, Dict, Optional

from generated_tools.common import client


def initiate_guest_checkout_session(
    marketplace_id: str,
    contact_email: str,
    line_item_inputs: list[dict[str, Any]],
    shipping_address: dict[str, Any],
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Content-Type": "application/json"}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request(
        "POST",
        "/buy/order/v2/guest_checkout_session/initiate",
        headers=headers,
        json_body={
            "contactEmail": contact_email,
            "lineItemInputs": line_item_inputs,
            "shippingAddress": shipping_address,
        },
    )


def get_guest_checkout_session(checkout_session_id: str, marketplace_id: str, enduserctx: Optional[str] = None) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request("GET", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}", headers=headers)


def apply_guest_coupon(
    checkout_session_id: str,
    marketplace_id: str,
    redemption_code: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Content-Type": "application/json"}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/apply_coupon",
        headers=headers,
        json_body={"redemptionCode": redemption_code},
    )


def remove_guest_coupon(
    checkout_session_id: str,
    marketplace_id: str,
    redemption_code: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Content-Type": "application/json"}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/remove_coupon",
        headers=headers,
        json_body={"redemptionCode": redemption_code},
    )


def update_guest_quantity(
    checkout_session_id: str,
    marketplace_id: str,
    line_item_id: str,
    quantity: int,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Content-Type": "application/json"}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_quantity",
        headers=headers,
        json_body={"lineItemId": line_item_id, "quantity": quantity},
    )


def update_guest_shipping_address(
    checkout_session_id: str,
    marketplace_id: str,
    shipping_address: dict[str, Any],
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Content-Type": "application/json"}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_address",
        headers=headers,
        json_body=shipping_address,
    )


def update_guest_shipping_option(
    checkout_session_id: str,
    marketplace_id: str,
    line_item_id: str,
    shipping_option_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Content-Type": "application/json"}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_option",
        headers=headers,
        json_body={"lineItemId": line_item_id, "shippingOptionId": shipping_option_id},
    )
