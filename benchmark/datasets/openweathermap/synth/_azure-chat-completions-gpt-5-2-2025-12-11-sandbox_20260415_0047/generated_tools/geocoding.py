"""Tools for OpenWeatherMap Geocoding API (direct, reverse, zip)."""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from .http import get_json


def geocode_direct(q: str, limit: int = 5) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """Direct geocoding: location name -> coordinates.

    Endpoint: /geo/1.0/direct

    Args:
        q: City name query, e.g. "San Francisco,US".
        limit: Max results (docs say up to 5).

    Returns:
        List of locations, or {"error": ...}.
    """
    params: Dict[str, Any] = {"q": q, "limit": limit}
    return get_json("/geo/1.0/direct", params=params)  # type: ignore[return-value]


def geocode_reverse(lat: float, lon: float, limit: int = 5) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """Reverse geocoding: coordinates -> nearby location names.

    Endpoint: /geo/1.0/reverse
    """
    params: Dict[str, Any] = {"lat": lat, "lon": lon, "limit": limit}
    return get_json("/geo/1.0/reverse", params=params)  # type: ignore[return-value]


def geocode_zip(zip_code: str, country_code: str) -> Dict[str, Any]:
    """Geocode by ZIP/postal code.

    Endpoint: /geo/1.0/zip

    Args:
        zip_code: ZIP/postal code.
        country_code: ISO 3166 country code.
    """
    params: Dict[str, Any] = {"zip": f"{zip_code},{country_code}"}
    return get_json("/geo/1.0/zip", params=params)
