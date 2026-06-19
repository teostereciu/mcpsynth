from mcp.server.fastmcp import FastMCP

from generated_tools.air_pollution import (
    get_air_pollution_current,
    get_air_pollution_forecast,
    get_air_pollution_history,
)
from generated_tools.current_weather import (
    get_current_weather_by_city_name,
    get_current_weather_by_coords,
)
from generated_tools.forecast import get_5day_forecast_by_coords
from generated_tools.geocoding import geocode_direct, geocode_reverse, geocode_zip


mcp = FastMCP("openweathermap")


# Geocoding
@mcp.tool()
def geocode_direct_locations(q: str, limit: int = 5):
    """Convert a place name to coordinates using OpenWeather Geocoding API."""
    return geocode_direct(q=q, limit=limit)


@mcp.tool()
def geocode_reverse_locations(lat: float, lon: float, limit: int = 5):
    """Convert coordinates to nearby place names using OpenWeather Geocoding API."""
    return geocode_reverse(lat=lat, lon=lon, limit=limit)


@mcp.tool()
def geocode_zip_to_location(zip_code: str, country_code: str):
    """Convert a zip/post code to coordinates using OpenWeather Geocoding API."""
    return geocode_zip(zip_code=zip_code, country_code=country_code)


# Current weather
@mcp.tool()
def get_current_weather(lat: float, lon: float, units: str | None = None, lang: str | None = None):
    """Get current weather by coordinates."""
    return get_current_weather_by_coords(lat=lat, lon=lon, units=units, lang=lang)


@mcp.tool()
def get_current_weather_by_city(q: str, units: str | None = None, lang: str | None = None):
    """Get current weather by city name query (deprecated by OpenWeather but still supported)."""
    return get_current_weather_by_city_name(q=q, units=units, lang=lang)


# Forecast
@mcp.tool()
def get_5day_forecast(lat: float, lon: float, units: str | None = None, lang: str | None = None, cnt: int | None = None):
    """Get 5 day / 3 hour forecast by coordinates."""
    return get_5day_forecast_by_coords(lat=lat, lon=lon, units=units, lang=lang, cnt=cnt)


# Air pollution
@mcp.tool()
def get_air_quality_current(lat: float, lon: float):
    """Get current air quality (AQI + pollutants) by coordinates."""
    return get_air_pollution_current(lat=lat, lon=lon)


@mcp.tool()
def get_air_quality_forecast(lat: float, lon: float):
    """Get air quality forecast (up to 4 days hourly) by coordinates."""
    return get_air_pollution_forecast(lat=lat, lon=lon)


@mcp.tool()
def get_air_quality_history(lat: float, lon: float, start: int, end: int):
    """Get historical air quality by coordinates and unix time range."""
    return get_air_pollution_history(lat=lat, lon=lon, start=start, end=end)


if __name__ == "__main__":
    mcp.run()
