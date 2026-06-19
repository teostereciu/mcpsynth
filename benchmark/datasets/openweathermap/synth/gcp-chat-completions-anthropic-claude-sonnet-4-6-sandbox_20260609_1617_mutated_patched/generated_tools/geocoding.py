"""
Tools for OpenWeatherMap Geocoding API (v1.0).
Endpoints:
  - GET /geo/1.0/direct  (city name → coordinates)
  - GET /geo/1.0/zip     (zip/postal code → coordinates)
  - GET /geo/1.0/reverse (coordinates → location names)
"""

import os
import requests

_BASE = "https://api.openweathermap.org/geo/1.0"


def _api_key() -> str:
    key = os.environ.get("OPENWEATHER_API_KEY", "")
    if not key:
        raise ValueError("OPENWEATHER_API_KEY environment variable is not set")
    return key


def _get(path: str, params: dict):
    """Internal HTTP helper — not exposed as an MCP tool."""
    try:
        params["appid"] = _api_key()
        url = f"{_BASE}/{path}"
        resp = requests.get(url, params=params, timeout=10)
        if resp.status_code == 200:
            return resp.json()
        try:
            err = resp.json()
        except Exception:
            err = {"message": resp.text}
        return {"error": f"HTTP {resp.status_code}", "details": err}
    except ValueError as exc:
        return {"error": str(exc)}
    except requests.RequestException as exc:
        return {"error": f"Request failed: {exc}"}


# ── Tool functions ────────────────────────────────────────────────────────────

def geocode_by_location_name(
    city_name: str,
    state_code: str = "",
    country_code: str = "",
    limit: int = 5,
) -> list:
    """
    Convert a city / location name into geographic coordinates (direct geocoding).

    Useful for resolving ambiguous city names — e.g. 'London' exists in both
    the UK and the US; use country_code to disambiguate.

    Args:
        city_name:    Name of the city or area (e.g. 'London', 'New York').
        state_code:   US state code (only for US locations, e.g. 'NY').
        country_code: ISO 3166 country code (e.g. 'GB', 'US').
        limit:        Maximum number of results to return (1–5). Defaults to 5.

    Returns:
        List of matching location dicts, each containing:
          - name: location name
          - lat, lon: geographic coordinates
          - country: country code
          - state: state (where available)
          - local_names: dict of names in various languages (where available)
        Returns a dict with 'error' key on failure.
    """
    parts = [city_name]
    if state_code:
        parts.append(state_code)
    if country_code:
        parts.append(country_code)
    return _get("direct", {"q": ",".join(parts), "limit": limit})


def geocode_by_zip_code(zip_code: str, country_code: str = "US") -> dict:
    """
    Convert a ZIP / postal code into geographic coordinates.

    Args:
        zip_code:     ZIP or postal code (e.g. '90210', 'E14', 'SW1A 1AA').
        country_code: ISO 3166 country code (e.g. 'US', 'GB'). Defaults to
                      'US'.

    Returns:
        Dict containing:
          - zip: the requested zip code
          - name: name of the found area
          - lat, lon: geographic coordinates of the centroid
          - country: country code
        Returns a dict with 'error' key on failure.
    """
    return _get("zip", {"zip": f"{zip_code},{country_code}"})


def reverse_geocode(
    latitude: float,
    longitude: float,
    limit: int = 5,
) -> list:
    """
    Convert geographic coordinates into location / city names (reverse geocoding).

    Args:
        latitude:  Latitude of the location.
        longitude: Longitude of the location.
        limit:     Maximum number of location names to return. Defaults to 5.

    Returns:
        List of nearby location dicts, each containing:
          - name: location name
          - lat, lon: geographic coordinates
          - country: country code
          - state: state (where available)
          - local_names: dict of names in various languages (where available)
        Returns a dict with 'error' key on failure.
    """
    return _get(
        "reverse",
        {"lat": latitude, "lon": longitude, "limit": limit},
    )
