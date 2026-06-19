import os
import time
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.openweathermap.org"


def _get_api_key() -> Optional[str]:
    return os.getenv("OPENWEATHER_API_KEY")


def _clean_params(params: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}


def _request_json(path: str, params: Dict[str, Any]) -> Dict[str, Any]:
    api_key = _get_api_key()
    if not api_key:
        return {"error": "Missing OPENWEATHER_API_KEY environment variable"}

    url = f"{BASE_URL}{path}"
    q = dict(params)
    q["appid"] = api_key

    try:
        resp = requests.get(url, params=_clean_params(q), timeout=30)
    except requests.RequestException as e:
        return {"error": f"Network error: {e}"}

    content_type = resp.headers.get("content-type", "")
    if resp.status_code >= 400:
        # OpenWeather often returns JSON with message/cod; sometimes plain text.
        try:
            data = resp.json()
        except Exception:
            data = {"message": resp.text}
        return {
            "error": "OpenWeather API error",
            "status_code": resp.status_code,
            "response": data,
            "url": resp.url,
        }

    if "application/json" in content_type or content_type.endswith("+json"):
        try:
            return resp.json()
        except Exception:
            return {"error": "Failed to parse JSON response", "status_code": resp.status_code, "text": resp.text}

    # For mode=xml/html, return raw text.
    return {"content_type": content_type, "text": resp.text, "url": resp.url}


mcp = FastMCP("openweathermap")


@mcp.tool()
def geocode_direct(q: str, limit: int = 5) -> Any:
    """Direct geocoding: convert a location name to coordinates.

    Args:
      q: City name, optionally with state code and country code separated by commas (e.g. "London", "Austin,TX,US").
      limit: Max number of results (up to 5 per docs).
    """
    return _request_json("/geo/1.0/direct", {"q": q, "limit": limit})


@mcp.tool()
def geocode_zip(zip: str) -> Any:
    """Geocode by zip/post code.

    Args:
      zip: Zip/post code and country code separated by comma (e.g. "E14,GB" or "90210,US").
    """
    return _request_json("/geo/1.0/zip", {"zip": zip})


@mcp.tool()
def geocode_reverse(latitude: float, longitude: float, limit: int = 5) -> Any:
    """Reverse geocoding: convert coordinates to nearby location names."""
    return _request_json("/geo/1.0/reverse", {"lat": latitude, "lon": longitude, "limit": limit})


@mcp.tool()
def weather_current_by_coords(
    latitude: float,
    longitude: float,
    units: str = "standard",
    lang: Optional[str] = None,
    mode: Optional[str] = None,
) -> Any:
    """Get current weather by geographic coordinates.

    Args:
      latitude: Latitude.
      longitude: Longitude.
      units: standard|metric|imperial.
      lang: Language code.
      mode: Optional response format: xml|html (JSON by default).
    """
    return _request_json(
        "/data/2.5/weather",
        {"lat": latitude, "lon": longitude, "units": units, "lang": lang, "mode": mode},
    )


@mcp.tool()
def weather_current_by_query(
    q: str,
    units: str = "standard",
    lang: Optional[str] = None,
    mode: Optional[str] = None,
) -> Any:
    """Get current weather by city query string.

    Note: Built-in geocoder by city name is deprecated per docs, but still available.

    Args:
      q: City name, optionally with country/state codes (e.g. "London,GB" or "Austin,TX,US").
      units: standard|metric|imperial.
      lang: Language code.
      mode: Optional response format: xml|html (JSON by default).
    """
    return _request_json("/data/2.5/weather", {"q": q, "units": units, "lang": lang, "mode": mode})


@mcp.tool()
def forecast_5day_by_coords(
    latitude: float,
    longitude: float,
    units: str = "standard",
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
    mode: Optional[str] = None,
) -> Any:
    """Get 5 day / 3 hour forecast by geographic coordinates.

    Args:
      latitude: Latitude.
      longitude: Longitude.
      units: standard|metric|imperial.
      lang: Language code.
      cnt: Number of timestamps to return.
      mode: Optional response format: xml (JSON by default).
    """
    return _request_json(
        "/data/2.5/forecast",
        {"lat": latitude, "lon": longitude, "units": units, "lang": lang, "cnt": cnt, "mode": mode},
    )


@mcp.tool()
def air_pollution_current(latitude: float, longitude: float) -> Any:
    """Get current air pollution data by coordinates."""
    return _request_json("/data/2.5/air_pollution", {"lat": latitude, "lon": longitude})


@mcp.tool()
def air_pollution_forecast(latitude: float, longitude: float) -> Any:
    """Get air pollution forecast (up to 4 days, hourly) by coordinates."""
    return _request_json("/data/2.5/air_pollution/forecast", {"lat": latitude, "lon": longitude})


@mcp.tool()
def air_pollution_history(latitude: float, longitude: float, start: int, end: int) -> Any:
    """Get historical air pollution data by coordinates and unix time range (UTC).

    Args:
      start: Start unix time (UTC).
      end: End unix time (UTC).
    """
    return _request_json(
        "/data/2.5/air_pollution/history",
        {"lat": latitude, "lon": longitude, "start": start, "end": end},
    )


@mcp.tool()
def unix_time_now() -> Dict[str, Any]:
    """Utility: return current unix time (UTC seconds). Useful for air pollution history ranges."""
    return {"unix": int(time.time())}


if __name__ == "__main__":
    mcp.run()
