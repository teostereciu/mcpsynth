from typing import Any, Dict, Optional

from .client import request_json


# Inventory items

def get_inventory_item(inventory_item_id: int) -> Any:
    return request_json("GET", f"/inventory_items/{inventory_item_id}.json")


def update_inventory_item(inventory_item_id: int, inventory_item: Dict[str, Any]) -> Any:
    return request_json("PUT", f"/inventory_items/{inventory_item_id}.json", json={"inventory_item": inventory_item})


# Inventory levels

def list_inventory_levels(*, inventory_item_ids: Optional[str] = None, location_ids: Optional[str] = None, limit: int = 50) -> Any:
    params: Dict[str, Any] = {"limit": limit}
    if inventory_item_ids:
        params["inventory_item_ids"] = inventory_item_ids
    if location_ids:
        params["location_ids"] = location_ids
    return request_json("GET", "/inventory_levels.json", params=params)


def adjust_inventory_level(location_id: int, inventory_item_id: int, available_adjustment: int) -> Any:
    payload = {"location_id": location_id, "inventory_item_id": inventory_item_id, "available_adjustment": available_adjustment}
    return request_json("POST", "/inventory_levels/adjust.json", json=payload)


def set_inventory_level(location_id: int, inventory_item_id: int, available: int, *, disconnect_if_necessary: Optional[bool] = None) -> Any:
    payload: Dict[str, Any] = {"location_id": location_id, "inventory_item_id": inventory_item_id, "available": available}
    if disconnect_if_necessary is not None:
        payload["disconnect_if_necessary"] = disconnect_if_necessary
    return request_json("POST", "/inventory_levels/set.json", json=payload)


def connect_inventory_level(location_id: int, inventory_item_id: int, *, relocate_if_necessary: Optional[bool] = None) -> Any:
    payload: Dict[str, Any] = {"location_id": location_id, "inventory_item_id": inventory_item_id}
    if relocate_if_necessary is not None:
        payload["relocate_if_necessary"] = relocate_if_necessary
    return request_json("POST", "/inventory_levels/connect.json", json=payload)


def delete_inventory_level(location_id: int, inventory_item_id: int) -> Any:
    payload = {"location_id": location_id, "inventory_item_id": inventory_item_id}
    return request_json("POST", "/inventory_levels/delete.json", json=payload)
