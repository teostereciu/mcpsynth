from typing import Any, Dict, Optional

from .client import OpenWeatherClient, _clean_none, _coerce_lang, _coerce_units


def get_current_weather_by_city(
    client: OpenWeatherClient,
    city_name: str,
    state_code: Optional[str] = None,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    """Current weather by city name.

    OpenWeather endpoint: GET /data/2.5/weather?q={city},{state},{country}
    """
    q = city_name
    if state_code:
        q += f",{state_code}"
    if country_code:
        q += f",{country_code}"

    params = _clean_none({"q": q, "units": _coerce_units(units), "lang": _coerce_lang(lang)})
    return client._request("/data/2.5/weather", params=params)


def get_current_weather_by_coordinates(
    client: OpenWeatherClient,
    lat: float,
    lon: float,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    """Current weather by geographic coordinates.

    Endpoint: GET /data/2.5/weather?lat={lat}&lon={lon}
    """
    params = _clean_none({"lat": lat, "lon": lon, "units": _coerce_units(units), "lang": _coerce_lang(lang)})
    return client._request("/data/2.5/weather", params=params)


def get_current_weather_by_city_id(
    client: OpenWeatherClient,
    city_id: int,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    """Current weather by OpenWeather city ID.

    Endpoint: GET /data/2.5/weather?id={id}
    """
    params = _clean_none({"id": city_id, "units": _coerce_units(units), "lang": _coerce_lang(lang)})
    return client._request("/data/2.5/weather", params=params)


def get_current_weather_by_zip(
    client: OpenWeatherClient,
    zip_code: str,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    """Current weather by ZIP/postal code.

    Endpoint: GET /data/2.5/weather?zip={zip},{country}
    """
    z = zip_code
    if country_code:
        z += f",{country_code}"
    params = _clean_none({"zip": z, "units": _coerce_units(units), "lang": _coerce_lang(lang)})
    return client._request("/data/2.5/weather", params=params)


def get_current_weather_by_bbox(
    client: OpenWeatherClient,
    lon_left: float,
    lat_bottom: float,
    lon_right: float,
    lat_top: float,
    zoom: int = 10,
    cluster: Optional[bool] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    """Current weather for cities within a bounding box.

    Endpoint: GET /data/2.5/box/city?bbox=lon-left,lat-bottom,lon-right,lat-top,zoom
    """
    bbox = f"{lon_left},{lat_bottom},{lon_right},{lat_top},{zoom}"
    params = _clean_none(
        {
            "bbox": bbox,
            "cluster": "yes" if cluster else None,
            "units": _coerce_units(units),
            "lang": _coerce_lang(lang),
        }
    )
    return client._request("/data/2.5/box/city", params=params)
