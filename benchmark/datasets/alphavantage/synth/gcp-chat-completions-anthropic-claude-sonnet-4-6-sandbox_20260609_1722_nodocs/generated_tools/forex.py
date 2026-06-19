"""
Alpha Vantage – Forex (FX) tools
Covers: real-time exchange rate, FX intraday, FX daily, FX weekly, FX monthly
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


def get_fx_exchange_rate(from_currency: str, to_currency: str) -> dict:
    """
    Return the real-time exchange rate for a currency pair.

    :param from_currency: Source currency code, e.g. "USD" or "BTC".
    :param to_currency: Destination currency code, e.g. "EUR" or "USD".
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
    Return intraday FX OHLCV time series for a currency pair.

    :param from_symbol: Source currency code, e.g. "EUR".
    :param to_symbol: Destination currency code, e.g. "USD".
    :param interval: One of 1min | 5min | 15min | 30min | 60min.
    :param outputsize: "compact" (latest 100 data points) or "full".
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
    Return daily FX OHLCV time series for a currency pair.

    :param from_symbol: Source currency code, e.g. "EUR".
    :param to_symbol: Destination currency code, e.g. "USD".
    :param outputsize: "compact" (latest 100 data points) or "full".
    """
    return _get({
        "function": "FX_DAILY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "outputsize": outputsize,
    })


def get_fx_weekly(from_symbol: str, to_symbol: str) -> dict:
    """
    Return weekly FX OHLCV time series for a currency pair.

    :param from_symbol: Source currency code, e.g. "EUR".
    :param to_symbol: Destination currency code, e.g. "USD".
    """
    return _get({
        "function": "FX_WEEKLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
    })


def get_fx_monthly(from_symbol: str, to_symbol: str) -> dict:
    """
    Return monthly FX OHLCV time series for a currency pair.

    :param from_symbol: Source currency code, e.g. "EUR".
    :param to_symbol: Destination currency code, e.g. "USD".
    """
    return _get({
        "function": "FX_MONTHLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
    })
