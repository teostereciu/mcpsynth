"""
MCP Server — OpenWeatherMap Free Tier
Runs over stdio using FastMCP.

Tools exposed
─────────────
Current Weather (4):
  get_current_weather_by_coordinates
  get_current_weather_by_city_name
  get_current_weather_by_city_id
  get_current_weather_by_zip_code

5-Day / 3-Hour Forecast (4):
  get_5day_forecast_by_coordinates
  get_5day_forecast_by_city_name
  get_5day_forecast_by_city_id
  get_5day_forecast_by_zip_code

Air Pollution (3):
  get_current_air_pollution
  get_air_pollution_forecast
  get_air_pollution_history

Geocoding (3):
  geocode_by_location_name
  geocode_by_zip_code
  reverse_geocode
"""

from mcp.server.fastmcp import FastMCP

from generated_tools.current_weather import (
    get_current_weather_by_coordinates,
    get_current_weather_by_city_name,
    get_current_weather_by_city_id,
    get_current_weather_by_zip_code,
)
from generated_tools.forecast import (
    get_5day_forecast_by_coordinates,
    get_5day_forecast_by_city_name,
    get_5day_forecast_by_city_id,
    get_5day_forecast_by_zip_code,
)
from generated_tools.air_pollution import (
    get_current_air_pollution,
    get_air_pollution_forecast,
    get_air_pollution_history,
)
from generated_tools.geocoding import (
    geocode_by_location_name,
    geocode_by_zip_code,
    reverse_geocode,
)

# ── Server setup ──────────────────────────────────────────────────────────────

mcp = FastMCP(
    name="openweathermap",
    description=(
        "Comprehensive OpenWeatherMap free-tier API server. "
        "Provides current weather, 5-day forecasts, air pollution data, "
        "and geocoding (direct and reverse)."
    ),
)

# ── Current Weather tools ─────────────────────────────────────────────────────

@mcp.tool()
def get_current_weather_by_coordinates(
    lat: float,
    lon: float,
    units: str = "standard",
    lang: str | None = None,
) -> dict:
    """
    Get current weather data for a specific geographic location.

    Args:
        lat:   Latitude of the location.
        lon:   Longitude of the location.
        units: Units of measurement — 'standard' (Kelvin), 'metric' (Celsius),
               or 'imperial' (Fahrenheit). Defaults to 'standard'.
        lang:  Optional language code for weather descriptions (e.g. 'en', 'de').

    Returns:
        Current weather data as a dict, or an error dict.
    """
    from generated_tools.current_weather import get_current_weather_by_coordinates as _fn
    return _fn(lat=lat, lon=lon, units=units, lang=lang)


@mcp.tool()
def get_current_weather_by_city_name(
    city_name: str,
    state_code: str | None = None,
    country_code: str | None = None,
    units: str = "standard",
    lang: str | None = None,
) -> dict:
    """
    Get current weather data by city name (optionally with state/country code).

    Args:
        city_name:    Name of the city (e.g. 'London').
        state_code:   US state code (e.g. 'CA'). Only applicable for US locations.
        country_code: ISO 3166 country code (e.g. 'GB').
        units:        Units of measurement — 'standard', 'metric', or 'imperial'.
        lang:         Optional language code for weather descriptions.

    Returns:
        Current weather data as a dict, or an error dict.
    """
    from generated_tools.current_weather import get_current_weather_by_city_name as _fn
    return _fn(
        city_name=city_name,
        state_code=state_code,
        country_code=country_code,
        units=units,
        lang=lang,
    )


@mcp.tool()
def get_current_weather_by_city_id(
    city_id: int,
    units: str = "standard",
    lang: str | None = None,
) -> dict:
    """
    Get current weather data by OpenWeatherMap city ID.

    Args:
        city_id: Numeric city ID (e.g. 2643743 for London).
        units:   Units of measurement — 'standard', 'metric', or 'imperial'.
        lang:    Optional language code for weather descriptions.

    Returns:
        Current weather data as a dict, or an error dict.
    """
    from generated_tools.current_weather import get_current_weather_by_city_id as _fn
    return _fn(city_id=city_id, units=units, lang=lang)


