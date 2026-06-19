from typing import Any, Dict, Optional

from shopify_client import ShopifyClient


def list_inventory_items(*, limit: Optional[int] = 50, ids: Optional[str] = None) -> Dict[str, Any]:
    """GET /inventory_items.json"""
    c = ShopifyClient()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if ids is not None:
        params["ids"] = ids
    return c.request("GET", "/inventory_items.json", params=params)


def get_inventory_item(*, inventory_item_id: int) -> Dict[str, Any]:
    """GET /inventory_items/{inventory_item_id}.json"""
    c = ShopifyClient()
    return c.request("GET", f"/inventory_items/{inventory_item_id}.json")


def update_inventory_item(*, inventory_item_id: int, inventory_item: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /inventory_items/{inventory_item_id}.json"""
    c = ShopifyClient()
    body = {"inventory_item": {**inventory_item, "id": inventory_item_id}}
    return c.request("PUT", f"/inventory_items/{inventory_item_id}.json", json=body)


def list_inventory_levels(*, inventory_item_ids: Optional[str] = None, location_ids: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /inventory_levels.json"""
    c = ShopifyClient()
    params: Dict[str, Any] = {}
    if inventory_item_ids is not None:
        params["inventory_item_ids"] = inventory_item_ids
    if location_ids is not None:
        params["location_ids"] = location_ids
    if limit is not None:
        params["limit"] = limit
    return c.request("GET", "/inventory_levels.json", params=params)


def adjust_inventory_level(*, inventory_item_id: int, location_id: int, available_adjustment: int) -> Dict[str, Any]:
    """POST /inventory_levels/adjust.json"""
    c = ShopifyClient()
    return c.request(
        "POST",
        "/inventory_levels/adjust.json",
        json={
            "inventory_item_id": inventory_item_id,
            "location_id": location_id,
            "available_adjustment": available_adjustment,
        },
    )


def set_inventory_level(*, inventory_item_id: int, location_id: int, available: int, disconnect_if_necessary: Optional[bool] = None) -> Dict[str, Any]:
    """POST /inventory_levels/set.json"""
    c = ShopifyClient()
    payload: Dict[str, Any] = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "available": available,
    }
    if disconnect_if_necessary is not None:
        payload["disconnect_if_necessary"] = disconnect_if_necessary
    return c.request("POST", "/inventory_levels/set.json", json=payload)


def connect_inventory_level(*, inventory_item_id: int, location_id: int, relocate_if_necessary: Optional[bool] = None) -> Dict[str, Any]:
    """POST /inventory_levels/connect.json"""
    c = ShopifyClient()
    payload: Dict[str, Any] = {"inventory_item_id": inventory_item_id, "location_id": location_id}
    if relocate_if_necessary is not None:
        payload["relocate_if_necessary"] = relocate_if_necessary
    return c.request("POST", "/inventory_levels/connect.json", json=payload)
