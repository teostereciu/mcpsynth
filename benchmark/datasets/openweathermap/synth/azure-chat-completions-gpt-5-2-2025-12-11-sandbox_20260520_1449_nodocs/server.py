import os
from typing import Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.geocoding import geocode_direct, geocode_reverse
from generated_tools.weather import (
    get_current_weather_by_city,
    get_current_weather_by_coords,
    get_current_weather_by_zip,
    get_current_weather_by_city_id,
    get_5day_forecast_by_city,
    get_5day_forecast_by_coords,
    get_5day_forecast_by_zip,
    get_5day_forecast_by_city_id,
)
from generated_tools.air_pollution import (
    get_air_pollution_current,
    get_air_pollution_forecast,
    get_air_pollution_history,
)

mcp = FastMCP("openweathermap")


@mcp.tool()
def owm_geocode_direct(q: str, limit: int = 5):
    return geocode_direct(q, limit=limit)


@mcp.tool()
def owm_geocode_reverse(lat: float, lon: float, limit: int = 5):
    return geocode_reverse(lat, lon, limit=limit)


@mcp.tool()
def owm_current_weather_by_city(
    city: str,
    state_code: Optional[str] = None,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
):
    return get_current_weather_by_city(
        city,
        state_code=state_code,
        country_code=country_code,
        units=units,
        lang=lang,
    )


@mcp.tool()
def owm_current_weather_by_coords(
    lat: float,
    lon: float,
    units: Optional[str] = None,
    lang: Optional[str] = None,
):
    return get_current_weather_by_coords(lat, lon, units=units, lang=lang)


@mcp.tool()
def owm_current_weather_by_zip(
    zip_code: str,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
):
    return get_current_weather_by_zip(zip_code, country_code=country_code, units=units, lang=lang)


@mcp.tool()
def owm_current_weather_by_city_id(
    city_id: int,
    units: Optional[str] = None,
    lang: Optional[str] = None,
):
    return get_current_weather_by_city_id(city_id, units=units, lang=lang)


@mcp.tool()
def owm_forecast_5day_by_city(
    city: str,
    state_code: Optional[str] = None,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
):
    return get_5day_forecast_by_city(
        city,
        state_code=state_code,
        country_code=country_code,
        units=units,
        lang=lang,
    )


@mcp.tool()
def owm_forecast_5day_by_coords(
    lat: float,
    lon: float,
    units: Optional[str] = None,
    lang: Optional[str] = None,
):
    return get_5day_forecast_by_coords(lat, lon, units=units, lang=lang)


@mcp.tool()
def owm_forecast_5day_by_zip(
    zip_code: str,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
):
    return get_5day_forecast_by_zip(zip_code, country_code=country_code, units=units, lang=lang)


@mcp.tool()
def owm_forecast_5day_by_city_id(
    city_id: int,
    units: Optional[str] = None,
    lang: Optional[str] = None,
):
    return get_5day_forecast_by_city_id(city_id, units=units, lang=lang)


@mcp.tool()
def owm_air_pollution_current(lat: float, lon: float):
    return get_air_pollution_current(lat, lon)


@mcp.tool()
def owm_air_pollution_forecast(lat: float, lon: float):
    return get_air_pollution_forecast(lat, lon)


@mcp.tool()
def owm_air_pollution_history(lat: float, lon: float, start: int, end: int):
    return get_air_pollution_history(lat, lon, start, end)


if __name__ == "__main__":
    # FastMCP runs over stdio by default
    mcp.run()
