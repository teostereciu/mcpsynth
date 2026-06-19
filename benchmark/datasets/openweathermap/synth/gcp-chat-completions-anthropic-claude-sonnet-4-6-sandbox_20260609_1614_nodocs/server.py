"""
MCP Server for OpenWeatherMap API (Free Tier)
Covers:
  - Current Weather Data (API 2.5)
  - 5-Day / 3-Hour Forecast (API 2.5)
  - Air Pollution API
  - Geocoding API (direct + reverse)
"""

import os
import requests
from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Initialisation
# ---------------------------------------------------------------------------

mcp = FastMCP("openweathermap")

BASE_URL = "https://api.openweathermap.org"
API_KEY = os.environ.get("OPENWEATHER_API_KEY", "")


# ---------------------------------------------------------------------------
# Internal HTTP helper (NOT registered as a tool)
# ---------------------------------------------------------------------------

def _get(path: str, params: dict) -> dict | list:
    """Execute a GET request against the OpenWeatherMap API.

    Injects the API key automatically and returns parsed JSON.
    On any HTTP or network error a dict with an ``error`` key is returned
    so callers never have to deal with unhandled exceptions.
    """
    if not API_KEY:
        return {"error": "OPENWEATHER_API_KEY environment variable is not set."}

    params = {k: v for k, v in params.items() if v is not None}
    params["appid"] = API_KEY

    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=10)
        if resp.status_code == 200:
            return resp.json()
        # Surface the API's own error message when available
        try:
            body = resp.json()
            message = body.get("message", resp.text)
        except Exception:
            message = resp.text
        return {"error": f"HTTP {resp.status_code}: {message}"}
    except requests.exceptions.Timeout:
        return {"error": "Request timed out."}
    except requests.exceptions.ConnectionError as exc:
        return {"error": f"Connection error: {exc}"}
    except Exception as exc:
        return {"error": f"Unexpected error: {exc}"}


# ===========================================================================
# CURRENT WEATHER DATA  (API 2.5)
# ===========================================================================

@mcp.tool()
def get_current_weather_by_city(
    city: str,
    country_code: str = None,
    state_code: str = None,
    units: str = "metric",
    lang: str = "en",
) -> dict:
    """Get the current weather for a city by name.

    Args:
        city: City name (e.g. "London").
        country_code: ISO 3166 two-letter country code (e.g. "GB"). Optional
            but recommended to disambiguate city names.
        state_code: US state code (e.g. "CA"). Only relevant for US cities.
        units: Unit system – "metric" (°C, m/s), "imperial" (°F, mph), or
            "standard" (K, m/s). Defaults to "metric".
        lang: Language code for weather descriptions (e.g. "en", "de", "fr").
            Defaults to "en".

    Returns:
        Full current-weather JSON from OpenWeatherMap, or a dict with an
        ``error`` key on failure.
    """
    q_parts = [city]
    if state_code:
        q_parts.append(state_code)
    if country_code:
        q_parts.append(country_code)
    q = ",".join(q_parts)

    return _get("/data/2.5/weather", {"q": q, "units": units, "lang": lang})


@mcp.tool()
def get_current_weather_by_coordinates(
    lat: float,
    lon: float,
    units: str = "metric",
    lang: str = "en",
) -> dict:
    """Get the current weather for a specific geographic location.

    Args:
        lat: Latitude in decimal degrees (e.g. 51.5074).
        lon: Longitude in decimal degrees (e.g. -0.1278).
        units: Unit system – "metric", "imperial", or "standard".
        lang: Language code for weather descriptions.

    Returns:
        Full current-weather JSON from OpenWeatherMap, or a dict with an
        ``error`` key on failure.
    """
    return _get("/data/2.5/weather", {"lat": lat, "lon": lon, "units": units, "lang": lang})


@mcp.tool()
def get_current_weather_by_zip(
    zip_code: str,
    country_code: str = "US",
    units: str = "metric",
    lang: str = "en",
) -> dict:
    """Get the current weather for a location identified by ZIP / postal code.

    Args:
        zip_code: ZIP or postal code (e.g. "90210").
        country_code: ISO 3166 two-letter country code. Defaults to "US".
        units: Unit system – "metric", "imperial", or "standard".
        lang: Language code for weather descriptions.

    Returns:
        Full current-weather JSON from OpenWeatherMap, or a dict with an
        ``error`` key on failure.
    """
    zip_param = f"{zip_code},{country_code}"
    return _get("/data/2.5/weather", {"zip": zip_param, "units": units, "lang": lang})


