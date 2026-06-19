import os
from fastmcp import FastMCP

from generated_tools.weather import get_current_weather_by_coords, get_current_weather_by_city, get_5day_forecast_by_coords
from generated_tools.air_pollution import get_air_pollution_current, get_air_pollution_forecast, get_air_pollution_history
from generated_tools.geocoding import direct_geocoding, geocoding_by_zip, reverse_geocoding

TOOLS = [
    get_current_weather_by_coords,
    get_current_weather_by_city,
    get_5day_forecast_by_coords,
    get_air_pollution_current,
    get_air_pollution_forecast,
    get_air_pollution_history,
    direct_geocoding,
    geocoding_by_zip,
    reverse_geocoding,
]

if __name__ == "__main__":
    FastMCP(
        tools=TOOLS,
        stdio=True,
    ).run()
