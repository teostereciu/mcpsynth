# OpenWeatherMap MCP Server

An MCP (Model Context Protocol) server that provides weather information tools using the OpenWeatherMap API.

## Features

This server exposes the following tools for weather information:

1. **get_current_weather** - Get current weather data by coordinates, city name, ZIP code, or city ID
2. **get_forecast** - Get 5-day weather forecast by coordinates, city name, ZIP code, or city ID
3. **get_air_pollution** - Get current, forecast, or historical air pollution data
4. **geocode_location** - Convert between location names and coordinates

## Setup

1. Get an API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Set the API key as an environment variable:
   ```bash
   export OPENWEATHER_API_KEY=your_api_key_here
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the server:
```bash
python server.py
```

The server will listen on stdin/stdout for MCP protocol messages.

## Tools Documentation

### get_current_weather
Get current weather information for a location.

**Parameters:**
- `lat` (float): Latitude coordinate
- `lon` (float): Longitude coordinate  
- `city` (string): City name
- `country` (string): Country code (ISO 3166)
- `state` (string): State code (for US cities)
- `zip_code` (string): ZIP/Postal code
- `city_id` (integer): OpenWeatherMap city ID
- `lang` (string): Language code for weather descriptions

### get_forecast
Get 5-day weather forecast for a location.

**Parameters:**
- `lat` (float): Latitude coordinate
- `lon` (float): Longitude coordinate  
- `city` (string): City name
- `country` (string): Country code (ISO 3166)
- `state` (string): State code (for US cities)
- `zip_code` (string): ZIP/Postal code
- `city_id` (integer): OpenWeatherMap city ID
- `lang` (string): Language code for weather descriptions

### get_air_pollution
Get air pollution data for a location.

**Parameters:**
- `lat` (float): Latitude coordinate
- `lon` (float): Longitude coordinate
- `forecast` (boolean): If True, get forecast data; if False, get current data
- `history_start` (integer): Start timestamp for history (required if history=True)
- `history_end` (integer): End timestamp for history (required if history=True)

### geocode_location
Convert location names to coordinates or vice versa.

**Parameters:**
- `city` (string): City name
- `country` (string): Country code (ISO 3166)
- `state` (string): State code (for US cities)
- `zip_code` (string): ZIP/Postal code
- `lat` (float): Latitude coordinate (for reverse geocoding)
- `lon` (float): Longitude coordinate (for reverse geocoding)
- `limit` (integer): Maximum number of results to return