from typing import Any, Dict, Optional

from .client import ShopifyClient


def list_inventory_items(limit: int = 50, ids: Optional[str] = None) -> Dict[str, Any]:
    """GET /inventory_items.json"""
    client = ShopifyClient()
    params: Dict[str, Any] = {"limit": limit}
    if ids:
        params["ids"] = ids
    return client.request("GET", "/inventory_items.json", params=params)


def get_inventory_item(inventory_item_id: int) -> Dict[str, Any]:
    """GET /inventory_items/{inventory_item_id}.json"""
    client = ShopifyClient()
    return client.request("GET", f"/inventory_items/{inventory_item_id}.json")


def update_inventory_item(inventory_item_id: int, inventory_item: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /inventory_items/{inventory_item_id}.json"""
    client = ShopifyClient()
    body = {"inventory_item": {**inventory_item, "id": inventory_item_id}}
    return client.request("PUT", f"/inventory_items/{inventory_item_id}.json", json_body=body)


def list_locations(limit: int = 50) -> Dict[str, Any]:
    """GET /locations.json"""
    client = ShopifyClient()
    return client.request("GET", "/locations.json", params={"limit": limit})


def list_inventory_levels(
    location_ids: Optional[str] = None,
    inventory_item_ids: Optional[str] = None,
    limit: int = 50,
) -> Dict[str, Any]:
    """GET /inventory_levels.json"""
    client = ShopifyClient()
    params: Dict[str, Any] = {"limit": limit}
    if location_ids:
        params["location_ids"] = location_ids
    if inventory_item_ids:
        params["inventory_item_ids"] = inventory_item_ids
    return client.request("GET", "/inventory_levels.json", params=params)


def adjust_inventory_level(inventory_item_id: int, location_id: int, available_adjustment: int) -> Dict[str, Any]:
    """POST /inventory_levels/adjust.json"""
    client = ShopifyClient()
    body = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "available_adjustment": available_adjustment,
    }
    return client.request("POST", "/inventory_levels/adjust.json", json_body=body)


def set_inventory_level(inventory_item_id: int, location_id: int, available: int, disconnect_if_necessary: bool = False) -> Dict[str, Any]:
    """POST /inventory_levels/set.json"""
    client = ShopifyClient()
    body = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "available": available,
        "disconnect_if_necessary": disconnect_if_necessary,
    }
    return client.request("POST", "/inventory_levels/set.json", json_body=body)


def connect_inventory_level(inventory_item_id: int, location_id: int, relocate_if_necessary: bool = False) -> Dict[str, Any]:
    """POST /inventory_levels/connect.json"""
    client = ShopifyClient()
    body = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "relocate_if_necessary": relocate_if_necessary,
    }
    return client.request("POST", "/inventory_levels/connect.json", json_body=body)
