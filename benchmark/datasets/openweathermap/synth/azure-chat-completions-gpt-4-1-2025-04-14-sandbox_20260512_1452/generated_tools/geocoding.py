import os
import requests
from fastmcp import tool

OPENWEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org"

@tool("direct_geocoding")
def direct_geocoding(q: str, limit: int = 5):
    """
    Direct geocoding: get coordinates by location name (city, state, country).
    Args:
        q (str): City name, state code (US only), country code (comma-separated)
        limit (int): Max number of results (default 5)
    Returns:
        list: List of locations or error
    """
    params = {
        "q": q,
        "limit": limit,
        "appid": OPENWEATHER_API_KEY,
    }
    try:
        resp = requests.get(f"{BASE_URL}/geo/1.0/direct", params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("geocoding_by_zip")
def geocoding_by_zip(zip_code: str):
    """
    Get coordinates by zip/post code and country code.
    Args:
        zip_code (str): Zip/post code and country code (comma-separated)
    Returns:
        dict: Location info or error
    """
    params = {
        "zip": zip_code,
        "appid": OPENWEATHER_API_KEY,
    }
    try:
        resp = requests.get(f"{BASE_URL}/geo/1.0/zip", params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("reverse_geocoding")
def reverse_geocoding(lat: float, lon: float, limit: int = 5):
    """
    Reverse geocoding: get location names by coordinates.
    Args:
        lat (float): Latitude
        lon (float): Longitude
        limit (int): Max number of results (default 5)
    Returns:
        list: List of locations or error
    """
    params = {
        "lat": lat,
        "lon": lon,
        "limit": limit,
        "appid": OPENWEATHER_API_KEY,
    }
    try:
        resp = requests.get(f"{BASE_URL}/geo/1.0/reverse", params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
