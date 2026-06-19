"""
Tools for OpenWeatherMap 5 Day / 3 Hour Forecast API (2.5).
Endpoint base: https://api.openweathermap.org/data/2.5/forecast
"""

import os
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"


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

def get_5day_forecast_by_coordinates(
    lat: float,
    lon: float,
    units: str = "standard",
    cnt: int | None = None,
    lang: str | None = None,
) -> dict:
    """
    Get a 5-day weather forecast with 3-hour step for a geographic location.

    Args:
        lat:   Latitude of the location.
        lon:   Longitude of the location.
        units: Units of measurement — 'standard' (Kelvin), 'metric' (Celsius),
               or 'imperial' (Fahrenheit). Defaults to 'standard'.
        cnt:   Optional number of 3-hour timestamps to return (max 40).
        lang:  Optional language code for weather descriptions (e.g. 'en', 'de').

    Returns:
        Forecast data dict with 'list' of up to 40 3-hour slots and 'city' info,
        or an error dict.
    """
    params: dict = {"lat": lat, "lon": lon, "units": units}
    if cnt is not None:
        params["cnt"] = cnt
    if lang:
        params["lang"] = lang
    return _get(params)


def get_5day_forecast_by_city_name(
    city_name: str,
    state_code: str | None = None,
    country_code: str | None = None,
    units: str = "standard",
    cnt: int | None = None,
    lang: str | None = None,
) -> dict:
    """
    Get a 5-day / 3-hour weather forecast by city name.

    Args:
        city_name:    Name of the city (e.g. 'Paris').
        state_code:   US state code (only for US locations, e.g. 'TX').
        country_code: ISO 3166 country code (e.g. 'FR').
        units:        Units of measurement — 'standard', 'metric', or 'imperial'.
        cnt:          Optional number of 3-hour timestamps to return (max 40).
        lang:         Optional language code for weather descriptions.

    Returns:
        Forecast data dict, or an error dict.

    Note: Built-in geocoding by city name is deprecated; prefer coordinates.
    """
    q_parts = [city_name]
    if state_code:
        q_parts.append(state_code)
    if country_code:
        q_parts.append(country_code)
    params: dict = {"q": ",".join(q_parts), "units": units}
    if cnt is not None:
        params["cnt"] = cnt
    if lang:
        params["lang"] = lang
    return _get(params)


def get_5day_forecast_by_city_id(
    city_id: int,
    units: str = "standard",
    cnt: int | None = None,
    lang: str | None = None,
) -> dict:
    """
    Get a 5-day / 3-hour weather forecast by OpenWeatherMap city ID.

    Args:
        city_id: Numeric city ID (e.g. 524901 for Moscow).
        units:   Units of measurement — 'standard', 'metric', or 'imperial'.
        cnt:     Optional number of 3-hour timestamps to return (max 40).
        lang:    Optional language code for weather descriptions.

    Returns:
        Forecast data dict, or an error dict.

    Note: Built-in geocoding by city ID is deprecated; prefer coordinates.
    """
    params: dict = {"id": city_id, "units": units}
    if cnt is not None:
        params["cnt"] = cnt
    if lang:
        params["lang"] = lang
    return _get(params)


def get_5day_forecast_by_zip_code(
    zip_code: str,
    country_code: str = "US",
    units: str = "standard",
    cnt: int | None = None,
    lang: str | None = None,
) -> dict:
    """
    Get a 5-day / 3-hour weather forecast by ZIP / postal code.

    Args:
        zip_code:     ZIP or postal code (e.g. '10001').
        country_code: ISO 3166 country code (e.g. 'US', 'DE'). Defaults to 'US'.
        units:        Units of measurement — 'standard', 'metric', or 'imperial'.
        cnt:          Optional number of 3-hour timestamps to return (max 40).
        lang:         Optional language code for weather descriptions.

    Returns:
        Forecast data dict, or an error dict.

    Note: Built-in geocoding by zip code is deprecated; prefer coordinates.
    """
    params: dict = {"zip": f"{zip_code},{country_code}", "units": units}
    if cnt is not None:
        params["cnt"] = cnt
    if lang:
        params["lang"] = lang
    return _get(params)
