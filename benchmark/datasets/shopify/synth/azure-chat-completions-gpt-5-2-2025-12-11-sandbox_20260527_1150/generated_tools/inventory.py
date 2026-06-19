from typing import Any, Dict, Optional

from .http_client import ShopifyAdminClient


def list_inventory_levels(
    *,
    api_version: str = "2026-01",
    inventory_item_ids: Optional[str] = None,
    location_ids: Optional[str] = None,
    limit: Optional[int] = None,
    updated_at_min: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/inventory_levels.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {}
    for k, v in {
        "inventory_item_ids": inventory_item_ids,
        "location_ids": location_ids,
        "limit": limit,
        "updated_at_min": updated_at_min,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/inventory_levels.json", params=params or None)


def adjust_inventory_level(location_id: int, inventory_item_id: int, available_adjustment: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/inventory_levels/adjust.json"""
    client = ShopifyAdminClient(api_version=api_version)
    body = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available_adjustment": available_adjustment,
    }
    return client.request("POST", "/inventory_levels/adjust.json", json_body=body)


def set_inventory_level(
    location_id: int,
    inventory_item_id: int,
    available: int,
    *,
    api_version: str = "2026-01",
    disconnect_if_necessary: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /admin/api/2026-01/inventory_levels/set.json"""
    client = ShopifyAdminClient(api_version=api_version)
    body: Dict[str, Any] = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available": available,
    }
    if disconnect_if_necessary is not None:
        body["disconnect_if_necessary"] = disconnect_if_necessary
    return client.request("POST", "/inventory_levels/set.json", json_body=body)


def connect_inventory_item(
    location_id: int,
    inventory_item_id: int,
    *,
    api_version: str = "2026-01",
    relocate_if_necessary: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /admin/api/2026-01/inventory_levels/connect.json"""
    client = ShopifyAdminClient(api_version=api_version)
    body: Dict[str, Any] = {"location_id": location_id, "inventory_item_id": inventory_item_id}
    if relocate_if_necessary is not None:
        body["relocate_if_necessary"] = relocate_if_necessary
    return client.request("POST", "/inventory_levels/connect.json", json_body=body)


def delete_inventory_level(location_id: int, inventory_item_id: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/inventory_levels.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params = {"location_id": location_id, "inventory_item_id": inventory_item_id}
    return client.request("DELETE", "/inventory_levels.json", params=params)


def list_locations(*, api_version: str = "2026-01", limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/locations.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params = {"limit": limit} if limit is not None else None
    return client.request("GET", "/locations.json", params=params)


def get_location(location_id: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """GET /admin/api/2026-01/locations/{location_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("GET", f"/locations/{location_id}.json")


def count_locations(*, api_version: str = "2026-01") -> Dict[str, Any]:
    """GET /admin/api/2026-01/locations/count.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("GET", "/locations/count.json")


def list_location_inventory_levels(
    location_id: int,
    *,
    api_version: str = "2026-01",
    limit: Optional[int] = None,
    updated_at_min: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/locations/{location_id}/inventory_levels.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "updated_at_min": updated_at_min}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", f"/locations/{location_id}/inventory_levels.json", params=params or None)
