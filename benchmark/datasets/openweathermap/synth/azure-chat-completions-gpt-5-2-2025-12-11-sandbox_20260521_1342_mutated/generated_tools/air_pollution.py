from typing import Any, Dict

from .http import owm_get


def get_current_air_pollution(latitude: float, longitude: float) -> Dict[str, Any]:
    """Current air pollution data by coordinates.

    Endpoint: GET /data/2.5/air_pollution
    Docs: docs/api_air_pollution.md
    """
    return owm_get("/data/2.5/air_pollution", {"latitude": latitude, "longitude": longitude})


def get_air_pollution_forecast(latitude: float, longitude: float) -> Dict[str, Any]:
    """Forecast air pollution data by coordinates.

    Endpoint: GET /data/2.5/air_pollution/forecast
    Docs: docs/api_air_pollution.md
    """
    return owm_get(
        "/data/2.5/air_pollution/forecast", {"latitude": latitude, "longitude": longitude}
    )


def get_air_pollution_history(latitude: float, longitude: float, start: int, end: int) -> Dict[str, Any]:
    """Historical air pollution data by coordinates and time range.

    Endpoint: GET /data/2.5/air_pollution/history
    Docs: docs/api_air_pollution.md
    """
    return owm_get(
        "/data/2.5/air_pollution/history",
        {"latitude": latitude, "longitude": longitude, "start": start, "end": end},
    )
