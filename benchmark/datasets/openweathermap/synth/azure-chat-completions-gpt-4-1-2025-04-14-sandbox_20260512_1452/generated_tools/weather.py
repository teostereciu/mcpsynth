import os
import requests
from fastmcp import tool

OPENWEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"

@tool("get_current_weather_by_coords")
def get_current_weather_by_coords(lat: float, lon: float, units: str = "standard", lang: str = None):
    """
    Get current weather for a location by latitude and longitude.
    Args:
        lat (float): Latitude
        lon (float): Longitude
        units (str): Units of measurement ('standard', 'metric', 'imperial')
        lang (str): Language code (optional)
    Returns:
        dict: Weather data or error
    """
    params = {
        "lat": lat,
        "lon": lon,
        "appid": OPENWEATHER_API_KEY,
        "units": units,
    }
    if lang:
        params["lang"] = lang
    try:
        resp = requests.get(f"{BASE_URL}/weather", params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("get_current_weather_by_city")
def get_current_weather_by_city(q: str, units: str = "standard", lang: str = None):
    """
    Get current weather for a city (name, optionally state/country).
    Args:
        q (str): City name, optionally state code and country code (comma-separated)
        units (str): Units of measurement ('standard', 'metric', 'imperial')
        lang (str): Language code (optional)
    Returns:
        dict: Weather data or error
    """
    params = {
        "q": q,
        "appid": OPENWEATHER_API_KEY,
        "units": units,
    }
    if lang:
        params["lang"] = lang
    try:
        resp = requests.get(f"{BASE_URL}/weather", params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("get_5day_forecast_by_coords")
def get_5day_forecast_by_coords(lat: float, lon: float, units: str = "standard", lang: str = None, cnt: int = None):
    """
    Get 5 day / 3 hour forecast for a location by latitude and longitude.
    Args:
        lat (float): Latitude
        lon (float): Longitude
        units (str): Units of measurement ('standard', 'metric', 'imperial')
        lang (str): Language code (optional)
        cnt (int): Number of timestamps to return (optional)
    Returns:
        dict: Forecast data or error
    """
    params = {
        "lat": lat,
        "lon": lon,
        "appid": OPENWEATHER_API_KEY,
        "units": units,
    }
    if lang:
        params["lang"] = lang
    if cnt:
        params["cnt"] = cnt
    try:
        resp = requests.get(f"{BASE_URL}/forecast", params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