@mcp.tool()
def get_current_weather_by_zip_code(
    zip_code: str,
    country_code: str = "US",
    units: str = "standard",
    lang: str | None = None,
) -> dict:
    """
    Get current weather data by ZIP / postal code and country code.

    Args:
        zip_code:     ZIP or postal code (e.g. '90210').
        country_code: ISO 3166 country code (e.g. 'US', 'GB'). Defaults to 'US'.
        units:        Units of measurement — 'standard', 'metric', or 'imperial'.
        lang:         Optional language code for weather descriptions.

    Returns:
        Current weather data as a dict, or an error dict.
    """
    from generated_tools.current_weather import get_current_weather_by_zip_code as _fn
    return _fn(zip_code=zip_code, country_code=country_code, units=units, lang=lang)


# ── 5-Day Forecast tools ──────────────────────────────────────────────────────

@mcp.tool()
def get_5day_forecast_by_coordinates(
    lat: float,
    lon: float,
    units: str = "standard",
    cnt: int | None = None,
    lang: str | None = None,
) -> dict:
    """
    Get a 5-day weather forecast with 3-hour step for a geographic location.

    Args:
        lat:   Latitude of the location.
        lon:   Longitude of the location.
        units: Units of measurement — 'standard' (Kelvin), 'metric' (Celsius),
               or 'imperial' (Fahrenheit). Defaults to 'standard'.
        cnt:   Optional number of 3-hour timestamps to return (max 40).
        lang:  Optional language code for weather descriptions (e.g. 'en', 'de').

    Returns:
        Forecast data dict with 'list' of up to 40 3-hour slots and 'city' info,
        or an error dict.
    """
    from generated_tools.forecast import get_5day_forecast_by_coordinates as _fn
    return _fn(lat=lat, lon=lon, units=units, cnt=cnt, lang=lang)


@mcp.tool()
def get_5day_forecast_by_city_name(
    city_name: str,
    state_code: str | None = None,
    country_code: str | None = None,
    units: str = "standard",
    cnt: int | None = None,
    lang: str | None = None,
) -> dict:
    """
    Get a 5-day / 3-hour weather forecast by city name.

    Args:
        city_name:    Name of the city (e.g. 'Paris').
        state_code:   US state code (only for US locations, e.g. 'TX').
        country_code: ISO 3166 country code (e.g. 'FR').
        units:        Units of measurement — 'standard', 'metric', or 'imperial'.
        cnt:          Optional number of 3-hour timestamps to return (max 40).
        lang:         Optional language code for weather descriptions.

    Returns:
        Forecast data dict, or an error dict.
    """
    from generated_tools.forecast import get_5day_forecast_by_city_name as _fn
    return _fn(
        city_name=city_name,
        state_code=state_code,
        country_code=country_code,
        units=units,
        cnt=cnt,
        lang=lang,
    )


@mcp.tool()
def get_5day_forecast_by_city_id(
    city_id: int,
    units: str = "standard",
    cnt: int | None = None,
    lang: str | None = None,
) -> dict:
    """
    Get a 5-day / 3-hour weather forecast by OpenWeatherMap city ID.

    Args:
        city_id: Numeric city ID (e.g. 524901 for Moscow).
        units:   Units of measurement — 'standard', 'metric', or 'imperial'.
        cnt:     Optional number of 3-hour timestamps to return (max 40).
        lang:    Optional language code for weather descriptions.

    Returns:
        Forecast data dict, or an error dict.
    """
    from generated_tools.forecast import get_5day_forecast_by_city_id as _fn
    return _fn(city_id=city_id, units=units, cnt=cnt, lang=lang)


@mcp.tool()
def get_5day_forecast_by_zip_code(
    zip_code: str,
    country_code: str = "US",
    units: str = "standard",
    cnt: int | None = None,
    lang: str | None = None,
) -> dict:
    """
    Get a 5-day / 3-hour weather forecast by ZIP / postal code.

    Args:
        zip_code:     ZIP or postal code (e.g. '10001').
        country_code: ISO 3166 country code (e.g. 'US', 'DE'). Defaults to 'US'.
        units:        Units of measurement — 'standard', 'metric', or 'imperial'.
        cnt:          Optional number of 3-hour timestamps to return (max 40).
        lang:         Optional language code for weather descriptions.

    Returns:
        Forecast data dict, or an error dict.
    """
    from generated_tools.forecast import get_5day_forecast_by_zip_code as _fn
    return _fn(zip_code=zip_code, country_code=country_code, units=units, cnt=cnt, lang=lang)


# ── Air Pollution tools ───────────────────────────────────────────────────────

