from typing import Any, Dict, Optional

from .shopify_client import ShopifyClient, build_params


def list_locations(*, limit: Optional[int] = None, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/locations.json"""
    client = client or ShopifyClient()
    params = build_params(limit=limit)
    return client.request("GET", "/locations.json", params=params)


def count_locations(*, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/locations/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", "/locations/count.json")


def get_location(location_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/locations/{location_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/locations/{location_id}.json")


def list_location_inventory_levels(location_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/locations/{location_id}/inventory_levels.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/locations/{location_id}/inventory_levels.json")
