"""OpenWeatherMap Free Tier MCP server tools package."""

from __future__ import annotations

from fastmcp import FastMCP

from .air_pollution import air_pollution_current, air_pollution_forecast, air_pollution_history
from .current_weather import (
    current_weather_by_city_id,
    current_weather_by_city_name,
    current_weather_by_coordinates,
    current_weather_by_zip,
)
from .forecast import (
    forecast_5day_by_city_id,
    forecast_5day_by_city_name,
    forecast_5day_by_coordinates,
    forecast_5day_by_zip,
)
from .geocoding import geocode_direct, geocode_reverse, geocode_zip


mcp = FastMCP("openweathermap-free")

# Current weather
mcp.tool()(current_weather_by_city_name)
mcp.tool()(current_weather_by_coordinates)
mcp.tool()(current_weather_by_city_id)
mcp.tool()(current_weather_by_zip)

# Forecast
mcp.tool()(forecast_5day_by_city_name)
mcp.tool()(forecast_5day_by_coordinates)
mcp.tool()(forecast_5day_by_city_id)
mcp.tool()(forecast_5day_by_zip)

# Geocoding
mcp.tool()(geocode_direct)
mcp.tool()(geocode_reverse)
mcp.tool()(geocode_zip)

# Air pollution
mcp.tool()(air_pollution_current)
mcp.tool()(air_pollution_forecast)
mcp.tool()(air_pollution_history)
