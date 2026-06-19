from typing import Any, Dict, Optional

from .client import request_json


def list_locations() -> Dict[str, Any]:
    return request_json("GET", "/locations.json")


def list_fulfillment_orders(order_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/orders/{order_id}/fulfillment_orders.json")


def get_fulfillment_order(fulfillment_order_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


def move_fulfillment_order(fulfillment_order_id: int, *, new_location_id: int) -> Dict[str, Any]:
    return request_json(
        "POST",
        f"/fulfillment_orders/{fulfillment_order_id}/move.json",
        json_body={"fulfillment_order": {"new_location_id": new_location_id}},
    )


def cancel_fulfillment_order(fulfillment_order_id: int) -> Dict[str, Any]:
    return request_json("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json")


def create_fulfillment(fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", "/fulfillments.json", json_body={"fulfillment": fulfillment})


def get_fulfillment(order_id: int, fulfillment_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")


def update_fulfillment(order_id: int, fulfillment_id: int, fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    body = {"fulfillment": {**fulfillment, "id": fulfillment_id}}
    return request_json("PUT", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json", json_body=body)


def cancel_fulfillment(order_id: int, fulfillment_id: int) -> Dict[str, Any]:
    return request_json("POST", f"/orders/{order_id}/fulfillments/{fulfillment_id}/cancel.json")


def create_fulfillment_event(order_id: int, fulfillment_id: int, event: Dict[str, Any]) -> Dict[str, Any]:
    return request_json(
        "POST",
        f"/orders/{order_id}/fulfillments/{fulfillment_id}/events.json",
        json_body={"event": event},
    )
