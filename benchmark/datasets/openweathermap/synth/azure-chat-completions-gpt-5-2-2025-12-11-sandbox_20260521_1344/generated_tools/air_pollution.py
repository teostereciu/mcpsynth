from typing import Any, Dict, Optional

from .http_client import OpenWeatherClient


def get_air_pollution_current(lat: float, lon: float, client: Optional[OpenWeatherClient] = None) -> Any:
    """GET /data/2.5/air_pollution"""
    client = client or OpenWeatherClient()
    return client.get("/data/2.5/air_pollution", {"lat": float(lat), "lon": float(lon)})


def get_air_pollution_forecast(lat: float, lon: float, client: Optional[OpenWeatherClient] = None) -> Any:
    """GET /data/2.5/air_pollution/forecast"""
    client = client or OpenWeatherClient()
    return client.get("/data/2.5/air_pollution/forecast", {"lat": float(lat), "lon": float(lon)})


def get_air_pollution_history(
    lat: float,
    lon: float,
    start: int,
    end: int,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """GET /data/2.5/air_pollution/history"""
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"lat": float(lat), "lon": float(lon), "start": int(start), "end": int(end)}
    return client.get("/data/2.5/air_pollution/history", params)