@mcp.tool()
def get_current_weather_by_city_id(
    city_id: int,
    units: str = "metric",
    lang: str = "en",
) -> dict:
    """Get the current weather using an OpenWeatherMap city ID.

    City IDs can be found via the geocoding tools or the OWM city list.

    Args:
        city_id: Numeric OpenWeatherMap city identifier.
        units: Unit system – "metric", "imperial", or "standard".
        lang: Language code for weather descriptions.

    Returns:
        Full current-weather JSON from OpenWeatherMap, or a dict with an
        ``error`` key on failure.
    """
    return _get("/data/2.5/weather", {"id": city_id, "units": units, "lang": lang})


# ===========================================================================
# 5-DAY / 3-HOUR FORECAST  (API 2.5)
# ===========================================================================

@mcp.tool()
def get_forecast_by_city(
    city: str,
    country_code: str = None,
    state_code: str = None,
    cnt: int = None,
    units: str = "metric",
    lang: str = "en",
) -> dict:
    """Get a 5-day weather forecast (3-hour intervals) for a city by name.

    Args:
        city: City name (e.g. "Paris").
        country_code: ISO 3166 two-letter country code. Optional.
        state_code: US state code. Only relevant for US cities.
        cnt: Number of forecast time-steps to return (max 40, i.e. 5 days).
            Omit to receive all available steps.
        units: Unit system – "metric", "imperial", or "standard".
        lang: Language code for weather descriptions.

    Returns:
        Forecast JSON containing a ``list`` of up to 40 three-hour slots, or
        a dict with an ``error`` key on failure.
    """
    q_parts = [city]
    if state_code:
        q_parts.append(state_code)
    if country_code:
        q_parts.append(country_code)
    q = ",".join(q_parts)

    return _get("/data/2.5/forecast", {"q": q, "cnt": cnt, "units": units, "lang": lang})


@mcp.tool()
def get_forecast_by_coordinates(
    lat: float,
    lon: float,
    cnt: int = None,
    units: str = "metric",
    lang: str = "en",
) -> dict:
    """Get a 5-day weather forecast (3-hour intervals) for a geographic location.

    Args:
        lat: Latitude in decimal degrees.
        lon: Longitude in decimal degrees.
        cnt: Number of forecast time-steps to return (max 40). Omit for all.
        units: Unit system – "metric", "imperial", or "standard".
        lang: Language code for weather descriptions.

    Returns:
        Forecast JSON containing a ``list`` of up to 40 three-hour slots, or
        a dict with an ``error`` key on failure.
    """
    return _get(
        "/data/2.5/forecast",
        {"lat": lat, "lon": lon, "cnt": cnt, "units": units, "lang": lang},
    )


@mcp.tool()
def get_forecast_by_zip(
    zip_code: str,
    country_code: str = "US",
    cnt: int = None,
    units: str = "metric",
    lang: str = "en",
) -> dict:
    """Get a 5-day weather forecast (3-hour intervals) for a ZIP / postal code.

    Args:
        zip_code: ZIP or postal code.
        country_code: ISO 3166 two-letter country code. Defaults to "US".
        cnt: Number of forecast time-steps to return (max 40). Omit for all.
        units: Unit system – "metric", "imperial", or "standard".
        lang: Language code for weather descriptions.

    Returns:
        Forecast JSON containing a ``list`` of up to 40 three-hour slots, or
        a dict with an ``error`` key on failure.
    """
    zip_param = f"{zip_code},{country_code}"
    return _get(
        "/data/2.5/forecast",
        {"zip": zip_param, "cnt": cnt, "units": units, "lang": lang},
    )


@mcp.tool()
def get_forecast_by_city_id(
    city_id: int,
    cnt: int = None,
    units: str = "metric",
    lang: str = "en",
) -> dict:
    """Get a 5-day weather forecast (3-hour intervals) using an OWM city ID.

    Args:
        city_id: Numeric OpenWeatherMap city identifier.
        cnt: Number of forecast time-steps to return (max 40). Omit for all.
        units: Unit system – "metric", "imperial", or "standard".
        lang: Language code for weather descriptions.

    Returns:
        Forecast JSON containing a ``list`` of up to 40 three-hour slots, or
        a dict with an ``error`` key on failure.
    """
    return _get(
        "/data/2.5/forecast",
        {"id": city_id, "cnt": cnt, "units": units, "lang": lang},
    )


# ===========================================================================
# AIR POLLUTION API
# ===========================================================================

