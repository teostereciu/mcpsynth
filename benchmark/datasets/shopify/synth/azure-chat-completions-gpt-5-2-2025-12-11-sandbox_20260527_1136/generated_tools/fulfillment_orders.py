from typing import Any, Dict, Optional

from ._client import ShopifyClient, clean_params


# Source doc: docs/api_fulfillmentorder.md


def list_fulfillment_orders_for_order(order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /orders/{order_id}/fulfillment_orders.json"""
    c = client or ShopifyClient()
    return c.request("GET", f"/orders/{order_id}/fulfillment_orders.json")


def get_fulfillment_order(fulfillment_order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /fulfillment_orders/{fulfillment_order_id}.json"""
    c = client or ShopifyClient()
    return c.request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


def cancel_fulfillment_order(
    fulfillment_order_id: int,
    *,
    message: Optional[str] = None,
    notify_merchant: Optional[bool] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/cancel.json"""
    c = client or ShopifyClient()
    body = clean_params({"message": message, "notify_merchant": notify_merchant})
    return c.request("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json", json=body or {})


def close_fulfillment_order(
    fulfillment_order_id: int,
    *,
    message: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/close.json"""
    c = client or ShopifyClient()
    body = clean_params({"message": message})
    return c.request("POST", f"/fulfillment_orders/{fulfillment_order_id}/close.json", json=body or {})


def open_fulfillment_order(fulfillment_order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/open.json"""
    c = client or ShopifyClient()
    return c.request("POST", f"/fulfillment_orders/{fulfillment_order_id}/open.json", json={})


def hold_fulfillment_order(
    fulfillment_order_id: int,
    reason: str,
    *,
    reason_notes: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/hold.json"""
    c = client or ShopifyClient()
    body = clean_params({"fulfillment_hold": {"reason": reason, "reason_notes": reason_notes}})
    return c.request("POST", f"/fulfillment_orders/{fulfillment_order_id}/hold.json", json=body)


def release_fulfillment_order_hold(fulfillment_order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/release_hold.json"""
    c = client or ShopifyClient()
    return c.request("POST", f"/fulfillment_orders/{fulfillment_order_id}/release_hold.json", json={})


def move_fulfillment_order(
    fulfillment_order_id: int,
    new_location_id: int,
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/move.json"""
    c = client or ShopifyClient()
    body = {"fulfillment_order": {"new_location_id": new_location_id}}
    return c.request("POST", f"/fulfillment_orders/{fulfillment_order_id}/move.json", json=body)


def reschedule_fulfillment_order(
    fulfillment_order_id: int,
    fulfill_at: str,
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """POST /fulfillment_orders/{fulfillment_order_id}/reschedule.json"""
    c = client or ShopifyClient()
    body = {"fulfillment_order": {"fulfill_at": fulfill_at}}
    return c.request("POST", f"/fulfillment_orders/{fulfillment_order_id}/reschedule.json", json=body)


def set_fulfillment_orders_deadline(
    fulfillment_order_ids: list[int],
    fulfillment_deadline: str,
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """POST /fulfillment_orders/set_fulfillment_orders_deadline.json"""
    c = client or ShopifyClient()
    body = {"fulfillment_order_ids": fulfillment_order_ids, "fulfillment_deadline": fulfillment_deadline}
    return c.request("POST", "/fulfillment_orders/set_fulfillment_orders_deadline.json", json=body)
