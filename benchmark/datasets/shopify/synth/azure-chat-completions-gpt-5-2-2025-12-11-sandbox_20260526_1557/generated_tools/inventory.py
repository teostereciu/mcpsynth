from typing import Any, Dict, Optional

from .http import ShopifyClient


# Inventory items

def list_inventory_items(*, ids: str, limit: Optional[int] = 50) -> Dict[str, Any]:
    """GET /admin/api/2026-01/inventory_items.json"""
    params: Dict[str, Any] = {"ids": ids}
    if limit is not None:
        params["limit"] = limit
    return ShopifyClient().request("GET", "/inventory_items.json", params=params)


def get_inventory_item(*, inventory_item_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/inventory_items/{inventory_item_id}.json"""
    return ShopifyClient().request("GET", f"/inventory_items/{inventory_item_id}.json")


def update_inventory_item(*, inventory_item_id: int, inventory_item: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/inventory_items/{inventory_item_id}.json"""
    body = {"inventory_item": {**inventory_item, "id": inventory_item_id}}
    return ShopifyClient().request("PUT", f"/inventory_items/{inventory_item_id}.json", json_body=body)


# Inventory levels

def list_inventory_levels(
    *,
    location_ids: Optional[str] = None,
    inventory_item_ids: Optional[str] = None,
    limit: Optional[int] = 50,
    updated_at_min: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/inventory_levels.json"""
    params: Dict[str, Any] = {}
    if location_ids is not None:
        params["location_ids"] = location_ids
    if inventory_item_ids is not None:
        params["inventory_item_ids"] = inventory_item_ids
    if limit is not None:
        params["limit"] = limit
    if updated_at_min is not None:
        params["updated_at_min"] = updated_at_min
    return ShopifyClient().request("GET", "/inventory_levels.json", params=params)


def adjust_inventory_level(*, location_id: int, inventory_item_id: int, available_adjustment: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/inventory_levels/adjust.json"""
    body = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available_adjustment": available_adjustment,
    }
    return ShopifyClient().request("POST", "/inventory_levels/adjust.json", json_body=body)


def set_inventory_level(
    *,
    location_id: int,
    inventory_item_id: int,
    available: int,
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
    return ShopifyClient().request("POST", "/inventory_levels/set.json", json_body=body)


def connect_inventory_level(
    *,
    location_id: int,
    inventory_item_id: int,
    relocate_if_necessary: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /admin/api/2026-01/inventory_levels/connect.json"""
    body: Dict[str, Any] = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
    }
    if relocate_if_necessary is not None:
        body["relocate_if_necessary"] = relocate_if_necessary
    return ShopifyClient().request("POST", "/inventory_levels/connect.json", json_body=body)


def delete_inventory_level(*, inventory_item_id: int, location_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/inventory_levels.json"""
    params = {"inventory_item_id": inventory_item_id, "location_id": location_id}
    return ShopifyClient().request("DELETE", "/inventory_levels.json", params=params)
