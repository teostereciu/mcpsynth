from typing import Any, Optional

from .client import ShopifyClient, clean_params


def list_locations(*, limit: Optional[int] = None, client: Optional[ShopifyClient] = None) -> Any:
    """GET /locations.json"""
    client = client or ShopifyClient()
    params = clean_params({"limit": limit})
    return client.request("GET", "/locations.json", params=params)


def get_location(location_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """GET /locations/{location_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/locations/{location_id}.json")


def count_locations(*, client: Optional[ShopifyClient] = None) -> Any:
    """GET /locations/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", "/locations/count.json")


def list_location_inventory_levels(location_id: int, *, limit: Optional[int] = None, client: Optional[ShopifyClient] = None) -> Any:
    """GET /locations/{location_id}/inventory_levels.json"""
    client = client or ShopifyClient()
    params = clean_params({"limit": limit})
    return client.request("GET", f"/locations/{location_id}/inventory_levels.json", params=params)
