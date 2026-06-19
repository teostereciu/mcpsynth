import os
from typing import Any, Dict, Optional

import requests
from fastmcp import FastMCP

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
        if resp.status_code == 404:
            return {"error": "Resource not found"}
        if resp.status_code >= 400:
            try:
                data = resp.json()
            except Exception:
                data = {"message": resp.text}
            return {"error": data.get("message", f"HTTP {resp.status_code}")}
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def current_weather(q: Optional[str] = None, lat: Optional[float] = None, lon: Optional[float] = None, units: Optional[str] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if q is not None:
        params["q"] = q
    if lat is not None:
        params["lat"] = lat
    if lon is not None:
        params["lon"] = lon
    if units is not None:
        params["units"] = units
    if lang is not None:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


@mcp.tool()
def forecast_5_day_3_hour(q: Optional[str] = None, lat: Optional[float] = None, lon: Optional[float] = None, units: Optional[str] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if q is not None:
        params["q"] = q
    if lat is not None:
        params["lat"] = lat
    if lon is not None:
        params["lon"] = lon
    if units is not None:
        params["units"] = units
    if lang is not None:
        params["lang"] = lang
    return _request("/data/2.5/forecast", params)


@mcp.tool()
def air_pollution_current(lat: float, lon: float) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution", {"lat": lat, "lon": lon})


@mcp.tool()
def air_pollution_forecast(lat: float, lon: float) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution/forecast", {"lat": lat, "lon": lon})


@mcp.tool()
def air_pollution_history(lat: float, lon: float, start: int, end: int) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution/history", {"lat": lat, "lon": lon, "start": start, "end": end})


@mcp.tool()
def geocode_forward(q: str, limit: Optional[int] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"q": q}
    if limit is not None:
        params["limit"] = limit
    if lang is not None:
        params["lang"] = lang
    return _request("/geo/1.0/direct", params)


@mcp.tool()
def geocode_reverse(lat: float, lon: float, limit: Optional[int] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"lat": lat, "lon": lon}
    if limit is not None:
        params["limit"] = limit
    if lang is not None:
        params["lang"] = lang
    return _request("/geo/1.0/reverse", params)


if __name__ == "__main__":
    mcp.run(transport="stdio")
