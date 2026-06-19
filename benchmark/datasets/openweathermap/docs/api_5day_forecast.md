# 5 Day / 3 Hour Forecast (API 2.5)

*Source: https://openweathermap.org/forecast5*

---

- One Call API 3.0
- Current & Forecast
- Solar Irradiance
- Historical
- Maps
- Environmental
- Other
5 day weather forecast

### Product concept
5 day forecast is available at any location on the globe. It includes weather forecast data with 3-hour step. Forecast is available in JSON or XML format.
Call 5 day / 3 hour forecast data

### How to make an API call
You can search weather forecast for 5 days with data every 3 hours by geographic coordinates. All weather data can be obtained in JSON and XML formats.

## API call

```
api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
```

```
api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
```

[TABLE]
Parameters
lat | required | Latitude. If you need the geocoder to automatic convert city names and zip-codes to geo coordinates and the other way around, please use ourGeocoding API
lon | required | Longitude. If you need the geocoder to automatic convert city names and zip-codes to geo coordinates and the other way around, please use ourGeocoding API
appid | required | Your unique API key (you can always find it on your account page under the"API key" tab)
units | optional | Units of measurement.standard,metricandimperialunits are available. If you do not use theunitsparameter,standardunits will be applied by default.Learn more
mode | optional | Response format. JSON format is used by default. To get data in XML format usemode=xml.Learn more
cnt | optional | A number of timestamps, which will be returned in the API response.Learn more
units | optional | Units of measurement.standard,metricandimperialunits are available. If you do not use theunitsparameter,standardunits will be applied by default.Learn more
lang | optional | You can use thelangparameter to get the output in your language.Learn more
[/TABLE]
Parameters
lat
required
Latitude. If you need the geocoder to automatic convert city names and zip-codes to geo coordinates and the other way around, please use ourGeocoding API
lon
required
Longitude. If you need the geocoder to automatic convert city names and zip-codes to geo coordinates and the other way around, please use ourGeocoding API
appid
required
Your unique API key (you can always find it on your account page under the"API key" tab)
units
optional
Units of measurement.standard,metricandimperialunits are available. If you do not use theunitsparameter,standardunits will be applied by default.Learn more
mode
optional
Response format. JSON format is used by default. To get data in XML format usemode=xml.Learn more
cnt
optional
A number of timestamps, which will be returned in the API response.Learn more
units
optional
Units of measurement.standard,metricandimperialunits are available. If you do not use theunitsparameter,standardunits will be applied by default.Learn more
lang
optional
You can use thelangparameter to get the output in your language.Learn more
Please useGeocoder APIif you need automatic convert city names and zip-codes to geo coordinates and the other way around.
Please note thatbuilt-in geocoderhas been deprecated. Although it is still available for use, bug fixing and updates are no longer available for this functionality.

## Examples of API calls

```
To view the API response, expand the example by clicking the triangle.
```

```
To view the API response, expand the example by clicking the triangle.
```
API response
If you do not see some of the parameters in your API response it means that these weather phenomena are just not happened for the time of measurement for the city or location chosen. Only really measured or calculated data is displayed in API response.

## JSON

```
To view the API response, expand the example by clicking the triangle.
```

