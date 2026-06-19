# OpenWeatherMap MCP Server

A comprehensive Model Context Protocol (MCP) server implementation for the OpenWeatherMap API, enabling autonomous agents to access weather data, forecasts, air pollution information, and geocoding services.

## Quick Start

### Prerequisites
- Python 3.8+
- OpenWeatherMap API key (free tier available at https://openweathermap.org/api)

### Installation

```bash
# Clone or download this repository
cd openweathermap-mcp-server

# Install dependencies
pip install -r requirements.txt

# Set your API key
export OPENWEATHER_API_KEY="your_api_key_here"

# Run the server
python server.py
```

The server will start listening on stdio and expose all tools via the MCP protocol.

## Features

### 14 Tools Across 4 API Domains

#### Current Weather (4 tools)
- Get weather by coordinates (lat/lon)
- Get weather by city name
- Get weather by city ID
- Get weather by ZIP code

#### 5-Day Forecast (4 tools)
- Get forecast by coordinates
- Get forecast by city name
- Get forecast by city ID
- Get forecast by ZIP code

#### Air Pollution (3 tools)
- Get current air pollution data
- Get air pollution forecast (4 days)
- Get historical air pollution data

#### Geocoding (3 tools)
- Direct geocoding (name → coordinates)
- ZIP code geocoding
- Reverse geocoding (coordinates → name)

### Comprehensive Parameter Support
- **Units**: Standard (Kelvin), Metric (Celsius), Imperial (Fahrenheit)
- **Languages**: Multi-language support for weather descriptions
- **Limits**: Configurable result limits for geocoding
- **Time Ranges**: Historical data with Unix timestamp support
- **Forecast Counts**: Adjustable forecast intervals (up to 40)

## Architecture

### Core Files

| File | Purpose |
|------|---------|
| `server.py` | Main MCP server implementation (14 tools) |
| `requirements.txt` | Python dependencies |
| `grounding.json` | Tool-to-documentation mapping |

### Design Principles

1. **No Generic Passthrough**: Every tool is a specific, named operation
2. **Robust Error Handling**: Expected errors return error dicts, not exceptions
3. **JSON-Serializable Results**: All responses are JSON-compatible
4. **Multi-Query Support**: Each resource accessible via multiple methods
5. **Workflow-Friendly**: Tools designed for multi-step agent workflows

## API Coverage

All free-tier OpenWeatherMap endpoints are implemented:

| Endpoint | Tools | Status |
|----------|-------|--------|
| GET /data/2.5/weather | 4 | ✅ Complete |
| GET /data/2.5/forecast | 4 | ✅ Complete |
| GET /data/2.5/air_pollution | 1 | ✅ Complete |
| GET /data/2.5/air_pollution/forecast | 1 | ✅ Complete |
| GET /data/2.5/air_pollution/history | 1 | ✅ Complete |
| GET /geo/1.0/direct | 1 | ✅ Complete |
| GET /geo/1.0/zip | 1 | ✅ Complete |
| GET /geo/1.0/reverse | 1 | ✅ Complete |

## Usage Examples

### Get Current Weather by Coordinates
```python
{
  "tool": "get_current_weather_by_coordinates",
  "arguments": {
    "latitude": 51.5074,
    "longitude": -0.1278,
    "units": "metric"
  }
}
```

### Get 5-Day Forecast by City Name
```python
{
  "tool": "get_5day_forecast_by_city_name",
  "arguments": {
    "city_name": "London",
    "country_code": "GB",
    "units": "metric"
  }
}
```

### Check Air Quality
```python
{
  "tool": "get_current_air_pollution",
  "arguments": {
    "latitude": 48.8566,
    "longitude": 2.3522
  }
}
```

### Geocode a Location
```python
{
  "tool": "geocode_location_name",
  "arguments": {
    "location_name": "Paris",
    "country_code": "FR",
    "limit": 5
  }
}
```

See [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) for comprehensive examples and multi-step workflows.

## Tool Reference

### Current Weather Tools

#### `get_current_weather_by_coordinates`
Get current weather by latitude and longitude.
- **Parameters**: latitude, longitude, units (optional), lang (optional)
- **Returns**: Current weather data

#### `get_current_weather_by_city_name`
Get current weather by city name.
- **Parameters**: city_name, country_code (optional), state_code (optional), units (optional), lang (optional)
- **Returns**: Current weather data

#### `get_current_weather_by_city_id`
Get current weather by OpenWeatherMap city ID.
- **Parameters**: city_id, units (optional), lang (optional)
- **Returns**: Current weather data

#### `get_current_weather_by_zip_code`
Get current weather by ZIP/postal code.
- **Parameters**: zip_code, country_code, units (optional), lang (optional)
- **Returns**: Current weather data

### 5-Day Forecast Tools

#### `get_5day_forecast_by_coordinates`
Get 5-day forecast (3-hour intervals) by coordinates.
- **Parameters**: latitude, longitude, units (optional), count (optional), lang (optional)
- **Returns**: Forecast data with 3-hour intervals

#### `get_5day_forecast_by_city_name`
Get 5-day forecast by city name.
- **Parameters**: city_name, country_code (optional), state_code (optional), units (optional), count (optional), lang (optional)
- **Returns**: Forecast data

#### `get_5day_forecast_by_city_id`
Get 5-day forecast by city ID.
- **Parameters**: city_id, units (optional), count (optional), lang (optional)
- **Returns**: Forecast data

#### `get_5day_forecast_by_zip_code`
Get 5-day forecast by ZIP code.
- **Parameters**: zip_code, country_code, units (optional), count (optional), lang (optional)
- **Returns**: Forecast data

### Air Pollution Tools

#### `get_current_air_pollution`
Get current air pollution data.
- **Parameters**: latitude, longitude
- **Returns**: AQI and pollutant concentrations

#### `get_air_pollution_forecast`
Get air pollution forecast (4 days, hourly).
- **Parameters**: latitude, longitude
- **Returns**: Forecast data with hourly intervals

#### `get_air_pollution_history`
Get historical air pollution data.
- **Parameters**: latitude, longitude, start_timestamp, end_timestamp
- **Returns**: Historical pollution data

### Geocoding Tools

#### `geocode_location_name`
Convert location name to coordinates (direct geocoding).
- **Parameters**: location_name, country_code (optional), state_code (optional), limit (optional)
- **Returns**: List of matching locations with coordinates

#### `geocode_zip_code`
Convert ZIP code to coordinates.
- **Parameters**: zip_code, country_code
- **Returns**: Location data with coordinates

#### `reverse_geocode`
Convert coordinates to location names (reverse geocoding).
- **Parameters**: latitude, longitude, limit (optional)
- **Returns**: List of nearby locations

## Error Handling

All errors are returned as JSON dicts with an "error" key:

```json
{
  "error": "API request failed: 404 Client Error: Not Found"
}
```

The server handles:
- Network errors gracefully
- Invalid API responses
- Rate limiting
- Missing or invalid parameters

## Configuration

### Environment Variables

- `OPENWEATHER_API_KEY` (required): Your OpenWeatherMap API key

### Units of Measurement

- **standard** (default): Kelvin, m/s, hPa
- **metric**: Celsius, m/s, hPa
- **imperial**: Fahrenheit, mph, hPa

### Language Support

Supports 50+ languages for weather descriptions. Common codes:
- `en` - English
- `es` - Spanish
- `fr` - French
- `de` - German
- `it` - Italian
- `pt` - Portuguese
- `ru` - Russian
- `zh_cn` - Chinese (Simplified)

## Documentation

- [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) - Architecture and design decisions
- [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) - Detailed usage examples and workflows
- [DELIVERABLES_CHECKLIST.md](DELIVERABLES_CHECKLIST.md) - Verification of all requirements
- [grounding.json](grounding.json) - Tool-to-documentation mapping

## API Documentation

Original API documentation:
- [Current Weather API](https://openweathermap.org/current)
- [5-Day Forecast API](https://openweathermap.org/forecast5)
- [Air Pollution API](https://openweathermap.org/api/air-pollution)
- [Geocoding API](https://openweathermap.org/api/geocoding-api)

## Requirements

- Python 3.8+
- fastmcp==3.2.4
- requests==2.32.3

## License

This MCP server implementation is provided as-is for use with the OpenWeatherMap API.

## Support

For issues with:
- **This MCP server**: Check the implementation files and error messages
- **OpenWeatherMap API**: Visit https://openweathermap.org/api
- **MCP Protocol**: See https://modelcontextprotocol.io

## Workflow Examples

### Example 1: Check Weather and Air Quality for a City

1. Geocode the city name to get coordinates
2. Get current weather at those coordinates
3. Get current air pollution data
4. Return combined results to the agent

### Example 2: Plan a Multi-Day Trip

1. Geocode destination city
2. Get 5-day forecast for planning
3. Check air pollution forecast
4. Get historical weather patterns for comparison

### Example 3: Monitor Air Quality Trends

1. Get current air pollution
2. Get air pollution forecast
3. Get historical data for the past week
4. Analyze trends and provide recommendations

## Contributing

This is a complete implementation of the OpenWeatherMap free-tier API. All major endpoints and use cases are covered.

## Acknowledgments

Built with:
- [FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Python MCP framework
- [OpenWeatherMap API](https://openweathermap.org/api) - Weather data provider
- [Model Context Protocol](https://modelcontextprotocol.io) - Protocol specification
