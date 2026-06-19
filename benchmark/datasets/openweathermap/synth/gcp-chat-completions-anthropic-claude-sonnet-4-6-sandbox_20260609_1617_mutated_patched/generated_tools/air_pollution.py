"""
Tools for OpenWeatherMap Air Pollution API (v2.5).
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
        raise ValueError("OPENWEATHER_API_KEY environment variable is not set")
    return key


def _get(path: str, params: dict) -> dict:
    """Internal HTTP helper — not exposed as an MCP tool."""
    try:
        params["appid"] = _api_key()
        url = f"{_BASE}/{path}"
        resp = requests.get(url, params=params, timeout=10)
        if resp.status_code == 200:
            return resp.json()
        try:
            err = resp.json()
        except Exception:
            err = {"message": resp.text}
        return {"error": f"HTTP {resp.status_code}", "details": err}
    except ValueError as exc:
        return {"error": str(exc)}
    except requests.RequestException as exc:
        return {"error": f"Request failed: {exc}"}


# ── Tool functions ────────────────────────────────────────────────────────────

def get_current_air_pollution(latitude: float, longitude: float) -> dict:
    """
    Get current air pollution data for a geographic location.

    Returns the Air Quality Index (AQI) and concentrations of key pollutants:
    CO, NO, NO2, O3, SO2, PM2.5, PM10, and NH3.

    AQI scale: 1=Good, 2=Fair, 3=Moderate, 4=Poor, 5=Very Poor.

    Args:
        latitude:  Latitude of the location.
        longitude: Longitude of the location.

    Returns:
        JSON dict with 'coord' and 'list' containing one entry with:
          - dt: Unix timestamp (UTC)
          - main.aqi: Air Quality Index (1–5)
          - components: dict of pollutant concentrations in μg/m³
            (co, no, no2, o3, so2, pm2_5, pm10, nh3)
    """
    return _get("air_pollution", {"lat": latitude, "lon": longitude})


def get_air_pollution_forecast(latitude: float, longitude: float) -> dict:
    """
    Get air pollution forecast for the next 4 days (hourly granularity).

    Returns hourly AQI and pollutant concentration forecasts for the specified
    location.

    AQI scale: 1=Good, 2=Fair, 3=Moderate, 4=Poor, 5=Very Poor.

    Args:
        latitude:  Latitude of the location.
        longitude: Longitude of the location.

    Returns:
        JSON dict with 'coord' and 'list' of hourly forecast entries, each
        containing:
          - dt: Unix timestamp (UTC)
          - main.aqi: Air Quality Index (1–5)
          - components: dict of pollutant concentrations in μg/m³
    """
    return _get(
        "air_pollution/forecast",
        {"lat": latitude, "lon": longitude},
    )


def get_air_pollution_history(
    latitude: float,
    longitude: float,
    start: int,
    end: int,
) -> dict:
    """
    Get historical air pollution data for a location and time range.

    Historical data is available from 27 November 2020 onwards.

    Args:
        latitude:  Latitude of the location.
        longitude: Longitude of the location.
        start:     Start of the time range as a Unix timestamp (UTC).
                   Example: 1606488670
        end:       End of the time range as a Unix timestamp (UTC).
                   Example: 1606747870

    Returns:
        JSON dict with 'coord' and 'list' of historical entries, each
        containing:
          - dt: Unix timestamp (UTC)
          - main.aqi: Air Quality Index (1–5)
          - components: dict of pollutant concentrations in μg/m³
            (co, no, no2, o3, so2, pm2_5, pm10, nh3)
    """
    return _get(
        "air_pollution/history",
        {
            "lat": latitude,
            "lon": longitude,
            "start": start,
            "end": end,
        },
    )
