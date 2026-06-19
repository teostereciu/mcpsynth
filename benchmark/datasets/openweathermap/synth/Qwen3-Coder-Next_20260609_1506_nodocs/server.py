#!/usr/bin/env python3
"""OpenWeatherMap MCP Server.

This server provides tools for interacting with the OpenWeatherMap API,
including current weather, forecasts, air pollution, and geocoding.
"""

import os
import requests
from typing import Any

from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("openweather")

# Base URL for OpenWeatherMap API
BASE_URL = "https://api.openweathermap.org/data/2.5"


def _get_api_key() -> str:
    """Get the API key from environment variables."""
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        raise ValueError("OPENWEATHER_API_KEY environment variable is required")
    return api_key


def _make_request(endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
    """Make a request to the OpenWeatherMap API."""
    try:
        params["appid"] = _get_api_key()
        response = requests.get(f"{BASE_URL}/{endpoint}", params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return {"error": "Resource not found"}
        elif e.response.status_code == 401:
            return {"error": "Invalid API key"}
        elif e.response.status_code == 429:
            return {"error": "API rate limit exceeded"}
        else:
            return {"error": f"HTTP error: {e.response.status_code}"}
    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


@mcp.tool()
def get_current_weather_by_city(
    city_name: str,
    units: str = "standard",
    lang: str = "en",
) -> dict[str, Any]:
    """Get current weather data for a city by name.

    Args:
        city_name: Name of the city (e.g., "London" or "London,UK")
        units: Units of measurement ("standard", "metric", or "imperial")
        lang: Language for the response description

    Returns:
        Current weather data for the specified city
    """
    params = {
        "q": city_name,
        "units": units,
        "lang": lang,
    }
    return _make_request("weather", params)


@mcp.tool()
def get_current_weather_by_coords(
    lat: float,
    lon: float,
    units: str = "standard",
    lang: str = "en",
) -> dict[str, Any]:
    """Get current weather data for a location by coordinates.

    Args:
        lat: Latitude of the location
        lon: Longitude of the location
        units: Units of measurement ("standard", "metric", or "imperial")
        lang: Language for the response description

    Returns:
        Current weather data for the specified coordinates
    """
    params = {
        "lat": lat,
        "lon": lon,
        "units": units,
        "lang": lang,
    }
    return _make_request("weather", params)


@mcp.tool()
def get_current_weather_by_city_id(city_id: int, units: str = "standard") -> dict[str, Any]:
    """Get current weather data for a city by its ID.

    Args:
        city_id: City ID (see OpenWeatherMap city list)
        units: Units of measurement ("standard", "metric", or "imperial")

    Returns:
        Current weather data for the specified city ID
    """
    params = {
        "id": city_id,
        "units": units,
    }
    return _make_request("weather", params)


@mcp.tool()
def get_current_weather_by_zip(
    zip_code: str,
    country_code: str = "us",
    units: str = "standard",
) -> dict[str, Any]:
    """Get current weather data for a zip/postal code.

    Args:
        zip_code: Zip/postal code (e.g., "10001")
        country_code: 2-digit country code (e.g., "us", "gb")
        units: Units of measurement ("standard", "metric", or "imperial")

    Returns:
        Current weather data for the specified zip code
    """
    params = {
        "zip": f"{zip_code},{country_code}",
        "units": units,
    }
    return _make_request("weather", params)


@mcp.tool()
def get_5_day_forecast_by_city(
    city_name: str,
    units: str = "standard",
    lang: str = "en",
) -> dict[str, Any]:
    """Get 5-day weather forecast for a city by name.

    Args:
        city_name: Name of the city (e.g., "London" or "London,UK")
        units: Units of measurement ("standard", "metric", or "imperial")
        lang: Language for the response description

    Returns:
        5-day weather forecast data for the specified city
    """
    params = {
        "q": city_name,
        "units": units,
        "lang": lang,
    }
    return _make_request("forecast", params)


@mcp.tool()
def get_5_day_forecast_by_coords(
    lat: float,
    lon: float,
    units: str = "standard",
    lang: str = "en",
) -> dict[str, Any]:
    """Get 5-day weather forecast for a location by coordinates.

    Args:
        lat: Latitude of the location
        lon: Longitude of the location
        units: Units of measurement ("standard", "metric", or "imperial")
        lang: Language for the response description

    Returns:
        5-day weather forecast data for the specified coordinates
    """
    params = {
        "lat": lat,
        "lon": lon,
        "units": units,
        "lang": lang,
    }
    return _make_request("forecast", params)


@mcp.tool()
def get_5_day_forecast_by_city_id(city_id: int, units: str = "standard") -> dict[str, Any]:
    """Get 5-day weather forecast for a city by its ID.

    Args:
        city_id: City ID (see OpenWeatherMap city list)
        units: Units of measurement ("standard", "metric", or "imperial")

    Returns:
        5-day weather forecast data for the specified city ID
    """
    params = {
        "id": city_id,
        "units": units,
    }
    return _make_request("forecast", params)


@mcp.tool()
def get_5_day_forecast_by_zip(
    zip_code: str,
    country_code: str = "us",
    units: str = "standard",
) -> dict[str, Any]:
    """Get 5-day weather forecast for a zip/postal code.

    Args:
        zip_code: Zip/postal code (e.g., "10001")
        country_code: 2-digit country code (e.g., "us", "gb")
        units: Units of measurement ("standard", "metric", or "imperial")

    Returns:
        5-day weather forecast data for the specified zip code
    """
    params = {
        "zip": f"{zip_code},{country_code}",
        "units": units,
    }
    return _make_request("forecast", params)


@mcp.tool()
def get_air_pollution_by_coords(
    lat: float,
    lon: float,
) -> dict[str, Any]:
    """Get air pollution data for a location by coordinates.

    Args:
        lat: Latitude of the location
        lon: Longitude of the location

    Returns:
        Air pollution data for the specified coordinates
    """
    params = {
        "lat": lat,
        "lon": lon,
    }
    return _make_request("air_pollution", params)


@mcp.tool()
def get_air_pollution_by_city(city_name: str) -> dict[str, Any]:
    """Get air pollution data for a city by name.

    Args:
        city_name: Name of the city (e.g., "London" or "London,UK")

    Returns:
        Air pollution data for the specified city
    """
    params = {
        "q": city_name,
    }
    return _make_request("air_pollution", params)


@mcp.tool()
def get_air_pollution_history(
    lat: float,
    lon: float,
    start: int,
    end: int,
) -> dict[str, Any]:
    """Get historical air pollution data for a location.

    Args:
        lat: Latitude of the location
        lon: Longitude of the location
        start: Start timestamp (Unix time)
        end: End timestamp (Unix time)

    Returns:
        Historical air pollution data for the specified location and time range
    """
    params = {
        "lat": lat,
        "lon": lon,
        "start": start,
        "end": end,
    }
    return _make_request("air_pollution/history", params)


@mcp.tool()
def geocode_city_name(city_name: str) -> list[dict[str, Any]]:
    """Get geographic coordinates for a city name (geocoding).

    Args:
        city_name: Name of the city (e.g., "London" or "London,UK")

    Returns:
        List of matching locations with coordinates and metadata
    """
    params = {
        "q": city_name,
    }
    return _make_request("weather", params)


@mcp.tool()
def reverse_geocode(
    lat: float,
    lon: float,
    lang: str = "",
) -> list[dict[str, Any]]:
    """Get city name and other info for geographic coordinates (reverse geocoding).

    Args:
        lat: Latitude of the location
        lon: Longitude of the location
        lang: Language for the response (optional)

    Returns:
        List of locations near the coordinates with names and metadata
    """
    params = {
        "lat": lat,
        "lon": lon,
    }
    if lang:
        params["lang"] = lang
    return _make_request("weather", params)


@mcp.tool()
def get_weather_by_city_id_with_details(
    city_id: int,
    units: str = "standard",
    lang: str = "en",
) -> dict[str, Any]:
    """Get detailed weather data for a city by its ID (alternative endpoint).

    Args:
        city_id: City ID (see OpenWeatherMap city list)
        units: Units of measurement ("standard", "metric", or "imperial")
        lang: Language for the response description

    Returns:
        Detailed weather data for the specified city ID
    """
    params = {
        "id": city_id,
        "units": units,
        "lang": lang,
    }
    return _make_request("weather", params)


@mcp.tool()
def get_weather_alerts_by_coords(
    lat: float,
    lon: float,
) -> dict[str, Any]:
    """Get weather alerts for a location by coordinates.

    Args:
        lat: Latitude of the location
        lon: Longitude of the location

    Returns:
        Weather alerts for the specified coordinates
    """
    params = {
        "lat": lat,
        "lon": lon,
    }
    return _make_request("alerts", params)


@mcp.tool()
def get_weather_alerts_by_city(city_name: str) -> dict[str, Any]:
    """Get weather alerts for a city by name.

    Args:
        city_name: Name of the city (e.g., "London" or "London,UK")

    Returns:
        Weather alerts for the specified city
    """
    params = {
        "q": city_name,
    }
    return _make_request("alerts", params)


if __name__ == "__main__":
    mcp.run()
