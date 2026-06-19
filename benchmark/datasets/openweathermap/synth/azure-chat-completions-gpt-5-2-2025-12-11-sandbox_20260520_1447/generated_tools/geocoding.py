from typing import Any, Dict, Optional

from .http_client import OpenWeatherClient


def geocode_direct(
    q: str,
    limit: int = 5,
    *,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Direct geocoding: location name -> coordinates.

    Endpoint: GET /geo/1.0/direct
    Docs: docs/api_geocoding.md
    """
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"q": q, "limit": limit}
    return client._request("/geo/1.0/direct", params=params)


def geocode_zip(
    zip_code: str,
    country_code: str,
    *,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Zip/post code geocoding: zip -> coordinates.

    Endpoint: GET /geo/1.0/zip
    Docs: docs/api_geocoding.md
    """
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"zip": f"{zip_code},{country_code}"}
    return client._request("/geo/1.0/zip", params=params)


def geocode_reverse(
    lat: float,
    lon: float,
    limit: int = 5,
    *,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Reverse geocoding: coordinates -> nearby place names.

    Endpoint: GET /geo/1.0/reverse
    Docs: docs/api_geocoding.md
    """
    client = client or OpenWeatherClient()
    params: Dict[str, Any] = {"lat": lat, "lon": lon, "limit": limit}
    return client._request("/geo/1.0/reverse", params=params)