```
To view the API response, expand the example by clicking the triangle.
```
JSON format API response fields
- codInternal parameter
- messageInternal parameter
- cntA number of timestamps returned in the API response
- listlist.dtTime of data forecasted, unix, UTClist.mainlist.main.tempTemperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheitlist.main.feels_likeThis temperature parameter accounts for the human perception of weather. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheitlist.main.temp_minMinimum temperature at the moment of calculation. This is minimal forecasted temperature (within large megalopolises and urban areas), use this parameter optionally. Please find more infohere. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheitlist.main.temp_maxMaximum temperature at the moment of calculation. This is maximal forecasted temperature (within large megalopolises and urban areas), use this parameter optionally. Please find more infohere. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheitlist.main.pressureAtmospheric pressure on the sea level by default, hPalist.main.sea_levelAtmospheric pressure on the sea level, hPalist.main.grnd_levelAtmospheric pressure on the ground level, hPalist.main.humidityHumidity, %list.main.temp_kfInternal parameterlist.weatherlist.weather.idWeather condition idlist.weather.mainGroup of weather parameters (Rain, Snow, Clouds etc.)list.weather.descriptionWeather condition within the group. Please find morehere.You can get the output in your language.Learn morelist.weather.iconWeather icon idlist.cloudslist.clouds.allCloudiness, %list.windlist.wind.speedWind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hourlist.wind.degWind direction, degrees (meteorological)list.wind.gustWind gust. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hourlist.visibilityAverage visibility, metres. The maximum value of the visibility is 10kmlist.popProbability of precipitation. The values of the parameter vary between 0 and 1, where 0 is equal to 0%, 1 is equal to 100%list.rainlist.rain.3hRain volume for last 3 hours, mm. Please note that only mm as units of measurement are available for this parameterlist.snowlist.snow.3hSnow volume for last 3 hours. Please note that only mm as units of measurement are available for this parameterlist.syslist.sys.podPart of the day (n - night, d - day)list.dt_txtTime of data forecasted, ISO, UTC
- citycity.idCity ID. Please note that built-in geocoder functionality has been deprecated. Learn moreherecity.nameCity name. Please note that built-in geocoder functionality has been deprecated. Learn moreherecity.coordcity.coord.latGeo location, latitudecity.coord.lonGeo location, longitudecity.countryCountry code (GB, JP etc.). Please note that built-in geocoder functionality has been deprecated. Learn moreherecity.populationCity populationcity.timezoneShift in seconds from UTCcity.sunriseSunrise time, Unix, UTCcity.sunsetSunset time, Unix, UTC
- list.dtTime of data forecasted, unix, UTC
- list.mainlist.main.tempTemperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheitlist.main.feels_likeThis temperature parameter accounts for the human perception of weather. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheitlist.main.temp_minMinimum temperature at the moment of calculation. This is minimal forecasted temperature (within large megalopolises and urban areas), use this parameter optionally. Please find more infohere. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheitlist.main.temp_maxMaximum temperature at the moment of calculation. This is maximal forecasted temperature (within large megalopolises and urban areas), use this parameter optionally. Please find more infohere. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheitlist.main.pressureAtmospheric pressure on the sea level by default, hPalist.main.sea_levelAtmospheric pressure on the sea level, hPalist.main.grnd_levelAtmospheric pressure on the ground level, hPalist.main.humidityHumidity, %list.main.temp_kfInternal parameter
- list.weatherlist.weather.idWeather condition idlist.weather.mainGroup of weather parameters (Rain, Snow, Clouds etc.)list.weather.descriptionWeather condition within the group. Please find morehere.You can get the output in your language.Learn morelist.weather.iconWeather icon id
- list.cloudslist.clouds.allCloudiness, %
- list.windlist.wind.speedWind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hourlist.wind.degWind direction, degrees (meteorological)list.wind.gustWind gust. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour
- list.visibilityAverage visibility, metres. The maximum value of the visibility is 10km
- list.popProbability of precipitation. The values of the parameter vary between 0 and 1, where 0 is equal to 0%, 1 is equal to 100%
- list.rainlist.rain.3hRain volume for last 3 hours, mm. Please note that only mm as units of measurement are available for this parameter
- list.snowlist.snow.3hSnow volume for last 3 hours. Please note that only mm as units of measurement are available for this parameter
- list.syslist.sys.podPart of the day (n - night, d - day)
- list.dt_txtTime of data forecasted, ISO, UTC
- list.main.tempTemperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit
- list.main.feels_likeThis temperature parameter accounts for the human perception of weather. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit
- list.main.temp_minMinimum temperature at the moment of calculation. This is minimal forecasted temperature (within large megalopolises and urban areas), use this parameter optionally. Please find more infohere. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit
- list.main.temp_maxMaximum temperature at the moment of calculation. This is maximal forecasted temperature (within large megalopolises and urban areas), use this parameter optionally. Please find more infohere. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit
- list.main.pressureAtmospheric pressure on the sea level by default, hPa
- list.main.sea_levelAtmospheric pressure on the sea level, hPa
- list.main.grnd_levelAtmospheric pressure on the ground level, hPa
- list.main.humidityHumidity, %
- list.main.temp_kfInternal parameter
- list.weather.idWeather condition id
- list.weather.mainGroup of weather parameters (Rain, Snow, Clouds etc.)
- list.weather.descriptionWeather condition within the group. Please find morehere.You can get the output in your language.Learn more
- list.weather.iconWeather icon id
- list.clouds.allCloudiness, %
- list.wind.speedWind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour
- list.wind.degWind direction, degrees (meteorological)
- list.wind.gustWind gust. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour
- list.rain.3hRain volume for last 3 hours, mm. Please note that only mm as units of measurement are available for this parameter
- list.snow.3hSnow volume for last 3 hours. Please note that only mm as units of measurement are available for this parameter
- list.sys.podPart of the day (n - night, d - day)
- city.idCity ID. Please note that built-in geocoder functionality has been deprecated. Learn morehere
- city.nameCity name. Please note that built-in geocoder functionality has been deprecated. Learn morehere
- city.coordcity.coord.latGeo location, latitudecity.coord.lonGeo location, longitude
- city.countryCountry code (GB, JP etc.). Please note that built-in geocoder functionality has been deprecated. Learn morehere
- city.populationCity population
- city.timezoneShift in seconds from UTC
- city.sunriseSunrise time, Unix, UTC
- city.sunsetSunset time, Unix, UTC
- city.coord.latGeo location, latitude
- city.coord.lonGeo location, longitude
XML

