import os
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://api.openweathermap.org"
API_KEY_ENV = "OPENWEATHER_API_KEY"


def _get_api_key() -> Optional[str]:
    return os.getenv(API_KEY_ENV)


def _request(path: str, params: Dict[str, Any]) -> Dict[str, Any]:
    api_key = _get_api_key()
    if not api_key:
        return {"error": f"Missing environment variable: {API_KEY_ENV}"}

    query = dict(params)
    query["appid"] = api_key

    try:
        response = requests.get(f"{BASE_URL}{path}", params=query, timeout=30)
    except requests.RequestException as exc:
        return {"error": str(exc)}

    try:
        data = response.json()
    except ValueError:
        data = {"error": response.text}

    if not response.ok:
        if isinstance(data, dict):
            return data
        return {"error": f"HTTP {response.status_code}", "details": data}

    return data if isinstance(data, dict) else {"data": data}


def get_current_weather_by_city(
    city: str,
    state_code: Optional[str] = None,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    q = city
    if state_code:
        q += f",{state_code}"
    if country_code:
        q += f",{country_code}"
    params: Dict[str, Any] = {"q": q}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


def get_current_weather_by_coordinates(
    lat: float,
    lon: float,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"lat": lat, "lon": lon}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


def get_current_weather_by_zip(
    zip_code: str,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    zip_value = zip_code if not country_code else f"{zip_code},{country_code}"
    params: Dict[str, Any] = {"zip": zip_value}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


def get_current_weather_by_city_id(
    city_id: int,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"id": city_id}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


def get_forecast_by_city(
    city: str,
    state_code: Optional[str] = None,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
) -> Dict[str, Any]:
    q = city
    if state_code:
        q += f",{state_code}"
    if country_code:
        q += f",{country_code}"
    params: Dict[str, Any] = {"q": q}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if cnt is not None:
        params["cnt"] = cnt
    return _request("/data/2.5/forecast", params)


def get_forecast_by_coordinates(
    lat: float,
    lon: float,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"lat": lat, "lon": lon}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if cnt is not None:
        params["cnt"] = cnt
    return _request("/data/2.5/forecast", params)


def get_forecast_by_zip(
    zip_code: str,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
) -> Dict[str, Any]:
    zip_value = zip_code if not country_code else f"{zip_code},{country_code}"
    params: Dict[str, Any] = {"zip": zip_value}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if cnt is not None:
        params["cnt"] = cnt
    return _request("/data/2.5/forecast", params)


def get_forecast_by_city_id(
    city_id: int,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"id": city_id}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if cnt is not None:
        params["cnt"] = cnt
    return _request("/data/2.5/forecast", params)


def get_air_pollution_current(lat: float, lon: float) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution", {"lat": lat, "lon": lon})


def get_air_pollution_forecast(lat: float, lon: float) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution/forecast", {"lat": lat, "lon": lon})


def get_air_pollution_history(
    lat: float,
    lon: float,
    start: int,
    end: int,
) -> Dict[str, Any]:
    return _request(
        "/data/2.5/air_pollution/history",
        {"lat": lat, "lon": lon, "start": start, "end": end},
    )


def geocode_direct(
    q: str,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"q": q}
    if limit is not None:
        params["limit"] = limit
    return _request("/geo/1.0/direct", params)


def geocode_reverse(
    lat: float,
    lon: float,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"lat": lat, "lon": lon}
    if limit is not None:
        params["limit"] = limit
    return _request("/geo/1.0/reverse", params)


def geocode_zip(zip_code: str, country_code: Optional[str] = None) -> Dict[str, Any]:
    zip_value = zip_code if not country_code else f"{zip_code},{country_code}"
    return _request("/geo/1.0/zip", {"zip": zip_value})
