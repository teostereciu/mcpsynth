from typing import Any, Dict, Optional

from .http_client import OpenWeatherClient


def geocode_direct(
    q: str,
    limit: int = 5,
    *,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Direct geocoding: get coordinates by location name.

    Endpoint: /geo/1.0/direct
    Params:
      - q: "city,state,country" (state only for US)
      - limit: up to 5
    """
    client = client or OpenWeatherClient()
    return client._request("/geo/1.0/direct", {"q": q, "limit": limit})


def geocode_zip(zip_code: str, country_code: str, *, client: Optional[OpenWeatherClient] = None) -> Any:
    """Geocoding by zip/post code.

    Endpoint: /geo/1.0/zip
    Params:
      - zip: "{zip},{country}"
    """
    client = client or OpenWeatherClient()
    return client._request("/geo/1.0/zip", {"zip": f"{zip_code},{country_code}"})


def geocode_reverse(
    lat: float,
    lon: float,
    limit: int = 5,
    *,
    client: Optional[OpenWeatherClient] = None,
) -> Any:
    """Reverse geocoding: get location names by coordinates.

    Endpoint: /geo/1.0/reverse
    Params:
      - lat, lon
      - limit
    """
    client = client or OpenWeatherClient()
    return client._request("/geo/1.0/reverse", {"lat": lat, "lon": lon, "limit": limit})
