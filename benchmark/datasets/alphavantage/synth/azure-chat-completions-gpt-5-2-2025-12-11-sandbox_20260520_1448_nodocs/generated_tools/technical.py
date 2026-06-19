from typing import Any, Dict, Optional

from .client import call_alpha_vantage


def sma(symbol: str, interval: str, time_period: int, series_type: str,
        month: Optional[str] = None, outputsize: str = "compact", datatype: str = "json") -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "SMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
        "outputsize": outputsize,
        "datatype": datatype,
    }
    if month:
        params["month"] = month
    return call_alpha_vantage(params)


def ema(symbol: str, interval: str, time_period: int, series_type: str,
        month: Optional[str] = None, outputsize: str = "compact", datatype: str = "json") -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "EMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
        "outputsize": outputsize,
        "datatype": datatype,
    }
    if month:
        params["month"] = month
    return call_alpha_vantage(params)


def rsi(symbol: str, interval: str, time_period: int, series_type: str,
        month: Optional[str] = None, outputsize: str = "compact", datatype: str = "json") -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "RSI",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
        "outputsize": outputsize,
        "datatype": datatype,
    }
    if month:
        params["month"] = month
    return call_alpha_vantage(params)


def macd(symbol: str, interval: str, series_type: str,
         fastperiod: int = 12, slowperiod: int = 26, signalperiod: int = 9,
         month: Optional[str] = None, outputsize: str = "compact", datatype: str = "json") -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "MACD",
        "symbol": symbol,
        "interval": interval,
        "series_type": series_type,
        "fastperiod": fastperiod,
        "slowperiod": slowperiod,
        "signalperiod": signalperiod,
        "outputsize": outputsize,
        "datatype": datatype,
    }
    if month:
        params["month"] = month
    return call_alpha_vantage(params)


def bbands(symbol: str, interval: str, time_period: int, series_type: str,
           nbdevup: int = 2, nbdevdn: int = 2, matype: int = 0,
           month: Optional[str] = None, outputsize: str = "compact", datatype: str = "json") -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "BBANDS",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
        "nbdevup": nbdevup,
        "nbdevdn": nbdevdn,
        "matype": matype,
        "outputsize": outputsize,
        "datatype": datatype,
    }
    if month:
        params["month"] = month
    return call_alpha_vantage(params)
