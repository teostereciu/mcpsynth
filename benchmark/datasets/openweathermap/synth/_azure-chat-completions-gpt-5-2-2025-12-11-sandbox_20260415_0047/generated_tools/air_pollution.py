"""Tools for OpenWeatherMap Air Pollution API."""

from __future__ import annotations

from typing import Any, Dict

from .http import get_json


def air_pollution_current(lat: float, lon: float) -> Dict[str, Any]:
    """Get current air pollution data.

    Endpoint: /data/2.5/air_pollution
    """
    return get_json("/data/2.5/air_pollution", params={"lat": lat, "lon": lon})


def air_pollution_forecast(lat: float, lon: float) -> Dict[str, Any]:
    """Get forecast air pollution data.

    Endpoint: /data/2.5/air_pollution/forecast
    """
    return get_json("/data/2.5/air_pollution/forecast", params={"lat": lat, "lon": lon})


def air_pollution_history(lat: float, lon: float, start: int, end: int) -> Dict[str, Any]:
    """Get historical air pollution data.

    Endpoint: /data/2.5/air_pollution/history

    Args:
        start: Start time (unix UTC).
        end: End time (unix UTC).
    """
    return get_json(
        "/data/2.5/air_pollution/history",
        params={"lat": lat, "lon": lon, "start": start, "end": end},
    )
