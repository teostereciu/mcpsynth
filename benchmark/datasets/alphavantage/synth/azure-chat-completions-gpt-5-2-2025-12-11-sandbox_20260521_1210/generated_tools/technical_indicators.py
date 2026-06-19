from typing import Any, Dict, Optional

from .client import call_alpha_vantage


def sma(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    month: Optional[str] = None,
    datatype: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "SMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    }
    if month is not None:
        params["month"] = month
    if datatype is not None:
        params["datatype"] = datatype
    if entitlement is not None:
        params["entitlement"] = entitlement
    return call_alpha_vantage(params)


def ema(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    month: Optional[str] = None,
    datatype: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "EMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    }
    if month is not None:
        params["month"] = month
    if datatype is not None:
        params["datatype"] = datatype
    if entitlement is not None:
        params["entitlement"] = entitlement
    return call_alpha_vantage(params)


def rsi(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    month: Optional[str] = None,
    datatype: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "RSI",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    }
    if month is not None:
        params["month"] = month
    if datatype is not None:
        params["datatype"] = datatype
    if entitlement is not None:
        params["entitlement"] = entitlement
    return call_alpha_vantage(params)


def macd(
    symbol: str,
    interval: str,
    series_type: str,
    fastperiod: Optional[int] = None,
    slowperiod: Optional[int] = None,
    signalperiod: Optional[int] = None,
    month: Optional[str] = None,
    datatype: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "MACD",
        "symbol": symbol,
        "interval": interval,
        "series_type": series_type,
    }
    if fastperiod is not None:
        params["fastperiod"] = fastperiod
    if slowperiod is not None:
        params["slowperiod"] = slowperiod
    if signalperiod is not None:
        params["signalperiod"] = signalperiod
    if month is not None:
        params["month"] = month
    if datatype is not None:
        params["datatype"] = datatype
    if entitlement is not None:
        params["entitlement"] = entitlement
    return call_alpha_vantage(params)


def bbands(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    nbdevup: Optional[int] = None,
    nbdevdn: Optional[int] = None,
    matype: Optional[int] = None,
    month: Optional[str] = None,
    datatype: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "BBANDS",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    }
    if nbdevup is not None:
        params["nbdevup"] = nbdevup
    if nbdevdn is not None:
        params["nbdevdn"] = nbdevdn
    if matype is not None:
        params["matype"] = matype
    if month is not None:
        params["month"] = month
    if datatype is not None:
        params["datatype"] = datatype
    if entitlement is not None:
        params["entitlement"] = entitlement
    return call_alpha_vantage(params)
