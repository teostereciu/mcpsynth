from typing import Any, Dict, Optional

from .client import request_json


def locations_list(*, limit: Optional[int] = None) -> Any:
    """GET /locations.json"""
    params = {"limit": limit} if limit is not None else None
    return request_json("GET", "/locations.json", params=params)


def location_get(location_id: int) -> Any:
    """GET /locations/{location_id}.json"""
    return request_json("GET", f"/locations/{location_id}.json")


def locations_count() -> Any:
    """GET /locations/count.json"""
    return request_json("GET", "/locations/count.json")


def location_inventory_levels(location_id: int, *, limit: Optional[int] = None) -> Any:
    """GET /locations/{location_id}/inventory_levels.json"""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    return request_json("GET", f"/locations/{location_id}/inventory_levels.json", params=params or None)
