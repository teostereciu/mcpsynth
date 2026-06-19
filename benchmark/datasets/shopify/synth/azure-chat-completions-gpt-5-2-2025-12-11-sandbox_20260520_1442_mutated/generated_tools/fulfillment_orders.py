from typing import Any, Dict, Optional

from .http_client import request_json


def list_fulfillment_orders_for_order(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/fulfillment_orders.json

    Doc: docs/api_fulfillmentorder.md
    """
    return request_json("GET", f"/orders/{order_id}/fulfillment_orders.json")


def get_fulfillment_order(fulfillment_order_id: int) -> Dict[str, Any]:
    """GET /fulfillment_orders/{fulfillment_order_id}.json

    Doc: docs/api_fulfillmentorder.md
    """
    return request_json("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


def cancel_fulfillment_order(fulfillment_order_id: int, cancel: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/cancel.json

    Doc: docs/api_fulfillmentorder.md
    Body wrapper: {"fulfillment_order": {...}} or {"cancel": {...}} varies; accept raw dict.
    """
    return request_json(
        "POST",
        f"/fulfillment_orders/{fulfillment_order_id}/cancel.json",
        json_body=cancel,
    )


def close_fulfillment_order(fulfillment_order_id: int, close: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/close.json

    Doc: docs/api_fulfillmentorder.md
    """
    return request_json("POST", f"/fulfillment_orders/{fulfillment_order_id}/close.json", json_body=close)


def open_fulfillment_order(fulfillment_order_id: int) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/open.json

    Doc: docs/api_fulfillmentorder.md
    """
    return request_json("POST", f"/fulfillment_orders/{fulfillment_order_id}/open.json")


def hold_fulfillment_order(fulfillment_order_id: int, hold: Dict[str, Any]) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/hold.json

    Doc: docs/api_fulfillmentorder.md
    """
    return request_json("POST", f"/fulfillment_orders/{fulfillment_order_id}/hold.json", json_body=hold)


def release_fulfillment_order_hold(fulfillment_order_id: int) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/release_hold.json

    Doc: docs/api_fulfillmentorder.md
    """
    return request_json("POST", f"/fulfillment_orders/{fulfillment_order_id}/release_hold.json")


def move_fulfillment_order(fulfillment_order_id: int, move: Dict[str, Any]) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/move.json

    Doc: docs/api_fulfillmentorder.md
    """
    return request_json("POST", f"/fulfillment_orders/{fulfillment_order_id}/move.json", json_body=move)


def reschedule_fulfillment_order(fulfillment_order_id: int, reschedule: Dict[str, Any]) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/reschedule.json

    Doc: docs/api_fulfillmentorder.md
    """
    return request_json("POST", f"/fulfillment_orders/{fulfillment_order_id}/reschedule.json", json_body=reschedule)


def set_fulfillment_orders_deadline(payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /fulfillment_orders/set_fulfillment_orders_deadline.json

    Doc: docs/api_fulfillmentorder.md
    """
    return request_json("POST", "/fulfillment_orders/set_fulfillment_orders_deadline.json", json_body=payload)
