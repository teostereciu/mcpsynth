"""
MCP Server — OpenWeatherMap (free tier)
Runs over stdio using FastMCP.

Covered APIs:
  • Current Weather Data (v2.5)
  • 5-Day / 3-Hour Forecast (v2.5)
  • Air Pollution (current, forecast, history)
  • Geocoding (direct by name, by zip, reverse)
"""

from mcp.server.fastmcp import FastMCP

from generated_tools.current_weather import (
    get_current_weather_by_coordinates,
    get_current_weather_by_city_name,
    get_current_weather_by_city_id,
    get_current_weather_by_zip_code,
)
from generated_tools.forecast import (
    get_forecast_by_coordinates,
    get_forecast_by_city_name,
    get_forecast_by_city_id,
    get_forecast_by_zip_code,
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

# ── Server instance ───────────────────────────────────────────────────────────

mcp = FastMCP(
    name="openweathermap",
    description=(
        "MCP server providing comprehensive access to the OpenWeatherMap "
        "free-tier APIs: current weather, 5-day forecast, air pollution, "
        "and geocoding."
    ),
)

# ── Current Weather tools ─────────────────────────────────────────────────────

@mcp.tool()
def get_current_weather_by_coordinates(
    latitude: float,
    longitude: float,
    units: str = "standard",
    language: str = "en",
) -> dict:
    """
    Get current weather data for a specific geographic location.

    Args:
        latitude:  Latitude of the location (e.g. 44.34).
        longitude: Longitude of the location (e.g. 10.99).
        units:     Unit system — 'standard' (Kelvin), 'metric' (Celsius),
                   or 'imperial' (Fahrenheit). Defaults to 'standard'.
        language:  Language code for weather descriptions (e.g. 'en', 'de',
                   'fr'). Defaults to 'en'.

    Returns:
        JSON dict with coord, weather, main (temp, feels_like, humidity,
        pressure), wind, clouds, visibility, rain/snow, sys (sunrise/sunset),
        timezone, city name, and more.
    """
    from generated_tools.current_weather import get_current_weather_by_coordinates as _fn
    return _fn(latitude, longitude, units, language)


@mcp.tool()
def get_current_weather_by_city_name(
    city_name: str,
    state_code: str = "",
    country_code: str = "",
    units: str = "standard",
    language: str = "en",
) -> dict:
    """
    Get current weather data by city name (optionally with state/country).

    Args:
        city_name:    Name of the city (e.g. 'London').
        state_code:   US state code (e.g. 'CA'). Only applicable for US cities.
        country_code: ISO 3166 country code (e.g. 'GB', 'US').
        units:        Unit system — 'standard', 'metric', or 'imperial'.
        language:     Language code for weather descriptions.

    Returns:
        JSON dict with current weather data (same structure as coordinate-based
        call).
    """
    from generated_tools.current_weather import get_current_weather_by_city_name as _fn
    return _fn(city_name, state_code, country_code, units, language)


@mcp.tool()
def get_current_weather_by_city_id(
    city_id: int,
    units: str = "standard",
    language: str = "en",
) -> dict:
    """
    Get current weather data by OpenWeatherMap city ID.

    Args:
        city_id:  Numeric city ID from the OpenWeatherMap city list.
        units:    Unit system — 'standard', 'metric', or 'imperial'.
        language: Language code for weather descriptions.

    Returns:
        JSON dict with current weather data.
    """
    from generated_tools.current_weather import get_current_weather_by_city_id as _fn
    return _fn(city_id, units, language)


@mcp.tool()
def get_current_weather_by_zip_code(
    zip_code: str,
    country_code: str = "US",
    units: str = "standard",
    language: str = "en",
) -> dict:
    """
    Get current weather data by ZIP / postal code and country.

    Args:
        zip_code:     ZIP or postal code (e.g. '90210' or 'E14').
        country_code: ISO 3166 country code (e.g. 'US', 'GB'). Defaults to
                      'US'.
        units:        Unit system — 'standard', 'metric', or 'imperial'.
        language:     Language code for weather descriptions.

    Returns:
        JSON dict with current weather data.
    """
    from generated_tools.current_weather import get_current_weather_by_zip_code as _fn
    return _fn(zip_code, country_code, units, language)


# ── Forecast tools ────────────────────────────────────────────────────────────

@mcp.tool()
def get_forecast_by_coordinates(
    latitude: float,
    longitude: float,
    units: str = "standard",
    language: str = "en",
    count: int = 0,
) -> dict:
    """
    Get a 5-day weather forecast (3-hour step) for a geographic location.

    Args:
        latitude:  Latitude of the location.
        longitude: Longitude of the location.
        units:     Unit system — 'standard' (Kelvin), 'metric' (Celsius),
                   or 'imperial' (Fahrenheit). Defaults to 'standard'.
        language:  Language code for weather descriptions (e.g. 'en', 'de').
        count:     Number of 3-hour timestamps to return (0 = all, up to 40).

    Returns:
        JSON dict with 'list' of up to 40 forecast entries (each with dt,
        main, weather, clouds, wind, visibility, pop, rain/snow, sys, dt_txt)
        and 'city' metadata (name, coord, country, timezone, sunrise, sunset).
    """
    from generated_tools.forecast import get_forecast_by_coordinates as _fn
    return _fn(latitude, longitude, units, language, count)


@mcp.tool()
def get_forecast_by_city_name(
    city_name: str,
    state_code: str = "",
    country_code: str = "",
    units: str = "standard",
    language: str = "en",
    count: int = 0,
) -> dict:
    """
    Get a 5-day / 3-hour forecast by city name (optionally with state/country).

    Args:
        city_name:    Name of the city (e.g. 'Paris').
        state_code:   US state code (only for US cities, e.g. 'TX').
        country_code: ISO 3166 country code (e.g. 'FR', 'US').
        units:        Unit system — 'standard', 'metric', or 'imperial'.
        language:     Language code for weather descriptions.
        count:        Number of 3-hour timestamps to return (0 = all).

    Returns:
        JSON dict with forecast list and city metadata.
    """
    from generated_tools.forecast import get_forecast_by_city_name as _fn
    return _fn(city_name, state_code, country_code, units, language, count)


@mcp.tool()
def get_forecast_by_city_id(
    city_id: int,
    units: str = "standard",
    language: str = "en",
    count: int = 0,
) -> dict:
    """
    Get a 5-day / 3-hour forecast by OpenWeatherMap city ID.

    Args:
        city_id:  Numeric city ID from the OpenWeatherMap city list.
        units:    Unit system — 'standard', 'metric', or 'imperial'.
        language: Language code for weather descriptions.
        count:    Number of 3-hour timestamps to return (0 = all).

    Returns:
        JSON dict with forecast list and city metadata.
    """
    from generated_tools.forecast import get_forecast_by_city_id as _fn
    return _fn(city_id, units, language, count)


@mcp.tool()
def get_forecast_by_zip_code(
    zip_code: str,
    country_code: str = "US",
    units: str = "standard",
    language: str = "en",
    count: int = 0,
) -> dict:
    """
    Get a 5-day / 3-hour forecast by ZIP / postal code and country.

    Args:
        zip_code:     ZIP or postal code (e.g. '10001' or 'SW1A').
        country_code: ISO 3166 country code (e.g. 'US', 'GB'). Defaults to
                      'US'.
        units:        Unit system — 'standard', 'metric', or 'imperial'.
        language:     Language code for weather descriptions.
        count:        Number of 3-hour timestamps to return (0 = all).

    Returns:
        JSON dict with forecast list and city metadata.
    """
    from generated_tools.forecast import get_forecast_by_zip_code as _fn
    return _fn(zip_code, country_code, units, language, count)


# ── Air Pollution tools ───────────────────────────────────────────────────────

@mcp.tool()
def get_current_air_pollution(latitude: float, longitude: float) -> dict:
    """
    Get current air pollution data for a geographic location.

    Returns the Air Quality Index (AQI) and concentrations of key pollutants:
    CO, NO, NO2, O3, SO2, PM2.5, PM10, and NH3.

    AQI scale: 1=Good, 2=Fair, 3=Moderate, 4=Poor, 5=Very Poor.

    Args:
        latitude:  Latitude of the location.
        longitude: Longitude of the location.

    Returns:
        JSON dict with 'coord' and 'list' containing one entry with:
          - dt: Unix timestamp (UTC)
          - main.aqi: Air Quality Index (1–5)
          - components: dict of pollutant concentrations in μg/m³
            (co, no, no2, o3, so2, pm2_5, pm10, nh3)
    """
    from generated_tools.air_pollution import get_current_air_pollution as _fn
    return _fn(latitude, longitude)


@mcp.tool()
def get_air_pollution_forecast(latitude: float, longitude: float) -> dict:
    """
    Get air pollution forecast for the next 4 days (hourly granularity).

    Returns hourly AQI and pollutant concentration forecasts for the specified
    location.

    AQI scale: 1=Good, 2=Fair, 3=Moderate, 4=Poor, 5=Very Poor.

    Args:
        latitude:  Latitude of the location.
        longitude: Longitude of the location.

    Returns:
        JSON dict with 'coord' and 'list' of hourly forecast entries, each
        containing:
          - dt: Unix timestamp (UTC)
          - main.aqi: Air Quality Index (1–5)
          - components: dict of pollutant concentrations in μg/m³
    """
    from generated_tools.air_pollution import get_air_pollution_forecast as _fn
    return _fn(latitude, longitude)


@mcp.tool()
def get_air_pollution_history(
    latitude: float,
    longitude: float,
    start: int,
    end: int,
) -> dict:
    """
    Get historical air pollution data for a location and time range.

    Historical data is available from 27 November 2020 onwards.

    Args:
        latitude:  Latitude of the location.
        longitude: Longitude of the location.
        start:     Start of the time range as a Unix timestamp (UTC).
                   Example: 1606488670
        end:       End of the time range as a Unix timestamp (UTC).
                   Example: 1606747870

    Returns:
        JSON dict with 'coord' and 'list' of historical entries, each
        containing:
          - dt: Unix timestamp (UTC)
          - main.aqi: Air Quality Index (1–5)
          - components: dict of pollutant concentrations in μg/m³
            (co, no, no2, o3, so2, pm2_5, pm10, nh3)
    """
    from generated_tools.air_pollution import get_air_pollution_history as _fn
    return _fn(latitude, longitude, start, end)


# ── Geocoding tools ───────────────────────────────────────────────────────────

@mcp.tool()
def geocode_by_location_name(
    city_name: str,
    state_code: str = "",
    country_code: str = "",
    limit: int = 5,
) -> list:
    """
    Convert a city / location name into geographic coordinates (direct geocoding).

    Useful for resolving ambiguous city names — e.g. 'London' exists in both
    the UK and the US; use country_code to disambiguate.

    Args:
        city_name:    Name of the city or area (e.g. 'London', 'New York').
        state_code:   US state code (only for US locations, e.g. 'NY').
        country_code: ISO 3166 country code (e.g. 'GB', 'US').
        limit:        Maximum number of results to return (1–5). Defaults to 5.

    Returns:
        List of matching location dicts, each containing:
          - name: location name
          - lat, lon: geographic coordinates
          - country: country code
          - state: state (where available)
          - local_names: dict of names in various languages (where available)
        Returns a dict with 'error' key on failure.
    """
    from generated_tools.geocoding import geocode_by_location_name as _fn
    return _fn(city_name, state_code, country_code, limit)


@mcp.tool()
def geocode_by_zip_code(zip_code: str, country_code: str = "US") -> dict:
    """
    Convert a ZIP / postal code into geographic coordinates.

    Args:
        zip_code:     ZIP or postal code (e.g. '90210', 'E14', 'SW1A 1AA').
        country_code: ISO 3166 country code (e.g. 'US', 'GB'). Defaults to
                      'US'.

    Returns:
        Dict containing:
          - zip: the requested zip code
          - name: name of the found area
          - lat, lon: geographic coordinates of the centroid
          - country: country code
        Returns a dict with 'error' key on failure.
    """
    from generated_tools.geocoding import geocode_by_zip_code as _fn
    return _fn(zip_code, country_code)


@mcp.tool()
def reverse_geocode(
    latitude: float,
    longitude: float,
    limit: int = 5,
) -> list:
    """
    Convert geographic coordinates into location / city names (reverse geocoding).

    Args:
        latitude:  Latitude of the location.
        longitude: Longitude of the location.
        limit:     Maximum number of location names to return. Defaults to 5.

    Returns:
        List of nearby location dicts, each containing:
          - name: location name
          - lat, lon: geographic coordinates
          - country: country code
          - state: state (where available)
          - local_names: dict of names in various languages (where available)
        Returns a dict with 'error' key on failure.
    """
    from generated_tools.geocoding import reverse_geocode as _fn
    return _fn(latitude, longitude, limit)


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run()
