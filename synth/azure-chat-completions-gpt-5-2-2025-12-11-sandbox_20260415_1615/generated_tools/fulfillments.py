from typing import Any, Dict, Optional

from .http_client import get_client


def fulfillment_create(fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    """POST /fulfillments.json

    Note: fulfillment payload should follow Shopify's fulfillment-order based schema.
    """
    return get_client().request("POST", "/fulfillments.json", json_body={"fulfillment": fulfillment})


def fulfillments_list_for_order(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/fulfillments.json"""
    return get_client().request("GET", f"/orders/{order_id}/fulfillments.json")


def fulfillments_count_for_order(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/fulfillments/count.json"""
    return get_client().request("GET", f"/orders/{order_id}/fulfillments/count.json")


def fulfillment_get(order_id: int, fulfillment_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/fulfillments/{fulfillment_id}.json"""
    return get_client().request("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")


def fulfillments_list_for_fulfillment_order(fulfillment_order_id: int) -> Dict[str, Any]:
    """GET /fulfillment_orders/{fulfillment_order_id}/fulfillments.json"""
    return get_client().request("GET", f"/fulfillment_orders/{fulfillment_order_id}/fulfillments.json")


def fulfillment_cancel(fulfillment_id: int) -> Dict[str, Any]:
    """POST /fulfillments/{fulfillment_id}/cancel.json"""
    return get_client().request("POST", f"/fulfillments/{fulfillment_id}/cancel.json")


def fulfillment_update_tracking(fulfillment_id: int, tracking_info: Dict[str, Any], *, notify_customer: Optional[bool] = None) -> Dict[str, Any]:
    """POST /fulfillments/{fulfillment_id}/update_tracking.json"""
    body: Dict[str, Any] = {"tracking_info": tracking_info}
    if notify_customer is not None:
        body["notify_customer"] = notify_customer
    return get_client().request("POST", f"/fulfillments/{fulfillment_id}/update_tracking.json", json_body=body)
