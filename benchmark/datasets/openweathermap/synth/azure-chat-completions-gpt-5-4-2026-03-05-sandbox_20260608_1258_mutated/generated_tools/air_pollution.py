from generated_tools.geocoding import _request


def get_air_pollution_current(latitude: float, longitude: float):
    return _request("/data/2.5/air_pollution", {"lat": latitude, "lon": longitude, "latitude": latitude, "longitude": longitude})


def get_air_pollution_forecast(latitude: float, longitude: float):
    return _request("/data/2.5/air_pollution/forecast", {"lat": latitude, "lon": longitude, "latitude": latitude, "longitude": longitude})


def get_air_pollution_history(latitude: float, longitude: float, start: int, end: int):
    if start >= end:
        return {"error": "start must be less than end"}
    return _request("/data/2.5/air_pollution/history", {"lat": latitude, "lon": longitude, "start": start, "end": end, "latitude": latitude, "longitude": longitude})
