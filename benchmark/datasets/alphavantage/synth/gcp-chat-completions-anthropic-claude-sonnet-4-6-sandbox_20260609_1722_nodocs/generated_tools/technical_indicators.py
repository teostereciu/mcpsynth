"""
Alpha Vantage – Technical Indicators tools
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
        if "Note" in data:
            return {"error": "API rate limit reached", "note": data["Note"]}
        if "Information" in data:
            return {"error": "API limit / info", "information": data["Information"]}
        return data
    except requests.RequestException as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# SMA – Simple Moving Average
# ---------------------------------------------------------------------------

def get_sma(
    symbol: str,
    interval: str = "daily",
    time_period: int = 20,
    series_type: str = "close",
) -> dict:
    """
    Return Simple Moving Average (SMA) values for *symbol*.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: Time interval: 1min | 5min | 15min | 30min | 60min | daily | weekly | monthly.
    :param time_period: Number of data points used to calculate each SMA value.
    :param series_type: Price type: close | open | high | low.
    """
    return _get({
        "function": "SMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    })


# ---------------------------------------------------------------------------
# EMA – Exponential Moving Average
# ---------------------------------------------------------------------------

def get_ema(
    symbol: str,
    interval: str = "daily",
    time_period: int = 20,
    series_type: str = "close",
) -> dict:
    """
    Return Exponential Moving Average (EMA) values for *symbol*.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: Time interval: 1min | 5min | 15min | 30min | 60min | daily | weekly | monthly.
    :param time_period: Number of data points used to calculate each EMA value.
    :param series_type: Price type: close | open | high | low.
    """
    return _get({
        "function": "EMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    })


# ---------------------------------------------------------------------------
# RSI – Relative Strength Index
# ---------------------------------------------------------------------------

def get_rsi(
    symbol: str,
    interval: str = "daily",
    time_period: int = 14,
    series_type: str = "close",
) -> dict:
    """
    Return Relative Strength Index (RSI) values for *symbol*.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: Time interval: 1min | 5min | 15min | 30min | 60min | daily | weekly | monthly.
    :param time_period: Number of data points used to calculate each RSI value (typically 14).
    :param series_type: Price type: close | open | high | low.
    """
    return _get({
        "function": "RSI",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    })


# ---------------------------------------------------------------------------
# MACD – Moving Average Convergence/Divergence
# ---------------------------------------------------------------------------

def get_macd(
    symbol: str,
    interval: str = "daily",
    series_type: str = "close",
    fastperiod: int = 12,
    slowperiod: int = 26,
    signalperiod: int = 9,
) -> dict:
    """
    Return MACD values (MACD line, signal line, histogram) for *symbol*.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: Time interval: 1min | 5min | 15min | 30min | 60min | daily | weekly | monthly.
    :param series_type: Price type: close | open | high | low.
    :param fastperiod: Fast EMA period (default 12).
    :param slowperiod: Slow EMA period (default 26).
    :param signalperiod: Signal EMA period (default 9).
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


# ---------------------------------------------------------------------------
# BBANDS – Bollinger Bands
# ---------------------------------------------------------------------------

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
    Return Bollinger Bands (upper, middle, lower) for *symbol*.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: Time interval: 1min | 5min | 15min | 30min | 60min | daily | weekly | monthly.
    :param time_period: Number of data points used to calculate each band value.
    :param series_type: Price type: close | open | high | low.
    :param nbdevup: Standard deviation multiplier for the upper band.
    :param nbdevdn: Standard deviation multiplier for the lower band.
    :param matype: Moving average type (0=SMA, 1=EMA, 2=WMA, 3=DEMA, 4=TEMA, …).
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


# ---------------------------------------------------------------------------
# VWAP – Volume Weighted Average Price
# ---------------------------------------------------------------------------

def get_vwap(symbol: str, interval: str = "5min") -> dict:
    """
    Return Volume Weighted Average Price (VWAP) for *symbol*.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: Intraday interval: 1min | 5min | 15min | 30min | 60min.
    """
    return _get({
        "function": "VWAP",
        "symbol": symbol,
        "interval": interval,
    })


# ---------------------------------------------------------------------------
# STOCH – Stochastic Oscillator
# ---------------------------------------------------------------------------

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
    Return Stochastic Oscillator (SlowK, SlowD) for *symbol*.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: Time interval: 1min | 5min | 15min | 30min | 60min | daily | weekly | monthly.
    :param fastkperiod: Fast %K period.
    :param slowkperiod: Slow %K period.
    :param slowdperiod: Slow %D period.
    :param slowkmatype: Moving average type for Slow %K.
    :param slowdmatype: Moving average type for Slow %D.
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


# ---------------------------------------------------------------------------
# ADX – Average Directional Movement Index
# ---------------------------------------------------------------------------

def get_adx(
    symbol: str,
    interval: str = "daily",
    time_period: int = 14,
) -> dict:
    """
    Return Average Directional Movement Index (ADX) for *symbol*.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: Time interval: 1min | 5min | 15min | 30min | 60min | daily | weekly | monthly.
    :param time_period: Number of data points used to calculate each ADX value.
    """
    return _get({
        "function": "ADX",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
    })


# ---------------------------------------------------------------------------
# CCI – Commodity Channel Index
# ---------------------------------------------------------------------------

def get_cci(
    symbol: str,
    interval: str = "daily",
    time_period: int = 20,
) -> dict:
    """
    Return Commodity Channel Index (CCI) for *symbol*.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: Time interval: 1min | 5min | 15min | 30min | 60min | daily | weekly | monthly.
    :param time_period: Number of data points used to calculate each CCI value.
    """
    return _get({
        "function": "CCI",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
    })


# ---------------------------------------------------------------------------
# AROON – Aroon Indicator
# ---------------------------------------------------------------------------

def get_aroon(
    symbol: str,
    interval: str = "daily",
    time_period: int = 14,
) -> dict:
    """
    Return Aroon (Aroon Up, Aroon Down) indicator for *symbol*.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: Time interval: 1min | 5min | 15min | 30min | 60min | daily | weekly | monthly.
    :param time_period: Number of data points used to calculate each Aroon value.
    """
    return _get({
        "function": "AROON",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
    })
