#!/usr/bin/env python3
"""OpenWeatherMap MCP Server"""

import os
import requests
from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("openweather")

# Base URL for OpenWeatherMap API
BASE_URL = "https://api.openweathermap.org"

def get_api_key() -> str:
    """Get API key from environment variable."""
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        raise ValueError("OPENWEATHER_API_KEY environment variable is not set")
    return api_key

def make_request(endpoint: str, params: dict) -> dict:
    """Make a request to the OpenWeatherMap API."""
    try:
        api_key = get_api_key()
        full_params = {"appid": api_key}
        full_params.update(params)
        
        response = requests.get(f"{BASE_URL}{endpoint}", params=full_params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# ==========================================
# Current Weather Data (API 2.5)
# ==========================================

@mcp.tool()
def get_current_weather_by_coordinates(latitude: float, longitude: float, 
                                       units: str = "standard", 
                                       lang: str = "en") -> dict:
    """
    Get current weather data for a specific location using coordinates.
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
        units: Units of measurement (standard, metric, imperial)
        lang: Language for the response
    
    Returns:
        Current weather data for the location
    """
    params = {
        "lat": latitude,
        "lon": longitude,
        "units": units,
        "lang": lang
    }
    return make_request("/data/2.5/weather", params)

@mcp.tool()
def get_current_weather_by_city(city_name: str, country_code: str = None, 
                                state_code: str = None, 
                                units: str = "standard", 
                                lang: str = "en") -> dict:
    """
    Get current weather data by city name.
    
    Args:
        city_name: Name of the city
        country_code: Country code (ISO 3166)
        state_code: State code (for US locations)
        units: Units of measurement (standard, metric, imperial)
        lang: Language for the response
    
    Returns:
        Current weather data for the specified city
    """
    # Build query parameter
    if state_code and country_code:
        q = f"{city_name},{state_code},{country_code}"
    elif country_code:
        q = f"{city_name},{country_code}"
    else:
        q = city_name
    
    params = {
        "q": q,
        "units": units,
        "lang": lang
    }
    return make_request("/data/2.5/weather", params)

# ==========================================
# 5 Day / 3 Hour Forecast (API 2.5)
# ==========================================

@mcp.tool()
def get_forecast_by_coordinates(latitude: float, longitude: float,
                                units: str = "standard",
                                lang: str = "en") -> dict:
    """
    Get 5-day weather forecast by coordinates.
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
        units: Units of measurement (standard, metric, imperial)
        lang: Language for the response
    
    Returns:
        5-day weather forecast with 3-hour intervals
    """
    params = {
        "lat": latitude,
        "lon": longitude,
        "units": units,
        "lang": lang
    }
    return make_request("/data/2.5/forecast", params)

@mcp.tool()
def get_forecast_by_city_id(city_id: int, units: str = "standard",
                            lang: str = "en") -> dict:
    """
    Get 5-day weather forecast by city ID.
    
    Args:
        city_id: City ID (numeric identifier)
        units: Units of measurement (standard, metric, imperial)
        lang: Language for the response
    
    Returns:
        5-day weather forecast with 3-hour intervals
    """
    params = {
        "id": city_id,
        "units": units,
        "lang": lang
    }
    return make_request("/data/2.5/forecast", params)

@mcp.tool()
def get_forecast_by_city(city_name: str, country_code: str = None,
                         state_code: str = None,
                         units: str = "standard",
                         lang: str = "en") -> dict:
    """
    Get 5-day weather forecast by city name.
    
    Args:
        city_name: Name of the city
        country_code: Country code (ISO 3166)
        state_code: State code (for US locations)
        units: Units of measurement (standard, metric, imperial)
        lang: Language for the response
    
    Returns:
        5-day weather forecast with 3-hour intervals
    """
    # Build query parameter
    if state_code and country_code:
        q = f"{city_name},{state_code},{country_code}"
    elif country_code:
        q = f"{city_name},{country_code}"
    else:
        q = city_name
    
    params = {
        "q": q,
        "units": units,
        "lang": lang
    }
    return make_request("/data/2.5/forecast", params)

# ==========================================
# Air Pollution API
# ==========================================

@mcp.tool()
def get_air_pollution_by_coordinates(latitude: float, longitude: float) -> dict:
    """
    Get current air pollution data for a specific location.
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    
    Returns:
        Current air pollution data including AQI and component concentrations
    """
    params = {
        "lat": latitude,
        "lon": longitude
    }
    return make_request("/data/2.5/air_pollution", params)

@mcp.tool()
def get_current_weather_by_city_id(city_id: int, units: str = "standard", 
                                   lang: str = "en") -> dict:
    """
    Get current weather data by city ID.
    
    Args:
        city_id: City ID (numeric identifier)
        units: Units of measurement (standard, metric, imperial)
        lang: Language for the response
    
    Returns:
        Current weather data for the specified city ID
    """
    params = {
        "id": city_id,
        "units": units,
        "lang": lang
    }
    return make_request("/data/2.5/weather", params)

@mcp.tool()
def get_air_pollution_forecast_by_coordinates(latitude: float, longitude: float) -> dict:
    """
    Get 4-day air pollution forecast for a specific location.
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    
    Returns:
        Air pollution forecast with hourly granularity for 4 days
    """
    params = {
        "lat": latitude,
        "lon": longitude
    }
    return make_request("/data/2.5/air_pollution/forecast", params)

@mcp.tool()
def get_air_pollution_history_by_coordinates(latitude: float, longitude: float,
                                             start: int, end: int) -> dict:
    """
    Get historical air pollution data for a specific location.
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
        start: Start date (Unix time, UTC)
        end: End date (Unix time, UTC)
    
    Returns:
        Historical air pollution data
    """
    params = {
        "lat": latitude,
        "lon": longitude,
        "start": start,
        "end": end
    }
    return make_request("/data/2.5/air_pollution/history", params)

# ==========================================
# Geocoding API
# ==========================================

@mcp.tool()
def geocode_location(city_name: str, state_code: str = None, 
                     country_code: str = None, limit: int = 5) -> list:
    """
    Convert city name to geographical coordinates (latitude, longitude).
    
    Args:
        city_name: Name of the city
        state_code: State code (for US locations)
        country_code: Country code (ISO 3166)
        limit: Maximum number of results to return (1-5)
    
    Returns:
        List of locations matching the search criteria
    """
    # Build query parameter
    if state_code and country_code:
        q = f"{city_name},{state_code},{country_code}"
    elif country_code:
        q = f"{city_name},{country_code}"
    else:
        q = city_name
    
    params = {
        "q": q,
        "limit": min(limit, 5)
    }
    return make_request("/geo/1.0/direct", params)

@mcp.tool()
def geocode_by_zip(zip_code: str, country_code: str) -> dict:
    """
    Get coordinates for a zip/post code.
    
    Args:
        zip_code: Zip or postal code
        country_code: Country code (ISO 3166)
    
    Returns:
        Location information including coordinates for the zip code
    """
    params = {
        "zip": f"{zip_code},{country_code}"
    }
    return make_request("/geo/1.0/zip", params)

@mcp.tool()
def reverse_geocode(latitude: float, longitude: float, limit: int = 5) -> list:
    """
    Convert coordinates to location name(s).
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
        limit: Maximum number of results to return (1-5)
    
    Returns:
        List of location names near the coordinates
    """
    params = {
        "lat": latitude,
        "lon": longitude,
        "limit": min(limit, 5)
    }
    return make_request("/geo/1.0/reverse", params)


if __name__ == "__main__":
    mcp.run()
