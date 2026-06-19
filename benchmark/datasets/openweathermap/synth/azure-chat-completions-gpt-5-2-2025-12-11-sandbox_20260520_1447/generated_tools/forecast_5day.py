from typing import Any, Dict, Optional

from .http_client import OpenWeatherClient


def get_5day_forecast_by_coords(
    lat: float,
    lon: float,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    cnt: Optional[int] = None,
    *,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Get 5 day / 3 hour forecast by geographic coordinates.

    Endpoint: GET /data/2.5/forecast
    Docs: docs/api_5day_forecast.md
    """
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"lat": lat, "lon": lon}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if mode:
        params["mode"] = mode
    if cnt is not None:
        params["cnt"] = cnt
    return client._request("/data/2.5/forecast", params=params)


def get_5day_forecast_by_city_name(
    city: str,
    country_code: Optional[str] = None,
    state_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    cnt: Optional[int] = None,
    *,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Get 5 day / 3 hour forecast by city name (built-in geocoding; deprecated by OpenWeather but still supported).

    Endpoint: GET /data/2.5/forecast?q=...
    Docs: docs/api_5day_forecast.md
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
    if cnt is not None:
        params["cnt"] = cnt
    return client._request("/data/2.5/forecast", params=params)


def get_5day_forecast_by_city_id(
    city_id: int,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    cnt: Optional[int] = None,
    *,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Get 5 day / 3 hour forecast by OpenWeather city ID (deprecated by OpenWeather but still supported).

    Endpoint: GET /data/2.5/forecast?id=...
    Docs: docs/api_5day_forecast.md
    """
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"id": city_id}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if mode:
        params["mode"] = mode
    if cnt is not None:
        params["cnt"] = cnt
    return client._request("/data/2.5/forecast", params=params)


def get_5day_forecast_by_zip(
    zip_code: str,
    country_code: str,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    cnt: Optional[int] = None,
    *,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Get 5 day / 3 hour forecast by zip/post code (deprecated by OpenWeather but still supported).

    Endpoint: GET /data/2.5/forecast?zip=...
    Docs: docs/api_5day_forecast.md
    """
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"zip": f"{zip_code},{country_code}"}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if mode:
        params["mode"] = mode
    if cnt is not None:
        params["cnt"] = cnt
    return client._request("/data/2.5/forecast", params=params)
