from typing import Any, Dict, Optional

from ._client import get_client


def list_fulfillment_orders_for_order(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/fulfillment_orders.json

    Doc: docs/api_fulfillmentorder.md
    """
    return get_client().request("GET", f"/orders/{order_id}/fulfillment_orders.json")


def get_fulfillment_order(fulfillment_order_id: int) -> Dict[str, Any]:
    """GET /fulfillment_orders/{fulfillment_order_id}.json

    Doc: docs/api_fulfillmentorder.md
    """
    return get_client().request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


def cancel_fulfillment_order(fulfillment_order_id: int, body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/cancel.json

    Doc: docs/api_fulfillmentorder.md
    """
    return get_client().request("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json", json_body=body)


def close_fulfillment_order(fulfillment_order_id: int, body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/close.json

    Doc: docs/api_fulfillmentorder.md
    """
    return get_client().request("POST", f"/fulfillment_orders/{fulfillment_order_id}/close.json", json_body=body)


def open_fulfillment_order(fulfillment_order_id: int, body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/open.json

    Doc: docs/api_fulfillmentorder.md
    """
    return get_client().request("POST", f"/fulfillment_orders/{fulfillment_order_id}/open.json", json_body=body)


def hold_fulfillment_order(fulfillment_order_id: int, hold: Dict[str, Any]) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/hold.json

    Doc: docs/api_fulfillmentorder.md
    """
    return get_client().request("POST", f"/fulfillment_orders/{fulfillment_order_id}/hold.json", json_body={"fulfillment_hold": hold})


def release_hold_fulfillment_order(fulfillment_order_id: int) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/release_hold.json

    Doc: docs/api_fulfillmentorder.md
    """
    return get_client().request("POST", f"/fulfillment_orders/{fulfillment_order_id}/release_hold.json")


def move_fulfillment_order(fulfillment_order_id: int, new_location_id: int) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/move.json

    Doc: docs/api_fulfillmentorder.md
    """
    return get_client().request(
        "POST",
        f"/fulfillment_orders/{fulfillment_order_id}/move.json",
        json_body={"fulfillment_order": {"new_location_id": new_location_id}},
    )


def reschedule_fulfillment_order(fulfillment_order_id: int, fulfill_at: str) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/reschedule.json

    Doc: docs/api_fulfillmentorder.md
    """
    return get_client().request(
        "POST",
        f"/fulfillment_orders/{fulfillment_order_id}/reschedule.json",
        json_body={"fulfillment_order": {"fulfill_at": fulfill_at}},
    )


def set_fulfillment_orders_deadline(fulfillment_order_ids: list[int], fulfillment_deadline: str) -> Dict[str, Any]:
    """POST /fulfillment_orders/set_fulfillment_orders_deadline.json

    Doc: docs/api_fulfillmentorder.md
    """
    return get_client().request(
        "POST",
        "/fulfillment_orders/set_fulfillment_orders_deadline.json",
        json_body={"fulfillment_order_ids": fulfillment_order_ids, "fulfillment_deadline": fulfillment_deadline},
    )
