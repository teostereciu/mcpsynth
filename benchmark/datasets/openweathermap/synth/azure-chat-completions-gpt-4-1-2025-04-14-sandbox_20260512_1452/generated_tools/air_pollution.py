import os
import requests
from fastmcp import tool

OPENWEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"

@tool("get_air_pollution_current")
def get_air_pollution_current(lat: float, lon: float):
    """
    Get current air pollution data for a location by latitude and longitude.
    Args:
        lat (float): Latitude
        lon (float): Longitude
    Returns:
        dict: Air pollution data or error
    """
    params = {
        "lat": lat,
        "lon": lon,
        "appid": OPENWEATHER_API_KEY,
    }
    try:
        resp = requests.get(f"{BASE_URL}/air_pollution", params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("get_air_pollution_forecast")
def get_air_pollution_forecast(lat: float, lon: float):
    """
    Get forecast air pollution data for a location by latitude and longitude.
    Args:
        lat (float): Latitude
        lon (float): Longitude
    Returns:
        dict: Air pollution forecast data or error
    """
    params = {
        "lat": lat,
        "lon": lon,
        "appid": OPENWEATHER_API_KEY,
    }
    try:
        resp = requests.get(f"{BASE_URL}/air_pollution/forecast", params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("get_air_pollution_history")
def get_air_pollution_history(lat: float, lon: float, start: int, end: int):
    """
    Get historical air pollution data for a location by latitude and longitude.
    Args:
        lat (float): Latitude
        lon (float): Longitude
        start (int): Start date (unix time, UTC)
        end (int): End date (unix time, UTC)
    Returns:
        dict: Air pollution historical data or error
    """
    params = {
        "lat": lat,
        "lon": lon,
        "start": start,
        "end": end,
        "appid": OPENWEATHER_API_KEY,
    }
    try:
        resp = requests.get(f"{BASE_URL}/air_pollution/history", params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
