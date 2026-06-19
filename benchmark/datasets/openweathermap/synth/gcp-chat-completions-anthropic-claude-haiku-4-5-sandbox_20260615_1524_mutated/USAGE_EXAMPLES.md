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

## Tool Usage Examples

### 1. Get Current Weather by Coordinates

```python
# Get current weather for London (51.5074°N, -0.1278°W)
get_current_weather_by_coords(
    latitude=51.5074,
    longitude=-0.1278,
    units="metric",
    language="en"
)

# Response includes:
# - Temperature, feels_like, min/max temps
# - Humidity, pressure, visibility
# - Wind speed and direction
# - Cloud coverage
# - Weather conditions (rain, snow, etc.)
```

### 2. Get Current Weather by City Name

```python
# Get weather for Paris, France
get_current_weather_by_city_name(
    city_name="Paris",
    country_code="FR",
    units="metric"
)

# Get weather for New York, USA
get_current_weather_by_city_name(
    city_name="New York",
    state_code="NY",
    country_code="US",
    units="imperial"
)
```

### 3. Get 5-Day Forecast by Coordinates

```python
# Get 5-day forecast for Tokyo (35.6762°N, 139.6503°E)
get_5day_forecast_by_coords(
    latitude=35.6762,
    longitude=139.6503,
    units="metric",
    count=20  # Get 20 timestamps (about 2.5 days)
)

# Response includes:
# - 40 timestamps (3-hour intervals for 5 days)
# - Temperature, humidity, pressure for each period
# - Precipitation probability
# - Wind data
# - Cloud coverage
```

### 4. Get 5-Day Forecast by City Name

```python
# Get forecast for Sydney, Australia
get_5day_forecast_by_city_name(
    city_name="Sydney",
    country_code="AU",
    units="metric"
)
```

### 5. Get Current Air Pollution

```python
# Get air quality for Delhi, India (28.7041°N, 77.1025°E)
get_current_air_pollution(
    latitude=28.7041,
    longitude=77.1025
)

# Response includes:
# - Air Quality Index (AQI): 1-5 (Good to Very Poor)
# - Pollutant concentrations:
#   - CO (Carbon monoxide)
#   - NO (Nitrogen monoxide)
#   - NO2 (Nitrogen dioxide)
#   - O3 (Ozone)
#   - SO2 (Sulphur dioxide)
#   - PM2.5 (Fine particles)
#   - PM10 (Coarse particles)
#   - NH3 (Ammonia)
```

### 6. Get Air Pollution Forecast

```python
# Get 4-day air pollution forecast for Beijing (39.9042°N, 116.4074°E)
get_air_pollution_forecast(
    latitude=39.9042,
    longitude=116.4074
)

# Response includes hourly forecasts for the next 4 days
```

### 7. Get Historical Air Pollution Data

```python
import time

# Get air pollution data for the past week
end_time = int(time.time())
start_time = end_time - (7 * 24 * 3600)  # 7 days ago

get_air_pollution_history(
    latitude=40.7128,  # New York
    longitude=-74.0060,
    start=start_time,
    end=end_time
)

# Response includes historical AQI and pollutant data
```

### 8. Geocode Location Name (Direct Geocoding)

```python
# Find coordinates for "London"
geocode_location_name(
    location_name="London",
    country_code="GB",
    limit=5  # Get up to 5 results
)

# Response includes:
# - name: Location name
# - lat: Latitude
# - lon: Longitude
# - country: Country code
# - state: State (if applicable)
# - local_names: Names in different languages

# Example response:
# [
#   {
#     "name": "London",
#     "lat": 51.5085,
#     "lon": -0.1257,
#     "country": "GB"
#   }
# ]
```

### 9. Geocode Zip Code

```python
# Find coordinates for postal code
geocode_zip_code(
    zip_code="90210",
    country_code="US"
)

# Response:
# {
#   "zip": "90210",
#   "name": "Beverly Hills",
#   "lat": 34.0901,
#   "lon": -118.4065,
#   "country": "US"
# }
```

### 10. Reverse Geocode (Coordinates to Location Names)

```python
# Find location names for coordinates
reverse_geocode(
    latitude=48.8566,  # Paris
    longitude=2.3522,
    limit=5
)

# Response includes nearby locations:
# [
#   {
#     "name": "Paris",
#     "lat": 48.8566,
#     "lon": 2.3522,
#     "country": "FR"
#   },
#   ...
# ]
```

## Multi-Step Workflow Examples

### Workflow 1: Find Weather for a City by Name

```python
# Step 1: Geocode the city name to get coordinates
locations = geocode_location_name(
    location_name="Tokyo",
    country_code="JP",
    limit=1
)

if locations and len(locations) > 0:
    lat = locations[0]["lat"]
    lon = locations[0]["lon"]
    
    # Step 2: Get current weather using coordinates
    weather = get_current_weather_by_coords(
        latitude=lat,
        longitude=lon,
        units="metric"
    )
    
    # Now have weather data for Tokyo
```

### Workflow 2: Check Weather and Air Quality

```python
# Get both weather and air quality for a location
weather = get_current_weather_by_coords(
    latitude=35.6762,
    longitude=139.6503,
    units="metric"
)

air_quality = get_current_air_pollution(
    latitude=35.6762,
    longitude=139.6503
)

# Combine data for comprehensive environmental report
```

### Workflow 3: Forecast Analysis with Historical Comparison

```python
import time

# Get 5-day forecast
forecast = get_5day_forecast_by_coords(
    latitude=51.5074,
    longitude=-0.1278,
    units="metric"
)

# Get historical air pollution (past week)
end_time = int(time.time())
start_time = end_time - (7 * 24 * 3600)

history = get_air_pollution_history(
    latitude=51.5074,
    longitude=-0.1278,
    start=start_time,
    end=end_time
)

# Compare forecast with historical trends
```

### Workflow 4: Find Nearby Locations and Get Weather

```python
# Reverse geocode to find nearby locations
nearby = reverse_geocode(
    latitude=40.7128,
    longitude=-74.0060,
    limit=5
)

# Get weather for each nearby location
for location in nearby:
    weather = get_current_weather_by_coords(
        latitude=location["lat"],
        longitude=location["lon"],
        units="metric"
    )
    print(f"{location['name']}: {weather['main']['temp']}°C")
```

## Error Handling

All tools return error responses as JSON dicts:

```python
# Example error response
{
    "error": "API error: 401",
    "details": "Invalid API key"
}

# Example error response for network issues
{
    "error": "Request failed: Connection timeout"
}
```

## Units of Measurement

### Temperature Units
- `standard`: Kelvin (default)
- `metric`: Celsius
- `imperial`: Fahrenheit

### Wind Speed Units
- `standard`: meters/second
- `metric`: meters/second
- `imperial`: miles/hour

### Pressure Units
- All units: hPa (hectopascals)

### Precipitation Units
- All units: mm (millimeters)

## Language Support

The `language` parameter accepts ISO 639-1 language codes:
- `en`: English
- `es`: Spanish
- `fr`: French
- `de`: German
- `it`: Italian
- `pt`: Portuguese
- `ru`: Russian
- `zh_cn`: Chinese (Simplified)
- `ja`: Japanese
- And many more...

## Rate Limiting

OpenWeatherMap free tier has rate limits. The server includes:
- 10-second timeout per request
- Proper error handling for rate limit responses
- Graceful degradation on API errors

## Response Format

All successful responses are JSON objects containing the API response data. The structure varies by endpoint but always includes relevant weather/pollution/location data as documented in the OpenWeatherMap API documentation.
