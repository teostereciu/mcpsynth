from typing import Any, Dict, Optional

from generated_tools.common import client


def get_orders(filter: Optional[str] = None, limit: int = 50, offset: int = 0, order_ids: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if filter is not None:
        params["filter"] = filter
    if order_ids is not None:
        params["orderIds"] = order_ids
    return client.request("GET", "/sell/fulfillment/v1/order", params=params)


def get_order(order_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/fulfillment/v1/order/{order_id}")


def issue_refund(order_id: str, refund_payload: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", f"/sell/fulfillment/v1/order/{order_id}/issue_refund", json_body=refund_payload)


def get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment/{fulfillment_id}")


def get_shipping_fulfillments(order_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment")


def create_shipping_fulfillment(order_id: str, fulfillment_payload: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment", json_body=fulfillment_payload)


def update_shipping_fulfillment(order_id: str, fulfillment_id: str, fulfillment_payload: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment/{fulfillment_id}", json_body=fulfillment_payload)
