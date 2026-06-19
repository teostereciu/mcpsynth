from typing import Any, Dict, Optional

from .client import (
    AlphaVantageClient,
    normalize_interval,
    normalize_series_type,
    normalize_ma_type,
    safe_validate,
)


def sma(
    symbol: str,
    interval: str,
    time_period: int = 20,
    series_type: str = "close",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    _, err = safe_validate(normalize_interval, interval)
    if err:
        return {"error": err}
    _, err = safe_validate(normalize_series_type, series_type)
    if err:
        return {"error": err}
    return c.request("SMA", symbol=symbol, interval=interval, time_period=time_period, series_type=series_type)


def ema(symbol: str, interval: str, time_period: int = 20, series_type: str = "close", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    _, err = safe_validate(normalize_interval, interval)
    if err:
        return {"error": err}
    _, err = safe_validate(normalize_series_type, series_type)
    if err:
        return {"error": err}
    return c.request("EMA", symbol=symbol, interval=interval, time_period=time_period, series_type=series_type)


def rsi(symbol: str, interval: str, time_period: int = 14, series_type: str = "close", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    _, err = safe_validate(normalize_interval, interval)
    if err:
        return {"error": err}
    _, err = safe_validate(normalize_series_type, series_type)
    if err:
        return {"error": err}
    return c.request("RSI", symbol=symbol, interval=interval, time_period=time_period, series_type=series_type)


def macd(
    symbol: str,
    interval: str,
    series_type: str = "close",
    fastperiod: int = 12,
    slowperiod: int = 26,
    signalperiod: int = 9,
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    _, err = safe_validate(normalize_interval, interval)
    if err:
        return {"error": err}
    _, err = safe_validate(normalize_series_type, series_type)
    if err:
        return {"error": err}
    return c.request(
        "MACD",
        symbol=symbol,
        interval=interval,
        series_type=series_type,
        fastperiod=fastperiod,
        slowperiod=slowperiod,
        signalperiod=signalperiod,
    )


def bbands(
    symbol: str,
    interval: str,
    time_period: int = 20,
    series_type: str = "close",
    nbdevup: int = 2,
    nbdevdn: int = 2,
    matype: int = 0,
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    _, err = safe_validate(normalize_interval, interval)
    if err:
        return {"error": err}
    _, err = safe_validate(normalize_series_type, series_type)
    if err:
        return {"error": err}
    _, err = safe_validate(normalize_ma_type, matype)
    if err:
        return {"error": err}
    return c.request(
        "BBANDS",
        symbol=symbol,
        interval=interval,
        time_period=time_period,
        series_type=series_type,
        nbdevup=nbdevup,
        nbdevdn=nbdevdn,
        matype=matype,
    )
