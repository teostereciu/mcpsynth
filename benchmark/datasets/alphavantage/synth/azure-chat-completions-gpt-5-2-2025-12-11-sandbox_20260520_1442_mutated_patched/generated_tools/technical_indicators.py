from typing import Any, Dict, Optional

from .alphavantage_client import call_alpha_vantage


def sma(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
    format: Optional[str] = "json",
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    """SMA.

    Doc: docs/api_technical_indicators.md
    """
    params: Dict[str, Any] = {
        "function": "SMA",
        "symbol": ticker,
        "interval": time_interval,
        "time_period": str(time_period),
        "series_type": price_type,
    }
    if month:
        params["month"] = month
    if format:
        params["datatype"] = format
    if entitlement:
        params["entitlement"] = entitlement
    return call_alpha_vantage(params)


def ema(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
    format: Optional[str] = "json",
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    """EMA.

    Doc: docs/api_technical_indicators.md
    """
    params: Dict[str, Any] = {
        "function": "EMA",
        "symbol": ticker,
        "interval": time_interval,
        "time_period": str(time_period),
        "series_type": price_type,
    }
    if month:
        params["month"] = month
    if format:
        params["datatype"] = format
    if entitlement:
        params["entitlement"] = entitlement
    return call_alpha_vantage(params)


def rsi(
    ticker: str,
    time_interval: str,
    time_period: int,
    month: Optional[str] = None,
    format: Optional[str] = "json",
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    """RSI.

    Doc: docs/api_technical_indicators.md
    """
    params: Dict[str, Any] = {
        "function": "RSI",
        "symbol": ticker,
        "interval": time_interval,
        "time_period": str(time_period),
    }
    if month:
        params["month"] = month
    if format:
        params["datatype"] = format
    if entitlement:
        params["entitlement"] = entitlement
    return call_alpha_vantage(params)


def macd(
    ticker: str,
    time_interval: str,
    series_type: str = "close",
    fastperiod: int = 12,
    slowperiod: int = 26,
    signalperiod: int = 9,
    month: Optional[str] = None,
    format: Optional[str] = "json",
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    """MACD.

    Doc: docs/api_technical_indicators.md
    """
    params: Dict[str, Any] = {
        "function": "MACD",
        "symbol": ticker,
        "interval": time_interval,
        "series_type": series_type,
        "fastperiod": str(fastperiod),
        "slowperiod": str(slowperiod),
        "signalperiod": str(signalperiod),
    }
    if month:
        params["month"] = month
    if format:
        params["datatype"] = format
    if entitlement:
        params["entitlement"] = entitlement
    return call_alpha_vantage(params)


def bbands(
    ticker: str,
    time_interval: str,
    time_period: int,
    series_type: str = "close",
    nbdevup: int = 2,
    nbdevdn: int = 2,
    matype: int = 0,
    month: Optional[str] = None,
    format: Optional[str] = "json",
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    """BBANDS.

    Doc: docs/api_technical_indicators.md
    """
    params: Dict[str, Any] = {
        "function": "BBANDS",
        "symbol": ticker,
        "interval": time_interval,
        "time_period": str(time_period),
        "series_type": series_type,
        "nbdevup": str(nbdevup),
        "nbdevdn": str(nbdevdn),
        "matype": str(matype),
    }
    if month:
        params["month"] = month
    if format:
        params["datatype"] = format
    if entitlement:
        params["entitlement"] = entitlement
    return call_alpha_vantage(params)
