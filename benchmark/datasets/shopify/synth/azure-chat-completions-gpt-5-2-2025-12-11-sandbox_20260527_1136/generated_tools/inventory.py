from typing import Any, Dict, Optional

from .http_client import ShopifyClient


# Inventory items

def list_inventory_items(ids: str, *, client: Optional[ShopifyClient] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /inventory_items.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {"ids": ids}
    if limit is not None:
        params["limit"] = limit
    return client.request("GET", "/inventory_items.json", params=params)


def get_inventory_item(inventory_item_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /inventory_items/{inventory_item_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/inventory_items/{inventory_item_id}.json")


def update_inventory_item(inventory_item_id: int, inventory_item: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /inventory_items/{inventory_item_id}.json"""
    client = client or ShopifyClient()
    body = {"inventory_item": {**inventory_item, "id": inventory_item_id}}
    return client.request("PUT", f"/inventory_items/{inventory_item_id}.json", json_body=body)


# Inventory levels

def list_inventory_levels(
    *,
    client: Optional[ShopifyClient] = None,
    location_ids: Optional[str] = None,
    inventory_item_ids: Optional[str] = None,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
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
    return client.request("POST", "/inventory_levels/adjust.json", json_body=body)


def connect_inventory_level(
    location_id: int,
    inventory_item_id: int,
    *,
    client: Optional[ShopifyClient] = None,
    relocate_if_necessary: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /inventory_levels/connect.json"""
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
    client: Optional[ShopifyClient] = None,
    disconnect_if_necessary: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /inventory_levels/set.json"""
    client = client or ShopifyClient()
    body: Dict[str, Any] = {"location_id": location_id, "inventory_item_id": inventory_item_id, "available": available}
    if disconnect_if_necessary is not None:
        body["disconnect_if_necessary"] = disconnect_if_necessary
    return client.request("POST", "/inventory_levels/set.json", json_body=body)


def delete_inventory_level(location_id: int, inventory_item_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /inventory_levels.json"""
    client = client or ShopifyClient()
    params = {"location_id": location_id, "inventory_item_id": inventory_item_id}
    return client.request("DELETE", "/inventory_levels.json", params=params)


# Locations

def list_locations(*, client: Optional[ShopifyClient] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /locations.json"""
    client = client or ShopifyClient()
    params = {"limit": limit} if limit is not None else None
    return client.request("GET", "/locations.json", params=params)


def get_location(location_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /locations/{location_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/locations/{location_id}.json")


def count_locations(*, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /locations/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", "/locations/count.json")


def list_location_inventory_levels(location_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /locations/{location_id}/inventory_levels.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/locations/{location_id}/inventory_levels.json")
