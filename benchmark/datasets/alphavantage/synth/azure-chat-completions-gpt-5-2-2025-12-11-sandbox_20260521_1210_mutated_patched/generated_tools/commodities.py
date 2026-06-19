from typing import Any, Dict, Optional

from .client import av_get


def gold_silver_spot(ticker: str) -> Dict[str, Any]:
    return av_get({"function": "GOLD_SILVER_SPOT", "symbol": ticker})


def gold_silver_history(ticker: str, time_interval: str) -> Dict[str, Any]:
    return av_get({"function": "GOLD_SILVER_HISTORY", "symbol": ticker, "interval": time_interval})


def wti(time_interval: Optional[str] = None, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "WTI"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return av_get(params)


def brent(time_interval: Optional[str] = None, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "BRENT"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return av_get(params)


def natural_gas(time_interval: Optional[str] = None, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "NATURAL_GAS"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return av_get(params)


def copper(time_interval: Optional[str] = None, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "COPPER"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return av_get(params)


def aluminum(time_interval: Optional[str] = None, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "ALUMINUM"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return av_get(params)


def wheat(time_interval: Optional[str] = None, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "WHEAT"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return av_get(params)


def corn(time_interval: Optional[str] = None, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "CORN"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return av_get(params)


def cotton(time_interval: Optional[str] = None, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "COTTON"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return av_get(params)


def sugar(time_interval: Optional[str] = None, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "SUGAR"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return av_get(params)


def coffee(time_interval: Optional[str] = None, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "COFFEE"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return av_get(params)


def all_commodities(time_interval: Optional[str] = None, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "ALL_COMMODITIES"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return av_get(params)
