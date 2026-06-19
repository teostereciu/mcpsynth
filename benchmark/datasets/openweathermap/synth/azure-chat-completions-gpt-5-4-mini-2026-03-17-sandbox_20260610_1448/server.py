import os
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("openweather")
BASE_URL = "https://api.openweathermap.org"
API_KEY = os.getenv("OPENWEATHER_API_KEY")


def _request(path: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if not API_KEY:
        return {"error": "OPENWEATHER_API_KEY is not set"}
    try:
        resp = requests.get(f"{BASE_URL}{path}", params={**params, "appid": API_KEY}, timeout=30)
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text or f"HTTP {resp.status_code}"}
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def get_current_weather_by_coordinates(lat: float, lon: float, units: Optional[str] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"lat": lat, "lon": lon}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


@mcp.tool()
def get_current_weather_by_city(q: str, units: Optional[str] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"q": q}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


@mcp.tool()
def get_current_weather_by_zip(zip: str, units: Optional[str] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"zip": zip}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


@mcp.tool()
def get_forecast_by_coordinates(lat: float, lon: float, cnt: Optional[int] = None, units: Optional[str] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"lat": lat, "lon": lon}
    if cnt is not None:
        params["cnt"] = cnt
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/forecast", params)


@mcp.tool()
def get_air_pollution_current(lat: float, lon: float) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution", {"lat": lat, "lon": lon})


@mcp.tool()
def get_air_pollution_forecast(lat: float, lon: float) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution/forecast", {"lat": lat, "lon": lon})


@mcp.tool()
def get_air_pollution_history(lat: float, lon: float, start: int, end: int) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution/history", {"lat": lat, "lon": lon, "start": start, "end": end})


@mcp.tool()
def geocode_direct(q: str, limit: Optional[int] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"q": q}
    if limit is not None:
        params["limit"] = limit
    return _request("/geo/1.0/direct", params)


@mcp.tool()
def geocode_zip(zip: str) -> Dict[str, Any]:
    return _request("/geo/1.0/zip", {"zip": zip})


@mcp.tool()
def geocode_reverse(lat: float, lon: float, limit: Optional[int] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"lat": lat, "lon": lon}
    if limit is not None:
        params["limit"] = limit
    return _request("/geo/1.0/reverse", params)


if __name__ == "__main__":
    mcp.run(transport="stdio")
