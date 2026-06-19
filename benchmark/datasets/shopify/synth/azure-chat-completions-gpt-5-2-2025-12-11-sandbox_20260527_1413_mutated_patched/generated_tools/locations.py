from typing import Any, Dict, Optional

from .client import request_json


def list_locations(*, limit: Optional[int] = None) -> Any:
    """GET /locations.json"""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    return request_json("GET", "/locations.json", params=params)


def get_location(location_id: int) -> Any:
    """GET /locations/{location_id}.json"""
    return request_json("GET", f"/locations/{location_id}.json")


def list_location_inventory_levels(location_id: int) -> Any:
    """GET /locations/{location_id}/inventory_levels.json"""
    return request_json("GET", f"/locations/{location_id}/inventory_levels.json")


def count_locations() -> Any:
    """GET /locations/count.json"""
    return request_json("GET", "/locations/count.json")
