#!/usr/bin/env python3
"""
OpenWeatherMap MCP Server
Provides tools for accessing weather data, forecasts, air pollution data, and geocoding.
"""

import os
import requests
from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("openweather")

# Base URL for OpenWeatherMap API
BASE_URL = "https://api.openweathermap.org"


def get_api_key() -> str:
    """Get the OpenWeatherMap API key from environment variables."""
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        raise ValueError("OPENWEATHER_API_KEY environment variable is not set")
    return api_key


def make_request(endpoint: str, params: dict) -> dict:
    """Make a request to the OpenWeatherMap API."""
    api_key = get_api_key()
    params["appid"] = api_key
    
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return {"error": f"Resource not found: {e}"}
        elif e.response.status_code == 401:
            return {"error": "Unauthorized: Invalid API key"}
        elif e.response.status_code == 429:
            return {"error": "Rate limit exceeded"}
        else:
            return {"error": f"HTTP error: {e}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}
    except ValueError as e:
        return {"error": f"Failed to parse response: {e}"}


# ============================================
# Current Weather Data Tools
# ============================================

@mcp.tool()
def get_current_weather_by_coords(lat: float, lon: float, units: str = "standard", lang: str = "en") -> dict:
    """
    Get current weather data for a specific geographical location.
    
    Args:
        lat: Latitude of the location
        lon: Longitude of the location
        units: Units of measurement. Options: 'standard' (Kelvin), 'metric' (Celsius), 'imperial' (Fahrenheit)
        lang: Language for the weather description
    
    Returns:
        Current weather data including temperature, humidity, wind, and weather conditions
    """
    endpoint = "/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "units": units,
        "lang": lang
    }
    return make_request(endpoint, params)


@mcp.tool()
def get_current_weather_by_city(
    city_name: str,
    state_code: str = "",
    country_code: str = "",
    units: str = "standard",
    lang: str = "en"
) -> dict:
    """
    Get current weather data for a city.
    
    Args:
        city_name: Name of the city (required)
        state_code: State code (US only), e.g., 'NY' for New York
        country_code: Country code (ISO 3166), e.g., 'US', 'GB'
        units: Units of measurement. Options: 'standard' (Kelvin), 'metric' (Celsius), 'imperial' (Fahrenheit)
        lang: Language for the weather description
    
    Returns:
        Current weather data for the specified city
    """
    # Build the q parameter
    if state_code and country_code:
        q = f"{city_name},{state_code},{country_code}"
    elif country_code:
        q = f"{city_name},{country_code}"
    else:
        q = city_name
    
    endpoint = "/data/2.5/weather"
    params = {
        "q": q,
        "units": units,
        "lang": lang
    }
    return make_request(endpoint, params)


@mcp.tool()
def get_current_weather_by_zip(zip_code: str, country_code: str = "us", units: str = "standard", lang: str = "en") -> dict:
    """
    Get current weather data for a specific ZIP/post code.
    
    Args:
        zip_code: ZIP or postal code
        country_code: Country code (ISO 3166), e.g., 'US', 'GB'
        units: Units of measurement. Options: 'standard' (Kelvin), 'metric' (Celsius), 'imperial' (Fahrenheit)
        lang: Language for the weather description
    
    Returns:
        Current weather data for the specified ZIP code
    """
    q = f"{zip_code},{country_code}"
    
    endpoint = "/data/2.5/weather"
    params = {
        "q": q,
        "units": units,
        "lang": lang
    }
    return make_request(endpoint, params)


# ============================================
# 5 Day / 3 Hour Forecast Tools
# ============================================

@mcp.tool()
def get_forecast_by_coords(lat: float, lon: float, units: str = "standard", lang: str = "en") -> dict:
    """
    Get 5-day weather forecast with 3-hour intervals for a specific location.
    
    Args:
        lat: Latitude of the location
        lon: Longitude of the location
        units: Units of measurement. Options: 'standard' (Kelvin), 'metric' (Celsius), 'imperial' (Fahrenheit)
        lang: Language for the weather description
    
    Returns:
        5-day forecast data with 3-hour intervals including temperature, humidity, wind, and weather conditions
    """
    endpoint = "/data/2.5/forecast"
    params = {
        "lat": lat,
        "lon": lon,
        "units": units,
        "lang": lang
    }
    return make_request(endpoint, params)


@mcp.tool()
def get_forecast_by_city(
    city_name: str,
    state_code: str = "",
    country_code: str = "",
    units: str = "standard",
    lang: str = "en"
) -> dict:
    """
    Get 5-day weather forecast with 3-hour intervals for a city.
    
    Args:
        city_name: Name of the city (required)
        state_code: State code (US only), e.g., 'NY' for New York
        country_code: Country code (ISO 3166), e.g., 'US', 'GB'
        units: Units of measurement. Options: 'standard' (Kelvin), 'metric' (Celsius), 'imperial' (Fahrenheit)
        lang: Language for the weather description
    
    Returns:
        5-day forecast data for the specified city
    """
    # Build the q parameter
    if state_code and country_code:
        q = f"{city_name},{state_code},{country_code}"
    elif country_code:
        q = f"{city_name},{country_code}"
    else:
        q = city_name
    
    endpoint = "/data/2.5/forecast"
    params = {
        "q": q,
        "units": units,
        "lang": lang
    }
    return make_request(endpoint, params)


