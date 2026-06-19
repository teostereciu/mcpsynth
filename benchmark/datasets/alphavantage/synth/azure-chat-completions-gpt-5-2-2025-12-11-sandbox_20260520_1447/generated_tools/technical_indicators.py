from typing import Any, Dict, Optional, Union

from .client import av_get


def sma(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    month: Optional[str] = None,
    datatype: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Union[Dict[str, Any], str]:
    """SMA.

    Doc: docs/api_technical_indicators.md
    Endpoint: GET /query?function=SMA
    """
    params: Dict[str, Any] = {
        "function": "SMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    }
    if month:
        params["month"] = month
    if datatype:
        params["datatype"] = datatype
    if entitlement:
        params["entitlement"] = entitlement
    return av_get(params)


def ema(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    month: Optional[str] = None,
    datatype: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Union[Dict[str, Any], str]:
    """EMA.

    Doc: docs/api_technical_indicators.md
    Endpoint: GET /query?function=EMA
    """
    params: Dict[str, Any] = {
        "function": "EMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    }
    if month:
        params["month"] = month
    if datatype:
        params["datatype"] = datatype
    if entitlement:
        params["entitlement"] = entitlement
    return av_get(params)


def rsi(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    month: Optional[str] = None,
    datatype: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Union[Dict[str, Any], str]:
    """RSI.

    Doc: docs/api_technical_indicators.md
    Endpoint: GET /query?function=RSI
    """
    params: Dict[str, Any] = {
        "function": "RSI",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    }
    if month:
        params["month"] = month
    if datatype:
        params["datatype"] = datatype
    if entitlement:
        params["entitlement"] = entitlement
    return av_get(params)


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
) -> Union[Dict[str, Any], str]:
    """MACD.

    Doc: docs/api_technical_indicators.md
    Endpoint: GET /query?function=MACD
    """
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
    if month:
        params["month"] = month
    if datatype:
        params["datatype"] = datatype
    if entitlement:
        params["entitlement"] = entitlement
    return av_get(params)


def bollinger_bands(
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
) -> Union[Dict[str, Any], str]:
    """BBANDS (Bollinger Bands).

    Doc: docs/api_technical_indicators.md
    Endpoint: GET /query?function=BBANDS
    """
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
    if month:
        params["month"] = month
    if datatype:
        params["datatype"] = datatype
    if entitlement:
        params["entitlement"] = entitlement
    return av_get(params)