## Example of API response

```
To view the API response, expand the example by clicking the triangle.
```

```
To view the API response, expand the example by clicking the triangle.
```
- locationlocation.nameCity name. Please note that built-in geocoder functionality has been deprecated. Learn moreherelocation.typeInternal parameterlocation.countryCountry code (GB, JP etc.). Please note that built-in geocoder functionality has been deprecated. Learn moreherelocation.timezoneShift in seconds from UTClocation.locationlocation.location.altitudeGeo location, altitude above the sea levellocation.location.latitudeGeo location, latitudelocation.location.longitudeGeo location, longitudelocation.location.geobaseInternal parameterlocation.location.geobaseidInternal parameter
- metameta.lastupdatePrototype parametermeta.calctimeSpeed of data calculationmeta.nextupdatePrototype parameter
- sunsun.riseSunrise timesun.setSunset time
- forecastforecast.timeforecast.time.fromBeginning of the period of data forecastedforecast.time.toEnd of the period of data forecastedforecast.symbolforecast.symbol.numberWeather condition idforecast.symbol.nameWeather conditionforecast.symbol.varWeather icon idforecast.precipitationforecast.precipitation.probabilityProbability of precipitation. The values of the parameter vary between 0 and 1, where 0 is equal to 0%, 1 is equal to 100%forecast.precipitation.unitPeriod of measurements. Possible value is 1 hour, 3 hoursforecast.precipitation.valuePrecipitation volume for the last 3 hours, mm. Please note that only mm as units of measurement are available for this parameterforecast.precipitation.typeType of precipitation. Possible value is rain, snowforecast.windDirectionforecast.windDirection.degWind direction, degrees (meteorological)forecast.windDirection.codeCode of the wind direction. Possible value is WSW, N, S etc.forecast.windDirection.nameFull name of the wind directionforecast.windSpeedforecast.windSpeed.mpsWind speed, meters per secondforecast.windSpeed.unitWind speed units, m/sforecast.windSpeed.nameType of windforecast.windGustforecast.windGust.gustWind gust, meters per secondforecast.windGust.unitWind gust units, m/sforecast.temperatureforecast.temperature.unitUnit of measurements. Possible value is Celsius, Kelvin, Fahrenhei.forecast.temperature.valueTemperatureforecast.temperature.minMinimum temperature at the moment of calculation. This is minimal forecasted temperature (within large megalopolises and urban areas), use this parameter optionally. Please find more infohereforecast.temperature.maxMaximum temperature at the moment of calculation. This is maximal forecasted temperature (within large megalopolises and urban areas), use this parameter optionally. Please find more infohereforecast.feels_likeforecast.feels_like.unitUnit of measurements. Possible value is Celsius, Kelvin, Fahrenheit. Unit Default: Kelvinforecast.feels_like.valueTemperature. This temperature parameter accounts for the human perception of weatherforecast.pressureforecast.pressure.unithPaforecast.pressure.valuePressure valueforecast.humidityforecast.humidity.unit%forecast.humidity.valueHumidity valueforecast.cloudsforecast.pressure.valueName of the cloudinessforecast.pressure.allCloudinessforecast.pressure.unit%forecast.visibilityforecast.visibility.valueAverage visibility, metres. The maximum value of the visibility is 10km
- location.nameCity name. Please note that built-in geocoder functionality has been deprecated. Learn morehere
- location.typeInternal parameter
- location.countryCountry code (GB, JP etc.). Please note that built-in geocoder functionality has been deprecated. Learn morehere
- location.timezoneShift in seconds from UTC
- location.locationlocation.location.altitudeGeo location, altitude above the sea levellocation.location.latitudeGeo location, latitudelocation.location.longitudeGeo location, longitudelocation.location.geobaseInternal parameterlocation.location.geobaseidInternal parameter
- location.location.altitudeGeo location, altitude above the sea level
- location.location.latitudeGeo location, latitude
- location.location.longitudeGeo location, longitude
- location.location.geobaseInternal parameter
- location.location.geobaseidInternal parameter
- meta.lastupdatePrototype parameter
- meta.calctimeSpeed of data calculation
- meta.nextupdatePrototype parameter
- sun.riseSunrise time
- sun.setSunset time
- forecast.timeforecast.time.fromBeginning of the period of data forecastedforecast.time.toEnd of the period of data forecasted
- forecast.symbolforecast.symbol.numberWeather condition idforecast.symbol.nameWeather conditionforecast.symbol.varWeather icon id
- forecast.precipitationforecast.precipitation.probabilityProbability of precipitation. The values of the parameter vary between 0 and 1, where 0 is equal to 0%, 1 is equal to 100%forecast.precipitation.unitPeriod of measurements. Possible value is 1 hour, 3 hoursforecast.precipitation.valuePrecipitation volume for the last 3 hours, mm. Please note that only mm as units of measurement are available for this parameterforecast.precipitation.typeType of precipitation. Possible value is rain, snow
- forecast.windDirectionforecast.windDirection.degWind direction, degrees (meteorological)forecast.windDirection.codeCode of the wind direction. Possible value is WSW, N, S etc.forecast.windDirection.nameFull name of the wind direction
- forecast.windSpeedforecast.windSpeed.mpsWind speed, meters per secondforecast.windSpeed.unitWind speed units, m/sforecast.windSpeed.nameType of wind
- forecast.windGustforecast.windGust.gustWind gust, meters per secondforecast.windGust.unitWind gust units, m/s
- forecast.temperatureforecast.temperature.unitUnit of measurements. Possible value is Celsius, Kelvin, Fahrenhei.forecast.temperature.valueTemperatureforecast.temperature.minMinimum temperature at the moment of calculation. This is minimal forecasted temperature (within large megalopolises and urban areas), use this parameter optionally. Please find more infohereforecast.temperature.maxMaximum temperature at the moment of calculation. This is maximal forecasted temperature (within large megalopolises and urban areas), use this parameter optionally. Please find more infohere
- forecast.feels_likeforecast.feels_like.unitUnit of measurements. Possible value is Celsius, Kelvin, Fahrenheit. Unit Default: Kelvinforecast.feels_like.valueTemperature. This temperature parameter accounts for the human perception of weather
- forecast.pressureforecast.pressure.unithPaforecast.pressure.valuePressure value
- forecast.humidityforecast.humidity.unit%forecast.humidity.valueHumidity value
- forecast.cloudsforecast.pressure.valueName of the cloudinessforecast.pressure.allCloudinessforecast.pressure.unit%
- forecast.visibilityforecast.visibility.valueAverage visibility, metres. The maximum value of the visibility is 10km
- forecast.time.fromBeginning of the period of data forecasted
- forecast.time.toEnd of the period of data forecasted
- forecast.symbol.numberWeather condition id
- forecast.symbol.nameWeather condition
- forecast.symbol.varWeather icon id
- forecast.precipitation.probabilityProbability of precipitation. The values of the parameter vary between 0 and 1, where 0 is equal to 0%, 1 is equal to 100%
- forecast.precipitation.unitPeriod of measurements. Possible value is 1 hour, 3 hours
- forecast.precipitation.valuePrecipitation volume for the last 3 hours, mm. Please note that only mm as units of measurement are available for this parameter
- forecast.precipitation.typeType of precipitation. Possible value is rain, snow
- forecast.windDirection.degWind direction, degrees (meteorological)
- forecast.windDirection.codeCode of the wind direction. Possible value is WSW, N, S etc.
- forecast.windDirection.nameFull name of the wind direction
- forecast.windSpeed.mpsWind speed, meters per second
- forecast.windSpeed.unitWind speed units, m/s
- forecast.windSpeed.nameType of wind
- forecast.windGust.gustWind gust, meters per second
- forecast.windGust.unitWind gust units, m/s
- forecast.temperature.unitUnit of measurements. Possible value is Celsius, Kelvin, Fahrenhei.
- forecast.temperature.valueTemperature
- forecast.temperature.minMinimum temperature at the moment of calculation. This is minimal forecasted temperature (within large megalopolises and urban areas), use this parameter optionally. Please find more infohere
- forecast.temperature.maxMaximum temperature at the moment of calculation. This is maximal forecasted temperature (within large megalopolises and urban areas), use this parameter optionally. Please find more infohere
- forecast.feels_like.unitUnit of measurements. Possible value is Celsius, Kelvin, Fahrenheit. Unit Default: Kelvin
- forecast.feels_like.valueTemperature. This temperature parameter accounts for the human perception of weather
- forecast.pressure.unithPa
- forecast.pressure.valuePressure value
- forecast.humidity.unit%
- forecast.humidity.valueHumidity value
- forecast.pressure.valueName of the cloudiness
- forecast.pressure.allCloudiness
- forecast.pressure.unit%
- forecast.visibility.valueAverage visibility, metres. The maximum value of the visibility is 10km
We provide a broad variety of products such asOne Call API 3.0,Solar Irradiance & Energy Prediction service,Road Risk API,Air Pollution APIand solutions for advanced weather parameters like solar irradiance data, UVI, dew point, government weather alerts, etc. Please review ourproduct listpage and find more info in the product documentation andpricingpages.

