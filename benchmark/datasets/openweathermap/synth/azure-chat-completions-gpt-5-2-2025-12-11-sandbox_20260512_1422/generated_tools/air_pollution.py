from typing import Any, Dict, Optional

from .http_client import OpenWeatherClient


def air_pollution_current(lat: float, lon: float, *, client: Optional[OpenWeatherClient] = None) -> Any:
    """Current air pollution data by coordinates.

    Endpoint: /data/2.5/air_pollution
    """
    client = client or OpenWeatherClient()
    return client._request("/data/2.5/air_pollution", {"lat": lat, "lon": lon})


def air_pollution_forecast(lat: float, lon: float, *, client: Optional[OpenWeatherClient] = None) -> Any:
    """Forecast air pollution data by coordinates.

    Endpoint: /data/2.5/air_pollution/forecast
    """
    client = client or OpenWeatherClient()
    return client._request("/data/2.5/air_pollution/forecast", {"lat": lat, "lon": lon})


def air_pollution_history(
    lat: float,
    lon: float,
    start: int,
    end: int,
    *,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Historical air pollution data by coordinates.

    Endpoint: /data/2.5/air_pollution/history
    Required: start, end (unix UTC)
    """
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"lat": lat, "lon": lon, "start": start, "end": end}
    return client._request("/data/2.5/air_pollution/history", params)
