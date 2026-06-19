from typing import Any, Dict, Optional

from .client import ShopifyClient


def list_inventory_levels(*, client: Optional[ShopifyClient] = None, location_ids: Optional[str] = None, inventory_item_ids: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /inventory_levels.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    for k, v in {"location_ids": location_ids, "inventory_item_ids": inventory_item_ids, "limit": limit}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/inventory_levels.json", params=params or None)


def adjust_inventory_level(location_id: int, inventory_item_id: int, available_adjustment: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /inventory_levels/adjust.json"""
    client = client or ShopifyClient()
    body = {"location_id": location_id, "inventory_item_id": inventory_item_id, "available_adjustment": available_adjustment}
    return client.request("POST", "/inventory_levels/adjust.json", json=body)


def set_inventory_level(location_id: int, inventory_item_id: int, available: int, *, client: Optional[ShopifyClient] = None, disconnect_if_necessary: Optional[bool] = None) -> Dict[str, Any]:
    """POST /inventory_levels/set.json"""
    client = client or ShopifyClient()
    body: Dict[str, Any] = {"location_id": location_id, "inventory_item_id": inventory_item_id, "available": available}
    if disconnect_if_necessary is not None:
        body["disconnect_if_necessary"] = disconnect_if_necessary
    return client.request("POST", "/inventory_levels/set.json", json=body)


def connect_inventory_level(location_id: int, inventory_item_id: int, *, client: Optional[ShopifyClient] = None, relocate_if_necessary: Optional[bool] = None) -> Dict[str, Any]:
    """POST /inventory_levels/connect.json"""
    client = client or ShopifyClient()
    body: Dict[str, Any] = {"location_id": location_id, "inventory_item_id": inventory_item_id}
    if relocate_if_necessary is not None:
        body["relocate_if_necessary"] = relocate_if_necessary
    return client.request("POST", "/inventory_levels/connect.json", json=body)


def delete_inventory_level(location_id: int, inventory_item_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /inventory_levels.json?inventory_item_id=...&location_id=..."""
    client = client or ShopifyClient()
    params = {"location_id": location_id, "inventory_item_id": inventory_item_id}
    return client.request("DELETE", "/inventory_levels.json", params=params)
