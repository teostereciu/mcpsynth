from typing import Any, Dict, Optional

from .http_client import get_client


def inventory_levels_list(*, location_ids: Optional[str] = None, inventory_item_ids: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /inventory_levels.json"""
    params: Dict[str, Any] = {}
    for k, v in {"location_ids": location_ids, "inventory_item_ids": inventory_item_ids, "limit": limit}.items():
        if v is not None:
            params[k] = v
    return get_client().request("GET", "/inventory_levels.json", params=params or None)


def inventory_levels_adjust(location_id: int, inventory_item_id: int, available_adjustment: int) -> Dict[str, Any]:
    """POST /inventory_levels/adjust.json"""
    body = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available_adjustment": available_adjustment,
    }
    return get_client().request("POST", "/inventory_levels/adjust.json", json_body=body)


def inventory_levels_set(
    location_id: int,
    inventory_item_id: int,
    available: int,
    *,
    disconnect_if_necessary: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /inventory_levels/set.json"""
    body: Dict[str, Any] = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available": available,
    }
    if disconnect_if_necessary is not None:
        body["disconnect_if_necessary"] = disconnect_if_necessary
    return get_client().request("POST", "/inventory_levels/set.json", json_body=body)


def inventory_levels_connect(
    location_id: int,
    inventory_item_id: int,
    *,
    relocate_if_necessary: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /inventory_levels/connect.json"""
    body: Dict[str, Any] = {"location_id": location_id, "inventory_item_id": inventory_item_id}
    if relocate_if_necessary is not None:
        body["relocate_if_necessary"] = relocate_if_necessary
    return get_client().request("POST", "/inventory_levels/connect.json", json_body=body)


def inventory_levels_delete(inventory_item_id: int, location_id: int) -> Dict[str, Any]:
    """DELETE /inventory_levels.json?inventory_item_id=...&location_id=..."""
    params = {"inventory_item_id": inventory_item_id, "location_id": location_id}
    return get_client().request("DELETE", "/inventory_levels.json", params=params)
