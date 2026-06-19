from typing import Any, Dict, Optional

from .client import shopify_request


def list_inventory_levels(
    *,
    inventory_item_ids: Optional[str] = None,
    location_ids: Optional[str] = None,
    limit: Optional[int] = None,
    updated_at_min: Optional[str] = None,
) -> Any:
    """GET /inventory_levels.json"""
    params: Dict[str, Any] = {}
    for k, v in {
        "inventory_item_ids": inventory_item_ids,
        "location_ids": location_ids,
        "limit": limit,
        "updated_at_min": updated_at_min,
    }.items():
        if v is not None:
            params[k] = v
    return shopify_request("GET", "/inventory_levels.json", params=params or None)


def adjust_inventory_level(location_id: int, inventory_item_id: int, available_adjustment: int) -> Any:
    """POST /inventory_levels/adjust.json"""
    body = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available_adjustment": available_adjustment,
    }
    return shopify_request("POST", "/inventory_levels/adjust.json", json=body)


def connect_inventory_level(
    location_id: int,
    inventory_item_id: int,
    *,
    relocate_if_necessary: Optional[bool] = None,
) -> Any:
    """POST /inventory_levels/connect.json"""
    body: Dict[str, Any] = {"location_id": location_id, "inventory_item_id": inventory_item_id}
    if relocate_if_necessary is not None:
        body["relocate_if_necessary"] = relocate_if_necessary
    return shopify_request("POST", "/inventory_levels/connect.json", json=body)


def set_inventory_level(
    location_id: int,
    inventory_item_id: int,
    available: int,
    *,
    disconnect_if_necessary: Optional[bool] = None,
) -> Any:
    """POST /inventory_levels/set.json"""
    body: Dict[str, Any] = {"location_id": location_id, "inventory_item_id": inventory_item_id, "available": available}
    if disconnect_if_necessary is not None:
        body["disconnect_if_necessary"] = disconnect_if_necessary
    return shopify_request("POST", "/inventory_levels/set.json", json=body)


def delete_inventory_level(inventory_item_id: int, location_id: int) -> Any:
    """DELETE /inventory_levels.json"""
    params = {"inventory_item_id": inventory_item_id, "location_id": location_id}
    return shopify_request("DELETE", "/inventory_levels.json", params=params)
