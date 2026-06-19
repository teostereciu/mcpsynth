import os
from typing import Any, Dict, Optional

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
    params = {k: v for k, v in params.items() if v is not None}
    params["appid"] = api_key
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=30)
    except requests.RequestException as e:
        return {"error": str(e)}
    try:
        data = resp.json()
    except ValueError:
        data = resp.text
    if resp.status_code >= 400:
        return {"error": "OpenWeatherMap API error", "status_code": resp.status_code, "response": data}
    return data


@mcp.tool()
def get_current_weather_by_coordinates(latitude: float, longitude: float, units: Optional[str] = None, language: Optional[str] = None, mode: Optional[str] = None) -> Dict[str, Any]:
    return _request("/data/2.5/weather", {"latitude": latitude, "longitude": longitude, "units": units, "language": language, "mode": mode})


@mcp.tool()
def get_current_weather_by_city_name(city_name: str, units: Optional[str] = None, language: Optional[str] = None, mode: Optional[str] = None) -> Dict[str, Any]:
    return _request("/data/2.5/weather", {"q": city_name, "units": units, "language": language, "mode": mode})


@mcp.tool()
def get_current_weather_by_zip(zip_code: str, units: Optional[str] = None, language: Optional[str] = None, mode: Optional[str] = None) -> Dict[str, Any]:
    return _request("/data/2.5/weather", {"zip": zip_code, "units": units, "language": language, "mode": mode})


@mcp.tool()
def get_forecast_by_coordinates(latitude: float, longitude: float, count: Optional[int] = None, units: Optional[str] = None, language: Optional[str] = None, mode: Optional[str] = None) -> Dict[str, Any]:
    return _request("/data/2.5/forecast", {"latitude": latitude, "longitude": longitude, "cnt": count, "units": units, "language": language, "mode": mode})


@mcp.tool()
def get_forecast_by_city_name(city_name: str, count: Optional[int] = None, units: Optional[str] = None, language: Optional[str] = None, mode: Optional[str] = None) -> Dict[str, Any]:
    return _request("/data/2.5/forecast", {"q": city_name, "cnt": count, "units": units, "language": language, "mode": mode})


@mcp.tool()
def get_forecast_by_zip(zip_code: str, count: Optional[int] = None, units: Optional[str] = None, language: Optional[str] = None, mode: Optional[str] = None) -> Dict[str, Any]:
    return _request("/data/2.5/forecast", {"zip": zip_code, "cnt": count, "units": units, "language": language, "mode": mode})


@mcp.tool()
def get_air_pollution_current(latitude: float, longitude: float) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution", {"latitude": latitude, "longitude": longitude})


@mcp.tool()
def get_air_pollution_forecast(latitude: float, longitude: float) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution/forecast", {"latitude": latitude, "longitude": longitude})


@mcp.tool()
def get_air_pollution_history(latitude: float, longitude: float, start: int, end: int) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution/history", {"latitude": latitude, "longitude": longitude, "start": start, "end": end})


@mcp.tool()
def geocode_direct(query: str, limit: Optional[int] = None) -> Dict[str, Any]:
    return _request("/geo/1.0/direct", {"q": query, "limit": limit})


@mcp.tool()
def geocode_zip(zip_code: str) -> Dict[str, Any]:
    return _request("/geo/1.0/zip", {"zip": zip_code})


@mcp.tool()
def geocode_reverse(latitude: float, longitude: float, limit: Optional[int] = None) -> Dict[str, Any]:
    return _request("/geo/1.0/reverse", {"latitude": latitude, "longitude": longitude, "limit": limit})


if __name__ == "__main__":
    mcp.run()
