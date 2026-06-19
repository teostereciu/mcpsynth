from mcp.server.fastmcp import FastMCP

from generated_tools.air_pollution import (
    get_air_pollution_forecast,
    get_air_pollution_history,
    get_current_air_pollution,
)
from generated_tools.current_weather import (
    get_current_weather_by_city_id,
    get_current_weather_by_city_name,
    get_current_weather_by_coordinates,
    get_current_weather_by_zip,
)
from generated_tools.forecast_5day import (
    get_5day_forecast_by_city_id,
    get_5day_forecast_by_city_name,
    get_5day_forecast_by_coordinates,
    get_5day_forecast_by_zip,
)
from generated_tools.geocoding import geocode_direct, geocode_reverse, geocode_zip

mcp = FastMCP("openweathermap")


@mcp.tool()
def geocode_direct_locations(q: str, limit: int = 5):
    return geocode_direct(q=q, limit=limit)


@mcp.tool()
def geocode_zip_code(zip_code: str, country_code: str | None = None):
    return geocode_zip(zip_code=zip_code, country_code=country_code)


@mcp.tool()
def geocode_reverse_locations(latitude: float, longitude: float, limit: int = 5):
    return geocode_reverse(latitude=latitude, longitude=longitude, limit=limit)


@mcp.tool()
def current_weather_by_coordinates(
    latitude: float,
    longitude: float,
    units: str | None = None,
    language: str | None = None,
    mode: str | None = None,
):
    return get_current_weather_by_coordinates(
        latitude=latitude, longitude=longitude, units=units, language=language, mode=mode
    )


@mcp.tool()
def current_weather_by_city_name(
    q: str,
    units: str | None = None,
    language: str | None = None,
    mode: str | None = None,
):
    return get_current_weather_by_city_name(q=q, units=units, language=language, mode=mode)


@mcp.tool()
def current_weather_by_city_id(
    city_id: int,
    units: str | None = None,
    language: str | None = None,
    mode: str | None = None,
):
    return get_current_weather_by_city_id(city_id=city_id, units=units, language=language, mode=mode)


@mcp.tool()
def current_weather_by_zip(
    zip_code: str,
    country_code: str | None = None,
    units: str | None = None,
    language: str | None = None,
    mode: str | None = None,
):
    return get_current_weather_by_zip(
        zip_code=zip_code,
        country_code=country_code,
        units=units,
        language=language,
        mode=mode,
    )


@mcp.tool()
def forecast_5day_by_coordinates(
    latitude: float,
    longitude: float,
    units: str | None = None,
    language: str | None = None,
    mode: str | None = None,
    count: int | None = None,
):
    return get_5day_forecast_by_coordinates(
        latitude=latitude,
        longitude=longitude,
        units=units,
        language=language,
        mode=mode,
        count=count,
    )


@mcp.tool()
def forecast_5day_by_city_name(
    q: str,
    units: str | None = None,
    language: str | None = None,
    mode: str | None = None,
    count: int | None = None,
):
    return get_5day_forecast_by_city_name(q=q, units=units, language=language, mode=mode, count=count)


@mcp.tool()
def forecast_5day_by_city_id(
    city_id: int,
    units: str | None = None,
    language: str | None = None,
    mode: str | None = None,
    count: int | None = None,
):
    return get_5day_forecast_by_city_id(
        city_id=city_id, units=units, language=language, mode=mode, count=count
    )


@mcp.tool()
def forecast_5day_by_zip(
    zip_code: str,
    country_code: str | None = None,
    units: str | None = None,
    language: str | None = None,
    mode: str | None = None,
    count: int | None = None,
):
    return get_5day_forecast_by_zip(
        zip_code=zip_code,
        country_code=country_code,
        units=units,
        language=language,
        mode=mode,
        count=count,
    )


@mcp.tool()
def air_pollution_current(latitude: float, longitude: float):
    return get_current_air_pollution(latitude=latitude, longitude=longitude)


@mcp.tool()
def air_pollution_forecast(latitude: float, longitude: float):
    return get_air_pollution_forecast(latitude=latitude, longitude=longitude)


@mcp.tool()
def air_pollution_history(latitude: float, longitude: float, start: int, end: int):
    return get_air_pollution_history(latitude=latitude, longitude=longitude, start=start, end=end)


if __name__ == "__main__":
    mcp.run()
