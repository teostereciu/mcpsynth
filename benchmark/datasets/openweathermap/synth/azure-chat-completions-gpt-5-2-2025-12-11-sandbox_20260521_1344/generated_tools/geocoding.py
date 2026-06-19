from typing import Any, Dict, Optional

from .http_client import OpenWeatherClient


def geocode_direct(
    q: str,
    limit: Optional[int] = 5,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """GET /geo/1.0/direct

    q: "city,state,country" (state only for US; country ISO 3166)
    limit: up to 5
    """
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"q": q}
    if limit is not None:
        params["limit"] = int(limit)
    return client.get("/geo/1.0/direct", params)


def geocode_zip(zip_code: str, country_code: str, client: Optional[OpenWeatherClient] = None) -> Any:
    """GET /geo/1.0/zip"""
    client = client or OpenWeatherClient()
    return client.get("/geo/1.0/zip", {"zip": f"{zip_code},{country_code}"})


def geocode_reverse(
    lat: float,
    lon: float,
    limit: Optional[int] = 5,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """GET /geo/1.0/reverse"""
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"lat": float(lat), "lon": float(lon)}
    if limit is not None:
        params["limit"] = int(limit)
    return client.get("/geo/1.0/reverse", params)
