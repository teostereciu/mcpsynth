from typing import Any, Dict, Optional

from .http_client import OpenWeatherClient


def get_current_weather_by_coords(
    lat: float,
    lon: float,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """GET /data/2.5/weather (by lat/lon)"""
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"lat": float(lat), "lon": float(lon)}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if mode:
        params["mode"] = mode
    return client.get("/data/2.5/weather", params)


def get_current_weather_by_city_name(
    q: str,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """GET /data/2.5/weather (by city name query)

    Note: built-in geocoder is deprecated by OpenWeather, but still available.
    Prefer using Geocoding API + coords.
    """
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"q": q}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if mode:
        params["mode"] = mode
    return client.get("/data/2.5/weather", params)
