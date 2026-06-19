from mcp.server.fastmcp import FastMCP

from generated_tools.air_pollution import (
    get_air_pollution_current,
    get_air_pollution_forecast,
    get_air_pollution_history,
)
from generated_tools.geocoding import geocode_direct, geocode_reverse, geocode_zip
from generated_tools.weather import (
    get_current_weather_by_city,
    get_current_weather_by_city_id,
    get_current_weather_by_coordinates,
    get_current_weather_by_zip,
    get_forecast_by_city,
    get_forecast_by_city_id,
    get_forecast_by_coordinates,
    get_forecast_by_zip,
)

mcp = FastMCP("openweathermap")

mcp.tool()(geocode_direct)
mcp.tool()(geocode_zip)
mcp.tool()(geocode_reverse)
mcp.tool()(get_current_weather_by_coordinates)
mcp.tool()(get_current_weather_by_city)
mcp.tool()(get_current_weather_by_city_id)
mcp.tool()(get_current_weather_by_zip)
mcp.tool()(get_forecast_by_coordinates)
mcp.tool()(get_forecast_by_city)
mcp.tool()(get_forecast_by_city_id)
mcp.tool()(get_forecast_by_zip)
mcp.tool()(get_air_pollution_current)
mcp.tool()(get_air_pollution_forecast)
mcp.tool()(get_air_pollution_history)


if __name__ == "__main__":
    mcp.run()
