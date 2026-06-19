from typing import Any, Dict, Optional

from shopify_client import ShopifyClient


def list_locations(*, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /locations.json"""
    c = ShopifyClient()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    return c.request("GET", "/locations.json", params=params)


def list_fulfillment_orders(*, order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/fulfillment_orders.json"""
    c = ShopifyClient()
    return c.request("GET", f"/orders/{order_id}/fulfillment_orders.json")


def get_fulfillment_order(*, fulfillment_order_id: int) -> Dict[str, Any]:
    """GET /fulfillment_orders/{fulfillment_order_id}.json"""
    c = ShopifyClient()
    return c.request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


def create_fulfillment(*, fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    """POST /fulfillments.json"""
    c = ShopifyClient()
    return c.request("POST", "/fulfillments.json", json={"fulfillment": fulfillment})


def get_fulfillment(*, order_id: int, fulfillment_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/fulfillments/{fulfillment_id}.json"""
    c = ShopifyClient()
    return c.request("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")


def update_fulfillment_tracking(*, fulfillment_id: int, tracking_info: Dict[str, Any], notify_customer: Optional[bool] = None) -> Dict[str, Any]:
    """PUT /fulfillments/{fulfillment_id}/update_tracking.json"""
    c = ShopifyClient()
    payload: Dict[str, Any] = {"tracking_info": tracking_info}
    if notify_customer is not None:
        payload["notify_customer"] = notify_customer
    return c.request("PUT", f"/fulfillments/{fulfillment_id}/update_tracking.json", json=payload)
