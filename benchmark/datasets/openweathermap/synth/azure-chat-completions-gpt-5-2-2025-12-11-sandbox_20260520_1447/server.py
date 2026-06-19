from typing import Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.air_pollution import (
    get_air_pollution_forecast,
    get_air_pollution_history,
    get_current_air_pollution,
)
from generated_tools.current_weather import (
    get_current_weather_by_city_id,
    get_current_weather_by_city_name,
    get_current_weather_by_coords,
    get_current_weather_by_zip,
)
from generated_tools.forecast_5day import (
    get_5day_forecast_by_city_id,
    get_5day_forecast_by_city_name,
    get_5day_forecast_by_coords,
    get_5day_forecast_by_zip,
)
from generated_tools.geocoding import geocode_direct, geocode_reverse, geocode_zip


mcp = FastMCP("openweathermap")


# --- Geocoding ---
@mcp.tool()
def geocode_direct_tool(q: str, limit: int = 5):
    """Direct geocoding: location name -> coordinates."""
    return geocode_direct(q=q, limit=limit)


@mcp.tool()
def geocode_zip_tool(zip_code: str, country_code: str):
    """Zip/post code geocoding: zip -> coordinates."""
    return geocode_zip(zip_code=zip_code, country_code=country_code)


@mcp.tool()
def geocode_reverse_tool(lat: float, lon: float, limit: int = 5):
    """Reverse geocoding: coordinates -> nearby place names."""
    return geocode_reverse(lat=lat, lon=lon, limit=limit)


# --- Current weather ---
@mcp.tool()
def get_current_weather_by_coords_tool(
    lat: float,
    lon: float,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
):
    """Get current weather by geographic coordinates."""
    return get_current_weather_by_coords(lat=lat, lon=lon, units=units, lang=lang, mode=mode)


@mcp.tool()
def get_current_weather_by_city_name_tool(
    city: str,
    country_code: Optional[str] = None,
    state_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
):
    """Get current weather by city name (built-in geocoding; deprecated by OpenWeather but still supported)."""
    return get_current_weather_by_city_name(
        city=city,
        country_code=country_code,
        state_code=state_code,
        units=units,
        lang=lang,
        mode=mode,
    )


@mcp.tool()
def get_current_weather_by_city_id_tool(
    city_id: int,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
):
    """Get current weather by OpenWeather city ID (deprecated by OpenWeather but still supported)."""
    return get_current_weather_by_city_id(city_id=city_id, units=units, lang=lang, mode=mode)


@mcp.tool()
def get_current_weather_by_zip_tool(
    zip_code: str,
    country_code: str,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
):
    """Get current weather by zip/post code (deprecated by OpenWeather but still supported)."""
    return get_current_weather_by_zip(
        zip_code=zip_code,
        country_code=country_code,
        units=units,
        lang=lang,
        mode=mode,
    )


# --- 5 day / 3 hour forecast ---
@mcp.tool()
def get_5day_forecast_by_coords_tool(
    lat: float,
    lon: float,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    cnt: Optional[int] = None,
):
    """Get 5 day / 3 hour forecast by geographic coordinates."""
    return get_5day_forecast_by_coords(lat=lat, lon=lon, units=units, lang=lang, mode=mode, cnt=cnt)


@mcp.tool()
def get_5day_forecast_by_city_name_tool(
    city: str,
    country_code: Optional[str] = None,
    state_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    cnt: Optional[int] = None,
):
    """Get 5 day / 3 hour forecast by city name (built-in geocoding; deprecated by OpenWeather but still supported)."""
    return get_5day_forecast_by_city_name(
        city=city,
        country_code=country_code,
        state_code=state_code,
        units=units,
        lang=lang,
        mode=mode,
        cnt=cnt,
    )


@mcp.tool()
def get_5day_forecast_by_city_id_tool(
    city_id: int,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    cnt: Optional[int] = None,
):
    """Get 5 day / 3 hour forecast by OpenWeather city ID (deprecated by OpenWeather but still supported)."""
    return get_5day_forecast_by_city_id(city_id=city_id, units=units, lang=lang, mode=mode, cnt=cnt)


@mcp.tool()
def get_5day_forecast_by_zip_tool(
    zip_code: str,
    country_code: str,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    cnt: Optional[int] = None,
):
    """Get 5 day / 3 hour forecast by zip/post code (deprecated by OpenWeather but still supported)."""
    return get_5day_forecast_by_zip(
        zip_code=zip_code,
        country_code=country_code,
        units=units,
        lang=lang,
        mode=mode,
        cnt=cnt,
    )


# --- Air pollution ---
@mcp.tool()
def get_current_air_pollution_tool(lat: float, lon: float):
    """Get current air pollution data for coordinates."""
    return get_current_air_pollution(lat=lat, lon=lon)


@mcp.tool()
def get_air_pollution_forecast_tool(lat: float, lon: float):
    """Get forecast air pollution data for coordinates."""
    return get_air_pollution_forecast(lat=lat, lon=lon)


@mcp.tool()
def get_air_pollution_history_tool(lat: float, lon: float, start: int, end: int):
    """Get historical air pollution data for coordinates and time range (unix timestamps)."""
    return get_air_pollution_history(lat=lat, lon=lon, start=start, end=end)


if __name__ == "__main__":
    mcp.run_stdio()
