#!/usr/bin/env python3
"""
MCP Server for OpenWeatherMap API
Provides tools for accessing weather data, forecasts, air pollution, and geocoding.
"""

import os
import json
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("openweathermap")

# Configuration
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org"

if not API_KEY:
    raise ValueError("OPENWEATHER_API_KEY environment variable is required")


def make_request(endpoint: str, params: dict) -> dict:
    """Make an HTTP request to the OpenWeatherMap API."""
    params["appid"] = API_KEY
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response from API"}


# ============================================================================
# Current Weather API Tools
# ============================================================================

@mcp.tool()
def get_current_weather_by_coordinates(
    latitude: float,
    longitude: float,
    units: Optional[str] = None,
    lang: Optional[str] = None
) -> dict:
    """
    Get current weather data for a location by latitude and longitude.
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
        units: Units of measurement (standard, metric, imperial). Default: standard
        lang: Language code for weather descriptions (e.g., 'en', 'es', 'fr')
    
    Returns:
        Current weather data including temperature, conditions, wind, etc.
    """
    params = {"lat": latitude, "lon": longitude}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    return make_request("/data/2.5/weather", params)


@mcp.tool()
def get_current_weather_by_city_name(
    city_name: str,
    country_code: Optional[str] = None,
    state_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None
) -> dict:
    """
    Get current weather data for a location by city name.
    
    Args:
        city_name: Name of the city
        country_code: ISO 3166 country code (e.g., 'US', 'GB')
        state_code: State code (only for US locations)
        units: Units of measurement (standard, metric, imperial)
        lang: Language code for weather descriptions
    
    Returns:
        Current weather data for the specified city.
    """
    q_parts = [city_name]
    if state_code:
        q_parts.append(state_code)
    if country_code:
        q_parts.append(country_code)
    
    params = {"q": ",".join(q_parts)}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    return make_request("/data/2.5/weather", params)


@mcp.tool()
def get_current_weather_by_city_id(
    city_id: int,
    units: Optional[str] = None,
    lang: Optional[str] = None
) -> dict:
    """
    Get current weather data for a location by city ID.
    
    Args:
        city_id: OpenWeatherMap city ID
        units: Units of measurement (standard, metric, imperial)
        lang: Language code for weather descriptions
    
    Returns:
        Current weather data for the specified city ID.
    """
    params = {"id": city_id}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    return make_request("/data/2.5/weather", params)


@mcp.tool()
def get_current_weather_by_zip_code(
    zip_code: str,
    country_code: str,
    units: Optional[str] = None,
    lang: Optional[str] = None
) -> dict:
    """
    Get current weather data for a location by ZIP code.
    
    Args:
        zip_code: ZIP or postal code
        country_code: ISO 3166 country code (e.g., 'US', 'GB')
        units: Units of measurement (standard, metric, imperial)
        lang: Language code for weather descriptions
    
    Returns:
        Current weather data for the specified ZIP code.
    """
    params = {"zip": f"{zip_code},{country_code}"}
    if units:
        params["units"] = units
    if lang:
        params["lang"] = lang
    return make_request("/data/2.5/weather", params)


# ============================================================================
# 5-Day Forecast API Tools
# ============================================================================

@mcp.tool()
def get_5day_forecast_by_coordinates(
    latitude: float,
    longitude: float,
    units: Optional[str] = None,
    count: Optional[int] = None,
    lang: Optional[str] = None
) -> dict:
    """
    Get 5-day weather forecast (3-hour intervals) for a location by coordinates.
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
        units: Units of measurement (standard, metric, imperial)
        count: Number of forecast timestamps to return (max 40)
        lang: Language code for weather descriptions
    
    Returns:
        5-day forecast data with 3-hour intervals.
    """
    params = {"lat": latitude, "lon": longitude}
    if units:
        params["units"] = units
    if count:
        params["cnt"] = count
    if lang:
        params["lang"] = lang
    return make_request("/data/2.5/forecast", params)


@mcp.tool()
def get_5day_forecast_by_city_name(
    city_name: str,
    country_code: Optional[str] = None,
    state_code: Optional[str] = None,
    units: Optional[str] = None,
    count: Optional[int] = None,
    lang: Optional[str] = None
) -> dict:
    """
    Get 5-day weather forecast for a location by city name.
    
    Args:
        city_name: Name of the city
        country_code: ISO 3166 country code
        state_code: State code (only for US)
        units: Units of measurement (standard, metric, imperial)
        count: Number of forecast timestamps to return
        lang: Language code for weather descriptions
    
    Returns:
        5-day forecast data for the specified city.
    """
    q_parts = [city_name]
    if state_code:
        q_parts.append(state_code)
    if country_code:
        q_parts.append(country_code)
    
    params = {"q": ",".join(q_parts)}
    if units:
        params["units"] = units
    if count:
        params["cnt"] = count
    if lang:
        params["lang"] = lang
    return make_request("/data/2.5/forecast", params)