@mcp.tool()
def get_forecast_by_zip(zip_code: str, country_code: str = "us", units: str = "standard", lang: str = "en") -> dict:
    """
    Get 5-day weather forecast with 3-hour intervals for a specific ZIP/post code.
    
    Args:
        zip_code: ZIP or postal code
        country_code: Country code (ISO 3166), e.g., 'US', 'GB'
        units: Units of measurement. Options: 'standard' (Kelvin), 'metric' (Celsius), 'imperial' (Fahrenheit)
        lang: Language for the weather description
    
    Returns:
        5-day forecast data for the specified ZIP code
    """
    q = f"{zip_code},{country_code}"
    
    endpoint = "/data/2.5/forecast"
    params = {
        "q": q,
        "units": units,
        "lang": lang
    }
    return make_request(endpoint, params)


# ============================================
# Air Pollution Tools
# ============================================

@mcp.tool()
def get_air_pollution_by_coords(lat: float, lon: float) -> dict:
    """
    Get current air pollution data for a specific location.
    
    Args:
        lat: Latitude of the location
        lon: Longitude of the location
    
    Returns:
        Current air pollution data including AQI and pollutant concentrations
    """
    endpoint = "/data/2.5/air_pollution"
    params = {
        "lat": lat,
        "lon": lon
    }
    return make_request(endpoint, params)


@mcp.tool()
def get_air_pollution_forecast_by_coords(lat: float, lon: float) -> dict:
    """
    Get 4-day air pollution forecast with hourly intervals for a specific location.
    
    Args:
        lat: Latitude of the location
        lon: Longitude of the location
    
    Returns:
        Air pollution forecast data including AQI and pollutant concentrations
    """
    endpoint = "/data/2.5/air_pollution/forecast"
    params = {
        "lat": lat,
        "lon": lon
    }
    return make_request(endpoint, params)


@mcp.tool()
def get_air_pollution_history_by_coords(
    lat: float,
    lon: float,
    start: int,
    end: int
) -> dict:
    """
    Get historical air pollution data for a specific location.
    
    Args:
        lat: Latitude of the location
        lon: Longitude of the location
        start: Start time as Unix timestamp (UTC)
        end: End time as Unix timestamp (UTC)
    
    Returns:
        Historical air pollution data including AQI and pollutant concentrations
    """
    endpoint = "/data/2.5/air_pollution/history"
    params = {
        "lat": lat,
        "lon": lon,
        "start": start,
        "end": end
    }
    return make_request(endpoint, params)


# ============================================
# Geocoding Tools
# ============================================

@mcp.tool()
def geocode_location(
    city_name: str,
    state_code: str = "",
    country_code: str = "",
    limit: int = 5
) -> list:
    """
    Convert a location name to geographical coordinates (latitude and longitude).
    
    Args:
        city_name: Name of the city or location (required)
        state_code: State code (US only), e.g., 'NY' for New York
        country_code: Country code (ISO 3166), e.g., 'US', 'GB'
        limit: Maximum number of results to return (1-5)
    
    Returns:
        List of locations matching the search criteria with their coordinates
    """
    # Build the q parameter
    if state_code and country_code:
        q = f"{city_name},{state_code},{country_code}"
    elif country_code:
        q = f"{city_name},{country_code}"
    else:
        q = city_name
    
    endpoint = "/geo/1.0/direct"
    params = {
        "q": q,
        "limit": limit
    }
    return make_request(endpoint, params)


@mcp.tool()
def geocode_by_zip(zip_code: str, country_code: str = "us") -> dict:
    """
    Convert a ZIP/post code to geographical coordinates.
    
    Args:
        zip_code: ZIP or postal code
        country_code: Country code (ISO 3166), e.g., 'US', 'GB'
    
    Returns:
        Location information including coordinates for the ZIP code
    """
    endpoint = "/geo/1.0/zip"
    params = {
        "zip": f"{zip_code},{country_code}"
    }
    return make_request(endpoint, params)


@mcp.tool()
def reverse_geocode(lat: float, lon: float, limit: int = 5) -> list:
    """
    Convert geographical coordinates to a location name.
    
    Args:
        lat: Latitude of the location
        lon: Longitude of the location
        limit: Maximum number of results to return (1-5)
    
    Returns:
        List of locations near the coordinates with their names
    """
    endpoint = "/geo/1.0/reverse"
    params = {
        "lat": lat,
        "lon": lon,
        "limit": limit
    }
    return make_request(endpoint, params)


if __name__ == "__main__":
    # Run the MCP server over stdio
    mcp.run()
