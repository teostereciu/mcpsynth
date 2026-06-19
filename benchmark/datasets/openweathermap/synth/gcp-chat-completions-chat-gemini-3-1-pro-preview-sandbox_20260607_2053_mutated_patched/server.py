import os
import requests
from typing import Optional, Dict, Any, Union, List
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("openweathermap")

# Base URL for OpenWeatherMap API
BASE_URL = "https://api.openweathermap.org"

def get_api_key() -> str:
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        raise ValueError("OPENWEATHER_API_KEY environment variable is not set")
    return api_key

def make_request(path: str, params: Dict[str, Any]) -> Any:
    try:
        api_key = get_api_key()
        params["appid"] = api_key
        url = f"{BASE_URL}{path}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        if e.response is not None:
            try:
                return e.response.json()
            except ValueError:
                return {"error": str(e)}
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_current_weather(
    q: Optional[str] = None,
    lat: Optional[float] = None,
    lon: Optional[float] = None,
    units: str = "metric",
    lang: str = "en"
) -> Any:
    """
    Get current weather data for a location.
    Provide either city name (q) or coordinates (lat, lon).
    """
    params = {"units": units, "lang": lang}
    if q:
        params["q"] = q
    elif lat is not None and lon is not None:
        params["lat"] = lat
        params["lon"] = lon
    else:
        return {"error": "Must provide either 'q' or both 'lat' and 'lon'"}
    
    return make_request("/data/2.5/weather", params)

@mcp.tool()
def get_5day_forecast(
    q: Optional[str] = None,
    lat: Optional[float] = None,
    lon: Optional[float] = None,
    units: str = "metric",
    lang: str = "en"
) -> Any:
    """
    Get 5-day/3-hour forecast data for a location.
    Provide either city name (q) or coordinates (lat, lon).
    """
    params = {"units": units, "lang": lang}
    if q:
        params["q"] = q
    elif lat is not None and lon is not None:
        params["lat"] = lat
        params["lon"] = lon
    else:
        return {"error": "Must provide either 'q' or both 'lat' and 'lon'"}
    
    return make_request("/data/2.5/forecast", params)

@mcp.tool()
def get_air_pollution(lat: float, lon: float) -> Any:
    """
    Get current air pollution data for coordinates.
    """
    params = {"lat": lat, "lon": lon}
    return make_request("/data/2.5/air_pollution", params)

@mcp.tool()
def get_air_pollution_forecast(lat: float, lon: float) -> Any:
    """
    Get forecast air pollution data for coordinates.
    """
    params = {"lat": lat, "lon": lon}
    return make_request("/data/2.5/air_pollution/forecast", params)

@mcp.tool()
def get_air_pollution_history(lat: float, lon: float, start: int, end: int) -> Any:
    """
    Get historical air pollution data for coordinates.
    start and end are Unix timestamps.
    """
    params = {"lat": lat, "lon": lon, "start": start, "end": end}
    return make_request("/data/2.5/air_pollution/history", params)

@mcp.tool()
def geocode_direct(q: str, limit: int = 5) -> Any:
    """
    Direct geocoding: get coordinates by location name.
    q: city name, state code (only for US), and country code divided by comma.
    """
    params = {"q": q, "limit": limit}
    return make_request("/geo/1.0/direct", params)

@mcp.tool()
def geocode_reverse(lat: float, lon: float, limit: int = 5) -> Any:
    """
    Reverse geocoding: get location name by coordinates.
    """
    params = {"lat": lat, "lon": lon, "limit": limit}
    return make_request("/geo/1.0/reverse", params)

@mcp.tool()
def geocode_zip(zip_code: str) -> Any:
    """
    Zip geocoding: get coordinates by zip/post code.
    zip_code: zip/post code and country code divided by comma.
    """
    params = {"zip": zip_code}
    return make_request("/geo/1.0/zip", params)

if __name__ == "__main__":
    mcp.run()
