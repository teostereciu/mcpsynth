import os
from typing import Any, Dict, List, Optional

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.openweathermap.org"
API_KEY_ENV = "OPENWEATHER_API_KEY"

mcp = FastMCP("openweathermap")


def _api_key() -> Optional[str]:
    return os.getenv(API_KEY_ENV)


def _request(path: str, params: Dict[str, Any]) -> Dict[str, Any]:
    api_key = _api_key()
    if not api_key:
        return {"error": f"Missing environment variable {API_KEY_ENV}"}
    query = dict(params)
    query["appid"] = api_key
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=query, timeout=30)
    except requests.RequestException as exc:
        return {"error": str(exc)}
    if resp.status_code >= 400:
        try:
            payload = resp.json()
        except ValueError:
            payload = resp.text
        return {"error": "OpenWeatherMap API error", "status_code": resp.status_code, "details": payload}
    try:
        return resp.json()
    except ValueError:
        return {"error": "Invalid JSON response from OpenWeatherMap", "status_code": resp.status_code, "details": resp.text}


@mcp.tool()
def get_current_weather_by_coordinates(latitude: float, longitude: float, units: str = "standard", lang: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"lat": latitude, "lon": longitude, "units": units}
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


@mcp.tool()
def get_current_weather_by_city_name(city_name: str, units: str = "standard", lang: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"q": city_name, "units": units}
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


@mcp.tool()
def get_current_weather_by_city_id(city_id: int, units: str = "standard", lang: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"id": city_id, "units": units}
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


@mcp.tool()
def get_current_weather_by_zip(zip_code: str, units: str = "standard", lang: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"zip": zip_code, "units": units}
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


@mcp.tool()
def get_forecast_by_coordinates(latitude: float, longitude: float, units: str = "standard", lang: Optional[str] = None, count: Optional[int] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"lat": latitude, "lon": longitude, "units": units}
    if lang:
        params["lang"] = lang
    if count is not None:
        params["cnt"] = count
    return _request("/data/2.5/forecast", params)


@mcp.tool()
def get_air_pollution_current(latitude: float, longitude: float) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution", {"lat": latitude, "lon": longitude})


@mcp.tool()
def get_air_pollution_forecast(latitude: float, longitude: float) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution/forecast", {"lat": latitude, "lon": longitude})


@mcp.tool()
def get_air_pollution_history(latitude: float, longitude: float, start: int, end: int) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution/history", {"lat": latitude, "lon": longitude, "start": start, "end": end})


@mcp.tool()
def geocode_direct(query: str, limit: int = 5) -> List[Dict[str, Any]]:
    result = _request("/geo/1.0/direct", {"q": query, "limit": limit})
    return result if isinstance(result, list) else [result]


@mcp.tool()
def geocode_zip(zip_code: str) -> Dict[str, Any]:
    return _request("/geo/1.0/zip", {"zip": zip_code})


@mcp.tool()
def geocode_reverse(latitude: float, longitude: float, limit: int = 5) -> List[Dict[str, Any]]:
    result = _request("/geo/1.0/reverse", {"lat": latitude, "lon": longitude, "limit": limit})
    return result if isinstance(result, list) else [result]


if __name__ == "__main__":
    mcp.run(transport="stdio")
