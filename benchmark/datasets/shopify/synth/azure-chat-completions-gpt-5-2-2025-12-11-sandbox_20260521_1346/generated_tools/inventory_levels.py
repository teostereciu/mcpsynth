from typing import Any, Dict, Optional

from .client import ShopifyClient, clean_params


def list_inventory_levels(
    *,
    location_ids: Optional[str] = None,
    inventory_item_ids: Optional[str] = None,
    limit: Optional[int] = None,
    updated_at_min: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Any:
    """GET /inventory_levels.json"""
    client = client or ShopifyClient()
    params = clean_params(
        {
            "location_ids": location_ids,
            "inventory_item_ids": inventory_item_ids,
            "limit": limit,
            "updated_at_min": updated_at_min,
        }
    )
    return client.request("GET", "/inventory_levels.json", params=params)


def adjust_inventory_level(location_id: int, inventory_item_id: int, available_adjustment: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """POST /inventory_levels/adjust.json"""
    client = client or ShopifyClient()
    body = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available_adjustment": available_adjustment,
    }
    return client.request("POST", "/inventory_levels/adjust.json", json=body)


def set_inventory_level(
    location_id: int,
    inventory_item_id: int,
    available: int,
    *,
    disconnect_if_necessary: Optional[bool] = None,
    client: Optional[ShopifyClient] = None,
) -> Any:
    """POST /inventory_levels/set.json"""
    client = client or ShopifyClient()
    body = clean_params(
        {
            "location_id": location_id,
            "inventory_item_id": inventory_item_id,
            "available": available,
            "disconnect_if_necessary": disconnect_if_necessary,
        }
    )
    return client.request("POST", "/inventory_levels/set.json", json=body)


def connect_inventory_level(
    location_id: int,
    inventory_item_id: int,
    *,
    relocate_if_necessary: Optional[bool] = None,
    client: Optional[ShopifyClient] = None,
) -> Any:
    """POST /inventory_levels/connect.json"""
    client = client or ShopifyClient()
    body = clean_params(
        {
            "location_id": location_id,
            "inventory_item_id": inventory_item_id,
            "relocate_if_necessary": relocate_if_necessary,
        }
    )
    return client.request("POST", "/inventory_levels/connect.json", json=body)


def delete_inventory_level(location_id: int, inventory_item_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """DELETE /inventory_levels.json"""
    client = client or ShopifyClient()
    params = {"location_id": location_id, "inventory_item_id": inventory_item_id}
    return client.request("DELETE", "/inventory_levels.json", params=params)
