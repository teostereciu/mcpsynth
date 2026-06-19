from typing import Any, Dict, Optional

from .client import AlphaVantageClient


def sma(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    month: Optional[str] = None,
    datatype: str = "json",
    entitlement: Optional[str] = None,
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Simple moving average.

    function=SMA
    """
    c = client or AlphaVantageClient()
    params: Dict[str, Any] = {
        "function": "SMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": str(time_period),
        "series_type": series_type,
        "datatype": datatype,
    }
    if month:
        params["month"] = month
    if entitlement:
        params["entitlement"] = entitlement
    return c.request(params)


def ema(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    month: Optional[str] = None,
    datatype: str = "json",
    entitlement: Optional[str] = None,
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Exponential moving average.

    function=EMA
    """
    c = client or AlphaVantageClient()
    params: Dict[str, Any] = {
        "function": "EMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": str(time_period),
        "series_type": series_type,
        "datatype": datatype,
    }
    if month:
        params["month"] = month
    if entitlement:
        params["entitlement"] = entitlement
    return c.request(params)


def rsi(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    month: Optional[str] = None,
    datatype: str = "json",
    entitlement: Optional[str] = None,
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Relative strength index.

    function=RSI
    """
    c = client or AlphaVantageClient()
    params: Dict[str, Any] = {
        "function": "RSI",
        "symbol": symbol,
        "interval": interval,
        "time_period": str(time_period),
        "series_type": series_type,
        "datatype": datatype,
    }
    if month:
        params["month"] = month
    if entitlement:
        params["entitlement"] = entitlement
    return c.request(params)


def macd(
    symbol: str,
    interval: str,
    series_type: str,
    fastperiod: int = 12,
    slowperiod: int = 26,
    signalperiod: int = 9,
    month: Optional[str] = None,
    datatype: str = "json",
    entitlement: Optional[str] = None,
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Moving average convergence/divergence.

    function=MACD
    """
    c = client or AlphaVantageClient()
    params: Dict[str, Any] = {
        "function": "MACD",
        "symbol": symbol,
        "interval": interval,
        "series_type": series_type,
        "fastperiod": str(fastperiod),
        "slowperiod": str(slowperiod),
        "signalperiod": str(signalperiod),
        "datatype": datatype,
    }
    if month:
        params["month"] = month
    if entitlement:
        params["entitlement"] = entitlement
    return c.request(params)


def bbands(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    nbdevup: int = 2,
    nbdevdn: int = 2,
    matype: int = 0,
    month: Optional[str] = None,
    datatype: str = "json",
    entitlement: Optional[str] = None,
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Bollinger Bands.

    function=BBANDS
    """
    c = client or AlphaVantageClient()
    params: Dict[str, Any] = {
        "function": "BBANDS",
        "symbol": symbol,
        "interval": interval,
        "time_period": str(time_period),
        "series_type": series_type,
        "nbdevup": str(nbdevup),
        "nbdevdn": str(nbdevdn),
        "matype": str(matype),
        "datatype": datatype,
    }
    if month:
        params["month"] = month
    if entitlement:
        params["entitlement"] = entitlement
    return c.request(params)
