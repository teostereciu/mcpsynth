from typing import Any, Dict, Optional

from .client import shopify_request


def list_locations(*, limit: Optional[int] = None) -> Any:
    """GET /locations.json"""
    params = {"limit": limit} if limit is not None else None
    return shopify_request("GET", "/locations.json", params=params)


def get_location(location_id: int) -> Any:
    """GET /locations/{location_id}.json"""
    return shopify_request("GET", f"/locations/{location_id}.json")


def count_locations() -> Any:
    """GET /locations/count.json"""
    return shopify_request("GET", "/locations/count.json")


def get_location_inventory_levels(location_id: int) -> Any:
    """GET /locations/{location_id}/inventory_levels.json"""
    return shopify_request("GET", f"/locations/{location_id}/inventory_levels.json")
