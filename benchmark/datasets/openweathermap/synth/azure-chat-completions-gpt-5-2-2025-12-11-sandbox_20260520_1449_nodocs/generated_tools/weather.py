from typing import Any, Dict, Optional

from .client import request_json


def get_current_weather_by_city(
    city: str,
    *,
    state_code: Optional[str] = None,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    """Current weather by city name.

    Endpoint: GET /data/2.5/weather (q)
    """
    q = city
    if state_code:
        q += f",{state_code}"
    if country_code:
        q += f",{country_code}"
    return request_json(
        "/data/2.5/weather",
        {"q": q, "units": units, "lang": lang},
    )


def get_current_weather_by_coords(
    lat: float,
    lon: float,
    *,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    """Current weather by coordinates.

    Endpoint: GET /data/2.5/weather (lat,lon)
    """
    return request_json(
        "/data/2.5/weather",
        {"lat": lat, "lon": lon, "units": units, "lang": lang},
    )


def get_current_weather_by_zip(
    zip_code: str,
    *,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    """Current weather by ZIP/postal code.

    Endpoint: GET /data/2.5/weather (zip)
    """
    z = zip_code if not country_code else f"{zip_code},{country_code}"
    return request_json(
        "/data/2.5/weather",
        {"zip": z, "units": units, "lang": lang},
    )


def get_current_weather_by_city_id(
    city_id: int,
    *,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    """Current weather by OpenWeather city ID.

    Endpoint: GET /data/2.5/weather (id)
    """
    return request_json(
        "/data/2.5/weather",
        {"id": city_id, "units": units, "lang": lang},
    )


def get_5day_forecast_by_city(
    city: str,
    *,
    state_code: Optional[str] = None,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    """5 day / 3 hour forecast by city name.

    Endpoint: GET /data/2.5/forecast (q)
    """
    q = city
    if state_code:
        q += f",{state_code}"
    if country_code:
        q += f",{country_code}"
    return request_json(
        "/data/2.5/forecast",
        {"q": q, "units": units, "lang": lang},
    )


def get_5day_forecast_by_coords(
    lat: float,
    lon: float,
    *,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    """5 day / 3 hour forecast by coordinates.

    Endpoint: GET /data/2.5/forecast (lat,lon)
    """
    return request_json(
        "/data/2.5/forecast",
        {"lat": lat, "lon": lon, "units": units, "lang": lang},
    )


def get_5day_forecast_by_zip(
    zip_code: str,
    *,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    """5 day / 3 hour forecast by ZIP/postal code.

    Endpoint: GET /data/2.5/forecast (zip)
    """
    z = zip_code if not country_code else f"{zip_code},{country_code}"
    return request_json(
        "/data/2.5/forecast",
        {"zip": z, "units": units, "lang": lang},
    )


def get_5day_forecast_by_city_id(
    city_id: int,
    *,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    """5 day / 3 hour forecast by OpenWeather city ID.

    Endpoint: GET /data/2.5/forecast (id)
    """
    return request_json(
        "/data/2.5/forecast",
        {"id": city_id, "units": units, "lang": lang},
    )
