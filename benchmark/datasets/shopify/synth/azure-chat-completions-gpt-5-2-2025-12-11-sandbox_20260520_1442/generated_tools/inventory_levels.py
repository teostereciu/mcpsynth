from typing import Any, Dict, Optional

from .client import ShopifyClient


def adjust_inventory_level(
    location_id: int,
    inventory_item_id: int,
    available_adjustment: int,
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """POST /admin/api/2026-01/inventory_levels/adjust.json"""
    client = client or ShopifyClient()
    body = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available_adjustment": available_adjustment,
    }
    return client.request("POST", "/inventory_levels/adjust.json", json_body=body)


def connect_inventory_level(
    location_id: int,
    inventory_item_id: int,
    *,
    relocate_if_necessary: Optional[bool] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """POST /admin/api/2026-01/inventory_levels/connect.json"""
    client = client or ShopifyClient()
    body: Dict[str, Any] = {"location_id": location_id, "inventory_item_id": inventory_item_id}
    if relocate_if_necessary is not None:
        body["relocate_if_necessary"] = relocate_if_necessary
    return client.request("POST", "/inventory_levels/connect.json", json_body=body)


def set_inventory_level(
    location_id: int,
    inventory_item_id: int,
    available: int,
    *,
    disconnect_if_necessary: Optional[bool] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """POST /admin/api/2026-01/inventory_levels/set.json"""
    client = client or ShopifyClient()
    body: Dict[str, Any] = {"location_id": location_id, "inventory_item_id": inventory_item_id, "available": available}
    if disconnect_if_necessary is not None:
        body["disconnect_if_necessary"] = disconnect_if_necessary
    return client.request("POST", "/inventory_levels/set.json", json_body=body)


def list_inventory_levels(
    *,
    location_ids: Optional[str] = None,
    inventory_item_ids: Optional[str] = None,
    limit: Optional[int] = None,
    updated_at_min: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/inventory_levels.json"""
    client = client or ShopifyClient()
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


def delete_inventory_level(inventory_item_id: int, location_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/inventory_levels.json"""
    client = client or ShopifyClient()
    params = {"inventory_item_id": inventory_item_id, "location_id": location_id}
    return client.request("DELETE", "/inventory_levels.json", params=params)