### List of weather condition codes
List ofweather condition codeswith icons (range of thunderstorm, drizzle, rain, snow, clouds, atmosphere etc.)

### Min/max temperature in current weather API and forecast API
- In5 day / 3 hour forecast API,Hourly forecast APIandCurrent weather API-temp_minandtemp_maxare optional parameters mean min / max temperature in the city at the current moment just for your reference. For large cities and megalopolises geographically expanded it might be applicable. In most cases bothtemp_minandtemp_maxparameters have the same volume as 'temp'. Please usetemp_minandtemp_maxparameters in current weather API optionally.
- In16 Day forecast-minandmaxmean maximum and minimum temperature in the day.

## Example of Current Weather API response

```
"main":{
  "temp":306.15, //current temperature
  "pressure":1013,
  "humidity":44,
  "temp_min":30.15, //min current temperature in the city
  "temp_max":306.15 //max current temperature in the city
},
```

```
"main":{
  "temp":306.15, //current temperature
  "pressure":1013,
  "humidity":44,
  "temp_min":30.15, //min current temperature in the city
  "temp_max":306.15 //max current temperature in the city
},
```
For comparison take a look at example of Daily Forecast Weather API response:

## Example of API response

```
"dt":1406080800,
"temp":{
        "day":297.77,  //daily averaged temperature
        "min":293.52, //daily min temperature
        "max":297.77, //daily max temperature
        "night":293.52, //night temperature
        "eve":297.77, //evening temperature
        "morn":297.77}, //morning temperature
```

