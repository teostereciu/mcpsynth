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
        return {"error": f"Missing required environment variable: {API_KEY_ENV}"}
    query = dict(params)
    query["appid"] = api_key
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=query, timeout=30)
    except requests.RequestException as e:
        return {"error": str(e)}
    try:
        data = resp.json()
    except ValueError:
        data = resp.text
    if resp.status_code >= 400:
        if isinstance(data, dict) and "message" in data:
            return {"error": data.get("message"), "status_code": resp.status_code}
        return {"error": f"HTTP {resp.status_code}", "status_code": resp.status_code, "body": data}
    return data


@mcp.tool()
def get_current_weather(city: str, units: str = "standard", lang: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"q": city, "units": units}
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


@mcp.tool()
def get_forecast_5day_3hour(city: str, units: str = "standard", lang: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"q": city, "units": units}
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/forecast", params)


@mcp.tool()
def get_air_pollution(lat: float, lon: float) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution", {"lat": lat, "lon": lon})


@mcp.tool()
def get_air_pollution_forecast(lat: float, lon: float) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution/forecast", {"lat": lat, "lon": lon})


@mcp.tool()
def get_air_pollution_history(lat: float, lon: float, start: int, end: int) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution/history", {"lat": lat, "lon": lon, "start": start, "end": end})


@mcp.tool()
def geocode_forward(city: str, limit: int = 5, country: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"q": city, "limit": limit}
    if country:
        params["country"] = country
    return _request("/geo/1.0/direct", params)


@mcp.tool()
def geocode_reverse(lat: float, lon: float, limit: int = 5) -> Dict[str, Any]:
    return _request("/geo/1.0/reverse", {"lat": lat, "lon": lon, "limit": limit})


if __name__ == "__main__":
    mcp.run(transport="stdio")
