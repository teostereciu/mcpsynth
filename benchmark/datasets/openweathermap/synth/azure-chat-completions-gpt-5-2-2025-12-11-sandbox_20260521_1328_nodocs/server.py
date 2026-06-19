import os
import requests
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.openweathermap.org"


def _api_key() -> Optional[str]:
    return os.getenv("OPENWEATHER_API_KEY")


def _request(path: str, params: Dict[str, Any]) -> Dict[str, Any]:
    key = _api_key()
    if not key:
        return {"error": "Missing OPENWEATHER_API_KEY environment variable"}

    url = f"{BASE_URL}{path}"
    q = dict(params or {})
    q["appid"] = key

    try:
        resp = requests.get(url, params=q, timeout=30)
    except requests.RequestException as e:
        return {"error": f"Network error: {e}"}

    # OpenWeatherMap often returns JSON even on errors
    try:
        data = resp.json()
    except ValueError:
        return {"error": f"Non-JSON response", "status": resp.status_code, "text": resp.text}

    if resp.status_code >= 400:
        return {"error": "API error", "status": resp.status_code, "response": data}

    return data


mcp = FastMCP("openweathermap")


# --- Geocoding API ---

@mcp.tool()
def geocode_direct(q: str, limit: int = 5) -> Dict[str, Any]:
    """Direct geocoding: city name -> coordinates."""
    return _request("/geo/1.0/direct", {"q": q, "limit": limit})


@mcp.tool()
def geocode_reverse(lat: float, lon: float, limit: int = 5) -> Dict[str, Any]:
    """Reverse geocoding: coordinates -> place names."""
    return _request("/geo/1.0/reverse", {"lat": lat, "lon": lon, "limit": limit})


# --- Current Weather Data (API 2.5) ---

@mcp.tool()
def weather_current_by_city(city: str, state_code: Optional[str] = None, country_code: Optional[str] = None,
                            units: str = "standard", lang: Optional[str] = None) -> Dict[str, Any]:
    """Current weather by city name (optionally state and country)."""
    q = city
    if state_code:
        q += f",{state_code}"
    if country_code:
        q += f",{country_code}"
    params: Dict[str, Any] = {"q": q, "units": units}
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


@mcp.tool()
def weather_current_by_coords(lat: float, lon: float, units: str = "standard", lang: Optional[str] = None) -> Dict[str, Any]:
    """Current weather by geographic coordinates."""
    params: Dict[str, Any] = {"lat": lat, "lon": lon, "units": units}
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


@mcp.tool()
def weather_current_by_zip(zip_code: str, country_code: Optional[str] = None,
                           units: str = "standard", lang: Optional[str] = None) -> Dict[str, Any]:
    """Current weather by ZIP/postal code."""
    z = zip_code if not country_code else f"{zip_code},{country_code}"
    params: Dict[str, Any] = {"zip": z, "units": units}
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


@mcp.tool()
def weather_current_by_city_id(city_id: int, units: str = "standard", lang: Optional[str] = None) -> Dict[str, Any]:
    """Current weather by OpenWeatherMap city ID."""
    params: Dict[str, Any] = {"id": city_id, "units": units}
    if lang:
        params["lang"] = lang
    return _request("/data/2.5/weather", params)


# --- 5 day / 3 hour forecast (API 2.5) ---

@mcp.tool()
def forecast_5day_by_city(city: str, state_code: Optional[str] = None, country_code: Optional[str] = None,
                          units: str = "standard", lang: Optional[str] = None, cnt: Optional[int] = None) -> Dict[str, Any]:
    """5 day / 3 hour forecast by city name."""
    q = city
    if state_code:
        q += f",{state_code}"
    if country_code:
        q += f",{country_code}"
    params: Dict[str, Any] = {"q": q, "units": units}
    if lang:
        params["lang"] = lang
    if cnt is not None:
        params["cnt"] = cnt
    return _request("/data/2.5/forecast", params)


@mcp.tool()
def forecast_5day_by_coords(lat: float, lon: float, units: str = "standard", lang: Optional[str] = None,
                            cnt: Optional[int] = None) -> Dict[str, Any]:
    """5 day / 3 hour forecast by coordinates."""
    params: Dict[str, Any] = {"lat": lat, "lon": lon, "units": units}
    if lang:
        params["lang"] = lang
    if cnt is not None:
        params["cnt"] = cnt
    return _request("/data/2.5/forecast", params)


# --- Air Pollution API ---

@mcp.tool()
def air_pollution_current(lat: float, lon: float) -> Dict[str, Any]:
    """Current air pollution data for coordinates."""
    return _request("/data/2.5/air_pollution", {"lat": lat, "lon": lon})


@mcp.tool()
def air_pollution_forecast(lat: float, lon: float) -> Dict[str, Any]:
    """Air pollution forecast for coordinates."""
    return _request("/data/2.5/air_pollution/forecast", {"lat": lat, "lon": lon})


@mcp.tool()
def air_pollution_history(lat: float, lon: float, start: int, end: int) -> Dict[str, Any]:
    """Air pollution history for coordinates between UNIX timestamps (start, end)."""
    return _request("/data/2.5/air_pollution/history", {"lat": lat, "lon": lon, "start": start, "end": end})


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
