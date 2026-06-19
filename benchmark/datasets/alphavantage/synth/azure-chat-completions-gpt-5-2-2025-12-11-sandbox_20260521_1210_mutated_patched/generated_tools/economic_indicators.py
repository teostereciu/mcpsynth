from typing import Any, Dict, Optional

from .client import av_get


def real_gdp(time_interval: Optional[str] = None, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "REAL_GDP"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return av_get(params)


def real_gdp_per_capita(format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "REAL_GDP_PER_CAPITA"}
    if format:
        params["datatype"] = format
    return av_get(params)


def treasury_yield(
    time_interval: Optional[str] = None,
    maturity: Optional[str] = None,
    format: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "TREASURY_YIELD"}
    if time_interval:
        params["interval"] = time_interval
    if maturity:
        params["maturity"] = maturity
    if format:
        params["datatype"] = format
    return av_get(params)


def federal_funds_rate(time_interval: Optional[str] = None, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "FEDERAL_FUNDS_RATE"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return av_get(params)


def cpi(format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "CPI"}
    if format:
        params["datatype"] = format
    return av_get(params)


def inflation(format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "INFLATION"}
    if format:
        params["datatype"] = format
    return av_get(params)


def unemployment(format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "UNEMPLOYMENT"}
    if format:
        params["datatype"] = format
    return av_get(params)
