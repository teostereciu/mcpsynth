from typing import Any, Dict, Optional

from .http_client import OpenWeatherClient


def current_weather_by_coords(
    lat: float,
    lon: float,
    *,
    units: str = "standard",
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Get current weather by geographic coordinates.

    Endpoint: /data/2.5/weather
    Required: lat, lon
    Optional: units (standard|metric|imperial), lang, mode (xml|html)
    """
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"lat": lat, "lon": lon, "units": units}
    if lang:
        params["lang"] = lang
    if mode:
        params["mode"] = mode
    return client._request("/data/2.5/weather", params)


def current_weather_by_city_name(
    city: str,
    *,
    state_code: Optional[str] = None,
    country_code: Optional[str] = None,
    units: str = "standard",
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Get current weather by city name (deprecated by OpenWeather but still available).

    Endpoint: /data/2.5/weather
    Param q supports: city, city,country, city,state,country
    """
    client = client or OpenWeatherClient()
    parts = [city]
    if state_code:
        parts.append(state_code)
    if country_code:
        parts.append(country_code)
    q = ",".join(parts)
    params: Dict[str, Any] = {"q": q, "units": units}
    if lang:
        params["lang"] = lang
    if mode:
        params["mode"] = mode
    return client._request("/data/2.5/weather", params)


def current_weather_by_zip(
    zip_code: str,
    country_code: str,
    *,
    units: str = "standard",
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Get current weather by ZIP/postal code (deprecated by OpenWeather but still available).

    Endpoint: /data/2.5/weather
    Param zip: "{zip},{country}"
    """
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"zip": f"{zip_code},{country_code}", "units": units}
    if lang:
        params["lang"] = lang
    if mode:
        params["mode"] = mode
    return client._request("/data/2.5/weather", params)


def current_weather_by_city_id(
    city_id: int,
    *,
    units: str = "standard",
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Get current weather by city ID (deprecated by OpenWeather but still available).

    Endpoint: /data/2.5/weather
    Param id: city id
    """
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"id": city_id, "units": units}
    if lang:
        params["lang"] = lang
    if mode:
        params["mode"] = mode
    return client._request("/data/2.5/weather", params)
