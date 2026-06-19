from typing import Any, Dict

from .http import shopify_request


def list_locations() -> Dict[str, Any]:
    """GET /locations.json"""
    return shopify_request("GET", "/locations.json")


def get_location(location_id: int) -> Dict[str, Any]:
    """GET /locations/{location_id}.json"""
    return shopify_request("GET", f"/locations/{location_id}.json")


def count_locations() -> Dict[str, Any]:
    """GET /locations/count.json"""
    return shopify_request("GET", "/locations/count.json")


def location_inventory_levels(location_id: int) -> Dict[str, Any]:
    """GET /locations/{location_id}/inventory_levels.json"""
    return shopify_request("GET", f"/locations/{location_id}/inventory_levels.json")
