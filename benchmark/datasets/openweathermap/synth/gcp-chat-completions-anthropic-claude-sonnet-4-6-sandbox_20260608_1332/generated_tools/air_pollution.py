"""
Tools for OpenWeatherMap Air Pollution API (2.5).
Endpoints:
  - GET /data/2.5/air_pollution          (current)
  - GET /data/2.5/air_pollution/forecast (4-day hourly forecast)
  - GET /data/2.5/air_pollution/history  (historical, from 27 Nov 2020)
"""

import os
import requests

_BASE = "https://api.openweathermap.org/data/2.5"


def _api_key() -> str:
    key = os.environ.get("OPENWEATHER_API_KEY", "")
    if not key:
        raise RuntimeError("OPENWEATHER_API_KEY environment variable is not set")
    return key


def _get(path: str, params: dict) -> dict:
    """Internal HTTP helper — not exposed as an MCP tool."""
    try:
        params["appid"] = _api_key()
        resp = requests.get(f"{_BASE}{path}", params=params, timeout=10)
        if resp.status_code == 200:
            return resp.json()
        try:
            body = resp.json()
        except Exception:
            body = resp.text
        return {"error": f"HTTP {resp.status_code}", "details": body}
    except RuntimeError as exc:
        return {"error": str(exc)}
    except requests.RequestException as exc:
        return {"error": f"Request failed: {exc}"}


# ── Tool functions ────────────────────────────────────────────────────────────

def get_current_air_pollution(lat: float, lon: float) -> dict:
    """
    Get current air pollution data for a geographic location.

    Returns the Air Quality Index (AQI) and concentrations of key pollutants:
    CO, NO, NO2, O3, SO2, PM2.5, PM10, NH3.

    AQI scale: 1=Good, 2=Fair, 3=Moderate, 4=Poor, 5=Very Poor.

    Args:
        lat: Latitude of the location.
        lon: Longitude of the location.

    Returns:
        Dict with 'coord' and 'list' of pollution readings, or an error dict.
    """
    return _get("/air_pollution", {"lat": lat, "lon": lon})


def get_air_pollution_forecast(lat: float, lon: float) -> dict:
    """
    Get air pollution forecast for a geographic location.

    Provides hourly air quality data for the next 4 days, including AQI and
    pollutant concentrations (CO, NO, NO2, O3, SO2, PM2.5, PM10, NH3).

    Args:
        lat: Latitude of the location.
        lon: Longitude of the location.

    Returns:
        Dict with 'coord' and 'list' of hourly forecast pollution readings,
        or an error dict.
    """
    return _get("/air_pollution/forecast", {"lat": lat, "lon": lon})


def get_air_pollution_history(
    lat: float,
    lon: float,
    start: int,
    end: int,
) -> dict:
    """
    Get historical air pollution data for a geographic location.

    Historical data is available from 27th November 2020 onwards.

    Args:
        lat:   Latitude of the location.
        lon:   Longitude of the location.
        start: Start of the time range as a Unix timestamp (UTC),
               e.g. 1606488670.
        end:   End of the time range as a Unix timestamp (UTC),
               e.g. 1606747870.

    Returns:
        Dict with 'coord' and 'list' of historical pollution readings,
        or an error dict.
    """
    return _get(
        "/air_pollution/history",
        {"lat": lat, "lon": lon, "start": start, "end": end},
    )
