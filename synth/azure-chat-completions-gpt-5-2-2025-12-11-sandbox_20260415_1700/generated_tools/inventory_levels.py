from typing import Any, Dict, Optional

from .client import request_json


def inventory_levels_list(*, location_ids: Optional[str] = None, inventory_item_ids: Optional[str] = None, limit: Optional[int] = None) -> Any:
    """GET /inventory_levels.json"""
    params: Dict[str, Any] = {}
    for k, v in {"location_ids": location_ids, "inventory_item_ids": inventory_item_ids, "limit": limit}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/inventory_levels.json", params=params)


def inventory_levels_adjust(location_id: int, inventory_item_id: int, available_adjustment: int) -> Any:
    """POST /inventory_levels/adjust.json"""
    body = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available_adjustment": available_adjustment,
    }
    return request_json("POST", "/inventory_levels/adjust.json", json_body=body)


def inventory_levels_set(
    location_id: int,
    inventory_item_id: int,
    available: int,
    *,
    disconnect_if_necessary: Optional[bool] = None,
) -> Any:
    """POST /inventory_levels/set.json"""
    body: Dict[str, Any] = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available": available,
    }
    if disconnect_if_necessary is not None:
        body["disconnect_if_necessary"] = disconnect_if_necessary
    return request_json("POST", "/inventory_levels/set.json", json_body=body)


def inventory_levels_connect(
    location_id: int,
    inventory_item_id: int,
    *,
    relocate_if_necessary: Optional[bool] = None,
) -> Any:
    """POST /inventory_levels/connect.json"""
    body: Dict[str, Any] = {"location_id": location_id, "inventory_item_id": inventory_item_id}
    if relocate_if_necessary is not None:
        body["relocate_if_necessary"] = relocate_if_necessary
    return request_json("POST", "/inventory_levels/connect.json", json_body=body)


def inventory_levels_delete(inventory_item_id: int, location_id: int) -> Any:
    """DELETE /inventory_levels.json"""
    return request_json(
        "DELETE",
        "/inventory_levels.json",
        params={"inventory_item_id": inventory_item_id, "location_id": location_id},
    )
