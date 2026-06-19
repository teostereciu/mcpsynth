"""
Tools for OpenWeatherMap Geocoding API (1.0).
Endpoints:
  - GET /geo/1.0/direct  (city name → coordinates)
  - GET /geo/1.0/zip     (zip/post code → coordinates)
  - GET /geo/1.0/reverse (coordinates → location names)
"""

import os
import requests

_BASE = "https://api.openweathermap.org/geo/1.0"


def _api_key() -> str:
    key = os.environ.get("OPENWEATHER_API_KEY", "")
    if not key:
        raise RuntimeError("OPENWEATHER_API_KEY environment variable is not set")
    return key


def _get(path: str, params: dict) -> dict | list:
    """Internal HTTP helper — not exposed as an MCP tool."""
    try:
        params["appid"] = _api_key()
        resp = requests.get(f"{_BASE}{path}", params=params, timeout=10)
        if resp.status_code == 200:
            return resp.json()
        try:
            body = resp.json()
        except Exception:
            body = resp.text
        return {"error": f"HTTP {resp.status_code}", "details": body}
    except RuntimeError as exc:
        return {"error": str(exc)}
    except requests.RequestException as exc:
        return {"error": f"Request failed: {exc}"}


# ── Tool functions ────────────────────────────────────────────────────────────

def geocode_by_location_name(
    city_name: str,
    state_code: str | None = None,
    country_code: str | None = None,
    limit: int = 5,
) -> list | dict:
    """
    Convert a city or area name into geographic coordinates (direct geocoding).

    Args:
        city_name:    Name of the city or area (e.g. 'London', 'New York').
        state_code:   US state code (only for US locations, e.g. 'NY').
        country_code: ISO 3166 country code (e.g. 'GB', 'US').
        limit:        Maximum number of results to return (1–5). Defaults to 5.

    Returns:
        List of matching locations, each with 'name', 'lat', 'lon', 'country',
        and optionally 'state' and 'local_names'. Returns an error dict on failure.
    """
    q_parts = [city_name]
    if state_code:
        q_parts.append(state_code)
    if country_code:
        q_parts.append(country_code)
    return _get("/direct", {"q": ",".join(q_parts), "limit": limit})


def geocode_by_zip_code(
    zip_code: str,
    country_code: str = "US",
) -> dict:
    """
    Convert a ZIP / postal code into geographic coordinates.

    Args:
        zip_code:     ZIP or postal code (e.g. '90210', 'E14').
        country_code: ISO 3166 country code (e.g. 'US', 'GB'). Defaults to 'US'.

    Returns:
        Dict with 'zip', 'name', 'lat', 'lon', 'country', or an error dict.
    """
    return _get("/zip", {"zip": f"{zip_code},{country_code}"})


def reverse_geocode(
    lat: float,
    lon: float,
    limit: int = 5,
) -> list | dict:
    """
    Convert geographic coordinates into location names (reverse geocoding).

    Args:
        lat:   Latitude of the location.
        lon:   Longitude of the location.
        limit: Maximum number of location names to return. Defaults to 5.

    Returns:
        List of nearby locations, each with 'name', 'lat', 'lon', 'country',
        and optionally 'state' and 'local_names'. Returns an error dict on failure.
    """
    return _get("/reverse", {"lat": lat, "lon": lon, "limit": limit})