@mcp.tool()
def get_current_air_pollution(lat: float, lon: float) -> dict:
    """
    Get current air pollution data for a geographic location.

    Returns the Air Quality Index (AQI) and concentrations of key pollutants:
    CO, NO, NO2, O3, SO2, PM2.5, PM10, NH3.

    AQI scale: 1=Good, 2=Fair, 3=Moderate, 4=Poor, 5=Very Poor.

    Args:
        lat: Latitude of the location.
        lon: Longitude of the location.

    Returns:
        Dict with 'coord' and 'list' of pollution readings, or an error dict.
    """
    from generated_tools.air_pollution import get_current_air_pollution as _fn
    return _fn(lat=lat, lon=lon)


@mcp.tool()
def get_air_pollution_forecast(lat: float, lon: float) -> dict:
    """
    Get air pollution forecast for a geographic location.

    Provides hourly air quality data for the next 4 days, including AQI and
    pollutant concentrations (CO, NO, NO2, O3, SO2, PM2.5, PM10, NH3).

    Args:
        lat: Latitude of the location.
        lon: Longitude of the location.

    Returns:
        Dict with 'coord' and 'list' of hourly forecast pollution readings,
        or an error dict.
    """
    from generated_tools.air_pollution import get_air_pollution_forecast as _fn
    return _fn(lat=lat, lon=lon)


@mcp.tool()
def get_air_pollution_history(
    lat: float,
    lon: float,
    start: int,
    end: int,
) -> dict:
    """
    Get historical air pollution data for a geographic location.

    Historical data is available from 27th November 2020 onwards.

    Args:
        lat:   Latitude of the location.
        lon:   Longitude of the location.
        start: Start of the time range as a Unix timestamp (UTC),
               e.g. 1606488670.
        end:   End of the time range as a Unix timestamp (UTC),
               e.g. 1606747870.

    Returns:
        Dict with 'coord' and 'list' of historical pollution readings,
        or an error dict.
    """
    from generated_tools.air_pollution import get_air_pollution_history as _fn
    return _fn(lat=lat, lon=lon, start=start, end=end)


# ── Geocoding tools ───────────────────────────────────────────────────────────

@mcp.tool()
def geocode_by_location_name(
    city_name: str,
    state_code: str | None = None,
    country_code: str | None = None,
    limit: int = 5,
) -> list | dict:
    """
    Convert a city or area name into geographic coordinates (direct geocoding).

    Args:
        city_name:    Name of the city or area (e.g. 'London', 'New York').
        state_code:   US state code (only for US locations, e.g. 'NY').
        country_code: ISO 3166 country code (e.g. 'GB', 'US').
        limit:        Maximum number of results to return (1–5). Defaults to 5.

    Returns:
        List of matching locations, each with 'name', 'lat', 'lon', 'country',
        and optionally 'state' and 'local_names'. Returns an error dict on failure.
    """
    from generated_tools.geocoding import geocode_by_location_name as _fn
    return _fn(
        city_name=city_name,
        state_code=state_code,
        country_code=country_code,
        limit=limit,
    )


@mcp.tool()
def geocode_by_zip_code(
    zip_code: str,
    country_code: str = "US",
) -> dict:
    """
    Convert a ZIP / postal code into geographic coordinates.

    Args:
        zip_code:     ZIP or postal code (e.g. '90210', 'E14').
        country_code: ISO 3166 country code (e.g. 'US', 'GB'). Defaults to 'US'.

    Returns:
        Dict with 'zip', 'name', 'lat', 'lon', 'country', or an error dict.
    """
    from generated_tools.geocoding import geocode_by_zip_code as _fn
    return _fn(zip_code=zip_code, country_code=country_code)


@mcp.tool()
def reverse_geocode(
    lat: float,
    lon: float,
    limit: int = 5,
) -> list | dict:
    """
    Convert geographic coordinates into location names (reverse geocoding).

    Args:
        lat:   Latitude of the location.
        lon:   Longitude of the location.
        limit: Maximum number of location names to return. Defaults to 5.

    Returns:
        List of nearby locations, each with 'name', 'lat', 'lon', 'country',
        and optionally 'state' and 'local_names'. Returns an error dict on failure.
    """
    from generated_tools.geocoding import reverse_geocode as _fn
    return _fn(lat=lat, lon=lon, limit=limit)


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run()
