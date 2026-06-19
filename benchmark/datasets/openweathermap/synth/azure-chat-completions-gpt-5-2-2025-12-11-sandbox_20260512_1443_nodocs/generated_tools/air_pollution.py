from typing import Any, Dict, Optional

from .client import OpenWeatherClient, _clean_none


def get_air_pollution_current(
    client: OpenWeatherClient,
    lat: float,
    lon: float,
) -> Dict[str, Any]:
    """Current air pollution data.

    Endpoint: GET /data/2.5/air_pollution?lat={lat}&lon={lon}
    """
    params = _clean_none({"lat": lat, "lon": lon})
    return client._request("/data/2.5/air_pollution", params=params)


def get_air_pollution_forecast(
    client: OpenWeatherClient,
    lat: float,
    lon: float,
) -> Dict[str, Any]:
    """Air pollution forecast.

    Endpoint: GET /data/2.5/air_pollution/forecast?lat={lat}&lon={lon}
    """
    params = _clean_none({"lat": lat, "lon": lon})
    return client._request("/data/2.5/air_pollution/forecast", params=params)


def get_air_pollution_history(
    client: OpenWeatherClient,
    lat: float,
    lon: float,
    start: int,
    end: int,
) -> Dict[str, Any]:
    """Air pollution history for a time range.

    Endpoint: GET /data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start}&end={end}

    start/end are UNIX timestamps (UTC).
    """
    params = _clean_none({"lat": lat, "lon": lon, "start": start, "end": end})
    return client._request("/data/2.5/air_pollution/history", params=params)
