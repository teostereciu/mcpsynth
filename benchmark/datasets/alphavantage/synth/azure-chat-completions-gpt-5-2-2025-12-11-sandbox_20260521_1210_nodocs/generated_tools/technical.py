from typing import Any, Dict, Optional

from .client import av_get


def sma(symbol: str, interval: str, time_period: int, series_type: str,
        adjusted: bool = True, month: Optional[str] = None, datatype: str = "json") -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "SMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
        "adjusted": "true" if adjusted else "false",
        "datatype": datatype,
    }
    if month:
        params["month"] = month
    return av_get(params)


def ema(symbol: str, interval: str, time_period: int, series_type: str,
        adjusted: bool = True, month: Optional[str] = None, datatype: str = "json") -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "EMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
        "adjusted": "true" if adjusted else "false",
        "datatype": datatype,
    }
    if month:
        params["month"] = month
    return av_get(params)


def rsi(symbol: str, interval: str, time_period: int,
        adjusted: bool = True, month: Optional[str] = None, datatype: str = "json") -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "RSI",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": "close",
        "adjusted": "true" if adjusted else "false",
        "datatype": datatype,
    }
    if month:
        params["month"] = month
    return av_get(params)


def macd(symbol: str, interval: str, series_type: str = "close",
         fastperiod: int = 12, slowperiod: int = 26, signalperiod: int = 9,
         adjusted: bool = True, month: Optional[str] = None, datatype: str = "json") -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "MACD",
        "symbol": symbol,
        "interval": interval,
        "series_type": series_type,
        "fastperiod": fastperiod,
        "slowperiod": slowperiod,
        "signalperiod": signalperiod,
        "adjusted": "true" if adjusted else "false",
        "datatype": datatype,
    }
    if month:
        params["month"] = month
    return av_get(params)


def bbands(symbol: str, interval: str, time_period: int, series_type: str,
           nbdevup: int = 2, nbdevdn: int = 2, matype: int = 0,
           adjusted: bool = True, month: Optional[str] = None, datatype: str = "json") -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "BBANDS",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
        "nbdevup": nbdevup,
        "nbdevdn": nbdevdn,
        "matype": matype,
        "adjusted": "true" if adjusted else "false",
        "datatype": datatype,
    }
    if month:
        params["month"] = month
    return av_get(params)
