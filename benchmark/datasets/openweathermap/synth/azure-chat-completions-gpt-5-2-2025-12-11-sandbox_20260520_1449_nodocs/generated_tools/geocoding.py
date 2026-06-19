from typing import Any, Dict, Optional

from .client import request_json


def geocode_direct(
    q: str,
    *,
    limit: int = 5,
) -> Dict[str, Any]:
    """Direct geocoding: name -> coordinates.

    Endpoint: GET /geo/1.0/direct
    """
    return request_json("/geo/1.0/direct", {"q": q, "limit": limit})


def geocode_reverse(
    lat: float,
    lon: float,
    *,
    limit: int = 5,
) -> Dict[str, Any]:
    """Reverse geocoding: coordinates -> place names.

    Endpoint: GET /geo/1.0/reverse
    """
    return request_json("/geo/1.0/reverse", {"lat": lat, "lon": lon, "limit": limit})