```
"dt":1406080800,
"temp":{
        "day":297.77,  //daily averaged temperature
        "min":293.52, //daily min temperature
        "max":297.77, //daily max temperature
        "night":293.52, //night temperature
        "eve":297.77, //evening temperature
        "morn":297.77}, //morning temperature
```
Bulk downloading
We provide number of bulk files with current weather and forecasts. More information is on theBulk page.
Bulk downloading is available not for all accounts. To get more information please refer to thePrice page.
http://bulk.openweathermap.org/sample/
Other features

### Geocoding API
Requesting API calls by geographical coordinates is the most accurate way to specify any location. If you need to convert city names and zip-codes to geo coordinates and the other way around automatically, please use ourGeocoding API.

### Built-in geocoding
Please useGeocoder APIif you need automatic convert city names and zip-codes to geo coordinates and the other way around.
Please note that API requests by city name, zip-codes and city id have been deprecated. Although they are still available for use, bug fixing and updates are no longer available for this functionality.

### Built-in API request by city name
You can search weather forecast for 5 days with data every 3 hours by city name. All weather data can be obtained in JSON and XML formats.

## API call

```
api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}
```

```
api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}
```

## API call

```
api.openweathermap.org/data/2.5/forecast?q={city name},{country code}&appid={API key}
```

```
api.openweathermap.org/data/2.5/forecast?q={city name},{country code}&appid={API key}
```

## API call

```
api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={API key}
```

```
api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={API key}
```

