from typing import Any, Dict, Optional

from .http import owm_get


def get_current_weather_by_coordinates(
    latitude: float,
    longitude: float,
    units: Optional[str] = None,
    language: Optional[str] = None,
    mode: Optional[str] = None,
) -> Dict[str, Any]:
    """Get current weather by geographic coordinates.

    Endpoint: GET /data/2.5/weather
    Docs: docs/api_current_weather.md

    Notes:
      - Docs use parameter names latitude/longitude; OpenWeatherMap also accepts lat/lon.
    """
    params: Dict[str, Any] = {"latitude": latitude, "longitude": longitude}
    if units:
        params["units"] = units
    if language:
        params["language"] = language
    if mode:
        params["mode"] = mode
    return owm_get("/data/2.5/weather", params)


def get_current_weather_by_city_name(
    q: str,
    units: Optional[str] = None,
    language: Optional[str] = None,
    mode: Optional[str] = None,
) -> Dict[str, Any]:
    """Get current weather by city name query (deprecated built-in geocoding, still supported).

    Endpoint: GET /data/2.5/weather?q={q}
    Docs: docs/api_current_weather.md
    """
    params: Dict[str, Any] = {"q": q}
    if units:
        params["units"] = units
    if language:
        params["language"] = language
    if mode:
        params["mode"] = mode
    return owm_get("/data/2.5/weather", params)


def get_current_weather_by_city_id(
    city_id: int,
    units: Optional[str] = None,
    language: Optional[str] = None,
    mode: Optional[str] = None,
) -> Dict[str, Any]:
    """Get current weather by OpenWeatherMap city ID (deprecated built-in geocoding, still supported).

    Endpoint: GET /data/2.5/weather?id={id}
    Docs: docs/api_current_weather.md
    """
    params: Dict[str, Any] = {"id": city_id}
    if units:
        params["units"] = units
    if language:
        params["language"] = language
    if mode:
        params["mode"] = mode
    return owm_get("/data/2.5/weather", params)


def get_current_weather_by_zip(
    zip_code: str,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    language: Optional[str] = None,
    mode: Optional[str] = None,
) -> Dict[str, Any]:
    """Get current weather by zip/post code (deprecated built-in geocoding, still supported).

    Endpoint: GET /data/2.5/weather?zip={zip}
    Docs: docs/api_current_weather.md
    """
    z = zip_code if country_code is None else f"{zip_code},{country_code}"
    params: Dict[str, Any] = {"zip": z}
    if units:
        params["units"] = units
    if language:
        params["language"] = language
    if mode:
        params["mode"] = mode
    return owm_get("/data/2.5/weather", params)
