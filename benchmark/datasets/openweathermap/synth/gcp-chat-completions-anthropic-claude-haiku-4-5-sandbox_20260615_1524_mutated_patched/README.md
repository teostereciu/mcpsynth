# OpenWeatherMap MCP Server

A comprehensive Model Context Protocol (MCP) server implementation for the OpenWeatherMap API, providing tools for weather data, forecasts, air pollution monitoring, and geocoding operations.

## Features

- **10 MCP Tools** across 4 API domains
- **Current Weather Data** - Get real-time weather by coordinates or city name
- **5-Day Forecasts** - 3-hour interval forecasts for 5 days
- **Air Pollution Monitoring** - Current, forecast, and historical air quality data
- **Geocoding** - Direct geocoding (name→coordinates), reverse geocoding (coordinates→name), and zip code lookup
- **Robust Error Handling** - All errors returned as JSON, no unhandled exceptions
- **Multi-Step Workflows** - Support for complex queries combining multiple endpoints

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

The server will start listening on stdio and be ready to handle MCP protocol requests.

## Available Tools

### Current Weather (2 tools)
- `get_current_weather_by_coords` - Get weather by latitude/longitude
- `get_current_weather_by_city_name` - Get weather by city name

### 5-Day Forecast (2 tools)
- `get_5day_forecast_by_coords` - Get forecast by coordinates
- `get_5day_forecast_by_city_name` - Get forecast by city name

### Air Pollution (3 tools)
- `get_current_air_pollution` - Current air quality index and pollutants
- `get_air_pollution_forecast` - 4-day air pollution forecast
- `get_air_pollution_history` - Historical air pollution data

### Geocoding (3 tools)
- `geocode_location_name` - Convert location name to coordinates
- `geocode_zip_code` - Convert zip code to coordinates
- `reverse_geocode` - Convert coordinates to location names

## Usage Examples

### Get Current Weather
```python
get_current_weather_by_coords(
    latitude=51.5074,
    longitude=-0.1278,
    units="metric",
    language="en"
)
```

### Get 5-Day Forecast
```python
get_5day_forecast_by_coords(
    latitude=35.6762,
    longitude=139.6503,
    units="metric"
)
```

### Check Air Quality
```python
get_current_air_pollution(
    latitude=40.7128,
    longitude=-74.0060
)
```

### Find Coordinates for a City
```python
geocode_location_name(
    location_name="London",
    country_code="GB",
    limit=5
)
```

### Find Location Names for Coordinates
```python
reverse_geocode(
    latitude=48.8566,
    longitude=2.3522,
    limit=5
)
```

See [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) for more detailed examples and multi-step workflows.

## API Coverage

### Supported Endpoints
- ✅ Current Weather Data (API 2.5)
- ✅ 5-Day / 3-Hour Forecast (API 2.5)
- ✅ Air Pollution (Current, Forecast, Historical)
- ✅ Geocoding (Direct, Reverse, Zip Code)

All endpoints use the free tier of OpenWeatherMap API.

## Configuration

### Environment Variables
- `OPENWEATHER_API_KEY` (required) - Your OpenWeatherMap API key

### Optional Parameters
- `units` - Temperature units: `standard` (Kelvin), `metric` (Celsius), `imperial` (Fahrenheit)
- `language` - Weather description language (e.g., `en`, `es`, `fr`, `de`)
- `limit` - Maximum number of results for geocoding queries
- `count` - Number of forecast timestamps to return

## Error Handling

All errors are returned as JSON objects:

```json
{
  "error": "API error: 401",
  "details": "Invalid API key"
}
```

The server handles:
- Invalid API keys
- Network timeouts (10-second limit)
- Invalid parameters
- Rate limiting
- Malformed requests

## Documentation

- [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) - Technical implementation details
- [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) - Detailed usage examples and workflows
- [DELIVERABLES_CHECKLIST.md](DELIVERABLES_CHECKLIST.md) - Complete deliverables verification
- [grounding.json](grounding.json) - Tool-to-documentation mapping

## Project Structure

```
.
├── server.py                      # MCP server implementation
├── requirements.txt               # Python dependencies
├── grounding.json                 # Tool documentation mapping
├── README.md                      # This file
├── IMPLEMENTATION_SUMMARY.md      # Technical details
├── USAGE_EXAMPLES.md              # Usage examples
├── DELIVERABLES_CHECKLIST.md      # Verification checklist
└── docs/                          # API documentation
    ├── api_current_weather.md
    ├── api_5day_forecast.md
    ├── api_air_pollution.md
    └── api_geocoding.md
```

## Technical Details

### Framework
- **FastMCP** - Official MCP framework for Python
- **Requests** - HTTP client library

### Design Principles
- **No Generic Passthrough Tools** - Every tool is a specific named operation
- **JSON-Serializable Responses** - All responses are JSON-compatible
- **Graceful Error Handling** - Expected errors return error dicts, not exceptions
- **Comprehensive Documentation** - Each tool has detailed docstrings

### Multi-Step Workflow Support
The server enables complex workflows:
1. **Geocoding → Weather** - Find coordinates, then get weather
2. **Weather + Pollution** - Get both for comprehensive environmental data
3. **Forecast Analysis** - Compare forecasts with historical data
4. **Location Discovery** - Reverse geocode, then get weather for nearby locations

## Performance

- **Request Timeout**: 10 seconds per API call
- **Response Format**: Direct JSON pass-through from OpenWeatherMap API
- **Error Recovery**: Graceful handling of network and API errors

## Limitations

- Free tier rate limits apply (see OpenWeatherMap documentation)
- Historical air pollution data available from November 27, 2020 onwards
- Some response fields may vary by location and weather conditions

## Support

For issues with:
- **MCP Protocol**: See [Model Context Protocol documentation](https://modelcontextprotocol.io/)
- **OpenWeatherMap API**: See [OpenWeatherMap API documentation](https://openweathermap.org/api)
- **This Implementation**: Check the documentation files in this repository

## License

This MCP server implementation is provided as-is for use with the OpenWeatherMap API.

## Acknowledgments

- OpenWeatherMap for the comprehensive weather API
- Anthropic for the Model Context Protocol specification
- FastMCP framework for Python MCP implementation
