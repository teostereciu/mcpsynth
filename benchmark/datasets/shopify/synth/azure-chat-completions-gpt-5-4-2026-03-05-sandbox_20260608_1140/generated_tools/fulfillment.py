from typing import Any, Dict, Optional

from generated_tools.common import shopify_request


def list_locations(limit: Optional[int] = None) -> Any:
    params = {"limit": limit} if limit is not None else None
    return shopify_request("GET", "/locations.json", params=params)


def get_location(location_id: int) -> Any:
    return shopify_request("GET", f"/locations/{location_id}.json")


def count_locations() -> Any:
    return shopify_request("GET", "/locations/count.json")


def get_location_inventory_levels(location_id: int) -> Any:
    return shopify_request("GET", f"/locations/{location_id}/inventory_levels.json")


def get_fulfillment_order(fulfillment_order_id: int) -> Any:
    return shopify_request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


def list_order_fulfillment_orders(order_id: int) -> Any:
    return shopify_request("GET", f"/orders/{order_id}/fulfillment_orders.json")


def cancel_fulfillment_order(fulfillment_order_id: int) -> Any:
    return shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json")


def close_fulfillment_order(fulfillment_order_id: int, fulfillment_order: Optional[Dict[str, Any]] = None) -> Any:
    return shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/close.json", json_body=fulfillment_order)


def hold_fulfillment_order(fulfillment_order_id: int, fulfillment_hold: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/hold.json", json_body={"fulfillment_hold": fulfillment_hold})


def move_fulfillment_order(fulfillment_order_id: int, new_location_id: int, fulfillment_order_line_items: Optional[list[Dict[str, Any]]] = None) -> Any:
    body: Dict[str, Any] = {"new_location_id": new_location_id}
    if fulfillment_order_line_items is not None:
        body["fulfillment_order_line_items"] = fulfillment_order_line_items
    return shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/move.json", json_body=body)


def open_fulfillment_order(fulfillment_order_id: int) -> Any:
    return shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/open.json")


def release_fulfillment_order_hold(fulfillment_order_id: int) -> Any:
    return shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/release_hold.json")


def reschedule_fulfillment_order(fulfillment_order_id: int, new_fulfill_at: str) -> Any:
    return shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/reschedule.json", json_body={"fulfillment_order": {"new_fulfill_at": new_fulfill_at}})


def set_fulfillment_orders_deadline(fulfillment_order_ids: list[int], fulfillment_deadline: str) -> Any:
    return shopify_request("POST", "/fulfillment_orders/set_fulfillment_orders_deadline.json", json_body={"fulfillment_order_ids": fulfillment_order_ids, "fulfillment_deadline": fulfillment_deadline})
