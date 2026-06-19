from typing import Any, Dict, Optional

from .common import client


def get_order(order_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/fulfillment/v1/order/{order_id}")


def list_orders(limit: int = 50, offset: int = 0, filter: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    return client.request("GET", "/sell/fulfillment/v1/order", params=params)


def get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment/{fulfillment_id}")


def create_shipping_fulfillment(order_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment", json_body=data)


def list_shipping_fulfillments(order_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment")
