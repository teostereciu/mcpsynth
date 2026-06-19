from typing import Any, Dict, Optional

from .http_client import OpenWeatherClient


def get_current_air_pollution(
    lat: float,
    lon: float,
    *,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Get current air pollution data for coordinates.

    Endpoint: GET /data/2.5/air_pollution
    Docs: docs/api_air_pollution.md
    """
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"lat": lat, "lon": lon}
    return client._request("/data/2.5/air_pollution", params=params)


def get_air_pollution_forecast(
    lat: float,
    lon: float,
    *,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Get forecast air pollution data for coordinates.

    Endpoint: GET /data/2.5/air_pollution/forecast
    Docs: docs/api_air_pollution.md
    """
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"lat": lat, "lon": lon}
    return client._request("/data/2.5/air_pollution/forecast", params=params)


def get_air_pollution_history(
    lat: float,
    lon: float,
    start: int,
    end: int,
    *,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Get historical air pollution data for coordinates and time range.

    Endpoint: GET /data/2.5/air_pollution/history
    Docs: docs/api_air_pollution.md
    """
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"lat": lat, "lon": lon, "start": start, "end": end}
    return client._request("/data/2.5/air_pollution/history", params=params)