@mcp.tool()
def get_current_air_pollution(lat: float, lon: float) -> dict:
    """Get the current air pollution data for a geographic location.

    Returns the Air Quality Index (AQI) and concentrations of major
    pollutants: CO, NO, NO₂, O₃, SO₂, PM2.5, PM10, NH₃.

    AQI scale: 1 = Good, 2 = Fair, 3 = Moderate, 4 = Poor, 5 = Very Poor.

    Args:
        lat: Latitude in decimal degrees.
        lon: Longitude in decimal degrees.

    Returns:
        Air pollution JSON with ``list`` containing one entry for the current
        moment, or a dict with an ``error`` key on failure.
    """
    return _get("/data/2.5/air_pollution", {"lat": lat, "lon": lon})


@mcp.tool()
def get_air_pollution_forecast(lat: float, lon: float) -> dict:
    """Get the air pollution forecast for a geographic location.

    Provides hourly AQI and pollutant concentration forecasts for the next
    ~5 days.

    Args:
        lat: Latitude in decimal degrees.
        lon: Longitude in decimal degrees.

    Returns:
        Air pollution forecast JSON with a ``list`` of hourly entries, or a
        dict with an ``error`` key on failure.
    """
    return _get("/data/2.5/air_pollution/forecast", {"lat": lat, "lon": lon})


@mcp.tool()
def get_historical_air_pollution(
    lat: float,
    lon: float,
    start: int,
    end: int,
) -> dict:
    """Get historical air pollution data for a geographic location.

    Args:
        lat: Latitude in decimal degrees.
        lon: Longitude in decimal degrees.
        start: Start of the time range as a Unix timestamp (UTC).
        end: End of the time range as a Unix timestamp (UTC).

    Returns:
        Historical air pollution JSON with a ``list`` of hourly entries, or a
        dict with an ``error`` key on failure.
    """
    return _get(
        "/data/2.5/air_pollution/history",
        {"lat": lat, "lon": lon, "start": start, "end": end},
    )


# ===========================================================================
# GEOCODING API
# ===========================================================================

@mcp.tool()
def geocode_by_city_name(
    city: str,
    country_code: str = None,
    state_code: str = None,
    limit: int = 5,
) -> list:
    """Convert a city name to geographic coordinates (direct geocoding).

    Useful as a first step before calling weather or air-pollution endpoints
    that require lat/lon.

    Args:
        city: City name (e.g. "Amsterdam").
        country_code: ISO 3166 two-letter country code. Optional.
        state_code: US state code. Only relevant for US cities.
        limit: Maximum number of results to return (1–5). Defaults to 5.

    Returns:
        List of matching locations, each with ``name``, ``lat``, ``lon``,
        ``country``, and ``state`` fields. Returns a dict with an ``error``
        key on failure.
    """
    q_parts = [city]
    if state_code:
        q_parts.append(state_code)
    if country_code:
        q_parts.append(country_code)
    q = ",".join(q_parts)

    return _get("/geo/1.0/direct", {"q": q, "limit": limit})


@mcp.tool()
def geocode_by_zip(zip_code: str, country_code: str = "US") -> dict:
    """Convert a ZIP / postal code to geographic coordinates.

    Args:
        zip_code: ZIP or postal code (e.g. "10001").
        country_code: ISO 3166 two-letter country code. Defaults to "US".

    Returns:
        A single location dict with ``name``, ``lat``, ``lon``, ``country``,
        and ``zip`` fields, or a dict with an ``error`` key on failure.
    """
    zip_param = f"{zip_code},{country_code}"
    return _get("/geo/1.0/zip", {"zip": zip_param})


@mcp.tool()
def reverse_geocode(lat: float, lon: float, limit: int = 5) -> list:
    """Convert geographic coordinates to human-readable location names.

    Args:
        lat: Latitude in decimal degrees.
        lon: Longitude in decimal degrees.
        limit: Maximum number of results to return (1–5). Defaults to 5.

    Returns:
        List of matching locations, each with ``name``, ``lat``, ``lon``,
        ``country``, and ``state`` fields. Returns a dict with an ``error``
        key on failure.
    """
    return _get("/geo/1.0/reverse", {"lat": lat, "lon": lon, "limit": limit})


# ===========================================================================
# CONVENIENCE / MULTI-STEP WORKFLOW TOOLS
# ===========================================================================

