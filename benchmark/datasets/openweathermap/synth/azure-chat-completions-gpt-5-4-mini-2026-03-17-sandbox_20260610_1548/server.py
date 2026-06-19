import os
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("openweather")
BASE_URL = "https://api.openweathermap.org"
API_KEY = os.getenv("OPENWEATHER_API_KEY")


def _error(message: str) -> Dict[str, str]:
    return {"error": message}


def _request(path: str, params: Dict[str, Any]) -> Any:
    if not API_KEY:
        return _error("OPENWEATHER_API_KEY is not set")
    try:
        resp = requests.get(f"{BASE_URL}{path}", params={**params, "appid": API_KEY}, timeout=30)
        if resp.status_code >= 400:
            return {"error": f"OpenWeatherMap API error {resp.status_code}", "details": resp.text}
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def geocode_direct(query: str, limit: int = 5) -> Any:
    return _request("/geo/1.0/direct", {"q": query, "limit": limit})


@mcp.tool()
def geocode_zip(zip_code: str) -> Any:
    return _request("/geo/1.0/zip", {"zip": zip_code})


@mcp.tool()
def geocode_reverse(lat: float, lon: float, limit: int = 5) -> Any:
    return _request("/geo/1.0/reverse", {"lat": lat, "lon": lon, "limit": limit})


@mcp.tool()
def get_current_weather_by_coordinates(lat: float, lon: float, units: Optional[str] = None, lang: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"lat": lat, "lon": lon}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


@mcp.tool()
def get_current_weather_by_city(query: str, units: Optional[str] = None, lang: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"q": query}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


@mcp.tool()
def get_current_weather_by_zip(zip_code: str, units: Optional[str] = None, lang: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"zip": zip_code}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


@mcp.tool()
def get_forecast_5day_by_coordinates(lat: float, lon: float, cnt: Optional[int] = None, units: Optional[str] = None, lang: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"lat": lat, "lon": lon}
    if cnt is not None:
        params["cnt"] = cnt
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/forecast", params)


@mcp.tool()
def get_air_pollution_current(lat: float, lon: float) -> Any:
    return _request("/data/2.5/air_pollution", {"lat": lat, "lon": lon})


@mcp.tool()
def get_air_pollution_forecast(lat: float, lon: float) -> Any:
    return _request("/data/2.5/air_pollution/forecast", {"lat": lat, "lon": lon})


@mcp.tool()
def get_air_pollution_history(lat: float, lon: float, start: int, end: int) -> Any:
    return _request("/data/2.5/air_pollution/history", {"lat": lat, "lon": lon, "start": start, "end": end})


if __name__ == "__main__":
    mcp.run(transport="stdio")
