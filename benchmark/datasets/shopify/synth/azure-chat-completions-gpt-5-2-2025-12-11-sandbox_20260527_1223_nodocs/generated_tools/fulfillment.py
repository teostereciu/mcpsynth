from typing import Any, Dict, Optional

from .client import shopify_request


def list_locations() -> Dict[str, Any]:
    return shopify_request("GET", "/locations.json")


def list_fulfillment_orders(*, order_id: int) -> Dict[str, Any]:
    return shopify_request("GET", f"/orders/{order_id}/fulfillment_orders.json")


def get_fulfillment_order(*, fulfillment_order_id: int) -> Dict[str, Any]:
    return shopify_request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


def move_fulfillment_order(*, fulfillment_order_id: int, new_location_id: int) -> Dict[str, Any]:
    body = {"fulfillment_order": {"new_location_id": new_location_id}}
    return shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/move.json", json_body=body)


def cancel_fulfillment_order(*, fulfillment_order_id: int) -> Dict[str, Any]:
    return shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json")


def create_fulfillment(*, fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    return shopify_request("POST", "/fulfillments.json", json_body={"fulfillment": fulfillment})


def get_fulfillment(*, order_id: int, fulfillment_id: int) -> Dict[str, Any]:
    return shopify_request("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")


def update_fulfillment_tracking(*, fulfillment_id: int, tracking_info: Dict[str, Any], notify_customer: Optional[bool] = None) -> Dict[str, Any]:
    body: Dict[str, Any] = {"fulfillment": {"tracking_info": tracking_info}}
    if notify_customer is not None:
        body["fulfillment"]["notify_customer"] = notify_customer
    return shopify_request("PUT", f"/fulfillments/{fulfillment_id}.json", json_body=body)


def cancel_fulfillment(*, fulfillment_id: int) -> Dict[str, Any]:
    return shopify_request("POST", f"/fulfillments/{fulfillment_id}/cancel.json")
