# OpenWeatherMap MCP Server - Usage Examples

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Set your API key
export OPENWEATHER_API_KEY="your_api_key_here"

# Run the server
python server.py
```

The server will listen on stdio and expose all tools via the MCP protocol.

## Example Tool Calls

### Current Weather

#### Get weather by coordinates
```json
{
  "tool": "get_current_weather_by_coordinates",
  "arguments": {
    "latitude": 51.5074,
    "longitude": -0.1278,
    "units": "metric"
  }
}
```

Response includes: temperature, feels_like, humidity, pressure, wind speed, weather conditions, etc.

#### Get weather by city name
```json
{
  "tool": "get_current_weather_by_city_name",
  "arguments": {
    "city_name": "London",
    "country_code": "GB",
    "units": "metric"
  }
}
```

#### Get weather by ZIP code
```json
{
  "tool": "get_current_weather_by_zip_code",
  "arguments": {
    "zip_code": "90210",
    "country_code": "US",
    "units": "imperial"
  }
}
```

### 5-Day Forecast

#### Get forecast by coordinates
```json
{
  "tool": "get_5day_forecast_by_coordinates",
  "arguments": {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "units": "metric",
    "count": 20
  }
}
```

Returns 3-hour interval forecasts for 5 days (up to 40 timestamps).

#### Get forecast by city name
```json
{
  "tool": "get_5day_forecast_by_city_name",
  "arguments": {
    "city_name": "New York",
    "country_code": "US",
    "units": "imperial"
  }
}
```

### Air Pollution

#### Get current air pollution
```json
{
  "tool": "get_current_air_pollution",
  "arguments": {
    "latitude": 48.8566,
    "longitude": 2.3522
  }
}
```

Response includes:
- AQI (Air Quality Index): 1=Good, 2=Fair, 3=Moderate, 4=Poor, 5=Very Poor
- Pollutant concentrations: CO, NO, NO2, O3, SO2, PM2.5, PM10, NH3

#### Get pollution forecast
```json
{
  "tool": "get_air_pollution_forecast",
  "arguments": {
    "latitude": 48.8566,
    "longitude": 2.3522
  }
}
```

4-day forecast with hourly granularity.

#### Get historical pollution data
```json
{
  "tool": "get_air_pollution_history",
  "arguments": {
    "latitude": 35.6762,
    "longitude": 139.6503,
    "start_timestamp": 1606488670,
    "end_timestamp": 1606747870
  }
}
```

### Geocoding

#### Direct geocoding (name to coordinates)
```json
{
  "tool": "geocode_location_name",
  "arguments": {
    "location_name": "Paris",
    "country_code": "FR",
    "limit": 5
  }
}
```

Returns list of matching locations with coordinates.

#### ZIP code geocoding
```json
{
  "tool": "geocode_zip_code",
  "arguments": {
    "zip_code": "E14",
    "country_code": "GB"
  }
}
```

#### Reverse geocoding (coordinates to location names)
```json
{
  "tool": "reverse_geocode",
  "arguments": {
    "latitude": 51.5098,
    "longitude": -0.1180,
    "limit": 5
  }
}
```

## Multi-Step Workflow Example

### Scenario: Get weather for a city by name

1. **Geocode the city name** to get coordinates:
```json
{
  "tool": "geocode_location_name",
  "arguments": {
    "location_name": "Tokyo",
    "country_code": "JP"
  }
}
```
Response: `{"name": "Tokyo", "lat": 35.6762, "lon": 139.6503, ...}`

2. **Get current weather** using the coordinates:
```json
{
  "tool": "get_current_weather_by_coordinates",
  "arguments": {
    "latitude": 35.6762,
    "longitude": 139.6503,
    "units": "metric"
  }
}
```
Response: Current weather data

3. **Get air pollution** for the same location:
```json
{
  "tool": "get_current_air_pollution",
  "arguments": {
    "latitude": 35.6762,
    "longitude": 139.6503
  }
}
```
Response: Current AQI and pollutant data

4. **Get forecast** for planning:
```json
{
  "tool": "get_5day_forecast_by_coordinates",
  "arguments": {
    "latitude": 35.6762,
    "longitude": 139.6503,
    "units": "metric"
  }
}
```
Response: 5-day forecast with 3-hour intervals

## Units of Measurement

### Standard Units (default)
- Temperature: Kelvin
- Wind Speed: m/s
- Pressure: hPa

### Metric Units
- Temperature: Celsius
- Wind Speed: m/s
- Pressure: hPa

### Imperial Units
- Temperature: Fahrenheit
- Wind Speed: miles/hour
- Pressure: hPa

## Language Support

The `lang` parameter supports multi-language weather descriptions:
- `en` - English
- `es` - Spanish
- `fr` - French
- `de` - German
- `it` - Italian
- `pt` - Portuguese
- `ru` - Russian
- `zh_cn` - Chinese (Simplified)
- And many more...

Example:
```json
{
  "tool": "get_current_weather_by_coordinates",
  "arguments": {
    "latitude": 48.8566,
    "longitude": 2.3522,
    "lang": "fr"
  }
}
```

## Error Handling

All errors are returned as JSON dicts with an "error" key:

```json
{
  "error": "API request failed: 404 Client Error: Not Found"
}
```

Common error scenarios:
- Invalid coordinates (out of range)
- Non-existent city name
- Invalid API key
- Network connectivity issues
- Rate limiting (API quota exceeded)

## Response Examples

### Current Weather Response
```json
{
  "coord": {"lon": -0.1278, "lat": 51.5074},
  "weather": [{"id": 803, "main": "Clouds", "description": "broken clouds"}],
  "main": {
    "temp": 288.15,
    "feels_like": 287.15,
    "temp_min": 286.15,
    "temp_max": 290.15,
    "pressure": 1013,
    "humidity": 72
  },
  "wind": {"speed": 4.1, "deg": 230},
  "clouds": {"all": 75},
  "dt": 1726660758,
  "sys": {
    "country": "GB",
    "sunrise": 1726636384,
    "sunset": 1726680975
  },
  "name": "London"
}
```

### Geocoding Response
```json
[
  {
    "name": "London",
    "lat": 51.5085,
    "lon": -0.1257,
    "country": "GB",
    "state": "England"
  }
]
```

### Air Pollution Response
```json
{
  "coord": [51.5074, -0.1278],
  "list": [
    {
      "dt": 1726660758,
      "main": {"aqi": 2},
      "components": {
        "co": 201.94,
        "no": 0.02,
        "no2": 0.77,
        "o3": 68.66,
        "so2": 0.64,
        "pm2_5": 0.5,
        "pm10": 0.54,
        "nh3": 0.12
      }
    }
  ]
}
```

## Tips for Autonomous Agents

1. **Always geocode first** if you have a location name - this ensures accuracy
2. **Use metric units** for consistency in calculations
3. **Check AQI levels** before recommending outdoor activities
4. **Use forecast data** for planning multi-day activities
5. **Handle errors gracefully** - API may be rate-limited or temporarily unavailable
6. **Cache results** when possible - avoid redundant API calls
7. **Use appropriate limits** for geocoding to avoid too many results
