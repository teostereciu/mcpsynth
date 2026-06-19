from typing import Any, Dict, Optional

from .http import owm_get


def get_5day_forecast_by_coordinates(
    latitude: float,
    longitude: float,
    units: Optional[str] = None,
    language: Optional[str] = None,
    mode: Optional[str] = None,
    count: Optional[int] = None,
) -> Dict[str, Any]:
    """Get 5 day / 3 hour forecast by geographic coordinates.

    Endpoint: GET /data/2.5/forecast
    Docs: docs/api_5day_forecast.md
    """
    params: Dict[str, Any] = {"latitude": latitude, "longitude": longitude}
    if units:
        params["units"] = units
    if language:
        params["lang"] = language
    if mode:
        params["mode"] = mode
    if count is not None:
        params["cnt"] = count
    return owm_get("/data/2.5/forecast", params)


def get_5day_forecast_by_city_name(
    q: str,
    units: Optional[str] = None,
    language: Optional[str] = None,
    mode: Optional[str] = None,
    count: Optional[int] = None,
) -> Dict[str, Any]:
    """Get 5 day / 3 hour forecast by city name query (deprecated built-in geocoding, still supported).

    Endpoint: GET /data/2.5/forecast?q={q}
    Docs: docs/api_5day_forecast.md
    """
    params: Dict[str, Any] = {"q": q}
    if units:
        params["units"] = units
    if language:
        params["lang"] = language
    if mode:
        params["mode"] = mode
    if count is not None:
        params["cnt"] = count
    return owm_get("/data/2.5/forecast", params)


def get_5day_forecast_by_city_id(
    city_id: int,
    units: Optional[str] = None,
    language: Optional[str] = None,
    mode: Optional[str] = None,
    count: Optional[int] = None,
) -> Dict[str, Any]:
    """Get 5 day / 3 hour forecast by city ID (deprecated built-in geocoding, still supported).

    Endpoint: GET /data/2.5/forecast?id={id}
    Docs: docs/api_5day_forecast.md
    """
    params: Dict[str, Any] = {"id": city_id}
    if units:
        params["units"] = units
    if language:
        params["lang"] = language
    if mode:
        params["mode"] = mode
    if count is not None:
        params["cnt"] = count
    return owm_get("/data/2.5/forecast", params)


def get_5day_forecast_by_zip(
    zip_code: str,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    language: Optional[str] = None,
    mode: Optional[str] = None,
    count: Optional[int] = None,
) -> Dict[str, Any]:
    """Get 5 day / 3 hour forecast by zip/post code (deprecated built-in geocoding, still supported).

    Endpoint: GET /data/2.5/forecast?zip={zip}
    Docs: docs/api_5day_forecast.md
    """
    z = zip_code if country_code is None else f"{zip_code},{country_code}"
    params: Dict[str, Any] = {"zip": z}
    if units:
        params["units"] = units
    if language:
        params["lang"] = language
    if mode:
        params["mode"] = mode
    if count is not None:
        params["cnt"] = count
    return owm_get("/data/2.5/forecast", params)
