import os
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("openweathermap")

BASE_URL = "https://api.openweathermap.org"

def get_api_key():
    key = os.environ.get("OPENWEATHER_API_KEY")
    if not key:
        raise ValueError("OPENWEATHER_API_KEY environment variable is required")
    return key

@mcp.tool()
def get_current_weather(lat: float, lon: float, units: str = "metric", lang: str = "en") -> dict:
    """Get current weather data for a specific latitude and longitude."""
    try:
        params = {
            "lat": lat,
            "lon": lon,
            "appid": get_api_key(),
            "units": units,
            "lang": lang
        }
        response = requests.get(f"{BASE_URL}/data/2.5/weather", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_current_weather_by_query(q: str, units: str = "metric", lang: str = "en") -> dict:
    """Get current weather data by city name (e.g., 'London', 'London,GB', 'London,NY,US')."""
    try:
        params = {
            "q": q,
            "appid": get_api_key(),
            "units": units,
            "lang": lang
        }
        response = requests.get(f"{BASE_URL}/data/2.5/weather", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_forecast(lat: float, lon: float, units: str = "metric", lang: str = "en") -> dict:
    """Get 5-day/3-hour forecast data for a specific latitude and longitude."""
    try:
        params = {
            "lat": lat,
            "lon": lon,
            "appid": get_api_key(),
            "units": units,
            "lang": lang
        }
        response = requests.get(f"{BASE_URL}/data/2.5/forecast", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_forecast_by_query(q: str, units: str = "metric", lang: str = "en") -> dict:
    """Get 5-day/3-hour forecast data by city name (e.g., 'London', 'London,GB', 'London,NY,US')."""
    try:
        params = {
            "q": q,
            "appid": get_api_key(),
            "units": units,
            "lang": lang
        }
        response = requests.get(f"{BASE_URL}/data/2.5/forecast", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_air_pollution(lat: float, lon: float) -> dict:
    """Get current air pollution data for a specific latitude and longitude."""
    try:
        params = {
            "lat": lat,
            "lon": lon,
            "appid": get_api_key()
        }
        response = requests.get(f"{BASE_URL}/data/2.5/air_pollution", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def geocode_direct(q: str, limit: int = 5) -> dict:
    """Direct geocoding: get geographical coordinates (lat, lon) by location name (e.g., 'London', 'London,GB')."""
    try:
        params = {
            "q": q,
            "limit": limit,
            "appid": get_api_key()
        }
        response = requests.get(f"{BASE_URL}/geo/1.0/direct", params=params)
        response.raise_for_status()
        return {"results": response.json()}
    except requests.RequestException as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def geocode_reverse(lat: float, lon: float, limit: int = 5) -> dict:
    """Reverse geocoding: get location names by geographical coordinates (lat, lon)."""
    try:
        params = {
            "lat": lat,
            "lon": lon,
            "limit": limit,
            "appid": get_api_key()
        }
        response = requests.get(f"{BASE_URL}/geo/1.0/reverse", params=params)
        response.raise_for_status()
        return {"results": response.json()}
    except requests.RequestException as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    mcp.run()
