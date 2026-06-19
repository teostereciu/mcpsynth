"""
Alpha Vantage — Stock Time Series tools
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
        if "Information" in data:
            return {"error": data["Information"]}
        if "Note" in data:
            return {"error": data["Note"]}
        return data
    except requests.exceptions.RequestException as exc:
        return {"error": str(exc)}
    except ValueError as exc:
        return {"error": f"JSON decode error: {exc}"}


def get_intraday(symbol: str, interval: str = "5min", outputsize: str = "compact") -> dict:
    """
    Fetch intraday OHLCV time series for a given equity symbol.

    Args:
        symbol:     Ticker symbol (e.g. 'IBM', 'AAPL').
        interval:   Time interval between data points.
                    Allowed values: '1min', '5min', '15min', '30min', '60min'.
        outputsize: 'compact' returns the latest 100 data points;
                    'full' returns up to 20 years of historical data.

    Returns:
        Dict containing time series metadata and OHLCV data points.
    """
    return _get({
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "outputsize": outputsize,
    })


def get_daily(symbol: str, outputsize: str = "compact") -> dict:
    """
    Fetch daily OHLCV time series for a given equity symbol.

    Args:
        symbol:     Ticker symbol (e.g. 'IBM').
        outputsize: 'compact' returns the latest 100 trading days;
                    'full' returns up to 20 years of data.

    Returns:
        Dict containing daily time series metadata and OHLCV data points.
    """
    return _get({
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": outputsize,
    })


def get_daily_adjusted(symbol: str, outputsize: str = "compact") -> dict:
    """
    Fetch daily adjusted OHLCV time series (includes split/dividend adjustments).

    Args:
        symbol:     Ticker symbol (e.g. 'IBM').
        outputsize: 'compact' returns the latest 100 trading days;
                    'full' returns up to 20 years of data.

    Returns:
        Dict containing daily adjusted time series with split coefficient and
        dividend amount columns.
    """
    return _get({
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": symbol,
        "outputsize": outputsize,
    })


def get_weekly(symbol: str) -> dict:
    """
    Fetch weekly OHLCV time series for a given equity symbol.

    Args:
        symbol: Ticker symbol (e.g. 'IBM').

    Returns:
        Dict containing weekly time series metadata and OHLCV data points,
        covering 20+ years of historical data.
    """
    return _get({
        "function": "TIME_SERIES_WEEKLY",
        "symbol": symbol,
    })


def get_weekly_adjusted(symbol: str) -> dict:
    """
    Fetch weekly adjusted OHLCV time series (includes split/dividend adjustments).

    Args:
        symbol: Ticker symbol (e.g. 'IBM').

    Returns:
        Dict containing weekly adjusted time series with dividend amount column.
    """
    return _get({
        "function": "TIME_SERIES_WEEKLY_ADJUSTED",
        "symbol": symbol,
    })


def get_monthly(symbol: str) -> dict:
    """
    Fetch monthly OHLCV time series for a given equity symbol.

    Args:
        symbol: Ticker symbol (e.g. 'IBM').

    Returns:
        Dict containing monthly time series metadata and OHLCV data points.
    """
    return _get({
        "function": "TIME_SERIES_MONTHLY",
        "symbol": symbol,
    })


def get_monthly_adjusted(symbol: str) -> dict:
    """
    Fetch monthly adjusted OHLCV time series (includes split/dividend adjustments).

    Args:
        symbol: Ticker symbol (e.g. 'IBM').

    Returns:
        Dict containing monthly adjusted time series with dividend amount column.
    """
    return _get({
        "function": "TIME_SERIES_MONTHLY_ADJUSTED",
        "symbol": symbol,
    })


def get_global_quote(symbol: str) -> dict:
    """
    Fetch the latest price and volume information for a given equity symbol.

    Args:
        symbol: Ticker symbol (e.g. 'IBM').

    Returns:
        Dict with fields: open, high, low, price, volume, latest trading day,
        previous close, change, and change percent.
    """
    return _get({
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
    })


def search_symbol(keywords: str) -> dict:
    """
    Search for equity symbols and company names matching the given keywords.

    Args:
        keywords: Free-text search string (e.g. 'Apple', 'BA', 'Tesla').

    Returns:
        Dict containing a list of best-matching symbols with name, type,
        region, currency, and match score.
    """
    return _get({
        "function": "SYMBOL_SEARCH",
        "keywords": keywords,
    })
