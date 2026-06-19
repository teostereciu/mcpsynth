from typing import Any, Dict, Optional

from .http import request_json


def list_locations(*, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /locations.json"""
    params = {"limit": limit} if limit is not None else None
    return request_json("GET", "/locations.json", params=params)


def get_location(location_id: int) -> Dict[str, Any]:
    """GET /locations/{location_id}.json"""
    return request_json("GET", f"/locations/{location_id}.json")


def count_locations() -> Dict[str, Any]:
    """GET /locations/count.json"""
    return request_json("GET", "/locations/count.json")


def list_location_inventory_levels(location_id: int) -> Dict[str, Any]:
    """GET /locations/{location_id}/inventory_levels.json"""
    return request_json("GET", f"/locations/{location_id}/inventory_levels.json")
