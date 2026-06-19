"""Tools for OpenWeatherMap 5 day / 3 hour forecast (API 2.5)."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import get_json


def forecast_5day_by_coordinates(
    lat: float,
    lon: float,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
    mode: Optional[str] = None,
) -> Dict[str, Any]:
    """Get 5 day / 3 hour forecast by coordinates.

    Endpoint: /data/2.5/forecast

    Args:
        lat: Latitude.
        lon: Longitude.
        units: standard|metric|imperial
        lang: Language code.
        cnt: Number of timestamps to return.
        mode: Response format (json default; xml supported by API).

    Returns:
        API response JSON as dict, or {"error": ...}.
    """
    params: Dict[str, Any] = {"lat": lat, "lon": lon}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if cnt is not None:
        params["cnt"] = cnt
    if mode:
        params["mode"] = mode
    return get_json("/data/2.5/forecast", params=params)


def forecast_5day_by_city_name(
    q: str,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
    mode: Optional[str] = None,
) -> Dict[str, Any]:
    """Get 5 day / 3 hour forecast by city name query.

    Endpoint: /data/2.5/forecast

    Args:
        q: City query, e.g. "Tokyo,JP".
    """
    params: Dict[str, Any] = {"q": q}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if cnt is not None:
        params["cnt"] = cnt
    if mode:
        params["mode"] = mode
    return get_json("/data/2.5/forecast", params=params)


def forecast_5day_by_city_id(
    city_id: int,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
    mode: Optional[str] = None,
) -> Dict[str, Any]:
    """Get 5 day / 3 hour forecast by OpenWeatherMap city ID."""
    params: Dict[str, Any] = {"id": city_id}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if cnt is not None:
        params["cnt"] = cnt
    if mode:
        params["mode"] = mode
    return get_json("/data/2.5/forecast", params=params)


def forecast_5day_by_zip(
    zip_code: str,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
    mode: Optional[str] = None,
) -> Dict[str, Any]:
    """Get 5 day / 3 hour forecast by ZIP/postal code."""
    zip_param = f"{zip_code},{country_code}" if country_code else zip_code
    params: Dict[str, Any] = {"zip": zip_param}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if cnt is not None:
        params["cnt"] = cnt
    if mode:
        params["mode"] = mode
    return get_json("/data/2.5/forecast", params=params)
