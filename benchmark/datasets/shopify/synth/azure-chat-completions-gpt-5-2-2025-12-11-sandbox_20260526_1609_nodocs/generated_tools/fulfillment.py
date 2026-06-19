from typing import Any, Dict

from .client import ShopifyClient


def list_fulfillment_orders(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/fulfillment_orders.json"""
    return ShopifyClient().request("GET", f"/orders/{order_id}/fulfillment_orders.json")


def get_fulfillment_order(fulfillment_order_id: int) -> Dict[str, Any]:
    """GET /fulfillment_orders/{id}.json"""
    return ShopifyClient().request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


def move_fulfillment_order(fulfillment_order_id: int, new_location_id: int) -> Dict[str, Any]:
    """POST /fulfillment_orders/{id}/move.json"""
    return ShopifyClient().request(
        "POST",
        f"/fulfillment_orders/{fulfillment_order_id}/move.json",
        json={"fulfillment_order": {"new_location_id": new_location_id}},
    )


def cancel_fulfillment_order(fulfillment_order_id: int) -> Dict[str, Any]:
    """POST /fulfillment_orders/{id}/cancel.json"""
    return ShopifyClient().request("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json")


def create_fulfillment(fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    """POST /fulfillments.json"""
    return ShopifyClient().request("POST", "/fulfillments.json", json={"fulfillment": fulfillment})


def get_fulfillment(fulfillment_id: int) -> Dict[str, Any]:
    """GET /fulfillments/{id}.json"""
    return ShopifyClient().request("GET", f"/fulfillments/{fulfillment_id}.json")


def update_fulfillment(fulfillment_id: int, fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /fulfillments/{id}.json"""
    return ShopifyClient().request("PUT", f"/fulfillments/{fulfillment_id}.json", json={"fulfillment": fulfillment})


def cancel_fulfillment(fulfillment_id: int) -> Dict[str, Any]:
    """POST /fulfillments/{id}/cancel.json"""
    return ShopifyClient().request("POST", f"/fulfillments/{fulfillment_id}/cancel.json")
