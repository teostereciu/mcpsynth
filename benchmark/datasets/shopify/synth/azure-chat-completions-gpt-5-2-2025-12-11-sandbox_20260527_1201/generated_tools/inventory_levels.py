from typing import Any, Dict, Optional

from .http_client import request_json


def list_inventory_levels(*, location_ids: Optional[str] = None, inventory_item_ids: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/inventory_levels.json"""
    params: Dict[str, Any] = {}
    if location_ids is not None:
        params["location_ids"] = location_ids
    if inventory_item_ids is not None:
        params["inventory_item_ids"] = inventory_item_ids
    if limit is not None:
        params["limit"] = limit
    return request_json("GET", "/inventory_levels.json", params=params)


def adjust_inventory_level(location_id: int, inventory_item_id: int, available_adjustment: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/inventory_levels/adjust.json"""
    body = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available_adjustment": available_adjustment,
    }
    return request_json("POST", "/inventory_levels/adjust.json", json_body=body)


def set_inventory_level(
    location_id: int,
    inventory_item_id: int,
    available: int,
    *,
    disconnect_if_necessary: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /admin/api/2026-01/inventory_levels/set.json"""
    body: Dict[str, Any] = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available": available,
    }
    if disconnect_if_necessary is not None:
        body["disconnect_if_necessary"] = disconnect_if_necessary
    return request_json("POST", "/inventory_levels/set.json", json_body=body)


def connect_inventory_level(
    location_id: int,
    inventory_item_id: int,
    *,
    relocate_if_necessary: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /admin/api/2026-01/inventory_levels/connect.json"""
    body: Dict[str, Any] = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
    }
    if relocate_if_necessary is not None:
        body["relocate_if_necessary"] = relocate_if_necessary
    return request_json("POST", "/inventory_levels/connect.json", json_body=body)


def delete_inventory_level(inventory_item_id: int, location_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/inventory_levels.json?inventory_item_id=...&location_id=..."""
    params = {"inventory_item_id": inventory_item_id, "location_id": location_id}
    return request_json("DELETE", "/inventory_levels.json", params=params)
