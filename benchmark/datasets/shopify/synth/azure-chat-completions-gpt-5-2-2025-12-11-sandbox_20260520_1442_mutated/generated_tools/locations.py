from typing import Any, Dict, Optional

from .http_client import request_json


def list_locations(*, count: Optional[int] = None) -> Dict[str, Any]:
    """GET /locations.json

    Doc: docs/api_location.md
    """
    params: Dict[str, Any] = {}
    if count is not None:
        params["count"] = count
    return request_json("GET", "/locations.json", params=params)


def get_location(location_id: int) -> Dict[str, Any]:
    """GET /locations/{location_id}.json

    Doc: docs/api_location.md
    """
    return request_json("GET", f"/locations/{location_id}.json")


def count_locations() -> Dict[str, Any]:
    """GET /locations/count.json

    Doc: docs/api_location.md
    """
    return request_json("GET", "/locations/count.json")


def list_location_inventory_levels(location_id: int) -> Dict[str, Any]:
    """GET /locations/{location_id}/inventory_levels.json

    Doc: docs/api_location.md
    """
    return request_json("GET", f"/locations/{location_id}/inventory_levels.json")
