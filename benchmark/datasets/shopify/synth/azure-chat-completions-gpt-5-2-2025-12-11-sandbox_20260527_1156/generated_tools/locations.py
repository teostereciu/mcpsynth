from typing import Any, Dict, Optional

from ._client import get_client


def list_locations(*, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /locations.json

    Doc: docs/api_location.md
    """
    client = get_client()
    params = {"limit": limit} if limit is not None else None
    return client.request("GET", "/locations.json", params=params)


def get_location(location_id: int) -> Dict[str, Any]:
    """GET /locations/{location_id}.json

    Doc: docs/api_location.md
    """
    client = get_client()
    return client.request("GET", f"/locations/{location_id}.json")


def count_locations() -> Dict[str, Any]:
    """GET /locations/count.json

    Doc: docs/api_location.md
    """
    client = get_client()
    return client.request("GET", "/locations/count.json")


def list_location_inventory_levels(location_id: int) -> Dict[str, Any]:
    """GET /locations/{location_id}/inventory_levels.json

    Doc: docs/api_location.md
    """
    client = get_client()
    return client.request("GET", f"/locations/{location_id}/inventory_levels.json")
