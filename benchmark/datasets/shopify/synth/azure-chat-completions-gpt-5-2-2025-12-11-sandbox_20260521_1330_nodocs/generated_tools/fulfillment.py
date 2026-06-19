from typing import Any, Dict, Optional

from .client import request_json


def list_locations(limit: int = 50) -> Dict[str, Any]:
    return request_json("GET", "/locations.json", params={"limit": limit})


def list_fulfillment_orders(order_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/orders/{order_id}/fulfillment_orders.json")


def get_fulfillment_order(fulfillment_order_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


def move_fulfillment_order(fulfillment_order_id: int, new_location_id: int) -> Dict[str, Any]:
    return request_json("POST", f"/fulfillment_orders/{fulfillment_order_id}/move.json", json={"new_location_id": new_location_id})


def cancel_fulfillment_order(fulfillment_order_id: int) -> Dict[str, Any]:
    return request_json("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json")


def create_fulfillment(fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", "/fulfillments.json", json={"fulfillment": fulfillment})


def get_fulfillment(fulfillment_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/fulfillments/{fulfillment_id}.json")


def update_fulfillment(fulfillment_id: int, fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("PUT", f"/fulfillments/{fulfillment_id}.json", json={"fulfillment": fulfillment})


def cancel_fulfillment(fulfillment_id: int) -> Dict[str, Any]:
    return request_json("POST", f"/fulfillments/{fulfillment_id}/cancel.json")
