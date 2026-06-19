from typing import Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.weather import (
    geocode_direct,
    geocode_reverse,
    geocode_zip,
    get_air_pollution_current,
    get_air_pollution_forecast,
    get_air_pollution_history,
    get_current_weather_by_city,
    get_current_weather_by_city_id,
    get_current_weather_by_coordinates,
    get_current_weather_by_zip,
    get_forecast_by_city,
    get_forecast_by_city_id,
    get_forecast_by_coordinates,
    get_forecast_by_zip,
)

mcp = FastMCP("openweathermap-mcp")


@mcp.tool()
def get_current_weather_by_city_tool(
    city: str,
    state_code: Optional[str] = None,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
):
    return get_current_weather_by_city(city, state_code, country_code, units, lang)


@mcp.tool()
def get_current_weather_by_coordinates_tool(
    lat: float,
    lon: float,
    units: Optional[str] = None,
    lang: Optional[str] = None,
):
    return get_current_weather_by_coordinates(lat, lon, units, lang)


@mcp.tool()
def get_current_weather_by_zip_tool(
    zip_code: str,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
):
    return get_current_weather_by_zip(zip_code, country_code, units, lang)


@mcp.tool()
def get_current_weather_by_city_id_tool(
    city_id: int,
    units: Optional[str] = None,
    lang: Optional[str] = None,
):
    return get_current_weather_by_city_id(city_id, units, lang)


@mcp.tool()
def get_forecast_by_city_tool(
    city: str,
    state_code: Optional[str] = None,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
):
    return get_forecast_by_city(city, state_code, country_code, units, lang, cnt)


@mcp.tool()
def get_forecast_by_coordinates_tool(
    lat: float,
    lon: float,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
):
    return get_forecast_by_coordinates(lat, lon, units, lang, cnt)


@mcp.tool()
def get_forecast_by_zip_tool(
    zip_code: str,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
):
    return get_forecast_by_zip(zip_code, country_code, units, lang, cnt)


@mcp.tool()
def get_forecast_by_city_id_tool(
    city_id: int,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
):
    return get_forecast_by_city_id(city_id, units, lang, cnt)


@mcp.tool()
def get_air_pollution_current_tool(lat: float, lon: float):
    return get_air_pollution_current(lat, lon)


@mcp.tool()
def get_air_pollution_forecast_tool(lat: float, lon: float):
    return get_air_pollution_forecast(lat, lon)


@mcp.tool()
def get_air_pollution_history_tool(lat: float, lon: float, start: int, end: int):
    return get_air_pollution_history(lat, lon, start, end)


@mcp.tool()
def geocode_direct_tool(q: str, limit: Optional[int] = None):
    return geocode_direct(q, limit)


@mcp.tool()
def geocode_reverse_tool(lat: float, lon: float, limit: Optional[int] = None):
    return geocode_reverse(lat, lon, limit)


@mcp.tool()
def geocode_zip_tool(zip_code: str, country_code: Optional[str] = None):
    return geocode_zip(zip_code, country_code)


if __name__ == "__main__":
    mcp.run()
