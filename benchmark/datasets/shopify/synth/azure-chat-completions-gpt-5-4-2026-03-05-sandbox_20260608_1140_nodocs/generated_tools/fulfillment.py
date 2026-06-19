from typing import Any, Dict, Optional

from generated_tools.common import clean_params, shopify_request


def list_fulfillment_orders(order_id: int) -> Any:
    return shopify_request("GET", f"/orders/{order_id}/fulfillment_orders.json")


def get_assigned_fulfillment_orders(assignment_status: Optional[str] = None, location_ids: Optional[str] = None) -> Any:
    params = clean_params(assignment_status=assignment_status, location_ids=location_ids)
    return shopify_request("GET", "/assigned_fulfillment_orders.json", params=params)


def create_fulfillment(fulfillment: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/fulfillments.json", json_body={"fulfillment": fulfillment})


def update_tracking(fulfillment_id: int, fulfillment: Dict[str, Any], notify_customer: Optional[bool] = None) -> Any:
    body = {"fulfillment": fulfillment}
    params = clean_params(notify_customer=notify_customer)
    return shopify_request("POST", f"/fulfillments/{fulfillment_id}/update_tracking.json", params=params, json_body=body)


def cancel_fulfillment(fulfillment_id: int) -> Any:
    return shopify_request("POST", f"/fulfillments/{fulfillment_id}/cancel.json")


def move_fulfillment_order(fulfillment_order_id: int, new_location_id: int) -> Any:
    return shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/move.json", json_body={"fulfillment_order": {"new_location_id": new_location_id}})