@mcp.tool()
def get_5day_forecast_by_city_id(
    city_id: int,
    units: Optional[str] = None,
    count: Optional[int] = None,
    lang: Optional[str] = None
) -> dict:
    """
    Get 5-day weather forecast for a location by city ID.
    
    Args:
        city_id: OpenWeatherMap city ID
        units: Units of measurement (standard, metric, imperial)
        count: Number of forecast timestamps to return
        lang: Language code for weather descriptions
    
    Returns:
        5-day forecast data for the specified city ID.
    """
    params = {"id": city_id}
    if units:
        params["units"] = units
    if count:
        params["cnt"] = count
    if lang:
        params["lang"] = lang
    return make_request("/data/2.5/forecast", params)


@mcp.tool()
def get_5day_forecast_by_zip_code(
    zip_code: str,
    country_code: str,
    units: Optional[str] = None,
    count: Optional[int] = None,
    lang: Optional[str] = None
) -> dict:
    """
    Get 5-day weather forecast for a location by ZIP code.
    
    Args:
        zip_code: ZIP or postal code
        country_code: ISO 3166 country code
        units: Units of measurement (standard, metric, imperial)
        count: Number of forecast timestamps to return
        lang: Language code for weather descriptions
    
    Returns:
        5-day forecast data for the specified ZIP code.
    """
    params = {"zip": f"{zip_code},{country_code}"}
    if units:
        params["units"] = units
    if count:
        params["cnt"] = count
    if lang:
        params["lang"] = lang
    return make_request("/data/2.5/forecast", params)


# ============================================================================
# Air Pollution API Tools
# ============================================================================

@mcp.tool()
def get_current_air_pollution(
    latitude: float,
    longitude: float
) -> dict:
    """
    Get current air pollution data for a location.
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    
    Returns:
        Current air pollution data including AQI and pollutant concentrations.
    """
    params = {"lat": latitude, "lon": longitude}
    return make_request("/data/2.5/air_pollution", params)


@mcp.tool()
def get_air_pollution_forecast(
    latitude: float,
    longitude: float
) -> dict:
    """
    Get air pollution forecast for a location (4 days with hourly granularity).
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    
    Returns:
        Air pollution forecast data for the next 4 days.
    """
    params = {"lat": latitude, "lon": longitude}
    return make_request("/data/2.5/air_pollution/forecast", params)


@mcp.tool()
def get_air_pollution_history(
    latitude: float,
    longitude: float,
    start_timestamp: int,
    end_timestamp: int
) -> dict:
    """
    Get historical air pollution data for a location.
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
        start_timestamp: Start date as Unix timestamp (UTC)
        end_timestamp: End date as Unix timestamp (UTC)
    
    Returns:
        Historical air pollution data for the specified period.
    """
    params = {
        "lat": latitude,
        "lon": longitude,
        "start": start_timestamp,
        "end": end_timestamp
    }
    return make_request("/data/2.5/air_pollution/history", params)


# ============================================================================
# Geocoding API Tools
# ============================================================================

@mcp.tool()
def geocode_location_name(
    location_name: str,
    country_code: Optional[str] = None,
    state_code: Optional[str] = None,
    limit: Optional[int] = None
) -> dict:
    """
    Convert a location name to geographical coordinates (direct geocoding).
    
    Args:
        location_name: Name of the city or location
        country_code: ISO 3166 country code (e.g., 'US', 'GB')
        state_code: State code (only for US locations)
        limit: Maximum number of results to return (up to 5)
    
    Returns:
        List of locations with their coordinates and details.
    """
    q_parts = [location_name]
    if state_code:
        q_parts.append(state_code)
    if country_code:
        q_parts.append(country_code)
    
    params = {"q": ",".join(q_parts)}
    if limit:
        params["limit"] = limit
    return make_request("/geo/1.0/direct", params)


@mcp.tool()
def geocode_zip_code(
    zip_code: str,
    country_code: str
) -> dict:
    """
    Convert a ZIP/postal code to geographical coordinates.
    
    Args:
        zip_code: ZIP or postal code
        country_code: ISO 3166 country code (e.g., 'US', 'GB')
    
    Returns:
        Location data with coordinates for the specified ZIP code.
    """
    params = {"zip": f"{zip_code},{country_code}"}
    return make_request("/geo/1.0/zip", params)


@mcp.tool()
def reverse_geocode(
    latitude: float,
    longitude: float,
    limit: Optional[int] = None
) -> dict:
    """
    Convert geographical coordinates to location names (reverse geocoding).
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
        limit: Maximum number of results to return
    
    Returns:
        List of nearby locations with their names and details.
    """
    params = {"lat": latitude, "lon": longitude}
    if limit:
        params["limit"] = limit
    return make_request("/geo/1.0/reverse", params)


if __name__ == "__main__":
    mcp.run()