@mcp.tool()
def get_weather_and_forecast_by_city(
    city: str,
    country_code: str = None,
    state_code: str = None,
    forecast_steps: int = 8,
    units: str = "metric",
    lang: str = "en",
) -> dict:
    """Get both current weather AND the short-range forecast for a city in one call.

    Combines ``get_current_weather_by_city`` and ``get_forecast_by_city`` to
    reduce round-trips in multi-step workflows.

    Args:
        city: City name.
        country_code: ISO 3166 two-letter country code. Optional.
        state_code: US state code. Optional.
        forecast_steps: Number of 3-hour forecast slots to include (default 8
            = 24 hours ahead).
        units: Unit system – "metric", "imperial", or "standard".
        lang: Language code for weather descriptions.

    Returns:
        Dict with keys ``current`` (current weather) and ``forecast`` (list of
        forecast slots), or a dict with an ``error`` key if either sub-call
        fails.
    """
    q_parts = [city]
    if state_code:
        q_parts.append(state_code)
    if country_code:
        q_parts.append(country_code)
    q = ",".join(q_parts)

    current = _get("/data/2.5/weather", {"q": q, "units": units, "lang": lang})
    if "error" in current:
        return current

    forecast = _get(
        "/data/2.5/forecast",
        {"q": q, "cnt": forecast_steps, "units": units, "lang": lang},
    )
    if "error" in forecast:
        return forecast

    return {"current": current, "forecast": forecast}


@mcp.tool()
def get_weather_and_air_quality_by_coordinates(
    lat: float,
    lon: float,
    units: str = "metric",
    lang: str = "en",
) -> dict:
    """Get current weather AND current air quality for a location in one call.

    Useful for health-aware or environmental monitoring workflows.

    Args:
        lat: Latitude in decimal degrees.
        lon: Longitude in decimal degrees.
        units: Unit system – "metric", "imperial", or "standard".
        lang: Language code for weather descriptions.

    Returns:
        Dict with keys ``weather`` (current weather) and ``air_pollution``
        (current AQI + pollutants), or a dict with an ``error`` key on failure.
    """
    weather = _get(
        "/data/2.5/weather", {"lat": lat, "lon": lon, "units": units, "lang": lang}
    )
    if "error" in weather:
        return weather

    air = _get("/data/2.5/air_pollution", {"lat": lat, "lon": lon})
    if "error" in air:
        return air

    return {"weather": weather, "air_pollution": air}


@mcp.tool()
def find_city_coordinates(
    city: str,
    country_code: str = None,
    state_code: str = None,
) -> dict:
    """Resolve a city name to its best-matching lat/lon coordinates.

    Returns only the top result from the geocoding API, making it easy to
    chain into other tools that require lat/lon.

    Args:
        city: City name.
        country_code: ISO 3166 two-letter country code. Optional.
        state_code: US state code. Optional.

    Returns:
        Dict with ``name``, ``lat``, ``lon``, ``country``, and optionally
        ``state``, or a dict with an ``error`` key on failure.
    """
    q_parts = [city]
    if state_code:
        q_parts.append(state_code)
    if country_code:
        q_parts.append(country_code)
    q = ",".join(q_parts)

    result = _get("/geo/1.0/direct", {"q": q, "limit": 1})
    if isinstance(result, dict) and "error" in result:
        return result
    if not result:
        return {"error": f"No geocoding results found for '{city}'."}
    return result[0]


@mcp.tool()
def get_full_location_report(
    city: str,
    country_code: str = None,
    state_code: str = None,
    forecast_steps: int = 8,
    units: str = "metric",
    lang: str = "en",
) -> dict:
    """Get a comprehensive environmental report for a city.

    Performs geocoding, then fetches current weather, short-range forecast,
    and current air quality — all in one tool call.

    Args:
        city: City name.
        country_code: ISO 3166 two-letter country code. Optional.
        state_code: US state code. Optional.
        forecast_steps: Number of 3-hour forecast slots (default 8 = 24 h).
        units: Unit system – "metric", "imperial", or "standard".
        lang: Language code for weather descriptions.

    Returns:
        Dict with keys ``location``, ``weather``, ``forecast``, and
        ``air_pollution``, or a dict with an ``error`` key on failure.
    """
    # Step 1 – geocode
    location = find_city_coordinates(city, country_code, state_code)
    if "error" in location:
        return location

    lat, lon = location["lat"], location["lon"]

    # Step 2 – current weather
    weather = _get(
        "/data/2.5/weather", {"lat": lat, "lon": lon, "units": units, "lang": lang}
    )
    if "error" in weather:
        return weather

    # Step 3 – forecast
    forecast = _get(
        "/data/2.5/forecast",
        {"lat": lat, "lon": lon, "cnt": forecast_steps, "units": units, "lang": lang},
    )
    if "error" in forecast:
        return forecast

    # Step 4 – air pollution
    air = _get("/data/2.5/air_pollution", {"lat": lat, "lon": lon})
    if "error" in air:
        return air

    return {
        "location": location,
        "weather": weather,
        "forecast": forecast,
        "air_pollution": air,
    }


# ===========================================================================
# Entry point
# ===========================================================================

if __name__ == "__main__":
    mcp.run()
