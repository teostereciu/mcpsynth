from typing import Any, Dict

from .browse import _get, _post


def initiate_guest_checkout_session(payload: Dict[str, Any]):
    return _post("/buy/order/v1/guest_checkout_session/initiate", payload)


def get_guest_checkout_session(session_id: str):
    return _get(f"/buy/order/v1/guest_checkout_session/{session_id}")


def apply_guest_coupon(session_id: str, payload: Dict[str, Any]):
    return _post(f"/buy/order/v1/guest_checkout_session/{session_id}/apply_coupon", payload)


def remove_guest_coupon(session_id: str, payload: Dict[str, Any]):
    return _post(f"/buy/order/v1/guest_checkout_session/{session_id}/remove_coupon", payload)


def update_guest_quantity(session_id: str, payload: Dict[str, Any]):
    return _post(f"/buy/order/v1/guest_checkout_session/{session_id}/update_quantity", payload)


def update_guest_shipping_address(session_id: str, payload: Dict[str, Any]):
    return _post(f"/buy/order/v1/guest_checkout_session/{session_id}/update_shipping_address", payload)


def update_guest_shipping_option(session_id: str, payload: Dict[str, Any]):
    return _post(f"/buy/order/v1/guest_checkout_session/{session_id}/update_shipping_option", payload)


def get_guest_purchase_order(order_id: str):
    return _get(f"/buy/order/v1/guest_purchase_order/{order_id}")
