from typing import Any, Dict, Optional

from .client import OpenWeatherClient, _clean_none


def geocode_direct(
    client: OpenWeatherClient,
    query: str,
    limit: int = 5,
) -> Dict[str, Any]:
    """Direct geocoding: name -> coordinates.

    Endpoint: GET /geo/1.0/direct?q={query}&limit={limit}
    """
    params = _clean_none({"q": query, "limit": limit})
    return client._request("/geo/1.0/direct", params=params)


def geocode_reverse(
    client: OpenWeatherClient,
    lat: float,
    lon: float,
    limit: int = 5,
) -> Dict[str, Any]:
    """Reverse geocoding: coordinates -> place names.

    Endpoint: GET /geo/1.0/reverse?lat={lat}&lon={lon}&limit={limit}
    """
    params = _clean_none({"lat": lat, "lon": lon, "limit": limit})
    return client._request("/geo/1.0/reverse", params=params)


def geocode_zip(
    client: OpenWeatherClient,
    zip_code: str,
    country_code: Optional[str] = None,
) -> Dict[str, Any]:
    """Geocoding by ZIP/postal code.

    Endpoint: GET /geo/1.0/zip?zip={zip},{country}
    """
    z = zip_code
    if country_code:
        z += f",{country_code}"
    params = _clean_none({"zip": z})
    return client._request("/geo/1.0/zip", params=params)
