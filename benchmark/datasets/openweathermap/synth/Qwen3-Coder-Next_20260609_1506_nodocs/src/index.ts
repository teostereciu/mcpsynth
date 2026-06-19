import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequest,
  ListToolsRequest,
} from "@modelcontextprotocol/sdk/types.js";
import { createRouteHandler } from "@modelcontextprotocol/sdk/server/index.js";
import fetch from "node-fetch";

// Base URL for OpenWeatherMap API
const BASE_URL = "https://api.openweathermap.org/data/2.5";

interface ToolResponse {
  success: boolean;
  content: string;
}

interface ToolError {
  success: boolean;
  content: string;
}

interface GeocodingResult {
  name: string;
  lat: number;
  lon: number;
  country: string;
  state?: string;
}

interface WeatherResponse {
  coord: { lon: number; lat: number };
  weather: Array<{ id: number; main: string; description: string; icon: string }>;
  base: string;
  main: {
    temp: number;
    feels_like: number;
    temp_min: number;
    temp_max: number;
    pressure: number;
    humidity: number;
    sea_level: number;
    grnd_level: number;
  };
  visibility: number;
  wind: { speed: number; deg: number; gust?: number };
  rain?: { "1h"?: number; "3h"?: number };
  snow?: { "1h"?: number; "3h"?: number };
  clouds: { all: number };
  dt: number;
  sys: {
    type: number;
    id: number;
    country: string;
    sunrise: number;
    sunset: number;
  };
  timezone: number;
  id: number;
  name: string;
  cod: number;
  message?: number;
}

interface ForecastResponse {
  cod: string;
  message: number;
  cnt: number;
  list: Array<{
    dt: number;
    main: {
      temp: number;
      feels_like: number;
      temp_min: number;
      temp_max: number;
      pressure: number;
      sea_level: number;
      grnd_level: number;
      humidity: number;
      temp_kf: number;
    };
    weather: Array<{ id: number; main: string; description: string; icon: string }>;
    clouds: { all: number };
    wind: { speed: number; deg: number; gust: number };
    visibility: number;
    pop: number;
    rain?: { "3h": number };
    sys: { pod: string };
    dt_txt: string;
  }>;
  city: {
    id: number;
    name: string;
    coord: { lat: number; lon: number };
    country: string;
    population: number;
    timezone: number;
    sunrise: number;
    sunset: number;
  };
}

interface AirPollutionResponse {
  coord: { lon: number; lat: number };
  list: Array<{
    dt: number;
    main: { aqi: number };
    components: {
      co: number;
      no: number;
      no2: number;
      o3: number;
      so2: number;
      pm2_5: number;
      pm10: number;
      nh3: number;
    };
  }>;
  city: {
    name: string;
    timezone: string;
  };
}

interface AirPollutionHistoryResponse {
  list: Array<{
    dt: number;
    main: { aqi: number };
    components: {
      co: number;
      no: number;
      no2: number;
      o3: number;
      so2: number;
      pm2_5: number;
      pm10: number;
      nh3: number;
    };
  }>;
}

interface AlertResponse {
  weather: Array<{
    id: number;
    message: string;
    startTime: number;
    endTime: number;
    description: string;
    tags: string[];
  }>;
}

/**
 * Get API key from environment
 */
function getApiKey(): string {
  const apiKey = process.env.OPENWEATHER_API_KEY;
  if (!apiKey) {
    throw new Error("OPENWEATHER_API_KEY environment variable is required");
  }
  return apiKey;
}

/**
 * Make a request to the OpenWeatherMap API
 */
