from typing import Any, Dict, Optional

from .http_client import ShopifyClient


def inventory_items_list(ids: str, *, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/inventory_items.json?ids=..."""
    client = ShopifyClient()
    params: Dict[str, Any] = {"ids": ids}
    if limit is not None:
        params["limit"] = limit
    return client.request("GET", "/inventory_items.json", params=params)


def inventory_item_get(inventory_item_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/inventory_items/{inventory_item_id}.json"""
    client = ShopifyClient()
    return client.request("GET", f"/inventory_items/{inventory_item_id}.json")


def inventory_item_update(inventory_item_id: int, inventory_item: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/inventory_items/{inventory_item_id}.json"""
    client = ShopifyClient()
    body = {"inventory_item": {**inventory_item, "id": inventory_item_id}}
    return client.request(
        "PUT", f"/inventory_items/{inventory_item_id}.json", json_body=body
    )


def inventory_levels_list(
    *,
    location_ids: Optional[str] = None,
    inventory_item_ids: Optional[str] = None,
    limit: Optional[int] = None,
    updated_at_min: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/inventory_levels.json"""
    client = ShopifyClient()
    params: Dict[str, Any] = {}
    for k, v in {
        "location_ids": location_ids,
        "inventory_item_ids": inventory_item_ids,
        "limit": limit,
        "updated_at_min": updated_at_min,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/inventory_levels.json", params=params)


def inventory_levels_adjust(location_id: int, inventory_item_id: int, available_adjustment: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/inventory_levels/adjust.json"""
    client = ShopifyClient()
    body = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available_adjustment": available_adjustment,
    }
    return client.request("POST", "/inventory_levels/adjust.json", json_body=body)


def inventory_levels_set(
    location_id: int,
    inventory_item_id: int,
    available: int,
    *,
    disconnect_if_necessary: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /admin/api/2026-01/inventory_levels/set.json"""
    client = ShopifyClient()
    body: Dict[str, Any] = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available": available,
    }
    if disconnect_if_necessary is not None:
        body["disconnect_if_necessary"] = disconnect_if_necessary
    return client.request("POST", "/inventory_levels/set.json", json_body=body)


def inventory_levels_connect(
    location_id: int,
    inventory_item_id: int,
    *,
    relocate_if_necessary: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /admin/api/2026-01/inventory_levels/connect.json"""
    client = ShopifyClient()
    body: Dict[str, Any] = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
    }
    if relocate_if_necessary is not None:
        body["relocate_if_necessary"] = relocate_if_necessary
    return client.request("POST", "/inventory_levels/connect.json", json_body=body)


def inventory_levels_delete(inventory_item_id: int, location_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/inventory_levels.json?inventory_item_id=...&location_id=..."""
    client = ShopifyClient()
    params = {"inventory_item_id": inventory_item_id, "location_id": location_id}
    return client.request("DELETE", "/inventory_levels.json", params=params)
