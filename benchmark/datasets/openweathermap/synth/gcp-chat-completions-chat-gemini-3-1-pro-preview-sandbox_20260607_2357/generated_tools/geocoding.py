import os
import requests
from typing import Dict, Any, List

BASE_URL = "https://api.openweathermap.org"

def geocode_direct(q: str, limit: int = 5) -> List[Dict[str, Any]]:
    """Get geographical coordinates for a city name."""
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        return [{"error": "OPENWEATHER_API_KEY environment variable not set"}]
    
    url = f"{BASE_URL}/geo/1.0/direct"
    params = {
        "q": q,
        "limit": limit,
        "appid": api_key
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return [{"error": str(e)}]

def geocode_reverse(lat: float, lon: float, limit: int = 5) -> List[Dict[str, Any]]:
    """Get city name for geographical coordinates."""
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        return [{"error": "OPENWEATHER_API_KEY environment variable not set"}]
    
    url = f"{BASE_URL}/geo/1.0/reverse"
    params = {
        "lat": lat,
        "lon": lon,
        "limit": limit,
        "appid": api_key
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return [{"error": str(e)}]
