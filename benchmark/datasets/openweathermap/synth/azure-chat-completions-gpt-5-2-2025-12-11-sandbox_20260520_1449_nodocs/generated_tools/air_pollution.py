from typing import Any, Dict, Optional

from .client import request_json


def get_air_pollution_current(
    lat: float,
    lon: float,
) -> Dict[str, Any]:
    """Current air pollution data.

    Endpoint: GET /data/2.5/air_pollution
    """
    return request_json("/data/2.5/air_pollution", {"lat": lat, "lon": lon})


def get_air_pollution_forecast(
    lat: float,
    lon: float,
) -> Dict[str, Any]:
    """Air pollution forecast.

    Endpoint: GET /data/2.5/air_pollution/forecast
    """
    return request_json("/data/2.5/air_pollution/forecast", {"lat": lat, "lon": lon})


def get_air_pollution_history(
    lat: float,
    lon: float,
    start: int,
    end: int,
) -> Dict[str, Any]:
    """Air pollution history for a time range.

    start/end are UNIX timestamps (UTC).

    Endpoint: GET /data/2.5/air_pollution/history
    """
    return request_json(
        "/data/2.5/air_pollution/history",
        {"lat": lat, "lon": lon, "start": start, "end": end},
    )
