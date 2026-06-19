from typing import Any, Dict, Optional

from .http_client import request_json


def create_fulfillment(fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    """POST /fulfillments.json

    Doc: docs/api_fulfillment.md
    Body wrapper: {"fulfillment": {...}}
    """
    return request_json("POST", "/fulfillments.json", json_body={"fulfillment": fulfillment})


def list_fulfillments_for_order(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/fulfillments.json

    Doc: docs/api_fulfillment.md
    """
    return request_json("GET", f"/orders/{order_id}/fulfillments.json")


def get_fulfillment(order_id: int, fulfillment_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/fulfillments/{fulfillment_id}.json

    Doc: docs/api_fulfillment.md
    """
    return request_json("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")


def count_fulfillments_for_order(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/fulfillments/count.json

    Doc: docs/api_fulfillment.md
    """
    return request_json("GET", f"/orders/{order_id}/fulfillments/count.json")


def list_fulfillments_for_fulfillment_order(fulfillment_order_id: int) -> Dict[str, Any]:
    """GET /fulfillment_orders/{fulfillment_order_id}/fulfillments.json

    Doc: docs/api_fulfillment.md
    """
    return request_json("GET", f"/fulfillment_orders/{fulfillment_order_id}/fulfillments.json")


def cancel_fulfillment(fulfillment_id: int) -> Dict[str, Any]:
    """POST /fulfillments/{fulfillment_id}/cancel.json

    Doc: docs/api_fulfillment.md
    """
    return request_json("POST", f"/fulfillments/{fulfillment_id}/cancel.json")


def update_fulfillment_tracking(fulfillment_id: int, tracking: Dict[str, Any]) -> Dict[str, Any]:
    """POST /fulfillments/{fulfillment_id}/update_tracking.json

    Doc: docs/api_fulfillment.md
    Body wrapper: {"fulfillment": {...}} varies; accept raw dict.
    """
    return request_json("POST", f"/fulfillments/{fulfillment_id}/update_tracking.json", json_body=tracking)