async function makeRequest(
  endpoint: string,
  params: Record<string, string | number>
): Promise<Record<string, unknown> | Record<string, unknown>[]> {
  try {
    const apiKey = getApiKey();
    const url = new URL(`${BASE_URL}/${endpoint}`);
    url.searchParams.set("appid", apiKey);
    
    Object.entries(params).forEach(([key, value]) => {
      url.searchParams.set(key, value.toString());
    });

    const response = await fetch(url);

    if (!response.ok) {
      if (response.status === 404) {
        return { error: "Resource not found" };
      }
      if (response.status === 401) {
        return { error: "Invalid API key" };
      }
      if (response.status === 429) {
        return { error: "API rate limit exceeded" };
      }
      return { error: `HTTP error: ${response.status}` };
    }

    return await response.json();
  } catch (error) {
    if (error instanceof Error) {
      return { error: error.message };
    }
    return { error: "An unknown error occurred" };
  }
}

/**
 * Get current weather by city name
 */
async function getCurrentWeatherByCity(
  cityName: string,
  units: "standard" | "metric" | "imperial" = "standard",
  lang: string = "en"
): Promise<WeatherResponse | { error: string }> {
  return makeRequest("weather", {
    q: cityName,
    units,
    lang,
  });
}

/**
 * Get current weather by coordinates
 */
async function getCurrentWeatherByCoords(
  lat: number,
  lon: number,
  units: "standard" | "metric" | "imperial" = "standard",
  lang: string = "en"
): Promise<WeatherResponse | { error: string }> {
  return makeRequest("weather", {
    lat,
    lon,
    units,
    lang,
  });
}

/**
 * Get current weather by city ID
 */
async function getCurrentWeatherByCityId(
  cityId: number,
  units: "standard" | "metric" | "imperial" = "standard"
): Promise<WeatherResponse | { error: string }> {
  return makeRequest("weather", {
    id: cityId,
    units,
  });
}

/**
 * Get current weather by zip code
 */
async function getCurrentWeatherByZip(
  zipCode: string,
  countryCode: string = "us",
  units: "standard" | "metric" | "imperial" = "standard"
): Promise<WeatherResponse | { error: string }> {
  return makeRequest("weather", {
    zip: `${zipCode},${countryCode}`,
    units,
  });
}

/**
 * Get 5-day forecast by city name
 */
async function get5DayForecastByCity(
  cityName: string,
  units: "standard" | "metric" | "imperial" = "standard",
  lang: string = "en"
): Promise<ForecastResponse | { error: string }> {
  return makeRequest("forecast", {
    q: cityName,
    units,
    lang,
  });
}

/**
 * Get 5-day forecast by coordinates
 */
async function get5DayForecastByCoords(
  lat: number,
  lon: number,
  units: "standard" | "metric" | "imperial" = "standard",
  lang: string = "en"
): Promise<ForecastResponse | { error: string }> {
  return makeRequest("forecast", {
    lat,
    lon,
    units,
    lang,
  });
}

/**
 * Get 5-day forecast by city ID
 */
async function get5DayForecastByCityId(
  cityId: number,
  units: "standard" | "metric" | "imperial" = "standard"
): Promise<ForecastResponse | { error: string }> {
  return makeRequest("forecast", {
    id: cityId,
    units,
  });
}

/**
 * Get 5-day forecast by zip code
 */
async function get5DayForecastByZip(
  zipCode: string,
  countryCode: string = "us",
  units: "standard" | "metric" | "imperial" = "standard"
): Promise<ForecastResponse | { error: string }> {
  return makeRequest("forecast", {
    zip: `${zipCode},${countryCode}`,
    units,
  });
}

/**
 * Get air pollution by coordinates
 */
async function getAirPollutionByCoords(
  lat: number,
  lon: number
): Promise<AirPollutionResponse | { error: string }> {
  return makeRequest("air_pollution", {
    lat,
    lon,
  });
}

/**
 * Get air pollution by city name
 */
async function getAirPollutionByCity(
  cityName: string
): Promise<AirPollutionResponse | { error: string }> {
  return makeRequest("air_pollution", {
    q: cityName,
  });
}

/**
 * Get historical air pollution data
 */
async function getAirPollutionHistory(
  lat: number,
  lon: number,
  start: number,
  end: number
): Promise<AirPollutionHistoryResponse | { error: string }> {
  return makeRequest("air_pollution/history", {
    lat,
    lon,
    start,
    end,
  });
}

