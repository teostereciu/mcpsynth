from typing import Any, Dict, Optional

from .http_client import ShopifyClient


def locations_list(*, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/locations.json"""
    client = ShopifyClient()
    params = {"limit": limit} if limit is not None else None
    return client.request("GET", "/locations.json", params=params)


def locations_count() -> Dict[str, Any]:
    """GET /admin/api/2026-01/locations/count.json"""
    client = ShopifyClient()
    return client.request("GET", "/locations/count.json")


def location_get(location_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/locations/{location_id}.json"""
    client = ShopifyClient()
    return client.request("GET", f"/locations/{location_id}.json")


def location_inventory_levels(location_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/locations/{location_id}/inventory_levels.json"""
    client = ShopifyClient()
    return client.request("GET", f"/locations/{location_id}/inventory_levels.json")
