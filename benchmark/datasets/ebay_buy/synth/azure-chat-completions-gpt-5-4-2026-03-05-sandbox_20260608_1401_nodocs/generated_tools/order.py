from typing import Any, Dict, List, Optional

from generated_tools.auth import client

ORDER_SCOPE = "https://api.ebay.com/oauth/api_scope/buy.guest.order"


def initiate_guest_checkout(
    contact_email: str,
    line_item_id: str,
    quantity: int = 1,
) -> Dict[str, Any]:
    body = {
        "contactEmail": contact_email,
        "lineItemInputs": [
            {
                "lineItemId": line_item_id,
                "quantity": quantity,
            }
        ],
    }
    return client.request("POST", "/buy/order/v1/guest_checkout_session/initiate", json_body=body, scope=ORDER_SCOPE)


def get_guest_checkout_session(checkout_session_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/order/v1/guest_checkout_session/{checkout_session_id}", scope=ORDER_SCOPE)


def update_guest_shipping_address(checkout_session_id: str, address: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_shipping_address",
        json_body=address,
        scope=ORDER_SCOPE,
    )


def update_guest_quantity(checkout_session_id: str, line_item_id: str, quantity: int) -> Dict[str, Any]:
    body = {"lineItemId": line_item_id, "quantity": quantity}
    return client.request(
        "POST",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_quantity",
        json_body=body,
        scope=ORDER_SCOPE,
    )


def update_guest_payment_info(checkout_session_id: str, payment_info: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_payment_info",
        json_body=payment_info,
        scope=ORDER_SCOPE,
    )


def place_guest_order(checkout_session_id: str) -> Dict[str, Any]:
    return client.request("POST", f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/place_order", scope=ORDER_SCOPE)


def get_guest_purchase_order(purchase_order_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/order/v1/guest_purchase_order/{purchase_order_id}", scope=ORDER_SCOPE)
