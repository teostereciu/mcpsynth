#!/usr/bin/env python3
"""
MCP Server for OpenWeatherMap API
Provides tools for accessing weather, forecast, air pollution, and geocoding data.
"""

import os
import json
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("openweathermap")

# Configuration
BASE_URL = "https://api.openweathermap.org"
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("OPENWEATHER_API_KEY environment variable is required")


def make_request(endpoint: str, params: dict) -> dict:
    """Make an HTTP request to the OpenWeatherMap API."""
    params["appid"] = API_KEY
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"API error: {response.status_code}", "details": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# ============================================================================
# CURRENT WEATHER API TOOLS
# ============================================================================

@mcp.tool()
def get_current_weather_by_coords(
    latitude: float,
    longitude: float,
    units: Optional[str] = None,
    language: Optional[str] = None
) -> dict:
    """
    Get current weather data for a location by geographic coordinates.
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
        units: Units of measurement (standard, metric, imperial). Default: standard
        language: Language for weather descriptions (e.g., 'en', 'es', 'fr')
    
    Returns:
        Current weather data including temperature, conditions, wind, etc.
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
    }
    if units:
        params["units"] = units
    if language:
        params["lang"] = language
    
    return make_request("/data/2.5/weather", params)


@mcp.tool()
def get_current_weather_by_city_name(
    city_name: str,
    country_code: Optional[str] = None,
    state_code: Optional[str] = None,
    units: Optional[str] = None,
    language: Optional[str] = None
) -> dict:
    """
    Get current weather data by city name (deprecated but still available).
    
    Args:
        city_name: Name of the city
        country_code: ISO 3166 country code (optional)
        state_code: State code for US locations (optional)
        units: Units of measurement (standard, metric, imperial)
        language: Language for weather descriptions
    
    Returns:
        Current weather data
    """
    q_parts = [city_name]
    if state_code:
        q_parts.append(state_code)
    if country_code:
        q_parts.append(country_code)
    
    params = {"q": ",".join(q_parts)}
    if units:
        params["units"] = units
    if language:
        params["lang"] = language
    
    return make_request("/data/2.5/weather", params)


# ============================================================================
# 5-DAY FORECAST API TOOLS
# ============================================================================

@mcp.tool()
def get_5day_forecast_by_coords(
    latitude: float,
    longitude: float,
    units: Optional[str] = None,
    count: Optional[int] = None,
    language: Optional[str] = None
) -> dict:
    """
    Get 5-day weather forecast with 3-hour intervals by geographic coordinates.
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
        units: Units of measurement (standard, metric, imperial). Default: standard
        count: Number of timestamps to return (optional, max 40)
        language: Language for weather descriptions
    
    Returns:
        5-day forecast data with 3-hour intervals
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
    }
    if units:
        params["units"] = units
    if count:
        params["cnt"] = count
    if language:
        params["lang"] = language
    
    return make_request("/data/2.5/forecast", params)


@mcp.tool()
def get_5day_forecast_by_city_name(
    city_name: str,
    country_code: Optional[str] = None,
    state_code: Optional[str] = None,
    units: Optional[str] = None,
    count: Optional[int] = None,
    language: Optional[str] = None
) -> dict:
    """
    Get 5-day forecast by city name (deprecated but still available).
    
    Args:
        city_name: Name of the city
        country_code: ISO 3166 country code (optional)
        state_code: State code for US locations (optional)
        units: Units of measurement (standard, metric, imperial)
        count: Number of timestamps to return
        language: Language for weather descriptions
    
    Returns:
        5-day forecast data
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
    if language:
        params["lang"] = language
    
    return make_request("/data/2.5/forecast", params)


# ============================================================================
# AIR POLLUTION API TOOLS
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
        Current air pollution data including AQI and pollutant concentrations
        (CO, NO, NO2, O3, SO2, PM2.5, PM10, NH3)
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
    }
    return make_request("/data/2.5/air_pollution", params)


@mcp.tool()
def get_air_pollution_forecast(
    latitude: float,
    longitude: float
) -> dict:
    """
    Get 4-day air pollution forecast with hourly granularity.
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    
    Returns:
        Air pollution forecast data for the next 4 days
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
    }
    return make_request("/data/2.5/air_pollution/forecast", params)


@mcp.tool()
def get_air_pollution_history(
    latitude: float,
    longitude: float,
    start: int,
    end: int
) -> dict:
    """
    Get historical air pollution data for a location.
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
        start: Start date as Unix timestamp (UTC)
        end: End date as Unix timestamp (UTC)
    
    Returns:
        Historical air pollution data between the specified dates
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start": start,
        "end": end,
    }
    return make_request("/data/2.5/air_pollution/history", params)


# ============================================================================
# GEOCODING API TOOLS
# ============================================================================

@mcp.tool()
def geocode_location_name(
    location_name: str,
    country_code: Optional[str] = None,
    state_code: Optional[str] = None,
    limit: Optional[int] = None
) -> dict:
    """
    Convert a location name to geographic coordinates (direct geocoding).
    
    Args:
        location_name: Name of the city or location
        country_code: ISO 3166 country code (optional)
        state_code: State code for US locations (optional)
        limit: Maximum number of results to return (1-5, default: 1)
    
    Returns:
        List of matching locations with their coordinates and details
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
    Convert a zip/postal code to geographic coordinates.
    
    Args:
        zip_code: Zip or postal code
        country_code: ISO 3166 country code
    
    Returns:
        Location data with coordinates for the zip code
    """
    params = {
        "zip": f"{zip_code},{country_code}",
    }
    return make_request("/geo/1.0/zip", params)


@mcp.tool()
def reverse_geocode(
    latitude: float,
    longitude: float,
    limit: Optional[int] = None
) -> dict:
    """
    Convert geographic coordinates to location names (reverse geocoding).
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
        limit: Maximum number of results to return (optional)
    
    Returns:
        List of nearby locations with their names and details
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
    }
    if limit:
        params["limit"] = limit
    
    return make_request("/geo/1.0/reverse", params)


if __name__ == "__main__":
    mcp.run()
