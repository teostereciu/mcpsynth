from typing import Any, Dict, Optional

from generated_tools.geocoding import _request


VALID_UNITS = {"standard", "metric", "imperial"}


def _weather_params(units: Optional[str], lang: Optional[str]) -> Dict[str, Any]:
    if units is not None and units not in VALID_UNITS:
        return {"error": "units must be one of: standard, metric, imperial"}
    params: Dict[str, Any] = {}
    if units is not None:
        params["units"] = units
    if lang is not None:
        params["lang"] = lang
    return params


def get_current_weather_by_coordinates(lat: float, lon: float, units: Optional[str] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    params = _weather_params(units, lang)
    if "error" in params:
        return params
    params.update({"lat": lat, "lon": lon})
    return _request("/data/2.5/weather", params)


def get_current_weather_by_city_name(query: str, units: Optional[str] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    if not query:
        return {"error": "query is required"}
    params = _weather_params(units, lang)
    if "error" in params:
        return params
    params["q"] = query
    return _request("/data/2.5/weather", params)


def get_current_weather_by_city_id(city_id: int, units: Optional[str] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    params = _weather_params(units, lang)
    if "error" in params:
        return params
    params["id"] = city_id
    return _request("/data/2.5/weather", params)


def get_current_weather_by_zip(zip_code: str, country_code: Optional[str] = None, units: Optional[str] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    if not zip_code:
        return {"error": "zip_code is required"}
    params = _weather_params(units, lang)
    if "error" in params:
        return params
    params["zip"] = f"{zip_code},{country_code}" if country_code else zip_code
    return _request("/data/2.5/weather", params)


def _forecast_params(units: Optional[str], lang: Optional[str], cnt: Optional[int]) -> Dict[str, Any]:
    params = _weather_params(units, lang)
    if "error" in params:
        return params
    if cnt is not None:
        if cnt < 1:
            return {"error": "cnt must be at least 1"}
        params["cnt"] = cnt
    return params


def get_forecast_by_coordinates(lat: float, lon: float, units: Optional[str] = None, lang: Optional[str] = None, cnt: Optional[int] = None) -> Dict[str, Any]:
    params = _forecast_params(units, lang, cnt)
    if "error" in params:
        return params
    params.update({"lat": lat, "lon": lon})
    return _request("/data/2.5/forecast", params)


def get_forecast_by_city_name(query: str, units: Optional[str] = None, lang: Optional[str] = None, cnt: Optional[int] = None) -> Dict[str, Any]:
    if not query:
        return {"error": "query is required"}
    params = _forecast_params(units, lang, cnt)
    if "error" in params:
        return params
    params["q"] = query
    return _request("/data/2.5/forecast", params)


def get_forecast_by_city_id(city_id: int, units: Optional[str] = None, lang: Optional[str] = None, cnt: Optional[int] = None) -> Dict[str, Any]:
    params = _forecast_params(units, lang, cnt)
    if "error" in params:
        return params
    params["id"] = city_id
    return _request("/data/2.5/forecast", params)


def get_forecast_by_zip(zip_code: str, country_code: Optional[str] = None, units: Optional[str] = None, lang: Optional[str] = None, cnt: Optional[int] = None) -> Dict[str, Any]:
    if not zip_code:
        return {"error": "zip_code is required"}
    params = _forecast_params(units, lang, cnt)
    if "error" in params:
        return params
    params["zip"] = f"{zip_code},{country_code}" if country_code else zip_code
    return _request("/data/2.5/forecast", params)
