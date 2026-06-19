import os
import requests
from typing import Dict, Any, List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("OpenWeatherMap")

BASE_URL = "https://api.openweathermap.org"

def get_api_key() -> str:
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        raise ValueError("OPENWEATHER_API_KEY environment variable not set")
    return api_key

@mcp.tool()
def get_current_weather(lat: float, lon: float) -> Dict[str, Any]:
    """Get current weather data for a specific location."""
    try:
        api_key = get_api_key()
        url = f"{BASE_URL}/data/2.5/weather"
        params = {"lat": lat, "lon": lon, "appid": api_key}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_5day_forecast(lat: float, lon: float) -> Dict[str, Any]:
    """Get 5-day/3-hour forecast data for a specific location."""
    try:
        api_key = get_api_key()
        url = f"{BASE_URL}/data/2.5/forecast"
        params = {"lat": lat, "lon": lon, "appid": api_key}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_air_pollution(lat: float, lon: float) -> Dict[str, Any]:
    """Get current air pollution data for a specific location."""
    try:
        api_key = get_api_key()
        url = f"{BASE_URL}/data/2.5/air_pollution"
        params = {"lat": lat, "lon": lon, "appid": api_key}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def geocode_direct(q: str, limit: int = 5) -> List[Dict[str, Any]]:
    """Get geographical coordinates for a city name."""
    try:
        api_key = get_api_key()
        url = f"{BASE_URL}/geo/1.0/direct"
        params = {"q": q, "limit": limit, "appid": api_key}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return [{"error": str(e)}]

@mcp.tool()
def geocode_reverse(lat: float, lon: float, limit: int = 5) -> List[Dict[str, Any]]:
    """Get city name for geographical coordinates."""
    try:
        api_key = get_api_key()
        url = f"{BASE_URL}/geo/1.0/reverse"
        params = {"lat": lat, "lon": lon, "limit": limit, "appid": api_key}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return [{"error": str(e)}]

if __name__ == "__main__":
    mcp.run()
