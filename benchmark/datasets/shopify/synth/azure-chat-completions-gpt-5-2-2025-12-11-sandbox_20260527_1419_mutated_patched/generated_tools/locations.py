from typing import Any, Dict, Optional

from .client import ShopifyClient


def list_locations(*, client: Optional[ShopifyClient] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /locations.json"""
    client = client or ShopifyClient()
    params = {"limit": limit} if limit is not None else None
    return client.request("GET", "/locations.json", params=params)


def count_locations(*, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /locations/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", "/locations/count.json")


def get_location(location_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /locations/{location_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/locations/{location_id}.json")


def get_location_inventory_levels(location_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /locations/{location_id}/inventory_levels.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/locations/{location_id}/inventory_levels.json")
