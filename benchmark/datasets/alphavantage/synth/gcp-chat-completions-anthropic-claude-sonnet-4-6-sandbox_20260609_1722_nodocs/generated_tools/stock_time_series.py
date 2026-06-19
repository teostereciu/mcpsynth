"""
Alpha Vantage – Stock Time Series tools
Covers: intraday, daily, weekly, monthly OHLCV + global quote + symbol search
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
# Intraday
# ---------------------------------------------------------------------------

def get_intraday(
    symbol: str,
    interval: str = "5min",
    outputsize: str = "compact",
    adjusted: bool = True,
    extended_hours: bool = True,
    month: str = "",
) -> dict:
    """
    Return intraday OHLCV time series for *symbol*.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: One of 1min | 5min | 15min | 30min | 60min.
    :param outputsize: "compact" (latest 100 data points) or "full".
    :param adjusted: Whether to return adjusted OHLCV values.
    :param extended_hours: Include pre/post market data.
    :param month: Optional YYYY-MM to fetch a specific month of intraday data.
    """
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "outputsize": outputsize,
        "adjusted": str(adjusted).lower(),
        "extended_hours": str(extended_hours).lower(),
    }
    if month:
        params["month"] = month
    return _get(params)


# ---------------------------------------------------------------------------
# Daily
# ---------------------------------------------------------------------------

def get_daily(
    symbol: str,
    outputsize: str = "compact",
) -> dict:
    """
    Return daily OHLCV time series for *symbol* (unadjusted).

    :param symbol: Ticker symbol, e.g. "IBM".
    :param outputsize: "compact" (latest 100 data points) or "full".
    """
    return _get({
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": outputsize,
    })


def get_daily_adjusted(
    symbol: str,
    outputsize: str = "compact",
) -> dict:
    """
    Return daily adjusted OHLCV time series (includes split/dividend adjustments).

    :param symbol: Ticker symbol, e.g. "IBM".
    :param outputsize: "compact" (latest 100 data points) or "full".
    """
    return _get({
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": symbol,
        "outputsize": outputsize,
    })


# ---------------------------------------------------------------------------
# Weekly
# ---------------------------------------------------------------------------

def get_weekly(symbol: str) -> dict:
    """
    Return weekly OHLCV time series for *symbol* (unadjusted).

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return _get({"function": "TIME_SERIES_WEEKLY", "symbol": symbol})


def get_weekly_adjusted(symbol: str) -> dict:
    """
    Return weekly adjusted OHLCV time series for *symbol*.

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return _get({"function": "TIME_SERIES_WEEKLY_ADJUSTED", "symbol": symbol})


# ---------------------------------------------------------------------------
# Monthly
# ---------------------------------------------------------------------------

def get_monthly(symbol: str) -> dict:
    """
    Return monthly OHLCV time series for *symbol* (unadjusted).

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return _get({"function": "TIME_SERIES_MONTHLY", "symbol": symbol})


def get_monthly_adjusted(symbol: str) -> dict:
    """
    Return monthly adjusted OHLCV time series for *symbol*.

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return _get({"function": "TIME_SERIES_MONTHLY_ADJUSTED", "symbol": symbol})


# ---------------------------------------------------------------------------
# Quote & Search
# ---------------------------------------------------------------------------

def get_global_quote(symbol: str) -> dict:
    """
    Return the latest price, volume, and change data for *symbol*.

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return _get({"function": "GLOBAL_QUOTE", "symbol": symbol})


def search_symbol(keywords: str, datatype: str = "json") -> dict:
    """
    Search for ticker symbols and company names matching *keywords*.

    :param keywords: Search string, e.g. "Microsoft" or "AAPL".
    :param datatype: "json" or "csv".
    """
    return _get({"function": "SYMBOL_SEARCH", "keywords": keywords, "datatype": datatype})
