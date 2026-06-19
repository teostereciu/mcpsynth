from typing import Any, Dict, Optional

from .http_client import get_client


def fulfillment_orders_list(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/fulfillment_orders.json"""
    return get_client().request("GET", f"/orders/{order_id}/fulfillment_orders.json")


def fulfillment_order_get(fulfillment_order_id: int) -> Dict[str, Any]:
    """GET /fulfillment_orders/{fulfillment_order_id}.json"""
    return get_client().request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


def fulfillment_order_cancel(fulfillment_order_id: int) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/cancel.json"""
    return get_client().request("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json")


def fulfillment_order_close(fulfillment_order_id: int, *, message: Optional[str] = None) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/close.json"""
    body = {"message": message} if message is not None else None
    return get_client().request("POST", f"/fulfillment_orders/{fulfillment_order_id}/close.json", json_body=body)


def fulfillment_order_open(fulfillment_order_id: int) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/open.json"""
    return get_client().request("POST", f"/fulfillment_orders/{fulfillment_order_id}/open.json")


def fulfillment_order_hold(fulfillment_order_id: int, hold: Dict[str, Any]) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/hold.json"""
    return get_client().request("POST", f"/fulfillment_orders/{fulfillment_order_id}/hold.json", json_body=hold)


def fulfillment_order_release_hold(fulfillment_order_id: int) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/release_hold.json"""
    return get_client().request("POST", f"/fulfillment_orders/{fulfillment_order_id}/release_hold.json")


def fulfillment_order_move(fulfillment_order_id: int, new_location_id: int) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/move.json"""
    return get_client().request(
        "POST",
        f"/fulfillment_orders/{fulfillment_order_id}/move.json",
        json_body={"fulfillment_order": {"new_location_id": new_location_id}},
    )


def fulfillment_order_reschedule(fulfillment_order_id: int, fulfill_at: str) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/reschedule.json"""
    return get_client().request(
        "POST",
        f"/fulfillment_orders/{fulfillment_order_id}/reschedule.json",
        json_body={"fulfillment_order": {"fulfill_at": fulfill_at}},
    )


def fulfillment_orders_set_deadline(fulfillment_order_ids: list[int], fulfill_by: str) -> Dict[str, Any]:
    """POST /fulfillment_orders/set_fulfillment_orders_deadline.json"""
    return get_client().request(
        "POST",
        "/fulfillment_orders/set_fulfillment_orders_deadline.json",
        json_body={"fulfillment_order_ids": fulfillment_order_ids, "fulfill_by": fulfill_by},
    )