[TABLE]
Parameters
q | required | City name, state code and country code divided by comma, use ISO 3166 country codes.You can specify the parameter not only in English. In this case, the API response should be returned in the same language as the language of requested location name if the location is in our predefined list of more than 200,000 locations.
appid | required | Your unique API key (you can always find it on your account page under the"API key" tab)
mode | optional | Response format. JSON format is used by default. To get data in XML format usemode=xml.Learn more
cnt | optional | A number of timestamps, which will be returned in the API response.Learn more
units | optional | Units of measurement.standard,metricandimperialunits are available. If you do not use theunitsparameter,standardunits will be applied by default.Learn more
lang | optional | You can use thelangparameter to get the output in your language.Learn more
[/TABLE]
Parameters
required
City name, state code and country code divided by comma, use ISO 3166 country codes.You can specify the parameter not only in English. In this case, the API response should be returned in the same language as the language of requested location name if the location is in our predefined list of more than 200,000 locations.
appid
required
Your unique API key (you can always find it on your account page under the"API key" tab)
mode
optional
Response format. JSON format is used by default. To get data in XML format usemode=xml.Learn more
cnt
optional
A number of timestamps, which will be returned in the API response.Learn more
units
optional
Units of measurement.standard,metricandimperialunits are available. If you do not use theunitsparameter,standardunits will be applied by default.Learn more
lang
optional
You can use thelangparameter to get the output in your language.Learn more

## Examples of API calls

```
To view the API response, expand the example by clicking the triangle.
```

```
To view the API response, expand the example by clicking the triangle.
```
There is a possibility to receive a central district of the city/town with its own parameters (geographic coordinates/id/name) in API response. Please see the example below.

## Example of API response

```
To view the API response, expand the example by clicking the triangle.
```

```
To view the API response, expand the example by clicking the triangle.
```

### Built-in API request by city ID
You can search weather forecast for 5 days with data every 3 hours by city ID. All weather data can be obtained in JSON and XML formats.
List of city ID "city.list.json.gz" can be downloadedhere.
We recommend to call API by city ID to get unambiguous result for your city.

## API call

```
api.openweathermap.org/data/2.5/forecast?id={city ID}&appid={API key}
```

```
api.openweathermap.org/data/2.5/forecast?id={city ID}&appid={API key}
```

[TABLE]
Parameters
id | required | City ID. The list of city IDs 'city.list.json.gz' can be downloadedhere.
appid | required | Your unique API key (you can always find it on your account page under the"API key" tab)
mode | optional | Response format. JSON format is used by default. To get data in XML format usemode=xml.Learn more
cnt | optional | A number of timestamps, which will be returned in the API response.Learn more
units | optional | Units of measurement.standard,metricandimperialunits are available. If you do not use theunitsparameter,standardunits will be applied by default.Learn more
lang | optional | You can use thelangparameter to get the output in your language.Learn more
[/TABLE]
Parameters
id
required
City ID. The list of city IDs 'city.list.json.gz' can be downloadedhere.
appid
required
Your unique API key (you can always find it on your account page under the"API key" tab)
mode
optional
Response format. JSON format is used by default. To get data in XML format usemode=xml.Learn more
cnt
optional
A number of timestamps, which will be returned in the API response.Learn more
units
optional
Units of measurement.standard,metricandimperialunits are available. If you do not use theunitsparameter,standardunits will be applied by default.Learn more
lang
optional
You can use thelangparameter to get the output in your language.Learn more

## Examples of API calls

```
To view the API response, expand the example by clicking the triangle.
```

```
To view the API response, expand the example by clicking the triangle.
```

### Built-in API request by ZIP code
Please note if country is not specified then the search works for USA as a default.

## API call

```
api.openweathermap.org/data/2.5/forecast?zip={zip code},{country code}&appid={API key}
```

```
api.openweathermap.org/data/2.5/forecast?zip={zip code},{country code}&appid={API key}
```

[TABLE]
Parameters
zip | required | Zip code
appid | required | Your unique API key (you can always find it on your account page under the"API key" tab)
mode | optional | Response format. JSON format is used by default. To get data in XML format usemode=xml.Learn more
cnt | optional | A number of timestamps, which will be returned in the API response.Learn more
units | optional | Units of measurement.standard,metricandimperialunits are available. If you do not use theunitsparameter,standardunits will be applied by default.Learn more
lang | optional | You can use thelangparameter to get the output in your language.Learn more
[/TABLE]
Parameters
zip
required
Zip code
appid
required
Your unique API key (you can always find it on your account page under the"API key" tab)
mode
optional
Response format. JSON format is used by default. To get data in XML format usemode=xml.Learn more
cnt
optional
A number of timestamps, which will be returned in the API response.Learn more
units
optional
Units of measurement.standard,metricandimperialunits are available. If you do not use theunitsparameter,standardunits will be applied by default.Learn more
lang
optional
You can use thelangparameter to get the output in your language.Learn more

