from typing import Any, Dict, Optional

from shopify_api import shopify_request


def create_fulfillment(fulfillment: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/fulfillments.json", json_body={"fulfillment": fulfillment})


def cancel_fulfillment(fulfillment_id: int) -> Any:
    return shopify_request("POST", f"/fulfillments/{fulfillment_id}/cancel.json")


def update_fulfillment_tracking(fulfillment_id: int, fulfillment: Dict[str, Any], notify_customer: Optional[bool] = None) -> Any:
    body = {"fulfillment": fulfillment}
    if notify_customer is not None:
        body["notify_customer"] = notify_customer
    return shopify_request("POST", f"/fulfillments/{fulfillment_id}/update_tracking.json", json_body=body)


def list_fulfillments_for_order(order_id: int) -> Any:
    return shopify_request("GET", f"/orders/{order_id}/fulfillments.json")


def get_fulfillment(order_id: int, fulfillment_id: int) -> Any:
    return shopify_request("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")


def count_fulfillments_for_order(order_id: int) -> Any:
    return shopify_request("GET", f"/orders/{order_id}/fulfillments/count.json")


def list_fulfillments_for_fulfillment_order(fulfillment_order_id: int) -> Any:
    return shopify_request("GET", f"/fulfillment_orders/{fulfillment_order_id}/fulfillments.json")


def get_fulfillment_order(fulfillment_order_id: int) -> Any:
    return shopify_request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


def list_fulfillment_orders_for_order(order_id: int) -> Any:
    return shopify_request("GET", f"/orders/{order_id}/fulfillment_orders.json")


def cancel_fulfillment_order(fulfillment_order_id: int) -> Any:
    return shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json")


def close_fulfillment_order(fulfillment_order_id: int, message: Optional[str] = None) -> Any:
    body = {"fulfillment_order": {"message": message}} if message is not None else None
    return shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/close.json", json_body=body)


def hold_fulfillment_order(fulfillment_order_id: int, fulfillment_hold: Optional[Dict[str, Any]] = None) -> Any:
    body = {"fulfillment_hold": fulfillment_hold} if fulfillment_hold else None
    return shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/hold.json", json_body=body)


def move_fulfillment_order(fulfillment_order_id: int, new_location_id: int, fulfillment_order_line_items: Optional[list[Dict[str, Any]]] = None) -> Any:
    body: Dict[str, Any] = {"fulfillment_order": {"new_location_id": new_location_id}}
    if fulfillment_order_line_items is not None:
        body["fulfillment_order"]["fulfillment_order_line_items"] = fulfillment_order_line_items
    return shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/move.json", json_body=body)


def open_fulfillment_order(fulfillment_order_id: int) -> Any:
    return shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/open.json")


def release_fulfillment_order_hold(fulfillment_order_id: int) -> Any:
    return shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/release_hold.json")


def reschedule_fulfillment_order(fulfillment_order_id: int, fulfill_at: str) -> Any:
    return shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/reschedule.json", json_body={"fulfillment_order": {"fulfill_at": fulfill_at}})


def set_fulfillment_orders_deadline(fulfillment_order_ids: list[int], fulfillment_deadline: str) -> Any:
    return shopify_request("POST", "/fulfillment_orders/set_fulfillment_orders_deadline.json", json_body={"fulfillment_order_ids": fulfillment_order_ids, "fulfillment_deadline": fulfillment_deadline})
