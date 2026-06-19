from typing import Any, Dict, Optional

from .client import request_json


# Locations

def list_locations() -> Any:
    return request_json("GET", "/locations.json")


def get_location(location_id: int) -> Any:
    return request_json("GET", f"/locations/{location_id}.json")


# Fulfillment orders

def list_fulfillment_orders(order_id: int) -> Any:
    return request_json("GET", f"/orders/{order_id}/fulfillment_orders.json")


def get_fulfillment_order(fulfillment_order_id: int) -> Any:
    return request_json("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


def move_fulfillment_order(fulfillment_order_id: int, new_location_id: int) -> Any:
    return request_json(
        "POST",
        f"/fulfillment_orders/{fulfillment_order_id}/move.json",
        json={"fulfillment_order": {"new_location_id": new_location_id}},
    )


def cancel_fulfillment_order(fulfillment_order_id: int) -> Any:
    return request_json("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json")


def close_fulfillment_order(fulfillment_order_id: int, *, message: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"fulfillment_order": {}}
    if message:
        payload["fulfillment_order"]["message"] = message
    return request_json("POST", f"/fulfillment_orders/{fulfillment_order_id}/close.json", json=payload)


# Fulfillments

def list_fulfillments(order_id: int) -> Any:
    return request_json("GET", f"/orders/{order_id}/fulfillments.json")


def get_fulfillment(order_id: int, fulfillment_id: int) -> Any:
    return request_json("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")


def create_fulfillment(fulfillment: Dict[str, Any]) -> Any:
    return request_json("POST", "/fulfillments.json", json={"fulfillment": fulfillment})


def update_fulfillment_tracking(order_id: int, fulfillment_id: int, tracking_info: Dict[str, Any], *, notify_customer: Optional[bool] = None) -> Any:
    payload: Dict[str, Any] = {"fulfillment": {"tracking_info": tracking_info}}
    if notify_customer is not None:
        payload["fulfillment"]["notify_customer"] = notify_customer
    return request_json("PUT", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json", json=payload)


def cancel_fulfillment(order_id: int, fulfillment_id: int) -> Any:
    return request_json("POST", f"/orders/{order_id}/fulfillments/{fulfillment_id}/cancel.json")


def create_fulfillment_event(order_id: int, fulfillment_id: int, event: Dict[str, Any]) -> Any:
    return request_json("POST", f"/orders/{order_id}/fulfillments/{fulfillment_id}/events.json", json={"event": event})