## Examples of API calls

```
To view the API response, expand the example by clicking the triangle.
```

```
To view the API response, expand the example by clicking the triangle.
```

### Format
Response format. JSON format is used by default. To get data in XML format usemode=xml.

[TABLE]
Parameters
mode | optional | Response format. JSON format is used by default. To get data in XML format usemode=xml.
[/TABLE]
Parameters
mode
optional
Response format. JSON format is used by default. To get data in XML format usemode=xml.
JSON

## Examples of API calls

```
To view the API response, expand the example by clicking the triangle.
```

```
To view the API response, expand the example by clicking the triangle.
```
XML

## Example of API response

```
To view the API response, expand the example by clicking the triangle.
```

```
To view the API response, expand the example by clicking the triangle.
```

### Limitation of result
To limit number of timestamps in the API response please setupcnt.

[TABLE]
Parameters
cnt | optional | A number of timestamps, which will be returned in the API response.
[/TABLE]
Parameters
cnt
optional
A number of timestamps, which will be returned in the API response.

## Examples of API calls

```
To view the API response, expand the example by clicking the triangle.
```

```
To view the API response, expand the example by clicking the triangle.
```

### Units of measurement
standard,metric, andimperialunits are available.

[TABLE]
Parameters
units | optional | Units of measurement.standard,metricandimperialunits are available. If you do not use theunitsparameter,standardunits will be applied by default
[/TABLE]
Parameters
units
optional
Units of measurement.standard,metricandimperialunits are available. If you do not use theunitsparameter,standardunits will be applied by default
List of all API parameters with unitsopenweathermap.org/weather-data
Standard

## Examples of API calls

```
To view the API response, expand the example by clicking the triangle.
```

```
To view the API response, expand the example by clicking the triangle.
```
Metric

## Example of API response

```
To view the API response, expand the example by clicking the triangle.
```

```
To view the API response, expand the example by clicking the triangle.
```
Imperial

## Example of API response

```
To view the API response, expand the example by clicking the triangle.
```

```
To view the API response, expand the example by clicking the triangle.
```

### Multilingual support
You can use thelangparameter to get the output in your language.
Translation is applied to thecity nameanddescriptionfields.

## API call

```
http://api.openweathermap.org/data/2.5/forecast?id=524901&lang={lang}
```

```
http://api.openweathermap.org/data/2.5/forecast?id=524901&lang={lang}
```

[TABLE]
Parameters
lang | optional | You can use thelangparameter to get the output in your language.
[/TABLE]
Parameters
lang
optional
You can use thelangparameter to get the output in your language.

## Examples of API calls

```
To view the API response, expand the example by clicking the triangle.
```

```
To view the API response, expand the example by clicking the triangle.
```
We support the following languages that you can use with the corresponded lang values:
- sqAlbanian
- afAfrikaans
- arArabic
- azAzerbaijani
- euBasque
- beBelarusian
- bgBulgarian
- caCatalan
- zh_cnChinese Simplified
- zh_twChinese Traditional
- hrCroatian
- czCzech
- daDanish
- nlDutch
- enEnglish
- fiFinnish
- frFrench
- glGalician
- deGerman
- elGreek
- heHebrew
- hiHindi
- huHungarian
- isIcelandic
- idIndonesian
- itItalian
- jaJapanese
- krKorean
- kuKurmanji (Kurdish)
- laLatvian
- ltLithuanian
- mkMacedonian
- noNorwegian
- faPersian (Farsi)
- plPolish
- ptPortuguese
- pt_brPortuguês Brasil
- roRomanian
- ruRussian
- srSerbian
- skSlovak
- slSlovenian
- sp, esSpanish
- sv, seSwedish
- thThai
- trTurkish
- ua, ukUkrainian
- viVietnamese
- zuZulu

### Call back function for JavaScript code
To use JavaScript code you can transfercallbackfunctionName to JSONP callback.

## Examples of API calls

```
To view the API response, expand the example by clicking the triangle.
```

```
To view the API response, expand the example by clicking the triangle.
```