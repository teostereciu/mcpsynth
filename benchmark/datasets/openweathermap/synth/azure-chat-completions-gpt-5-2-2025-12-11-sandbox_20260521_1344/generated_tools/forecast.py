from typing import Any, Dict, Optional

from .http_client import OpenWeatherClient


def get_5day_forecast_by_coords(
    lat: float,
    lon: float,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    cnt: Optional[int] = None,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """GET /data/2.5/forecast (5 day / 3 hour)"""
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"lat": float(lat), "lon": float(lon)}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    if mode:
        params["mode"] = mode
    if cnt is not None:
        params["cnt"] = int(cnt)
    return client.get("/data/2.5/forecast", params)
