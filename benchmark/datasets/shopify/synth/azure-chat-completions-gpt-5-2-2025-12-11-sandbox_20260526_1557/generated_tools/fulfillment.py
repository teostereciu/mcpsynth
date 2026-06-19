from typing import Any, Dict, Optional

from .http import ShopifyClient


# Locations

def list_locations(*, limit: Optional[int] = 50) -> Dict[str, Any]:
    """GET /admin/api/2026-01/locations.json"""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    return ShopifyClient().request("GET", "/locations.json", params=params or None)


def get_location(*, location_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/locations/{location_id}.json"""
    return ShopifyClient().request("GET", f"/locations/{location_id}.json")


def count_locations() -> Dict[str, Any]:
    """GET /admin/api/2026-01/locations/count.json"""
    return ShopifyClient().request("GET", "/locations/count.json")


def list_location_inventory_levels(*, location_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/locations/{location_id}/inventory_levels.json"""
    return ShopifyClient().request("GET", f"/locations/{location_id}/inventory_levels.json")


# Fulfillment orders

def list_fulfillment_orders_for_order(*, order_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/{order_id}/fulfillment_orders.json"""
    return ShopifyClient().request("GET", f"/orders/{order_id}/fulfillment_orders.json")


def get_fulfillment_order(*, fulfillment_order_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/fulfillment_orders/{fulfillment_order_id}.json"""
    return ShopifyClient().request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


def cancel_fulfillment_order(*, fulfillment_order_id: int, message: Optional[str] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/fulfillment_orders/{fulfillment_order_id}/cancel.json"""
    body = {"message": message} if message is not None else None
    return ShopifyClient().request("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json", json_body=body)


def close_fulfillment_order(*, fulfillment_order_id: int, message: Optional[str] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/fulfillment_orders/{fulfillment_order_id}/close.json"""
    body = {"message": message} if message is not None else None
    return ShopifyClient().request("POST", f"/fulfillment_orders/{fulfillment_order_id}/close.json", json_body=body)


def open_fulfillment_order(*, fulfillment_order_id: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/fulfillment_orders/{fulfillment_order_id}/open.json"""
    return ShopifyClient().request("POST", f"/fulfillment_orders/{fulfillment_order_id}/open.json")


def hold_fulfillment_order(*, fulfillment_order_id: int, hold: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/fulfillment_orders/{fulfillment_order_id}/hold.json"""
    return ShopifyClient().request("POST", f"/fulfillment_orders/{fulfillment_order_id}/hold.json", json_body={"fulfillment_hold": hold})


def release_fulfillment_order_hold(*, fulfillment_order_id: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/fulfillment_orders/{fulfillment_order_id}/release_hold.json"""
    return ShopifyClient().request("POST", f"/fulfillment_orders/{fulfillment_order_id}/release_hold.json")


def move_fulfillment_order(*, fulfillment_order_id: int, new_location_id: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/fulfillment_orders/{fulfillment_order_id}/move.json"""
    return ShopifyClient().request(
        "POST",
        f"/fulfillment_orders/{fulfillment_order_id}/move.json",
        json_body={"fulfillment_order": {"new_location_id": new_location_id}},
    )


def reschedule_fulfillment_order(*, fulfillment_order_id: int, fulfill_at: str) -> Dict[str, Any]:
    """POST /admin/api/2026-01/fulfillment_orders/{fulfillment_order_id}/reschedule.json"""
    return ShopifyClient().request(
        "POST",
        f"/fulfillment_orders/{fulfillment_order_id}/reschedule.json",
        json_body={"fulfillment_order": {"fulfill_at": fulfill_at}},
    )


def set_fulfillment_orders_deadline(*, fulfillment_order_ids: list[int], fulfill_by: str) -> Dict[str, Any]:
    """POST /admin/api/2026-01/fulfillment_orders/set_fulfillment_orders_deadline.json"""
    return ShopifyClient().request(
        "POST",
        "/fulfillment_orders/set_fulfillment_orders_deadline.json",
        json_body={"fulfillment_order_ids": fulfillment_order_ids, "fulfill_by": fulfill_by},
    )
