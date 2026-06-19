from typing import Any, Dict, Optional

from .http_client import ShopifyClient


def fulfillment_orders_list_by_order(order_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/{order_id}/fulfillment_orders.json"""
    client = ShopifyClient()
    return client.request("GET", f"/orders/{order_id}/fulfillment_orders.json")


def fulfillment_order_get(fulfillment_order_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/fulfillment_orders/{fulfillment_order_id}.json"""
    client = ShopifyClient()
    return client.request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


def fulfillment_order_cancel(fulfillment_order_id: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/fulfillment_orders/{fulfillment_order_id}/cancel.json"""
    client = ShopifyClient()
    return client.request(
        "POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json"
    )


def fulfillment_order_close(fulfillment_order_id: int, *, message: Optional[str] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/fulfillment_orders/{fulfillment_order_id}/close.json"""
    client = ShopifyClient()
    body = {"message": message} if message else None
    return client.request(
        "POST", f"/fulfillment_orders/{fulfillment_order_id}/close.json", json_body=body
    )


def fulfillment_order_open(fulfillment_order_id: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/fulfillment_orders/{fulfillment_order_id}/open.json"""
    client = ShopifyClient()
    return client.request(
        "POST", f"/fulfillment_orders/{fulfillment_order_id}/open.json"
    )


def fulfillment_order_hold(
    fulfillment_order_id: int,
    hold: Dict[str, Any],
) -> Dict[str, Any]:
    """POST /admin/api/2026-01/fulfillment_orders/{fulfillment_order_id}/hold.json"""
    client = ShopifyClient()
    return client.request(
        "POST",
        f"/fulfillment_orders/{fulfillment_order_id}/hold.json",
        json_body={"fulfillment_hold": hold},
    )


def fulfillment_order_release_hold(fulfillment_order_id: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/fulfillment_orders/{fulfillment_order_id}/release_hold.json"""
    client = ShopifyClient()
    return client.request(
        "POST", f"/fulfillment_orders/{fulfillment_order_id}/release_hold.json"
    )


def fulfillment_order_move(fulfillment_order_id: int, new_location_id: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/fulfillment_orders/{fulfillment_order_id}/move.json"""
    client = ShopifyClient()
    body = {"fulfillment_order": {"new_location_id": new_location_id}}
    return client.request(
        "POST", f"/fulfillment_orders/{fulfillment_order_id}/move.json", json_body=body
    )


def fulfillment_order_reschedule(fulfillment_order_id: int, fulfill_at: str) -> Dict[str, Any]:
    """POST /admin/api/2026-01/fulfillment_orders/{fulfillment_order_id}/reschedule.json"""
    client = ShopifyClient()
    body = {"fulfillment_order": {"fulfill_at": fulfill_at}}
    return client.request(
        "POST",
        f"/fulfillment_orders/{fulfillment_order_id}/reschedule.json",
        json_body=body,
    )


def fulfillment_orders_set_deadline(fulfillment_order_ids: list[int], fulfillment_deadline: str) -> Dict[str, Any]:
    """POST /admin/api/2026-01/fulfillment_orders/set_fulfillment_orders_deadline.json"""
    client = ShopifyClient()
    body = {
        "fulfillment_order_ids": fulfillment_order_ids,
        "fulfillment_deadline": fulfillment_deadline,
    }
    return client.request(
        "POST", "/fulfillment_orders/set_fulfillment_orders_deadline.json", json_body=body
    )
