"""
Tools for OpenWeatherMap Current Weather Data API (v2.5).
Endpoint base: https://api.openweathermap.org/data/2.5/weather
"""

import os
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def _api_key() -> str:
    key = os.environ.get("OPENWEATHER_API_KEY", "")
    if not key:
        raise ValueError("OPENWEATHER_API_KEY environment variable is not set")
    return key


def _get(params: dict) -> dict:
    """Internal HTTP helper — not exposed as an MCP tool."""
    try:
        params["appid"] = _api_key()
        resp = requests.get(BASE_URL, params=params, timeout=10)
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

def get_current_weather_by_coordinates(
    latitude: float,
    longitude: float,
    units: str = "standard",
    language: str = "en",
) -> dict:
    """
    Get current weather data for a specific geographic location.

    Args:
        latitude:  Latitude of the location (e.g. 44.34).
        longitude: Longitude of the location (e.g. 10.99).
        units:     Unit system — 'standard' (Kelvin), 'metric' (Celsius),
                   or 'imperial' (Fahrenheit). Defaults to 'standard'.
        language:  Language code for weather descriptions (e.g. 'en', 'de',
                   'fr'). Defaults to 'en'.

    Returns:
        JSON dict with coord, weather, main (temp, feels_like, humidity,
        pressure), wind, clouds, visibility, rain/snow, sys (sunrise/sunset),
        timezone, city name, and more.
    """
    return _get({
        "latitude": latitude,
        "longitude": longitude,
        "units": units,
        "lang": language,
    })


def get_current_weather_by_city_name(
    city_name: str,
    state_code: str = "",
    country_code: str = "",
    units: str = "standard",
    language: str = "en",
) -> dict:
    """
    Get current weather data by city name (optionally with state/country).

    Args:
        city_name:    Name of the city (e.g. 'London').
        state_code:   US state code (e.g. 'CA'). Only applicable for US cities.
        country_code: ISO 3166 country code (e.g. 'GB', 'US').
        units:        Unit system — 'standard', 'metric', or 'imperial'.
        language:     Language code for weather descriptions.

    Returns:
        JSON dict with current weather data (same structure as coordinate-based
        call).
    """
    parts = [city_name]
    if state_code:
        parts.append(state_code)
    if country_code:
        parts.append(country_code)
    q = ",".join(parts)
    return _get({"q": q, "units": units, "lang": language})


def get_current_weather_by_city_id(
    city_id: int,
    units: str = "standard",
    language: str = "en",
) -> dict:
    """
    Get current weather data by OpenWeatherMap city ID.

    Args:
        city_id:  Numeric city ID from the OpenWeatherMap city list.
        units:    Unit system — 'standard', 'metric', or 'imperial'.
        language: Language code for weather descriptions.

    Returns:
        JSON dict with current weather data.
    """
    return _get({"id": city_id, "units": units, "lang": language})


def get_current_weather_by_zip_code(
    zip_code: str,
    country_code: str = "US",
    units: str = "standard",
    language: str = "en",
) -> dict:
    """
    Get current weather data by ZIP / postal code and country.

    Args:
        zip_code:     ZIP or postal code (e.g. '90210' or 'E14').
        country_code: ISO 3166 country code (e.g. 'US', 'GB'). Defaults to
                      'US'.
        units:        Unit system — 'standard', 'metric', or 'imperial'.
        language:     Language code for weather descriptions.

    Returns:
        JSON dict with current weather data.
    """
    return _get({
        "zip": f"{zip_code},{country_code}",
        "units": units,
        "lang": language,
    })
