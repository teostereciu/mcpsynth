from typing import Any, Dict, Optional

from .http import owm_get


def geocode_direct(q: str, limit: int = 5) -> Dict[str, Any]:
    """Direct geocoding: location name -> coordinates.

    Endpoint: GET /geo/1.0/direct
    Docs: docs/api_geocoding.md
    """
    params: Dict[str, Any] = {"q": q, "limit": limit}
    return owm_get("/geo/1.0/direct", params)


def geocode_zip(zip_code: str, country_code: Optional[str] = None) -> Dict[str, Any]:
    """Geocode by zip/post code.

    Endpoint: GET /geo/1.0/zip
    Docs: docs/api_geocoding.md
    """
    z = zip_code if country_code is None else f"{zip_code},{country_code}"
    params: Dict[str, Any] = {"zip": z}
    return owm_get("/geo/1.0/zip", params)


def geocode_reverse(latitude: float, longitude: float, limit: int = 5) -> Dict[str, Any]:
    """Reverse geocoding: coordinates -> nearby location names.

    Endpoint: GET /geo/1.0/reverse
    Docs: docs/api_geocoding.md
    """
    params: Dict[str, Any] = {"latitude": latitude, "longitude": longitude, "limit": limit}
    return owm_get("/geo/1.0/reverse", params)
