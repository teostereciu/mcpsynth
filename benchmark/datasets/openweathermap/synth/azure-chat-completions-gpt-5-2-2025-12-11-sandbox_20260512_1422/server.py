from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.air_pollution import (
    air_pollution_current,
    air_pollution_forecast,
    air_pollution_history,
)
from generated_tools.current_weather import (
    current_weather_by_city_id,
    current_weather_by_city_name,
    current_weather_by_coords,
    current_weather_by_zip,
)
from generated_tools.forecast_5day import (
    forecast_5day_by_city_id,
    forecast_5day_by_city_name,
    forecast_5day_by_coords,
    forecast_5day_by_zip,
)
from generated_tools.geocoding import geocode_direct, geocode_reverse, geocode_zip


mcp = FastMCP("openweathermap")


@mcp.tool()
def geocoding_direct(q: str, limit: int = 5) -> Any:
    """Direct geocoding: location name -> coordinates."""
    return geocode_direct(q=q, limit=limit)


@mcp.tool()
def geocoding_reverse(lat: float, lon: float, limit: int = 5) -> Any:
    """Reverse geocoding: coordinates -> nearby location names."""
    return geocode_reverse(lat=lat, lon=lon, limit=limit)


@mcp.tool()
def geocoding_zip(zip_code: str, country_code: str) -> Any:
    """Geocoding by zip/post code -> coordinates."""
    return geocode_zip(zip_code=zip_code, country_code=country_code)


@mcp.tool()
def weather_current_by_coords(
    lat: float,
    lon: float,
    units: str = "standard",
    lang: Optional[str] = None,
    mode: Optional[str] = None,
) -> Any:
    """Current weather by coordinates."""
    return current_weather_by_coords(lat=lat, lon=lon, units=units, lang=lang, mode=mode)


@mcp.tool()
def weather_current_by_city_name(
    city: str,
    state_code: Optional[str] = None,
    country_code: Optional[str] = None,
    units: str = "standard",
    lang: Optional[str] = None,
    mode: Optional[str] = None,
) -> Any:
    """Current weather by city name (q=city[,state][,country])."""
    return current_weather_by_city_name(
        city=city,
        state_code=state_code,
        country_code=country_code,
        units=units,
        lang=lang,
        mode=mode,
    )


@mcp.tool()
def weather_current_by_zip(
    zip_code: str,
    country_code: str,
    units: str = "standard",
    lang: Optional[str] = None,
    mode: Optional[str] = None,
) -> Any:
    """Current weather by ZIP/postal code."""
    return current_weather_by_zip(
        zip_code=zip_code,
        country_code=country_code,
        units=units,
        lang=lang,
        mode=mode,
    )


@mcp.tool()
def weather_current_by_city_id(
    city_id: int,
    units: str = "standard",
    lang: Optional[str] = None,
    mode: Optional[str] = None,
) -> Any:
    """Current weather by city ID."""
    return current_weather_by_city_id(city_id=city_id, units=units, lang=lang, mode=mode)


@mcp.tool()
def forecast_5day_by_coords_tool(
    lat: float,
    lon: float,
    units: str = "standard",
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    cnt: Optional[int] = None,
) -> Any:
    """5 day / 3 hour forecast by coordinates."""
    return forecast_5day_by_coords(lat=lat, lon=lon, units=units, lang=lang, mode=mode, cnt=cnt)


@mcp.tool()
def forecast_5day_by_city_name_tool(
    city: str,
    state_code: Optional[str] = None,
    country_code: Optional[str] = None,
    units: str = "standard",
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    cnt: Optional[int] = None,
) -> Any:
    """5 day / 3 hour forecast by city name."""
    return forecast_5day_by_city_name(
        city=city,
        state_code=state_code,
        country_code=country_code,
        units=units,
        lang=lang,
        mode=mode,
        cnt=cnt,
    )


@mcp.tool()
def forecast_5day_by_zip_tool(
    zip_code: str,
    country_code: str,
    units: str = "standard",
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    cnt: Optional[int] = None,
) -> Any:
    """5 day / 3 hour forecast by ZIP/postal code."""
    return forecast_5day_by_zip(
        zip_code=zip_code,
        country_code=country_code,
        units=units,
        lang=lang,
        mode=mode,
        cnt=cnt,
    )


@mcp.tool()
def forecast_5day_by_city_id_tool(
    city_id: int,
    units: str = "standard",
    lang: Optional[str] = None,
    mode: Optional[str] = None,
    cnt: Optional[int] = None,
) -> Any:
    """5 day / 3 hour forecast by city ID."""
    return forecast_5day_by_city_id(city_id=city_id, units=units, lang=lang, mode=mode, cnt=cnt)


@mcp.tool()
def air_quality_current(lat: float, lon: float) -> Any:
    """Current air quality (AQI + pollutants) by coordinates."""
    return air_pollution_current(lat=lat, lon=lon)


@mcp.tool()
def air_quality_forecast(lat: float, lon: float) -> Any:
    """Air quality forecast by coordinates."""
    return air_pollution_forecast(lat=lat, lon=lon)


@mcp.tool()
def air_quality_history(lat: float, lon: float, start: int, end: int) -> Any:
    """Historical air quality by coordinates (unix UTC start/end)."""
    return air_pollution_history(lat=lat, lon=lon, start=start, end=end)


if __name__ == "__main__":
    mcp.run()
