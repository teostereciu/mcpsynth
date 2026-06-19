#!/usr/bin/env python3
"""
OpenWeatherMap MCP Server
A Model Context Protocol server providing weather information tools.
"""

import os
import asyncio
import aiohttp
from typing import Dict, Any, Optional, List
from mcp.server.fastmcp import FastMCP
from mcp.types import Tool, ToolResult, TextContent, ImageContent, Content

# Configuration
BASE_URL = "https://api.openweathermap.org"
API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    raise ValueError("OPENWEATHER_API_KEY environment variable must be set")

# Create FastMCP server
app = FastMCP()

async def make_api_request(endpoint: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """Make an API request to OpenWeatherMap."""
    params['appid'] = API_KEY
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BASE_URL}{endpoint}", params=params) as response:
            if response.status != 200:
                raise Exception(f"API request failed with status {response.status}")
            return await response.json()

async def current_weather_by_coordinates(lat: float, lon: float, lang: Optional[str] = None) -> Dict[str, Any]:
    """Get current weather by coordinates."""
    params = {"lat": lat, "lon": lon}
    if lang:
        params["lang"] = lang
    return await make_api_request("/data/2.5/weather", params)

async def current_weather_by_city(city: str, country: Optional[str] = None, state: Optional[str] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    """Get current weather by city name."""
    params = {}
    if state and country:
        params["q"] = f"{city},{state},{country}"
    elif country:
        params["q"] = f"{city},{country}"
    else:
        params["q"] = city
    if lang:
        params["lang"] = lang
    return await make_api_request("/data/2.5/weather", params)

async def current_weather_by_zip(zip_code: str, country: str, lang: Optional[str] = None) -> Dict[str, Any]:
    """Get current weather by ZIP code."""
    params = {"zip": f"{zip_code},{country}"}
    if lang:
        params["lang"] = lang
    return await make_api_request("/data/2.5/weather", params)

async def current_weather_by_city_id(city_id: int, lang: Optional[str] = None) -> Dict[str, Any]:
    """Get current weather by city ID."""
    params = {"id": city_id}
    if lang:
        params["lang"] = lang
    return await make_api_request("/data/2.5/weather", params)

async def forecast_by_coordinates(lat: float, lon: float, lang: Optional[str] = None) -> Dict[str, Any]:
    """Get 5-day forecast by coordinates."""
    params = {"lat": lat, "lon": lon}
    if lang:
        params["lang"] = lang
    return await make_api_request("/data/2.5/forecast", params)

async def forecast_by_city(city: str, country: Optional[str] = None, state: Optional[str] = None, lang: Optional[str] = None) -> Dict[str, Any]:
    """Get 5-day forecast by city name."""
    params = {}
    if state and country:
        params["q"] = f"{city},{state},{country}"
    elif country:
        params["q"] = f"{city},{country}"
    else:
        params["q"] = city
    if lang:
        params["lang"] = lang
    return await make_api_request("/data/2.5/forecast", params)

async def forecast_by_zip(zip_code: str, country: str, lang: Optional[str] = None) -> Dict[str, Any]:
    """Get 5-day forecast by ZIP code."""
    params = {"zip": f"{zip_code},{country}"}
    if lang:
        params["lang"] = lang
    return await make_api_request("/data/2.5/forecast", params)

async def forecast_by_city_id(city_id: int, lang: Optional[str] = None) -> Dict[str, Any]:
    """Get 5-day forecast by city ID."""
    params = {"id": city_id}
    if lang:
        params["lang"] = lang
    return await make_api_request("/data/2.5/forecast", params)

async def air_pollution_by_coordinates(lat: float, lon: float) -> Dict[str, Any]:
    """Get air pollution data by coordinates."""
    params = {"lat": lat, "lon": lon}
    return await make_api_request("/data/2.5/air_pollution", params)

async def air_pollution_forecast_by_coordinates(lat: float, lon: float) -> Dict[str, Any]:
    """Get air pollution forecast by coordinates."""
    params = {"lat": lat, "lon": lon}
    return await make_api_request("/data/2.5/air_pollution/forecast", params)

async def air_pollution_history_by_coordinates(lat: float, lon: float, start: int, end: int) -> Dict[str, Any]:
    """Get air pollution history by coordinates."""
    params = {"lat": lat, "lon": lon, "start": start, "end": end}
    return await make_api_request("/data/2.5/air_pollution/history", params)

async def geocode_direct(city: str, country: Optional[str] = None, state: Optional[str] = None, limit: int = 5) -> Dict[str, Any]:
    """Get coordinates from city name."""
    params = {"q": f"{city},{state},{country}" if state and country else f"{city},{country}" if country else city, "limit": limit}
    return await make_api_request("/geo/1.0/direct", params)

async def geocode_zip(zip_code: str, country: str) -> Dict[str, Any]:
    """Get coordinates from ZIP code."""
    params = {"zip": f"{zip_code},{country}"}
    return await make_api_request("/geo/1.0/zip", params)

async def geocode_reverse(lat: float, lon: float, limit: int = 5) -> Dict[str, Any]:
    """Get location name from coordinates."""
    params = {"lat": lat, "lon": lon, "limit": limit}
    return await make_api_request("/geo/1.0/reverse", params)

@app.tool()
async def get_current_weather(
    lat: Optional[float] = None,
    lon: Optional[float] = None,
    city: Optional[str] = None,
    country: Optional[str] = None,
    state: Optional[str] = None,
    zip_code: Optional[str] = None,
    city_id: Optional[int] = None,
    lang: Optional[str] = None
) -> ToolResult:
    """
    Get current weather information for a location.
    
    Args:
        lat: Latitude coordinate
        lon: Longitude coordinate  
        city: City name
        country: Country code (ISO 3166)
        state: State code (for US cities)
        zip_code: ZIP/Postal code
        city_id: OpenWeatherMap city ID
        lang: Language code for weather descriptions
    
    Returns:
        Current weather data including temperature, humidity, pressure, wind speed, etc.
    """
    
    # Validate input combinations
    if sum(x is not None for x in [lat, lon, city, zip_code, city_id]) != 1:
        return ToolResult(
            content=[TextContent(type="text", text="Error: Must specify exactly one location method (lat/lon, city, zip, or city_id)")],
            isError=True
        )
    
    try:
        if lat is not None and lon is not None:
            data = await current_weather_by_coordinates(lat, lon, lang)
        elif city is not None:
            data = await current_weather_by_city(city, country, state, lang)
        elif zip_code is not None and country is not None:
            data = await current_weather_by_zip(zip_code, country, lang)
        elif city_id is not None:
            data = await current_weather_by_city_id(city_id, lang)
        else:
            return ToolResult(
                content=[TextContent(type="text", text="Error: Invalid combination of parameters")],
                isError=True
            )
        
        # Format response
        result_text = (
            f"Weather in {data['name']}, {data['sys']['country']}:\n"
            f"Temperature: {data['main']['temp']}K ({data['main']['temp'] - 273.15:.1f}°C)\n"
            f"Feels like: {data['main']['feels_like']}K ({data['main']['feels_like'] - 273.15:.1f}°C)\n"
            f"Description: {data['weather'][0]['description']}\n"
            f"Humidity: {data['main']['humidity']}%\n"
            f"Pressure: {data['main']['pressure']} hPa\n"
            f"Wind Speed: {data['wind']['speed']} m/s\n"
        )
        
        return ToolResult(content=[TextContent(type="text", text=result_text)])
        
    except Exception as e:
        return ToolResult(
            content=[TextContent(type="text", text=f"Error fetching weather data: {str(e)}")],
            isError=True
        )

@app.tool()
async def get_forecast(
    lat: Optional[float] = None,
    lon: Optional[float] = None,
    city: Optional[str] = None,
    country: Optional[str] = None,
    state: Optional[str] = None,
    zip_code: Optional[str] = None,
    city_id: Optional[int] = None,
    lang: Optional[str] = None
) -> ToolResult:
    """
    Get 5-day weather forecast for a location.
    
    Args:
        lat: Latitude coordinate
        lon: Longitude coordinate  
        city: City name
        country: Country code (ISO 3166)
        state: State code (for US cities)
        zip_code: ZIP/Postal code
        city_id: OpenWeatherMap city ID
        lang: Language code for weather descriptions
    
    Returns:
        5-day weather forecast data with 3-hour intervals
    """
    
    # Validate input combinations
    if sum(x is not None for x in [lat, lon, city, zip_code, city_id]) != 1:
        return ToolResult(
            content=[TextContent(type="text", text="Error: Must specify exactly one location method (lat/lon, city, zip, or city_id)")],
            isError=True
        )
    
    try:
        if lat is not None and lon is not None:
            data = await forecast_by_coordinates(lat, lon, lang)
        elif city is not None:
            data = await forecast_by_city(city, country, state, lang)
        elif zip_code is not None and country is not None:
            data = await forecast_by_zip(zip_code, country, lang)
        elif city_id is not None:
            data = await forecast_by_city_id(city_id, lang)
        else:
            return ToolResult(
                content=[TextContent(type="text", text="Error: Invalid combination of parameters")],
                isError=True
            )
        
        # Format response
        result_text = f"5-Day Forecast for {data['city']['name']}, {data['city']['country']}:\n\n"
        
        # Show first few forecasts
        for i, item in enumerate(data['list'][:5]):  # First 5 entries (3-hour intervals)
            dt_txt = item['dt_txt']
            temp = item['main']['temp']
            desc = item['weather'][0]['description']
            result_text += f"{dt_txt}: {temp - 273.15:.1f}°C, {desc}\n"
        
        return ToolResult(content=[TextContent(type="text", text=result_text)])
        
    except Exception as e:
        return ToolResult(
            content=[TextContent(type="text", text=f"Error fetching forecast data: {str(e)}")],
            isError=True
        )

@app.tool()
async def get_air_pollution(
    lat: float,
    lon: float,
    forecast: bool = False,
    history_start: Optional[int] = None,
    history_end: Optional[int] = None
) -> ToolResult:
    """
    Get air pollution data for a location.
    
    Args:
        lat: Latitude coordinate
        lon: Longitude coordinate
        forecast: If True, get forecast data; if False, get current data
        history_start: Start timestamp for history (required if history=True)
        history_end: End timestamp for history (required if history=True)
    
    Returns:
        Air pollution data including AQI and pollutant concentrations
    """
    
    try:
        if forecast:
            data = await air_pollution_forecast_by_coordinates(lat, lon)
            result_text = "Air Pollution Forecast:\n"
            for item in data['list']:
                aqi = item['main']['aqi']
                result_text += f"Time: {item['dt']}, AQI: {aqi}\n"
        elif history_start is not None and history_end is not None:
            data = await air_pollution_history_by_coordinates(lat, lon, history_start, history_end)
            result_text = "Air Pollution History:\n"
            for item in data['list']:
                aqi = item['main']['aqi']
                result_text += f"Time: {item['dt']}, AQI: {aqi}\n"
        else:
            data = await air_pollution_by_coordinates(lat, lon)
            aqi = data['list'][0]['main']['aqi']
            result_text = f"Current Air Quality Index: {aqi}\n"
            
            # Add pollutant details
            pollutants = data['list'][0]['components']
            result_text += "Pollutant concentrations:\n"
            for pollutant, concentration in pollutants.items():
                result_text += f"  {pollutant}: {concentration} μg/m³\n"
        
        return ToolResult(content=[TextContent(type="text", text=result_text)])
        
    except Exception as e:
        return ToolResult(
            content=[TextContent(type="text", text=f"Error fetching air pollution data: {str(e)}")],
            isError=True
        )

@app.tool()
async def geocode_location(
    city: Optional[str] = None,
    country: Optional[str] = None,
    state: Optional[str] = None,
    zip_code: Optional[str] = None,
    lat: Optional[float] = None,
    lon: Optional[float] = None,
    limit: int = 5
) -> ToolResult:
    """
    Convert location names to coordinates or vice versa.
    
    Args:
        city: City name
        country: Country code (ISO 3166)
        state: State code (for US cities)
        zip_code: ZIP/Postal code
        lat: Latitude coordinate (for reverse geocoding)
        lon: Longitude coordinate (for reverse geocoding)
        limit: Maximum number of results to return
    
    Returns:
        Location coordinates or names based on input type
    """
    
    # Validate input combinations
    if sum(x is not None for x in [city, zip_code, lat, lon]) > 1:
        return ToolResult(
            content=[TextContent(type="text", text="Error: Specify either city name, zip code, or coordinates")],
            isError=True
        )
    
    try:
        if city is not None:
            data = await geocode_direct(city, country, state, limit)
            if not data:
                return ToolResult(content=[TextContent(type="text", text="No location found")])
            
            result_text = "Matching locations:\n"
            for item in data:
                result_text += f"- {item['name']}, {item['country']} (lat: {item['lat']}, lon: {item['lon']})\n"
                
        elif zip_code is not None and country is not None:
            data = await geocode_zip(zip_code, country)
            result_text = f"ZIP Code {zip_code} corresponds to:\n"
            result_text += f"- {data['name']}, {data['country']} (lat: {data['lat']}, lon: {data['lon']})\n"
            
        elif lat is not None and lon is not None:
            data = await geocode_reverse(lat, lon, limit)
            if not data:
                return ToolResult(content=[TextContent(type="text", text="No location found")])
            
            result_text = "Nearby locations:\n"
            for item in data:
                result_text += f"- {item['name']}, {item['country']} (lat: {item['lat']}, lon: {item['lon']})\n"
        else:
            return ToolResult(
                content=[TextContent(type="text", text="Error: Invalid combination of parameters")],
                isError=True
            )
        
        return ToolResult(content=[TextContent(type="text", text=result_text)])
        
    except Exception as e:
        return ToolResult(
            content=[TextContent(type="text", text=f"Error in geocoding: {str(e)}")],
            isError=True
        )

# Register all tools
if __name__ == "__main__":
    # The server will automatically register all @app.tool() decorated functions
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "tools":
        # Print tool definitions for debugging
        print("Available tools:")
        for tool_def in TOOL_DEFINITIONS:
            print(f"- {tool_def.name}: {tool_def.description}")
    else:
        # Run the server
        app.run()