/**
 * Geocode city name to coordinates
 */
async function geocodeCityName(
  cityName: string
): Promise<GeocodingResult[] | { error: string }> {
  return makeRequest("weather", {
    q: cityName,
  }) as Promise<GeocodingResult[] | { error: string }>;
}

/**
 * Reverse geocode coordinates to city name
 */
async function reverseGeocode(
  lat: number,
  lon: number,
  lang?: string
): Promise<GeocodingResult[] | { error: string }> {
  const params: Record<string, string | number> = {
    lat,
    lon,
  };
  if (lang) {
    params.lang = lang;
  }
  return makeRequest("weather", params) as Promise<GeocodingResult[] | { error: string }>;
}

/**
 * Get weather alerts by coordinates
 */
async function getWeatherAlertsByCoords(
  lat: number,
  lon: number
): Promise<AlertResponse | { error: string }> {
  return makeRequest("alerts", {
    lat,
    lon,
  });
}

/**
 * Get weather alerts by city name
 */
async function getWeatherAlertsByCity(
  cityName: string
): Promise<AlertResponse | { error: string }> {
  return makeRequest("alerts", {
    q: cityName,
  });
}

// Create the tool handlers
const tools = [
  {
    name: "get_current_weather_by_city",
    description: "Get current weather data for a city by name",
    inputSchema: {
      type: "object",
      properties: {
        city_name: { type: "string", description: "Name of the city (e.g., 'London' or 'London,UK')" },
        units: { type: "string", enum: ["standard", "metric", "imperial"], default: "standard", description: "Units of measurement" },
        lang: { type: "string", default: "en", description: "Language for the response description" },
      },
      required: ["city_name"],
    },
  },
  {
    name: "get_current_weather_by_coords",
    description: "Get current weather data for a location by coordinates",
    inputSchema: {
      type: "object",
      properties: {
        lat: { type: "number", description: "Latitude of the location" },
        lon: { type: "number", description: "Longitude of the location" },
        units: { type: "string", enum: ["standard", "metric", "imperial"], default: "standard", description: "Units of measurement" },
        lang: { type: "string", default: "en", description: "Language for the response description" },
      },
      required: ["lat", "lon"],
    },
  },
  {
    name: "get_current_weather_by_city_id",
    description: "Get current weather data for a city by its ID",
    inputSchema: {
      type: "object",
      properties: {
        city_id: { type: "number", description: "City ID (see OpenWeatherMap city list)" },
        units: { type: "string", enum: ["standard", "metric", "imperial"], default: "standard", description: "Units of measurement" },
      },
      required: ["city_id"],
    },
  },
  {
    name: "get_current_weather_by_zip",
    description: "Get current weather data for a zip/postal code",
    inputSchema: {
      type: "object",
      properties: {
        zip_code: { type: "string", description: "Zip/postal code (e.g., '10001')" },
        country_code: { type: "string", default: "us", description: "2-digit country code (e.g., 'us', 'gb')" },
        units: { type: "string", enum: ["standard", "metric", "imperial"], default: "standard", description: "Units of measurement" },
      },
      required: ["zip_code"],
    },
  },
  {
    name: "get_5_day_forecast_by_city",
    description: "Get 5-day weather forecast for a city by name",
    inputSchema: {
      type: "object",
      properties: {
        city_name: { type: "string", description: "Name of the city (e.g., 'London' or 'London,UK')" },
        units: { type: "string", enum: ["standard", "metric", "imperial"], default: "standard", description: "Units of measurement" },
        lang: { type: "string", default: "en", description: "Language for the response description" },
      },
      required: ["city_name"],
    },
  },
  {
    name: "get_5_day_forecast_by_coords",
    description: "Get 5-day weather forecast for a location by coordinates",
    inputSchema: {
      type: "object",
      properties: {
        lat: { type: "number", description: "Latitude of the location" },
        lon: { type: "number", description: "Longitude of the location" },
        units: { type: "string", enum: ["standard", "metric", "imperial"], default: "standard", description: "Units of measurement" },
        lang: { type: "string", default: "en", description: "Language for the response description" },
      },
      required: ["lat", "lon"],
    },
  },
  {
    name: "get_5_day_forecast_by_city_id",
    description: "Get 5-day weather forecast for a city by its ID",
    inputSchema: {
      type: "object",
      properties: {
        city_id: { type: "number", description: "City ID (see OpenWeatherMap city list)" },
        units: { type: "string", enum: ["standard", "metric", "imperial"], default: "standard", description: "Units of measurement" },
      },
      required: ["city_id"],
    },
  },
  {
    name: "get_5_day_forecast_by_zip",
    description: "Get 5-day weather forecast for a zip/postal code",
    inputSchema: {
      type: "object",
      properties: {
        zip_code: { type: "string", description: "Zip/postal code (e.g., '10001')" },
        country_code: { type: "string", default: "us", description: "2-digit country code (e.g., 'us', 'gb')" },
        units: { type: "string", enum: ["standard", "metric", "imperial"], default: "standard", description: "Units of measurement" },
      },
      required: ["zip_code"],
    },
  },
  {
    name: "get_air_pollution_by_coords",
    description: "Get air pollution data for a location by coordinates",
    inputSchema: {
      type: "object",
      properties: {
        lat: { type: "number", description: "Latitude of the location" },
        lon: { type: "number", description: "Longitude of the location" },
      },
      required: ["lat", "lon"],
    },
  },
  {
    name: "get_air_pollution_by_city",
    description: "Get air pollution data for a city by name",
    inputSchema: {
      type: "object",
      properties: {
        city_name: { type: "string", description: "Name of the city (e.g., 'London' or 'London,UK')" },
      },
      required: ["city_name"],
    },
  },
  {
    name: "get_air_pollution_history",
    description: "Get historical air pollution data for a location",
    inputSchema: {
      type: "object",
      properties: {
        lat: { type: "number", description: "Latitude of the location" },
        lon: { type: "number", description: "Longitude of the location" },
        start: { type: "number", description: "Start timestamp (Unix time)" },
        end: { type: "number", description: "End timestamp (Unix time)" },
      },
      required: ["lat", "lon", "start", "end"],
    },
  },
  {
    name: "geocode_city_name",
    description: "Get geographic coordinates for a city name (geocoding)",
    inputSchema: {
      type: "object",
      properties: {
        city_name: { type: "string", description: "Name of the city (e.g., 'London' or 'London,UK')" },
      },
      required: ["city_name"],
    },
  },
  {
    name: "reverse_geocode",
    description: "Get city name and other info for geographic coordinates (reverse geocoding)",
    inputSchema: {
      type: "object",
      properties: {
        lat: { type: "number", description: "Latitude of the location" },
        lon: { type: "number", description: "Longitude of the location" },
        lang: { type: "string", description: "Language for the response (optional)" },
      },
      required: ["lat", "lon"],
    },
  },
  {
    name: "get_weather_by_city_id_with_details",
    description: "Get detailed weather data for a city by its ID (alternative endpoint)",
    inputSchema: {
      type: "object",
      properties: {
        city_id: { type: "number", description: "City ID (see OpenWeatherMap city list)" },
        units: { type: "string", enum: ["standard", "metric", "imperial"], default: "standard", description: "Units of measurement" },
        lang: { type: "string", default: "en", description: "Language for the response description" },
      },
      required: ["city_id"],
    },
  },
  {
    name: "get_weather_alerts_by_coords",
    description: "Get weather alerts for a location by coordinates",
    inputSchema: {
      type: "object",
      properties: {
        lat: { type: "number", description: "Latitude of the location" },
        lon: { type: "number", description: "Longitude of the location" },
      },
      required: ["lat", "lon"],
    },
  },
  {
    name: "get_weather_alerts_by_city",
    description: "Get weather alerts for a city by name",
    inputSchema: {
      type: "object",
      properties: {
        city_name: { type: "string", description: "Name of the city (e.g., 'London' or 'London,UK')" },
      },
      required: ["city_name"],
    },
  },
];

