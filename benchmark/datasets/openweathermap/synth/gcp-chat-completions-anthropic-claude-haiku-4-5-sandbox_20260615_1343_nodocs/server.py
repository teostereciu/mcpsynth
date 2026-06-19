#!/usr/bin/env python3
"""
MCP Server for OpenWeatherMap API
Provides tools for accessing weather data, forecasts, air pollution, and geocoding.
"""

import os
import json
import requests
from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP("openweathermap")

# Configuration
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org"

if not API_KEY:
    raise ValueError("OPENWEATHER_API_KEY environment variable is required")


# ============================================================================
# Helper Functions
# ============================================================================

def _make_request(
    method: str,
    endpoint: str,
    params: Optional[Dict[str, Any]] = None,
    json_data: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Make an HTTP request to the OpenWeatherMap API.
    
    Args:
        method: HTTP method (GET, POST, etc.)
        endpoint: API endpoint path (e.g., "/data/2.5/weather")
        params: Query parameters
        json_data: JSON body for POST requests
    
    Returns:
        Response JSON or error dict
    """
    if params is None:
        params = {}
    
    # Add API key to params
    params["appid"] = API_KEY
    
    url = f"{BASE_URL}{endpoint}"
    
    try:
        response = requests.request(
            method=method,
            url=url,
            params=params,
            json=json_data,
            timeout=10,
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response from API"}


# ============================================================================
# Current Weather Data (API 2.5)
# ============================================================================

@server.tool()
def get_current_weather_by_city(
    city: str,
    state_code: Optional[str] = None,
    country_code: Optional[str] = None,
    units: str = "metric",
) -> Dict[str, Any]:
    """
    Get current weather data for a city.
    
    Args:
        city: City name (required)
        state_code: State code (optional, US only)
        country_code: ISO 3166 country code (optional)
        units: Temperature units - 'metric' (Celsius), 'imperial' (Fahrenheit), or 'standard' (Kelvin)
    
    Returns:
        Current weather data including temperature, conditions, wind, etc.
    """
    q = city
    if state_code:
        q = f"{city},{state_code}"
    if country_code:
        q = f"{q},{country_code}"
    
    params = {"q": q, "units": units}
    return _make_request("GET", "/data/2.5/weather", params=params)


@server.tool()
def get_current_weather_by_coordinates(
    latitude: float,
    longitude: float,
    units: str = "metric",
) -> Dict[str, Any]:
    """
    Get current weather data by geographic coordinates.
    
    Args:
        latitude: Latitude (-90 to 90)
        longitude: Longitude (-180 to 180)
        units: Temperature units - 'metric' (Celsius), 'imperial' (Fahrenheit), or 'standard' (Kelvin)
    
    Returns:
        Current weather data including temperature, conditions, wind, etc.
    """
    params = {"lat": latitude, "lon": longitude, "units": units}
    return _make_request("GET", "/data/2.5/weather", params=params)


@server.tool()
def get_current_weather_by_zip(
    zip_code: str,
    country_code: Optional[str] = None,
    units: str = "metric",
) -> Dict[str, Any]:
    """
    Get current weather data by ZIP code.
    
    Args:
        zip_code: ZIP code
        country_code: ISO 3166 country code (optional)
        units: Temperature units - 'metric' (Celsius), 'imperial' (Fahrenheit), or 'standard' (Kelvin)
    
    Returns:
        Current weather data including temperature, conditions, wind, etc.
    """
    z = zip_code
    if country_code:
        z = f"{zip_code},{country_code}"
    
    params = {"zip": z, "units": units}
    return _make_request("GET", "/data/2.5/weather", params=params)


# ============================================================================
# 5-Day / 3-Hour Forecast (API 2.5)
# ============================================================================

@server.tool()
def get_forecast_by_city(
    city: str,
    state_code: Optional[str] = None,
    country_code: Optional[str] = None,
    units: str = "metric",
    count: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Get 5-day/3-hour forecast for a city.
    
    Args:
        city: City name (required)
        state_code: State code (optional, US only)
        country_code: ISO 3166 country code (optional)
        units: Temperature units - 'metric' (Celsius), 'imperial' (Fahrenheit), or 'standard' (Kelvin)
        count: Number of timestamps to return (1-40, default 40)
    
    Returns:
        5-day forecast with 3-hour intervals
    """
    q = city
    if state_code:
        q = f"{city},{state_code}"
    if country_code:
        q = f"{q},{country_code}"
    
    params = {"q": q, "units": units}
    if count is not None:
        params["cnt"] = count
    
    return _make_request("GET", "/data/2.5/forecast", params=params)


@server.tool()
def get_forecast_by_coordinates(
    latitude: float,
    longitude: float,
    units: str = "metric",
    count: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Get 5-day/3-hour forecast by geographic coordinates.
    
    Args:
        latitude: Latitude (-90 to 90)
        longitude: Longitude (-180 to 180)
        units: Temperature units - 'metric' (Celsius), 'imperial' (Fahrenheit), or 'standard' (Kelvin)
        count: Number of timestamps to return (1-40, default 40)
    
    Returns:
        5-day forecast with 3-hour intervals
    """
    params = {"lat": latitude, "lon": longitude, "units": units}
    if count is not None:
        params["cnt"] = count
    
    return _make_request("GET", "/data/2.5/forecast", params=params)


@server.tool()
def get_forecast_by_zip(
    zip_code: str,
    country_code: Optional[str] = None,
    units: str = "metric",
    count: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Get 5-day/3-hour forecast by ZIP code.
    
    Args:
        zip_code: ZIP code
        country_code: ISO 3166 country code (optional)
        units: Temperature units - 'metric' (Celsius), 'imperial' (Fahrenheit), or 'standard' (Kelvin)
        count: Number of timestamps to return (1-40, default 40)
    
    Returns:
        5-day forecast with 3-hour intervals
    """
    z = zip_code
    if country_code:
        z = f"{zip_code},{country_code}"
    
    params = {"zip": z, "units": units}
    if count is not None:
        params["cnt"] = count
    
    return _make_request("GET", "/data/2.5/forecast", params=params)


# ============================================================================
# Air Pollution API
# ============================================================================

@server.tool()
def get_air_pollution_current(
    latitude: float,
    longitude: float,
) -> Dict[str, Any]:
    """
    Get current air pollution data for coordinates.
    
    Args:
        latitude: Latitude (-90 to 90)
        longitude: Longitude (-180 to 180)
    
    Returns:
        Current air pollution data including AQI and pollutant concentrations
    """
    params = {"lat": latitude, "lon": longitude}
    return _make_request("GET", "/data/3.0/air_pollution", params=params)


@server.tool()
def get_air_pollution_forecast(
    latitude: float,
    longitude: float,
) -> Dict[str, Any]:
    """
    Get air pollution forecast for coordinates.
    
    Args:
        latitude: Latitude (-90 to 90)
        longitude: Longitude (-180 to 180)
    
    Returns:
        Air pollution forecast data
    """
    params = {"lat": latitude, "lon": longitude}
    return _make_request("GET", "/data/3.0/air_pollution/forecast", params=params)


@server.tool()
def get_air_pollution_history(
    latitude: float,
    longitude: float,
    start: int,
    end: int,
) -> Dict[str, Any]:
    """
    Get historical air pollution data for coordinates.
    
    Args:
        latitude: Latitude (-90 to 90)
        longitude: Longitude (-180 to 180)
        start: Unix timestamp for start of period
        end: Unix timestamp for end of period
    
    Returns:
        Historical air pollution data
    """
    params = {"lat": latitude, "lon": longitude, "start": start, "end": end}
    return _make_request("GET", "/data/3.0/air_pollution/history", params=params)


# ============================================================================
# Geocoding API
# ============================================================================

@server.tool()
def geocode_direct(
    query: str,
    limit: int = 5,
    country_code: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Convert city/location name to geographic coordinates (direct geocoding).
    
    Args:
        query: Location name (city, address, etc.)
        limit: Maximum number of results (1-5, default 5)
        country_code: ISO 3166 country code to limit results (optional)
    
    Returns:
        List of matching locations with coordinates
    """
    params = {"q": query, "limit": limit}
    if country_code:
        params["countryCode"] = country_code
    
    return _make_request("GET", "/geo/1.0/direct", params=params)


@server.tool()
def geocode_reverse(
    latitude: float,
    longitude: float,
    limit: int = 1,
) -> Dict[str, Any]:
    """
    Convert geographic coordinates to location name (reverse geocoding).
    
    Args:
        latitude: Latitude (-90 to 90)
        longitude: Longitude (-180 to 180)
        limit: Maximum number of results (1-5, default 1)
    
    Returns:
        List of locations at or near the coordinates
    """
    params = {"lat": latitude, "lon": longitude, "limit": limit}
    return _make_request("GET", "/geo/1.0/reverse", params=params)


@server.tool()
def geocode_zip(
    zip_code: str,
    country_code: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Convert ZIP code to geographic coordinates.
    
    Args:
        zip_code: ZIP code
        country_code: ISO 3166 country code (optional)
    
    Returns:
        Location with coordinates for the ZIP code
    """
    z = zip_code
    if country_code:
        z = f"{zip_code},{country_code}"
    
    params = {"zip": z}
    return _make_request("GET", "/geo/1.0/zip", params=params)


# ============================================================================
# Server Entry Point
# ============================================================================

if __name__ == "__main__":
    server.run()
