"""
Alpha Vantage — Technical Indicators tools
Covers: SMA, EMA, RSI, MACD, Bollinger Bands (BBANDS), VWAP, STOCH, ADX, CCI, AROON
"""

import os
import requests

BASE_URL = "https://www.alphavantage.co/query"


def _get(params: dict) -> dict:
    params["apikey"] = os.environ.get("ALPHAVANTAGE_API_KEY", "")
    try:
        resp = requests.get(BASE_URL, params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        if "Error Message" in data:
            return {"error": data["Error Message"]}
        if "Information" in data:
            return {"error": data["Information"]}
        if "Note" in data:
            return {"error": data["Note"]}
        return data
    except requests.exceptions.RequestException as exc:
        return {"error": str(exc)}
    except ValueError as exc:
        return {"error": f"JSON decode error: {exc}"}


def get_sma(
    symbol: str,
    interval: str = "daily",
    time_period: int = 20,
    series_type: str = "close",
) -> dict:
    """
    Fetch Simple Moving Average (SMA) values for a given equity.

    Args:
        symbol:      Ticker symbol (e.g. 'IBM').
        interval:    Time interval. Allowed: '1min','5min','15min','30min','60min',
                     'daily','weekly','monthly'.
        time_period: Number of data points used to calculate each SMA value (e.g. 20).
        series_type: Price type to use. Allowed: 'close','open','high','low'.

    Returns:
        Dict containing SMA values keyed by date/time.
    """
    return _get({
        "function": "SMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    })


def get_ema(
    symbol: str,
    interval: str = "daily",
    time_period: int = 20,
    series_type: str = "close",
) -> dict:
    """
    Fetch Exponential Moving Average (EMA) values for a given equity.

    Args:
        symbol:      Ticker symbol (e.g. 'IBM').
        interval:    Time interval. Allowed: '1min','5min','15min','30min','60min',
                     'daily','weekly','monthly'.
        time_period: Number of data points used to calculate each EMA value (e.g. 20).
        series_type: Price type to use. Allowed: 'close','open','high','low'.

    Returns:
        Dict containing EMA values keyed by date/time.
    """
    return _get({
        "function": "EMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    })


def get_rsi(
    symbol: str,
    interval: str = "daily",
    time_period: int = 14,
    series_type: str = "close",
) -> dict:
    """
    Fetch Relative Strength Index (RSI) values for a given equity.

    Args:
        symbol:      Ticker symbol (e.g. 'IBM').
        interval:    Time interval. Allowed: '1min','5min','15min','30min','60min',
                     'daily','weekly','monthly'.
        time_period: Number of data points used to calculate each RSI value (e.g. 14).
        series_type: Price type to use. Allowed: 'close','open','high','low'.

    Returns:
        Dict containing RSI values keyed by date/time.
    """
    return _get({
        "function": "RSI",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    })


def get_macd(
    symbol: str,
    interval: str = "daily",
    series_type: str = "close",
    fastperiod: int = 12,
    slowperiod: int = 26,
    signalperiod: int = 9,
) -> dict:
    """
    Fetch Moving Average Convergence/Divergence (MACD) values for a given equity.

    Args:
        symbol:       Ticker symbol (e.g. 'IBM').
        interval:     Time interval. Allowed: '1min','5min','15min','30min','60min',
                      'daily','weekly','monthly'.
        series_type:  Price type to use. Allowed: 'close','open','high','low'.
        fastperiod:   Fast EMA period (default 12).
        slowperiod:   Slow EMA period (default 26).
        signalperiod: Signal line period (default 9).

    Returns:
        Dict containing MACD, MACD_Signal, and MACD_Hist values keyed by date/time.
    """
    return _get({
        "function": "MACD",
        "symbol": symbol,
        "interval": interval,
        "series_type": series_type,
        "fastperiod": fastperiod,
        "slowperiod": slowperiod,
        "signalperiod": signalperiod,
    })


def get_bbands(
    symbol: str,
    interval: str = "daily",
    time_period: int = 20,
    series_type: str = "close",
    nbdevup: int = 2,
    nbdevdn: int = 2,
    matype: int = 0,
) -> dict:
    """
    Fetch Bollinger Bands (BBANDS) for a given equity.

    Args:
        symbol:      Ticker symbol (e.g. 'IBM').
        interval:    Time interval. Allowed: '1min','5min','15min','30min','60min',
                     'daily','weekly','monthly'.
        time_period: Number of data points per band calculation (e.g. 20).
        series_type: Price type to use. Allowed: 'close','open','high','low'.
        nbdevup:     Standard deviation multiplier for the upper band (default 2).
        nbdevdn:     Standard deviation multiplier for the lower band (default 2).
        matype:      Moving average type (0=SMA, 1=EMA, 2=WMA, 3=DEMA, 4=TEMA, ...).

    Returns:
        Dict containing Real Upper Band, Real Middle Band, and Real Lower Band
        values keyed by date/time.
    """
    return _get({
        "function": "BBANDS",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
        "nbdevup": nbdevup,
        "nbdevdn": nbdevdn,
        "matype": matype,
    })


def get_vwap(symbol: str, interval: str = "60min") -> dict:
    """
    Fetch Volume Weighted Average Price (VWAP) for a given equity.

    Args:
        symbol:   Ticker symbol (e.g. 'IBM').
        interval: Intraday time interval. Allowed: '1min','5min','15min','30min','60min'.

    Returns:
        Dict containing VWAP values keyed by date/time.
    """
    return _get({
        "function": "VWAP",
        "symbol": symbol,
        "interval": interval,
    })


def get_stoch(
    symbol: str,
    interval: str = "daily",
    fastkperiod: int = 5,
    slowkperiod: int = 3,
    slowdperiod: int = 3,
    slowkmatype: int = 0,
    slowdmatype: int = 0,
) -> dict:
    """
    Fetch Stochastic Oscillator (STOCH) values for a given equity.

    Args:
        symbol:       Ticker symbol (e.g. 'IBM').
        interval:     Time interval. Allowed: '1min','5min','15min','30min','60min',
                      'daily','weekly','monthly'.
        fastkperiod:  Fast %K period (default 5).
        slowkperiod:  Slow %K period (default 3).
        slowdperiod:  Slow %D period (default 3).
        slowkmatype:  MA type for slow %K (0=SMA, 1=EMA, ...).
        slowdmatype:  MA type for slow %D (0=SMA, 1=EMA, ...).

    Returns:
        Dict containing SlowK and SlowD values keyed by date/time.
    """
    return _get({
        "function": "STOCH",
        "symbol": symbol,
        "interval": interval,
        "fastkperiod": fastkperiod,
        "slowkperiod": slowkperiod,
        "slowdperiod": slowdperiod,
        "slowkmatype": slowkmatype,
        "slowdmatype": slowdmatype,
    })


def get_adx(
    symbol: str,
    interval: str = "daily",
    time_period: int = 14,
) -> dict:
    """
    Fetch Average Directional Movement Index (ADX) for a given equity.

    Args:
        symbol:      Ticker symbol (e.g. 'IBM').
        interval:    Time interval. Allowed: '1min','5min','15min','30min','60min',
                     'daily','weekly','monthly'.
        time_period: Number of data points per ADX calculation (default 14).

    Returns:
        Dict containing ADX values keyed by date/time.
    """
    return _get({
        "function": "ADX",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
    })


def get_cci(
    symbol: str,
    interval: str = "daily",
    time_period: int = 20,
) -> dict:
    """
    Fetch Commodity Channel Index (CCI) for a given equity.

    Args:
        symbol:      Ticker symbol (e.g. 'IBM').
        interval:    Time interval. Allowed: '1min','5min','15min','30min','60min',
                     'daily','weekly','monthly'.
        time_period: Number of data points per CCI calculation (default 20).

    Returns:
        Dict containing CCI values keyed by date/time.
    """
    return _get({
        "function": "CCI",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
    })


def get_aroon(
    symbol: str,
    interval: str = "daily",
    time_period: int = 14,
) -> dict:
    """
    Fetch Aroon indicator (Aroon Up and Aroon Down) for a given equity.

    Args:
        symbol:      Ticker symbol (e.g. 'IBM').
        interval:    Time interval. Allowed: '1min','5min','15min','30min','60min',
                     'daily','weekly','monthly'.
        time_period: Number of data points per Aroon calculation (default 14).

    Returns:
        Dict containing Aroon Up and Aroon Down values keyed by date/time.
    """
    return _get({
        "function": "AROON",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
    })
