# Scenario Solutions

## Scenario 1: Get current weather for a city name

1. Use `geocode_direct(q, limit)` to resolve the city name to coordinates.
2. Pick the best match from the returned list (country/state).
3. Call `weather_current_by_coords(latitude, longitude, units, lang)`.

## Scenario 2: Get 5-day / 3-hour forecast for a location

1. Resolve coordinates via `geocode_direct(...)` or `geocode_zip(...)`.
2. Call `forecast_5day_by_coords(latitude, longitude, units, lang, cnt)`.

## Scenario 3: Check current air quality and forecast

1. Resolve coordinates via `geocode_direct(...)`.
2. Call `air_pollution_current(latitude, longitude)`.
3. Call `air_pollution_forecast(latitude, longitude)`.

## Scenario 4: Fetch historical air pollution for the last 24 hours

1. Resolve coordinates via `geocode_direct(...)`.
2. Get current unix time via `unix_time_now()`.
3. Compute `start = now - 86400`, `end = now`.
4. Call `air_pollution_history(latitude, longitude, start, end)`.

## Scenario 5: Reverse geocode coordinates to a place name

1. Call `geocode_reverse(latitude, longitude, limit)`.
2. Use the first result as the nearest place name.
