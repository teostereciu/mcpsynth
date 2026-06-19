"""Tools for OpenWeatherMap Current Weather Data (API 2.5)."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import get_json


def current_weather_by_coordinates(
    lat: float,
    lon: float,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
) -> Dict[str, Any]:
    """Get current weather by geographic coordinates.

    Endpoint: /data/2.5/weather

    Args:
        lat: Latitude.
        lon: Longitude.
        units: standard|metric|imperial
        lang: Language code.
        mode: Response format (json default; xml/html supported by API).

    Returns:
        API response JSON as dict, or {"error": ...}.
    """
    params: Dict[str, Any] = {"lat": lat, "lon": lon}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if mode:
        params["mode"] = mode
    return get_json("/data/2.5/weather", params=params)


def current_weather_by_city_name(
    q: str,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
) -> Dict[str, Any]:
    """Get current weather by city name query.

    Endpoint: /data/2.5/weather

    Args:
        q: City name query, e.g. "New York,US" or "London,UK".
        units: standard|metric|imperial
        lang: Language code.
        mode: Response format.

    Returns:
        API response JSON as dict, or {"error": ...}.
    """
    params: Dict[str, Any] = {"q": q}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if mode:
        params["mode"] = mode
    return get_json("/data/2.5/weather", params=params)


def current_weather_by_city_id(
    city_id: int,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
) -> Dict[str, Any]:
    """Get current weather by OpenWeatherMap city ID.

    Endpoint: /data/2.5/weather
    """
    params: Dict[str, Any] = {"id": city_id}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if mode:
        params["mode"] = mode
    return get_json("/data/2.5/weather", params=params)


def current_weather_by_zip(
    zip_code: str,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
) -> Dict[str, Any]:
    """Get current weather by ZIP/postal code.

    Endpoint: /data/2.5/weather

    Args:
        zip_code: ZIP or postal code.
        country_code: Optional country code (e.g. "US").
    """
    zip_param = f"{zip_code},{country_code}" if country_code else zip_code
    params: Dict[str, Any] = {"zip": zip_param}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if mode:
        params["mode"] = mode
    return get_json("/data/2.5/weather", params=params)
