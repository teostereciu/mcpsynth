from mcp.server.fastmcp import FastMCP

from generated_tools.air_pollution import (
    get_air_pollution_forecast,
    get_air_pollution_history,
    get_current_air_pollution,
)
from generated_tools.geocoding import geocode_direct, geocode_reverse, geocode_zip
from generated_tools.weather import (
    get_current_weather_by_city_id,
    get_current_weather_by_city_name,
    get_current_weather_by_coordinates,
    get_current_weather_by_zip,
    get_forecast_by_city_id,
    get_forecast_by_city_name,
    get_forecast_by_coordinates,
    get_forecast_by_zip,
)

mcp = FastMCP("openweathermap")


@mcp.tool()
def geocode_direct_tool(query: str, limit: int = 5):
    return geocode_direct(query, limit)


@mcp.tool()
def geocode_zip_tool(zip_code: str, country_code: str | None = None):
    return geocode_zip(zip_code, country_code)


@mcp.tool()
def geocode_reverse_tool(lat: float, lon: float, limit: int = 5):
    return geocode_reverse(lat, lon, limit)


@mcp.tool()
def get_current_weather_by_coordinates_tool(lat: float, lon: float, units: str | None = None, lang: str | None = None):
    return get_current_weather_by_coordinates(lat, lon, units, lang)


@mcp.tool()
def get_current_weather_by_city_name_tool(query: str, units: str | None = None, lang: str | None = None):
    return get_current_weather_by_city_name(query, units, lang)


@mcp.tool()
def get_current_weather_by_city_id_tool(city_id: int, units: str | None = None, lang: str | None = None):
    return get_current_weather_by_city_id(city_id, units, lang)


@mcp.tool()
def get_current_weather_by_zip_tool(zip_code: str, country_code: str | None = None, units: str | None = None, lang: str | None = None):
    return get_current_weather_by_zip(zip_code, country_code, units, lang)


@mcp.tool()
def get_forecast_by_coordinates_tool(lat: float, lon: float, units: str | None = None, lang: str | None = None, cnt: int | None = None):
    return get_forecast_by_coordinates(lat, lon, units, lang, cnt)


@mcp.tool()
def get_forecast_by_city_name_tool(query: str, units: str | None = None, lang: str | None = None, cnt: int | None = None):
    return get_forecast_by_city_name(query, units, lang, cnt)


@mcp.tool()
def get_forecast_by_city_id_tool(city_id: int, units: str | None = None, lang: str | None = None, cnt: int | None = None):
    return get_forecast_by_city_id(city_id, units, lang, cnt)


@mcp.tool()
def get_forecast_by_zip_tool(zip_code: str, country_code: str | None = None, units: str | None = None, lang: str | None = None, cnt: int | None = None):
    return get_forecast_by_zip(zip_code, country_code, units, lang, cnt)


@mcp.tool()
def get_current_air_pollution_tool(lat: float, lon: float):
    return get_current_air_pollution(lat, lon)


@mcp.tool()
def get_air_pollution_forecast_tool(lat: float, lon: float):
    return get_air_pollution_forecast(lat, lon)


@mcp.tool()
def get_air_pollution_history_tool(lat: float, lon: float, start: int, end: int):
    return get_air_pollution_history(lat, lon, start, end)


if __name__ == "__main__":
    mcp.run()
