from typing import Any, Dict

from generated_tools.geocoding import _request


def get_current_air_pollution(lat: float, lon: float) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution", {"lat": lat, "lon": lon})


def get_air_pollution_forecast(lat: float, lon: float) -> Dict[str, Any]:
    return _request("/data/2.5/air_pollution/forecast", {"lat": lat, "lon": lon})


def get_air_pollution_history(lat: float, lon: float, start: int, end: int) -> Dict[str, Any]:
    if end < start:
        return {"error": "end must be greater than or equal to start"}
    return _request("/data/2.5/air_pollution/history", {"lat": lat, "lon": lon, "start": start, "end": end})
