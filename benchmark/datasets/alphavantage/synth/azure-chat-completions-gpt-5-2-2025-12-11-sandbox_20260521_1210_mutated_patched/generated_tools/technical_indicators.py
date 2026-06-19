from typing import Any, Dict, Optional

from .client import av_get


def sma(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
    format: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "SMA",
        "symbol": ticker,
        "interval": time_interval,
        "time_period": time_period,
        "series_type": price_type,
    }
    if month:
        params["month"] = month
    if format:
        params["datatype"] = format
    if entitlement:
        params["entitlement"] = entitlement
    return av_get(params)


def ema(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
    format: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "EMA",
        "symbol": ticker,
        "interval": time_interval,
        "time_period": time_period,
        "series_type": price_type,
    }
    if month:
        params["month"] = month
    if format:
        params["datatype"] = format
    if entitlement:
        params["entitlement"] = entitlement
    return av_get(params)


def rsi(
    ticker: str,
    time_interval: str,
    time_period: int,
    month: Optional[str] = None,
    format: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "RSI",
        "symbol": ticker,
        "interval": time_interval,
        "time_period": time_period,
    }
    if month:
        params["month"] = month
    if format:
        params["datatype"] = format
    if entitlement:
        params["entitlement"] = entitlement
    return av_get(params)


def macd(
    ticker: str,
    time_interval: str,
    series_type: str,
    month: Optional[str] = None,
    fastperiod: Optional[int] = None,
    slowperiod: Optional[int] = None,
    signalperiod: Optional[int] = None,
    format: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "MACD",
        "symbol": ticker,
        "interval": time_interval,
        "series_type": series_type,
    }
    if month:
        params["month"] = month
    if fastperiod is not None:
        params["fastperiod"] = fastperiod
    if slowperiod is not None:
        params["slowperiod"] = slowperiod
    if signalperiod is not None:
        params["signalperiod"] = signalperiod
    if format:
        params["datatype"] = format
    if entitlement:
        params["entitlement"] = entitlement
    return av_get(params)


def bollinger_bands(
    ticker: str,
    time_interval: str,
    time_period: int,
    series_type: str,
    nbdevup: Optional[int] = None,
    nbdevdn: Optional[int] = None,
    matype: Optional[int] = None,
    month: Optional[str] = None,
    format: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "BBANDS",
        "symbol": ticker,
        "interval": time_interval,
        "time_period": time_period,
        "series_type": series_type,
    }
    if nbdevup is not None:
        params["nbdevup"] = nbdevup
    if nbdevdn is not None:
        params["nbdevdn"] = nbdevdn
    if matype is not None:
        params["matype"] = matype
    if month:
        params["month"] = month
    if format:
        params["datatype"] = format
    if entitlement:
        params["entitlement"] = entitlement
    return av_get(params)
