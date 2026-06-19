from typing import Any, Dict, Optional

from generated_tools.common import shopify_request


def list_inventory_items(ids: str, limit: Optional[int] = None) -> Any:
    params = {k: v for k, v in {"ids": ids, "limit": limit}.items() if v is not None}
    return shopify_request("GET", "/inventory_items.json", params=params)


def get_inventory_item(inventory_item_id: int) -> Any:
    return shopify_request("GET", f"/inventory_items/{inventory_item_id}.json")


def update_inventory_item(inventory_item_id: int, inventory_item: Dict[str, Any]) -> Any:
    payload = dict(inventory_item)
    payload.setdefault("id", inventory_item_id)
    return shopify_request("PUT", f"/inventory_items/{inventory_item_id}.json", json_body={"inventory_item": payload})


def list_inventory_levels(location_ids: Optional[str] = None, inventory_item_ids: Optional[str] = None, limit: Optional[int] = None) -> Any:
    params = {k: v for k, v in {"location_ids": location_ids, "inventory_item_ids": inventory_item_ids, "limit": limit}.items() if v is not None}
    return shopify_request("GET", "/inventory_levels.json", params=params)


def adjust_inventory_level(location_id: int, inventory_item_id: int, available_adjustment: int) -> Any:
    return shopify_request("POST", "/inventory_levels/adjust.json", json_body={
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available_adjustment": available_adjustment,
    })


def connect_inventory_level(location_id: int, inventory_item_id: int, relocate_if_necessary: Optional[bool] = None) -> Any:
    body = {k: v for k, v in {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "relocate_if_necessary": relocate_if_necessary,
    }.items() if v is not None}
    return shopify_request("POST", "/inventory_levels/connect.json", json_body=body)


def set_inventory_level(location_id: int, inventory_item_id: int, available: int, disconnect_if_necessary: Optional[bool] = None) -> Any:
    body = {k: v for k, v in {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available": available,
        "disconnect_if_necessary": disconnect_if_necessary,
    }.items() if v is not None}
    return shopify_request("POST", "/inventory_levels/set.json", json_body=body)


def delete_inventory_level(location_id: int, inventory_item_id: int) -> Any:
    return shopify_request("DELETE", "/inventory_levels.json", params={"location_id": location_id, "inventory_item_id": inventory_item_id})
