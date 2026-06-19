import os
from typing import Any, Dict

import requests
from fastmcp import FastMCP

BASE_URL = "https://api.openweathermap.org"
API_KEY = os.getenv("OPENWEATHER_API_KEY")

mcp = FastMCP("openweathermap")


def _params(extra: Dict[str, Any] | None = None) -> Dict[str, Any]:
    params = {"appid": API_KEY}
    if extra:
        params.update({k: v for k, v in extra.items() if v is not None})
    return params


def _get(path: str, params: Dict[str, Any] | None = None):
    if not API_KEY:
        return {"error": "OPENWEATHER_API_KEY is not set"}
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=_params(params), timeout=30)
        data = resp.json()
        if resp.status_code >= 400:
            return {"error": data.get("message", f"HTTP {resp.status_code}"), "status": resp.status_code}
        return data
    except requests.RequestException as e:
        return {"error": str(e)}
    except ValueError:
        return {"error": "Invalid JSON response"}


@mcp.tool()
def get_current_weather(city: str, units: str | None = None, lang: str | None = None):
    """Get current weather by city name."""
    return _get("/data/2.5/weather", {"q": city, "units": units, "lang": lang})


@mcp.tool()
def get_current_weather_by_coords(lat: float, lon: float, units: str | None = None, lang: str | None = None):
    """Get current weather by coordinates."""
    return _get("/data/2.5/weather", {"lat": lat, "lon": lon, "units": units, "lang": lang})


@mcp.tool()
def get_forecast_5day_3hour(city: str, units: str | None = None, lang: str | None = None):
    """Get 5-day/3-hour forecast by city name."""
    return _get("/data/2.5/forecast", {"q": city, "units": units, "lang": lang})


@mcp.tool()
def get_forecast_5day_3hour_by_coords(lat: float, lon: float, units: str | None = None, lang: str | None = None):
    """Get 5-day/3-hour forecast by coordinates."""
    return _get("/data/2.5/forecast", {"lat": lat, "lon": lon, "units": units, "lang": lang})


@mcp.tool()
def get_air_pollution(lat: float, lon: float):
    """Get current air pollution data by coordinates."""
    return _get("/data/2.5/air_pollution", {"lat": lat, "lon": lon})


@mcp.tool()
def get_air_pollution_forecast(lat: float, lon: float):
    """Get air pollution forecast by coordinates."""
    return _get("/data/2.5/air_pollution/forecast", {"lat": lat, "lon": lon})


@mcp.tool()
def get_air_pollution_history(lat: float, lon: float, start: int, end: int):
    """Get air pollution history by coordinates and time range."""
    return _get("/data/2.5/air_pollution/history", {"lat": lat, "lon": lon, "start": start, "end": end})


@mcp.tool()
def geocode_city(city: str, limit: int | None = 5):
    """Forward geocoding for a city name."""
    return _get("/geo/1.0/direct", {"q": city, "limit": limit})


@mcp.tool()
def reverse_geocode(lat: float, lon: float, limit: int | None = 5):
    """Reverse geocoding for coordinates."""
    return _get("/geo/1.0/reverse", {"lat": lat, "lon": lon, "limit": limit})


if __name__ == "__main__":
    mcp.run()
