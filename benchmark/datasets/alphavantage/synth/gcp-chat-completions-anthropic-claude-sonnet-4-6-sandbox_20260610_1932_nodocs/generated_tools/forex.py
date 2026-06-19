"""
Alpha Vantage — Forex (FX) tools
Covers: real-time exchange rate, FX intraday, daily, weekly, monthly time series
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


def get_fx_exchange_rate(from_currency: str, to_currency: str) -> dict:
    """
    Fetch the real-time exchange rate for any pair of digital or physical currencies.

    Args:
        from_currency: The currency to convert from (e.g. 'USD', 'EUR', 'BTC').
        to_currency:   The currency to convert to   (e.g. 'JPY', 'GBP', 'ETH').

    Returns:
        Dict with bid price, ask price, exchange rate, and last refreshed timestamp.
    """
    return _get({
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": from_currency,
        "to_currency": to_currency,
    })


def get_fx_intraday(
    from_symbol: str,
    to_symbol: str,
    interval: str = "5min",
    outputsize: str = "compact",
) -> dict:
    """
    Fetch intraday FX time series for a currency pair.

    Args:
        from_symbol: From currency code (e.g. 'EUR').
        to_symbol:   To currency code   (e.g. 'USD').
        interval:    Time interval between data points.
                     Allowed values: '1min', '5min', '15min', '30min', '60min'.
        outputsize:  'compact' returns the latest 100 data points;
                     'full' returns the full intraday history.

    Returns:
        Dict containing intraday FX OHLC time series.
    """
    return _get({
        "function": "FX_INTRADAY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "interval": interval,
        "outputsize": outputsize,
    })


def get_fx_daily(
    from_symbol: str,
    to_symbol: str,
    outputsize: str = "compact",
) -> dict:
    """
    Fetch daily FX OHLC time series for a currency pair.

    Args:
        from_symbol: From currency code (e.g. 'EUR').
        to_symbol:   To currency code   (e.g. 'USD').
        outputsize:  'compact' returns the latest 100 trading days;
                     'full' returns up to 20 years of data.

    Returns:
        Dict containing daily FX OHLC time series.
    """
    return _get({
        "function": "FX_DAILY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "outputsize": outputsize,
    })


def get_fx_weekly(from_symbol: str, to_symbol: str) -> dict:
    """
    Fetch weekly FX OHLC time series for a currency pair.

    Args:
        from_symbol: From currency code (e.g. 'EUR').
        to_symbol:   To currency code   (e.g. 'USD').

    Returns:
        Dict containing weekly FX OHLC time series covering 20+ years.
    """
    return _get({
        "function": "FX_WEEKLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
    })


def get_fx_monthly(from_symbol: str, to_symbol: str) -> dict:
    """
    Fetch monthly FX OHLC time series for a currency pair.

    Args:
        from_symbol: From currency code (e.g. 'EUR').
        to_symbol:   To currency code   (e.g. 'USD').

    Returns:
        Dict containing monthly FX OHLC time series covering 20+ years.
    """
    return _get({
        "function": "FX_MONTHLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
    })
