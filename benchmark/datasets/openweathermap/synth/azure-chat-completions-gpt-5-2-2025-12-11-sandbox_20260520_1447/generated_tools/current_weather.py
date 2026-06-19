from typing import Any, Dict, Optional

from .http_client import OpenWeatherClient


def get_current_weather_by_coords(
    lat: float,
    lon: float,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    *,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Get current weather by geographic coordinates.

    Endpoint: GET /data/2.5/weather
    Docs: docs/api_current_weather.md
    """
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"lat": lat, "lon": lon}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if mode:
        params["mode"] = mode
    return client._request("/data/2.5/weather", params=params)


def get_current_weather_by_city_name(
    city: str,
    country_code: Optional[str] = None,
    state_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    *,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Get current weather by city name (built-in geocoding; deprecated by OpenWeather but still supported).

    Endpoint: GET /data/2.5/weather?q=...
    Docs: docs/api_current_weather.md
    """
    client = client or OpenWeatherClient()
    q = city
    if state_code and country_code:
        q = f"{city},{state_code},{country_code}"
    elif country_code:
        q = f"{city},{country_code}"

    params: Dict[str, Any] = {"q": q}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if mode:
        params["mode"] = mode
    return client._request("/data/2.5/weather", params=params)


def get_current_weather_by_city_id(
    city_id: int,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    *,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Get current weather by OpenWeather city ID (deprecated by OpenWeather but still supported).

    Endpoint: GET /data/2.5/weather?id=...
    Docs: docs/api_current_weather.md
    """
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"id": city_id}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if mode:
        params["mode"] = mode
    return client._request("/data/2.5/weather", params=params)


def get_current_weather_by_zip(
    zip_code: str,
    country_code: str,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    *,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Get current weather by zip/post code (deprecated by OpenWeather but still supported).

    Endpoint: GET /data/2.5/weather?zip=...
    Docs: docs/api_current_weather.md
    """
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"zip": f"{zip_code},{country_code}"}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if mode:
        params["mode"] = mode
    return client._request("/data/2.5/weather", params=params)
