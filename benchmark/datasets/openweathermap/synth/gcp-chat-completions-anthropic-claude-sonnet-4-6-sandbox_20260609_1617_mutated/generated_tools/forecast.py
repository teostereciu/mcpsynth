"""
Tools for OpenWeatherMap 5-Day / 3-Hour Forecast API (v2.5).
Endpoint base: https://api.openweathermap.org/data/2.5/forecast
"""

import os
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"


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

def get_forecast_by_coordinates(
    latitude: float,
    longitude: float,
    units: str = "standard",
    language: str = "en",
    count: int = 0,
) -> dict:
    """
    Get a 5-day weather forecast (3-hour step) for a geographic location.

    Args:
        latitude:  Latitude of the location.
        longitude: Longitude of the location.
        units:     Unit system — 'standard' (Kelvin), 'metric' (Celsius),
                   or 'imperial' (Fahrenheit). Defaults to 'standard'.
        language:  Language code for weather descriptions (e.g. 'en', 'de').
        count:     Number of 3-hour timestamps to return (0 = all, up to 40).

    Returns:
        JSON dict with 'list' of up to 40 forecast entries (each with dt,
        main, weather, clouds, wind, visibility, pop, rain/snow, sys, dt_txt)
        and 'city' metadata (name, coord, country, timezone, sunrise, sunset).
    """
    params: dict = {
        "latitude": latitude,
        "longitude": longitude,
        "units": units,
        "lang": language,
    }
    if count > 0:
        params["cnt"] = count
    return _get(params)


def get_forecast_by_city_name(
    city_name: str,
    state_code: str = "",
    country_code: str = "",
    units: str = "standard",
    language: str = "en",
    count: int = 0,
) -> dict:
    """
    Get a 5-day / 3-hour forecast by city name (optionally with state/country).

    Args:
        city_name:    Name of the city (e.g. 'Paris').
        state_code:   US state code (only for US cities, e.g. 'TX').
        country_code: ISO 3166 country code (e.g. 'FR', 'US').
        units:        Unit system — 'standard', 'metric', or 'imperial'.
        language:     Language code for weather descriptions.
        count:        Number of 3-hour timestamps to return (0 = all).

    Returns:
        JSON dict with forecast list and city metadata.
    """
    parts = [city_name]
    if state_code:
        parts.append(state_code)
    if country_code:
        parts.append(country_code)
    params: dict = {"q": ",".join(parts), "units": units, "lang": language}
    if count > 0:
        params["cnt"] = count
    return _get(params)


def get_forecast_by_city_id(
    city_id: int,
    units: str = "standard",
    language: str = "en",
    count: int = 0,
) -> dict:
    """
    Get a 5-day / 3-hour forecast by OpenWeatherMap city ID.

    Args:
        city_id:  Numeric city ID from the OpenWeatherMap city list.
        units:    Unit system — 'standard', 'metric', or 'imperial'.
        language: Language code for weather descriptions.
        count:    Number of 3-hour timestamps to return (0 = all).

    Returns:
        JSON dict with forecast list and city metadata.
    """
    params: dict = {"id": city_id, "units": units, "lang": language}
    if count > 0:
        params["cnt"] = count
    return _get(params)


def get_forecast_by_zip_code(
    zip_code: str,
    country_code: str = "US",
    units: str = "standard",
    language: str = "en",
    count: int = 0,
) -> dict:
    """
    Get a 5-day / 3-hour forecast by ZIP / postal code and country.

    Args:
        zip_code:     ZIP or postal code (e.g. '10001' or 'SW1A').
        country_code: ISO 3166 country code (e.g. 'US', 'GB'). Defaults to
                      'US'.
        units:        Unit system — 'standard', 'metric', or 'imperial'.
        language:     Language code for weather descriptions.
        count:        Number of 3-hour timestamps to return (0 = all).

    Returns:
        JSON dict with forecast list and city metadata.
    """
    params: dict = {
        "zip": f"{zip_code},{country_code}",
        "units": units,
        "lang": language,
    }
    if count > 0:
        params["cnt"] = count
    return _get(params)
