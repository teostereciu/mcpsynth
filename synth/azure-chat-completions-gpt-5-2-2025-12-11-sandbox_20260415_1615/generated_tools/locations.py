from typing import Any, Dict, Optional

from .http_client import get_client


def locations_list(*, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /locations.json"""
    params = {"limit": limit} if limit is not None else None
    return get_client().request("GET", "/locations.json", params=params)


def locations_count() -> Dict[str, Any]:
    """GET /locations/count.json"""
    return get_client().request("GET", "/locations/count.json")


def location_get(location_id: int) -> Dict[str, Any]:
    """GET /locations/{location_id}.json"""
    return get_client().request("GET", f"/locations/{location_id}.json")


def location_inventory_levels(location_id: int, *, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /locations/{location_id}/inventory_levels.json"""
    params = {"limit": limit} if limit is not None else None
    return get_client().request("GET", f"/locations/{location_id}/inventory_levels.json", params=params)
