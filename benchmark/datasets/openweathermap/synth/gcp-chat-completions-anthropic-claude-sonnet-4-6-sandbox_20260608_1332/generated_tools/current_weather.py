"""
Tools for OpenWeatherMap Current Weather Data API (2.5).
Endpoint base: https://api.openweathermap.org/data/2.5/weather
"""

import os
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def _api_key() -> str:
    key = os.environ.get("OPENWEATHER_API_KEY", "")
    if not key:
        raise RuntimeError("OPENWEATHER_API_KEY environment variable is not set")
    return key


def _get(params: dict) -> dict:
    """Internal HTTP helper — not exposed as an MCP tool."""
    try:
        params["appid"] = _api_key()
        resp = requests.get(BASE_URL, params=params, timeout=10)
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

def get_current_weather_by_coordinates(
    lat: float,
    lon: float,
    units: str = "standard",
    lang: str | None = None,
) -> dict:
    """
    Get current weather data for a specific geographic location.

    Args:
        lat:   Latitude of the location.
        lon:   Longitude of the location.
        units: Units of measurement — 'standard' (Kelvin), 'metric' (Celsius),
               or 'imperial' (Fahrenheit). Defaults to 'standard'.
        lang:  Optional language code for weather descriptions (e.g. 'en', 'de').

    Returns:
        Current weather data as a dict, or an error dict.
    """
    params: dict = {"lat": lat, "lon": lon, "units": units}
    if lang:
        params["lang"] = lang
    return _get(params)


def get_current_weather_by_city_name(
    city_name: str,
    state_code: str | None = None,
    country_code: str | None = None,
    units: str = "standard",
    lang: str | None = None,
) -> dict:
    """
    Get current weather data by city name (optionally with state/country code).

    Args:
        city_name:    Name of the city (e.g. 'London').
        state_code:   US state code (e.g. 'CA'). Only applicable for US locations.
        country_code: ISO 3166 country code (e.g. 'GB').
        units:        Units of measurement — 'standard', 'metric', or 'imperial'.
        lang:         Optional language code for weather descriptions.

    Returns:
        Current weather data as a dict, or an error dict.

    Note: Built-in geocoding by city name is deprecated; prefer
          get_current_weather_by_coordinates with geocoding results.
    """
    q_parts = [city_name]
    if state_code:
        q_parts.append(state_code)
    if country_code:
        q_parts.append(country_code)
    params: dict = {"q": ",".join(q_parts), "units": units}
    if lang:
        params["lang"] = lang
    return _get(params)


def get_current_weather_by_city_id(
    city_id: int,
    units: str = "standard",
    lang: str | None = None,
) -> dict:
    """
    Get current weather data by OpenWeatherMap city ID.

    Args:
        city_id: Numeric city ID (e.g. 2643743 for London).
        units:   Units of measurement — 'standard', 'metric', or 'imperial'.
        lang:    Optional language code for weather descriptions.

    Returns:
        Current weather data as a dict, or an error dict.

    Note: Built-in geocoding by city ID is deprecated; prefer coordinates.
    """
    params: dict = {"id": city_id, "units": units}
    if lang:
        params["lang"] = lang
    return _get(params)


def get_current_weather_by_zip_code(
    zip_code: str,
    country_code: str = "US",
    units: str = "standard",
    lang: str | None = None,
) -> dict:
    """
    Get current weather data by ZIP / postal code and country code.

    Args:
        zip_code:     ZIP or postal code (e.g. '90210').
        country_code: ISO 3166 country code (e.g. 'US', 'GB'). Defaults to 'US'.
        units:        Units of measurement — 'standard', 'metric', or 'imperial'.
        lang:         Optional language code for weather descriptions.

    Returns:
        Current weather data as a dict, or an error dict.

    Note: Built-in geocoding by zip code is deprecated; prefer coordinates.
    """
    params: dict = {"zip": f"{zip_code},{country_code}", "units": units}
    if lang:
        params["lang"] = lang
    return _get(params)
