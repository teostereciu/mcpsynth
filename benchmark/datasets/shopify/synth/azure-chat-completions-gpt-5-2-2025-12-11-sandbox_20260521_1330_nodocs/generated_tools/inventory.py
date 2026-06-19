from typing import Any, Dict, Optional

from .client import request_json


def list_inventory_items(limit: int = 50, **filters: Any) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    params.update({k: v for k, v in filters.items() if v is not None})
    return request_json("GET", "/inventory_items.json", params=params)


def get_inventory_item(inventory_item_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/inventory_items/{inventory_item_id}.json")


def update_inventory_item(inventory_item_id: int, inventory_item: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("PUT", f"/inventory_items/{inventory_item_id}.json", json={"inventory_item": inventory_item})


def list_inventory_levels(inventory_item_ids: str, location_ids: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"inventory_item_ids": inventory_item_ids}
    if location_ids:
        params["location_ids"] = location_ids
    return request_json("GET", "/inventory_levels.json", params=params)


def adjust_inventory_level(location_id: int, inventory_item_id: int, available_adjustment: int) -> Dict[str, Any]:
    payload = {"location_id": location_id, "inventory_item_id": inventory_item_id, "available_adjustment": available_adjustment}
    return request_json("POST", "/inventory_levels/adjust.json", json=payload)


def set_inventory_level(location_id: int, inventory_item_id: int, available: int, disconnect_if_necessary: Optional[bool] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"location_id": location_id, "inventory_item_id": inventory_item_id, "available": available}
    if disconnect_if_necessary is not None:
        payload["disconnect_if_necessary"] = disconnect_if_necessary
    return request_json("POST", "/inventory_levels/set.json", json=payload)


def connect_inventory_level(location_id: int, inventory_item_id: int, relocate_if_necessary: Optional[bool] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"location_id": location_id, "inventory_item_id": inventory_item_id}
    if relocate_if_necessary is not None:
        payload["relocate_if_necessary"] = relocate_if_necessary
    return request_json("POST", "/inventory_levels/connect.json", json=payload)
