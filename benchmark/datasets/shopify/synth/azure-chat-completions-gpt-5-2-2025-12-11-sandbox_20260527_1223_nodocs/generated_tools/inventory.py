from typing import Any, Dict, Optional

from .client import shopify_request


def list_inventory_items(*, limit: int = 50, since_id: Optional[int] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if since_id is not None:
        params["since_id"] = since_id
    return shopify_request("GET", "/inventory_items.json", params=params)


def get_inventory_item(*, inventory_item_id: int) -> Dict[str, Any]:
    return shopify_request("GET", f"/inventory_items/{inventory_item_id}.json")


def update_inventory_item(*, inventory_item_id: int, inventory_item: Dict[str, Any]) -> Dict[str, Any]:
    body = {"inventory_item": {**inventory_item, "id": inventory_item_id}}
    return shopify_request("PUT", f"/inventory_items/{inventory_item_id}.json", json_body=body)


def list_inventory_levels(*, inventory_item_ids: str, location_ids: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"inventory_item_ids": inventory_item_ids}
    if location_ids is not None:
        params["location_ids"] = location_ids
    return shopify_request("GET", "/inventory_levels.json", params=params)


def adjust_inventory_level(*, inventory_item_id: int, location_id: int, available_adjustment: int) -> Dict[str, Any]:
    body = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "available_adjustment": available_adjustment,
    }
    return shopify_request("POST", "/inventory_levels/adjust.json", json_body=body)


def set_inventory_level(*, inventory_item_id: int, location_id: int, available: int, disconnect_if_necessary: Optional[bool] = None) -> Dict[str, Any]:
    body: Dict[str, Any] = {"inventory_item_id": inventory_item_id, "location_id": location_id, "available": available}
    if disconnect_if_necessary is not None:
        body["disconnect_if_necessary"] = disconnect_if_necessary
    return shopify_request("POST", "/inventory_levels/set.json", json_body=body)


def connect_inventory_level(*, inventory_item_id: int, location_id: int, relocate_if_necessary: Optional[bool] = None) -> Dict[str, Any]:
    body: Dict[str, Any] = {"inventory_item_id": inventory_item_id, "location_id": location_id}
    if relocate_if_necessary is not None:
        body["relocate_if_necessary"] = relocate_if_necessary
    return shopify_request("POST", "/inventory_levels/connect.json", json_body=body)
