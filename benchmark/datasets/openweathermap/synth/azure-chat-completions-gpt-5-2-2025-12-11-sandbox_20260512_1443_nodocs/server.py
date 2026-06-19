import os
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.client import OpenWeatherClient
from generated_tools.weather import (
    get_current_weather_by_bbox,
    get_current_weather_by_city,
    get_current_weather_by_city_id,
    get_current_weather_by_coordinates,
    get_current_weather_by_zip,
)
from generated_tools.forecast import (
    get_5day_forecast_by_city,
    get_5day_forecast_by_city_id,
    get_5day_forecast_by_coordinates,
    get_5day_forecast_by_zip,
)
from generated_tools.air_pollution import (
    get_air_pollution_current,
    get_air_pollution_forecast,
    get_air_pollution_history,
)
from generated_tools.geocoding import geocode_direct, geocode_reverse, geocode_zip

mcp = FastMCP("openweathermap")


def _client() -> OpenWeatherClient:
    return OpenWeatherClient(api_key=os.getenv("OPENWEATHER_API_KEY"))


@mcp.tool()
def owm_geocode_direct(query: str, limit: int = 5) -> Dict[str, Any]:
    return geocode_direct(_client(), query=query, limit=limit)


@mcp.tool()
def owm_geocode_reverse(lat: float, lon: float, limit: int = 5) -> Dict[str, Any]:
    return geocode_reverse(_client(), lat=lat, lon=lon, limit=limit)


@mcp.tool()
def owm_geocode_zip(zip_code: str, country_code: Optional[str] = None) -> Dict[str, Any]:
    return geocode_zip(_client(), zip_code=zip_code, country_code=country_code)


@mcp.tool()
def owm_current_weather_by_city(
    city_name: str,
    state_code: Optional[str] = None,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    return get_current_weather_by_city(
        _client(),
        city_name=city_name,
        state_code=state_code,
        country_code=country_code,
        units=units,
        lang=lang,
    )


@mcp.tool()
def owm_current_weather_by_coordinates(
    lat: float,
    lon: float,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    return get_current_weather_by_coordinates(_client(), lat=lat, lon=lon, units=units, lang=lang)


@mcp.tool()
def owm_current_weather_by_city_id(
    city_id: int,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    return get_current_weather_by_city_id(_client(), city_id=city_id, units=units, lang=lang)


@mcp.tool()
def owm_current_weather_by_zip(
    zip_code: str,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    return get_current_weather_by_zip(
        _client(),
        zip_code=zip_code,
        country_code=country_code,
        units=units,
        lang=lang,
    )


@mcp.tool()
def owm_current_weather_by_bbox(
    lon_left: float,
    lat_bottom: float,
    lon_right: float,
    lat_top: float,
    zoom: int = 10,
    cluster: Optional[bool] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
) -> Dict[str, Any]:
    return get_current_weather_by_bbox(
        _client(),
        lon_left=lon_left,
        lat_bottom=lat_bottom,
        lon_right=lon_right,
        lat_top=lat_top,
        zoom=zoom,
        cluster=cluster,
        units=units,
        lang=lang,
    )


@mcp.tool()
def owm_forecast_5day_by_city(
    city_name: str,
    state_code: Optional[str] = None,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
) -> Dict[str, Any]:
    return get_5day_forecast_by_city(
        _client(),
        city_name=city_name,
        state_code=state_code,
        country_code=country_code,
        units=units,
        lang=lang,
        cnt=cnt,
    )


@mcp.tool()
def owm_forecast_5day_by_coordinates(
    lat: float,
    lon: float,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
) -> Dict[str, Any]:
    return get_5day_forecast_by_coordinates(_client(), lat=lat, lon=lon, units=units, lang=lang, cnt=cnt)


@mcp.tool()
def owm_forecast_5day_by_city_id(
    city_id: int,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
) -> Dict[str, Any]:
    return get_5day_forecast_by_city_id(_client(), city_id=city_id, units=units, lang=lang, cnt=cnt)


@mcp.tool()
def owm_forecast_5day_by_zip(
    zip_code: str,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
) -> Dict[str, Any]:
    return get_5day_forecast_by_zip(
        _client(),
        zip_code=zip_code,
        country_code=country_code,
        units=units,
        lang=lang,
        cnt=cnt,
    )


@mcp.tool()
def owm_air_pollution_current(lat: float, lon: float) -> Dict[str, Any]:
    return get_air_pollution_current(_client(), lat=lat, lon=lon)


@mcp.tool()
def owm_air_pollution_forecast(lat: float, lon: float) -> Dict[str, Any]:
    return get_air_pollution_forecast(_client(), lat=lat, lon=lon)


@mcp.tool()
def owm_air_pollution_history(lat: float, lon: float, start: int, end: int) -> Dict[str, Any]:
    return get_air_pollution_history(_client(), lat=lat, lon=lon, start=start, end=end)


if __name__ == "__main__":
    mcp.run()
