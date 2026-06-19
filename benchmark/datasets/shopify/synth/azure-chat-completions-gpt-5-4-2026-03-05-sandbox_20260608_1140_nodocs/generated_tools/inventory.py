from typing import Any, Dict, List, Optional

from generated_tools.common import clean_params, shopify_request


def list_inventory_items(ids: Optional[List[int]] = None, limit: Optional[int] = None) -> Any:
    params = clean_params(ids=",".join(str(x) for x in ids) if ids else None, limit=limit)
    return shopify_request("GET", "/inventory_items.json", params=params)


def get_inventory_item(inventory_item_id: int) -> Any:
    return shopify_request("GET", f"/inventory_items/{inventory_item_id}.json")


def update_inventory_item(inventory_item_id: int, inventory_item: Dict[str, Any]) -> Any:
    body = {"inventory_item": {"id": inventory_item_id, **inventory_item}}
    return shopify_request("PUT", f"/inventory_items/{inventory_item_id}.json", json_body=body)


def list_inventory_levels(inventory_item_ids: Optional[List[int]] = None, location_ids: Optional[List[int]] = None) -> Any:
    params = clean_params(
        inventory_item_ids=",".join(str(x) for x in inventory_item_ids) if inventory_item_ids else None,
        location_ids=",".join(str(x) for x in location_ids) if location_ids else None,
    )
    return shopify_request("GET", "/inventory_levels.json", params=params)


def adjust_inventory_level(location_id: int, inventory_item_id: int, available_adjustment: int) -> Any:
    body = {"location_id": location_id, "inventory_item_id": inventory_item_id, "available_adjustment": available_adjustment}
    return shopify_request("POST", "/inventory_levels/adjust.json", json_body=body)


def set_inventory_level(location_id: int, inventory_item_id: int, available: int, disconnect_if_necessary: Optional[bool] = None) -> Any:
    body = clean_params(location_id=location_id, inventory_item_id=inventory_item_id, available=available, disconnect_if_necessary=disconnect_if_necessary)
    return shopify_request("POST", "/inventory_levels/set.json", json_body=body)


def connect_inventory_level(location_id: int, inventory_item_id: int, relocate_if_necessary: Optional[bool] = None) -> Any:
    body = clean_params(location_id=location_id, inventory_item_id=inventory_item_id, relocate_if_necessary=relocate_if_necessary)
    return shopify_request("POST", "/inventory_levels/connect.json", json_body=body)


def list_locations(limit: Optional[int] = None) -> Any:
    params = clean_params(limit=limit)
    return shopify_request("GET", "/locations.json", params=params)
