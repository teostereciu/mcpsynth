from typing import Any, Dict, Optional

from generated_tools.geocoding import _request


def _weather_params(units: Optional[str] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    return {"units": units, "lang": lang}


def get_current_weather_by_coordinates(latitude: float, longitude: float, units: Optional[str] = None, lang: Optional[str] = None):
    params = {"lat": latitude, "lon": longitude, **_weather_params(units, lang), "latitude": latitude, "longitude": longitude}
    return _request("/data/2.5/weather", params)


def get_current_weather_by_city(query: str, units: Optional[str] = None, lang: Optional[str] = None):
    if not query:
        return {"error": "query is required"}
    params = {"q": query, **_weather_params(units, lang)}
    return _request("/data/2.5/weather", params)


def get_current_weather_by_city_id(city_id: int, units: Optional[str] = None, lang: Optional[str] = None):
    params = {"id": city_id, **_weather_params(units, lang)}
    return _request("/data/2.5/weather", params)


def get_current_weather_by_zip(zip_code: str, units: Optional[str] = None, lang: Optional[str] = None):
    if not zip_code:
        return {"error": "zip_code is required"}
    params = {"zip": zip_code, **_weather_params(units, lang)}
    return _request("/data/2.5/weather", params)


def get_forecast_by_coordinates(latitude: float, longitude: float, units: Optional[str] = None, lang: Optional[str] = None, count: Optional[int] = None):
    params = {"lat": latitude, "lon": longitude, "cnt": count, **_weather_params(units, lang), "latitude": latitude, "longitude": longitude}
    return _request("/data/2.5/forecast", params)


def get_forecast_by_city(query: str, units: Optional[str] = None, lang: Optional[str] = None, count: Optional[int] = None):
    if not query:
        return {"error": "query is required"}
    params = {"q": query, "cnt": count, **_weather_params(units, lang)}
    return _request("/data/2.5/forecast", params)


def get_forecast_by_city_id(city_id: int, units: Optional[str] = None, lang: Optional[str] = None, count: Optional[int] = None):
    params = {"id": city_id, "cnt": count, **_weather_params(units, lang)}
    return _request("/data/2.5/forecast", params)


def get_forecast_by_zip(zip_code: str, units: Optional[str] = None, lang: Optional[str] = None, count: Optional[int] = None):
    if not zip_code:
        return {"error": "zip_code is required"}
    params = {"zip": zip_code, "cnt": count, **_weather_params(units, lang)}
    return _request("/data/2.5/forecast", params)
