from typing import Any, Dict, Optional

from .client import ShopifyClient


def list_inventory_items(limit: int = 50, page_info: Optional[str] = None, **filters: Any) -> Dict[str, Any]:
    """GET /inventory_items.json"""
    params: Dict[str, Any] = {"limit": limit}
    if page_info:
        params["page_info"] = page_info
    params.update({k: v for k, v in filters.items() if v is not None})
    return ShopifyClient().request("GET", "/inventory_items.json", params=params)


def get_inventory_item(inventory_item_id: int) -> Dict[str, Any]:
    """GET /inventory_items/{id}.json"""
    return ShopifyClient().request("GET", f"/inventory_items/{inventory_item_id}.json")


def update_inventory_item(inventory_item_id: int, inventory_item: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /inventory_items/{id}.json"""
    return ShopifyClient().request("PUT", f"/inventory_items/{inventory_item_id}.json", json={"inventory_item": inventory_item})


def list_locations(limit: int = 250) -> Dict[str, Any]:
    """GET /locations.json"""
    return ShopifyClient().request("GET", "/locations.json", params={"limit": limit})


def list_inventory_levels(inventory_item_ids: str, location_ids: Optional[str] = None) -> Dict[str, Any]:
    """GET /inventory_levels.json"""
    params: Dict[str, Any] = {"inventory_item_ids": inventory_item_ids}
    if location_ids:
        params["location_ids"] = location_ids
    return ShopifyClient().request("GET", "/inventory_levels.json", params=params)


def adjust_inventory_level(inventory_item_id: int, location_id: int, available_adjustment: int) -> Dict[str, Any]:
    """POST /inventory_levels/adjust.json"""
    body = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "available_adjustment": available_adjustment,
    }
    return ShopifyClient().request("POST", "/inventory_levels/adjust.json", json=body)


def set_inventory_level(inventory_item_id: int, location_id: int, available: int, disconnect_if_necessary: bool = False) -> Dict[str, Any]:
    """POST /inventory_levels/set.json"""
    body = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "available": available,
        "disconnect_if_necessary": disconnect_if_necessary,
    }
    return ShopifyClient().request("POST", "/inventory_levels/set.json", json=body)


def connect_inventory_level(inventory_item_id: int, location_id: int, relocate_if_necessary: bool = False) -> Dict[str, Any]:
    """POST /inventory_levels/connect.json"""
    body = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "relocate_if_necessary": relocate_if_necessary,
    }
    return ShopifyClient().request("POST", "/inventory_levels/connect.json", json=body)
