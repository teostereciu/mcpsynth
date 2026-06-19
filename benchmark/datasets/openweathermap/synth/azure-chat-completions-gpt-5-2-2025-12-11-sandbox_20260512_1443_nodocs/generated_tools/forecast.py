from typing import Any, Dict, Optional

from .client import OpenWeatherClient, _clean_none, _coerce_lang, _coerce_units


def get_5day_forecast_by_city(
    client: OpenWeatherClient,
    city_name: str,
    state_code: Optional[str] = None,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
) -> Dict[str, Any]:
    """5 day / 3 hour forecast by city name.

    Endpoint: GET /data/2.5/forecast?q={city},{state},{country}
    """
    q = city_name
    if state_code:
        q += f",{state_code}"
    if country_code:
        q += f",{country_code}"

    params = _clean_none({"q": q, "units": _coerce_units(units), "lang": _coerce_lang(lang), "cnt": cnt})
    return client._request("/data/2.5/forecast", params=params)


def get_5day_forecast_by_coordinates(
    client: OpenWeatherClient,
    lat: float,
    lon: float,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
) -> Dict[str, Any]:
    """5 day / 3 hour forecast by coordinates.

    Endpoint: GET /data/2.5/forecast?lat={lat}&lon={lon}
    """
    params = _clean_none({"lat": lat, "lon": lon, "units": _coerce_units(units), "lang": _coerce_lang(lang), "cnt": cnt})
    return client._request("/data/2.5/forecast", params=params)


def get_5day_forecast_by_city_id(
    client: OpenWeatherClient,
    city_id: int,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
) -> Dict[str, Any]:
    """5 day / 3 hour forecast by city ID.

    Endpoint: GET /data/2.5/forecast?id={id}
    """
    params = _clean_none({"id": city_id, "units": _coerce_units(units), "lang": _coerce_lang(lang), "cnt": cnt})
    return client._request("/data/2.5/forecast", params=params)


def get_5day_forecast_by_zip(
    client: OpenWeatherClient,
    zip_code: str,
    country_code: Optional[str] = None,
    units: Optional[str] = None,
    lang: Optional[str] = None,
    cnt: Optional[int] = None,
) -> Dict[str, Any]:
    """5 day / 3 hour forecast by ZIP/postal code.

    Endpoint: GET /data/2.5/forecast?zip={zip},{country}
    """
    z = zip_code
    if country_code:
        z += f",{country_code}"
    params = _clean_none({"zip": z, "units": _coerce_units(units), "lang": _coerce_lang(lang), "cnt": cnt})
    return client._request("/data/2.5/forecast", params=params)
