# Geocoding API (Direct and Reverse)

*Source: https://openweathermap.org/api/geocoding-api*

---

- One Call API 3.0
- Current & Forecast
- Solar Irradiance
- Historical
- Maps
- Environmental
- Other
Geocoding API
Geocoding API is a simple tool that we have developed to ease the search for locations while working with geographic names and coordinates.
Supporting API calls by geographical coordinates is the most accurate way to specify any location, that is why this method is integrated in all OpenWeather APIs. However, this way is not always suitable for all users.Geocoding is the process of transformation of any location name into geographical coordinates, and the other way around (reverse geocoding). OpenWeather’s Geocoding API supports both the direct and reverse methods, working at the level of city names, areas and districts, countries and states:
- Direct geocodingconverts the specified name of a location or zip/post code into the exact geographical coordinates;
- Reverse geocodingconverts the geographical coordinates into the names of the nearby locations.
Direct geocoding
Direct geocoding allows to get geographical coordinates (latitude, longitude) by using name of the location (city name or area name). If you use thelimitparameter in the API call, you can cap how many locations with the same name will be seen in the API response (for instance, London in the UK and London in the US).

### Coordinates by location name

### How to make an API call

## API call

```
http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
```

```
http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
```

[TABLE]
Parameters
q | required | City name, state code (only for the US) and country code divided by comma. Please use ISO 3166 country codes.
appid | required | Your unique API key (you can always find it on your account page under the"API key" tab)
limit | optional | Number of the locations in the API response (up to 5 results can be returned in the API response)
[/TABLE]
Parameters
required
City name, state code (only for the US) and country code divided by comma. Please use ISO 3166 country codes.
appid
required
Your unique API key (you can always find it on your account page under the"API key" tab)
limit
optional
Number of the locations in the API response (up to 5 results can be returned in the API response)

## Example of API call

```
http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={API key}
```

```
http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={API key}
```

## Example of API response

```
To view the API response, expand the example by clicking the triangle.
```

```
To view the API response, expand the example by clicking the triangle.
```
Please note that the fields present will vary based on a country to which a location belongs as well as a specific location.
- nameName of the found location
- local_nameslocal_names.[language code]Name of the found location in different languages. The list of names can be different for different locationslocal_names.asciiInternal fieldlocal_names.feature_nameInternal field
- latGeographical coordinates of the found location (latitude)
- lonGeographical coordinates of the found location (longitude)
- countryCountry of the found location
- state(where available)State of the found location
- local_names.[language code]Name of the found location in different languages. The list of names can be different for different locations
- local_names.asciiInternal field
- local_names.feature_nameInternal field

### Coordinates by zip/post code

## How to make an API call

```
http://api.openweathermap.org/geo/1.0/zip?zip={zip code},{country code}&appid={API key}
```

```
http://api.openweathermap.org/geo/1.0/zip?zip={zip code},{country code}&appid={API key}
```

[TABLE]
Parameters
zip code | required | Zip/post code and country code divided by comma. Please use ISO 3166 country codes.
appid | required | Your unique API key (you can always find it on your account page under the"API key" tab)
[/TABLE]
Parameters
zip code
required
Zip/post code and country code divided by comma. Please use ISO 3166 country codes.
appid
required
Your unique API key (you can always find it on your account page under the"API key" tab)

## Example of API call

```
http://api.openweathermap.org/geo/1.0/zip?zip=E14,GB&appid={API key}
```

```
http://api.openweathermap.org/geo/1.0/zip?zip=E14,GB&appid={API key}
```

## Example of API response

```
{
  "zip": "90210",
  "name": "Beverly Hills",
  "latitude": 34.0901,
  "longitude": -118.4065,
  "country": "US"
}
```

```
{
  "zip": "90210",
  "name": "Beverly Hills",
  "latitude": 34.0901,
  "longitude": -118.4065,
  "country": "US"
}
```

### Fields in API response
- zipSpecified zip/post code in the API request
- nameName of the found area
- latGeographical coordinates of the centroid of found zip/post code (latitude)
- lonGeographical coordinates of the centroid of found zip/post code (longitude)
- countryCountry of the found zip/post code
Reverse geocoding
Reverse geocoding allows to get name of the location (city name or area name) by using geografical coordinates (latitude, longitude). Thelimitparameter in the API call allows you to cap how many location names you will see in the API response.

## API call

```
http://api.openweathermap.org/geo/1.0/reverse?latitude={latitude}&longitude={longitude}&limit={limit}&appid={API key}
```

```
http://api.openweathermap.org/geo/1.0/reverse?latitude={latitude}&longitude={longitude}&limit={limit}&appid={API key}
```

[TABLE]
Parameters
latitude, longitude | required | Geographical coordinates (latitude, longitude)
appid | required | Your unique API key (you can always find it on your account page under the"API key" tab)
limit | optional | Number of the location names in the API response (several results can be returned in the API response)
[/TABLE]
Parameters
latitude, longitude
required
Geographical coordinates (latitude, longitude)
appid
required
Your unique API key (you can always find it on your account page under the"API key" tab)
limit
optional
Number of the location names in the API response (several results can be returned in the API response)

## Example of API call

```
http://api.openweathermap.org/geo/1.0/reverse?latitude=51.5098&longitude=-0.1180&limit=5&appid={API key}
```

```
http://api.openweathermap.org/geo/1.0/reverse?latitude=51.5098&longitude=-0.1180&limit=5&appid={API key}
```

## Example of API response

```
To view the API response, expand the example by clicking the triangle.
```

```
To view the API response, expand the example by clicking the triangle.
```
Please note that the fields present will vary based on a country to which a location belongs as well as a specific location.
- nameName of the found location
- local_nameslocal_names.[language code]Name of the found location in different languages. The list of names can be different for different locations.local_names.asciiInternal fieldlocal_names.feature_nameInternal field
- latGeographical coordinates of the found location (latitude)
- lonGeographical coordinates of the found location (longitude)
- countryCountry of the found location
- state(where available)State of the found location
- local_names.[language code]Name of the found location in different languages. The list of names can be different for different locations.
- local_names.asciiInternal field
- local_names.feature_nameInternal field