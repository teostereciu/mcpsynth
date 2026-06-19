import os
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.openweathermap.org"
API_KEY = os.getenv("OPENWEATHER_API_KEY")

mcp = FastMCP("openweathermap")


def _request(path: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if not API_KEY:
        return {"error": "OPENWEATHER_API_KEY is not set"}
    try:
        merged = {k: v for k, v in params.items() if v is not None}
        merged["appid"] = API_KEY
        resp = requests.get(f"{BASE_URL}{path}", params=merged, timeout=30)
        if resp.status_code >= 400:
            try:
                data = resp.json()
            except Exception:
                data = resp.text
            return {"error": f"HTTP {resp.status_code}", "details": data}
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def get_current_weather_by_coordinates(lat: float, lon: float, units: Optional[str] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    return _request("/data/2.5/weather", {"lat": lat, "lon": lon, "units": units, "lang": lang})


@mcp.tool()
def get_current_weather_by_city_name(city_name: str, state_code: Optional[str] = None, country_code: Optional[str] = None, units: Optional[str] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    q = city_name
    if state_code:
        q += f",{state_code}"
    if country_code:
        q += f",{country_code}"
    return _request("/data/2.5/weather", {"q": q, "units": units, "lang": lang})


@mcp.tool()
def get_current_weather_by_city_id(city_id: int, units: Optional[str] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    return _request("/data/2.5/weather", {"id": city_id, "units": units, "lang": lang})


@mcp.tool()
def get_current_weather_by_zip(zip_code: str, units: Optional[str] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    return _request("/data/2.5/weather", {"zip": zip_code, "units": units, "lang": lang})


@mcp.tool()
def get_forecast_by_coordinates(lat: float, lon: float, cnt: Optional[int] = None, units: Optional[str] = None, lang: Optional[str] = None, mode: Optional[str] = None) -> Dict[str, Any]:
    return _request("/data/2.5/forecast", {"lat": lat, "lon": lon, "cnt": cnt, "units": units, "lang": lang, "mode": mode})


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
def geocode_direct(query: str, limit: Optional[int] = None) -> Dict[str, Any]:
    return _request("/geo/1.0/direct", {"q": query, "limit": limit})


@mcp.tool()
def geocode_zip(zip_code: str) -> Dict[str, Any]:
    return _request("/geo/1.0/zip", {"zip": zip_code})


@mcp.tool()
def geocode_reverse(lat: float, lon: float, limit: Optional[int] = None) -> Dict[str, Any]:
    return _request("/geo/1.0/reverse", {"lat": lat, "lon": lon, "limit": limit})


if __name__ == "__main__":
    mcp.run()
