import os
import requests
from typing import Dict, Any

BASE_URL = "https://api.openweathermap.org"

def get_current_weather(lat: float, lon: float) -> Dict[str, Any]:
    """Get current weather data for a specific location."""
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        return {"error": "OPENWEATHER_API_KEY environment variable not set"}
    
    url = f"{BASE_URL}/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
