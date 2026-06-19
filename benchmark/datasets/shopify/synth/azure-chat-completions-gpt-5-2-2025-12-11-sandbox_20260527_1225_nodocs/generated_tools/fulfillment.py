from typing import Any, Dict, Optional

from .client import ShopifyClient


def list_fulfillment_orders(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/fulfillment_orders.json"""
    client = ShopifyClient()
    return client.request("GET", f"/orders/{order_id}/fulfillment_orders.json")


def get_fulfillment_order(fulfillment_order_id: int) -> Dict[str, Any]:
    """GET /fulfillment_orders/{fulfillment_order_id}.json"""
    client = ShopifyClient()
    return client.request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


def list_fulfillments(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/fulfillments.json"""
    client = ShopifyClient()
    return client.request("GET", f"/orders/{order_id}/fulfillments.json")


def create_fulfillment(fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    """POST /fulfillments.json"""
    client = ShopifyClient()
    return client.request("POST", "/fulfillments.json", json_body={"fulfillment": fulfillment})


def cancel_fulfillment(fulfillment_id: int) -> Dict[str, Any]:
    """POST /fulfillments/{fulfillment_id}/cancel.json"""
    client = ShopifyClient()
    return client.request("POST", f"/fulfillments/{fulfillment_id}/cancel.json")


def update_fulfillment_tracking(fulfillment_id: int, tracking_info: Dict[str, Any], notify_customer: bool = False) -> Dict[str, Any]:
    """PUT /fulfillments/{fulfillment_id}/update_tracking.json"""
    client = ShopifyClient()
    body = {"fulfillment": {"tracking_info": tracking_info, "notify_customer": notify_customer}}
    return client.request("PUT", f"/fulfillments/{fulfillment_id}/update_tracking.json", json_body=body)


def list_assigned_fulfillment_orders(location_id: int, assignment_status: Optional[str] = None) -> Dict[str, Any]:
    """GET /assigned_fulfillment_orders.json"""
    client = ShopifyClient()
    params: Dict[str, Any] = {"location_ids": location_id}
    if assignment_status:
        params["assignment_status"] = assignment_status
    return client.request("GET", "/assigned_fulfillment_orders.json", params=params)