async function handleCallTool(request: CallToolRequest): Promise<Record<string, unknown>> {
  const { name, arguments: args } = request.params;

  try {
    let result: unknown;

    switch (name) {
      case "get_current_weather_by_city":
        result = await getCurrentWeatherByCity(
          args.city_name as string,
          args.units as "standard" | "metric" | "imperial" || "standard",
          args.lang as string || "en"
        );
        break;
      case "get_current_weather_by_coords":
        result = await getCurrentWeatherByCoords(
          args.lat as number,
          args.lon as number,
          args.units as "standard" | "metric" | "imperial" || "standard",
          args.lang as string || "en"
        );
        break;
      case "get_current_weather_by_city_id":
        result = await getCurrentWeatherByCityId(
          args.city_id as number,
          args.units as "standard" | "metric" | "imperial" || "standard"
        );
        break;
      case "get_current_weather_by_zip":
        result = await getCurrentWeatherByZip(
          args.zip_code as string,
          args.country_code as string || "us",
          args.units as "standard" | "metric" | "imperial" || "standard"
        );
        break;
      case "get_5_day_forecast_by_city":
        result = await get5DayForecastByCity(
          args.city_name as string,
          args.units as "standard" | "metric" | "imperial" || "standard",
          args.lang as string || "en"
        );
        break;
      case "get_5_day_forecast_by_coords":
        result = await get5DayForecastByCoords(
          args.lat as number,
          args.lon as number,
          args.units as "standard" | "metric" | "imperial" || "standard",
          args.lang as string || "en"
        );
        break;
      case "get_5_day_forecast_by_city_id":
        result = await get5DayForecastByCityId(
          args.city_id as number,
          args.units as "standard" | "metric" | "imperial" || "standard"
        );
        break;
      case "get_5_day_forecast_by_zip":
        result = await get5DayForecastByZip(
          args.zip_code as string,
          args.country_code as string || "us",
          args.units as "standard" | "metric" | "imperial" || "standard"
        );
        break;
      case "get_air_pollution_by_coords":
        result = await getAirPollutionByCoords(
          args.lat as number,
          args.lon as number
        );
        break;
      case "get_air_pollution_by_city":
        result = await getAirPollutionByCity(args.city_name as string);
        break;
      case "get_air_pollution_history":
        result = await getAirPollutionHistory(
          args.lat as number,
          args.lon as number,
          args.start as number,
          args.end as number
        );
        break;
      case "geocode_city_name":
        result = await geocodeCityName(args.city_name as string);
        break;
      case "reverse_geocode":
        result = await reverseGeocode(
          args.lat as number,
          args.lon as number,
          args.lang as string
        );
        break;
      case "get_weather_by_city_id_with_details":
        result = await getCurrentWeatherByCityId(
          args.city_id as number,
          args.units as "standard" | "metric" | "imperial" || "standard"
        );
        break;
      case "get_weather_alerts_by_coords":
        result = await getWeatherAlertsByCoords(
          args.lat as number,
          args.lon as number
        );
        break;
      case "get_weather_alerts_by_city":
        result = await getWeatherAlertsByCity(args.city_name as string);
        break;
      default:
        return { error: `Unknown tool: ${name}` };
    }

    return { content: JSON.stringify(result), role: "assistant" };
  } catch (error) {
    return { error: error instanceof Error ? error.message : "An unknown error occurred" };
  }
}

async function handleListTools(): Promise<Record<string, unknown>> {
  return { tools };
}

async function main() {
  const transport = new StdioServerTransport();
  const handler = createRouteHandler({
    listTools: handleListTools,
    callTool: handleCallTool,
  });

  await handler(transport);
}

main().catch((error) => {
  console.error("Server error:", error);
  process.exit(1);
});
