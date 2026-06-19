"""
Alpha Vantage – Cryptocurrency tools
Covers: digital currency exchange rate, crypto intraday, daily, weekly, monthly
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


def get_crypto_exchange_rate(from_currency: str, to_currency: str) -> dict:
    """
    Return the real-time exchange rate for a digital/physical currency pair.

    :param from_currency: Digital or physical currency code, e.g. "BTC".
    :param to_currency: Destination currency code, e.g. "USD".
    """
    return _get({
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": from_currency,
        "to_currency": to_currency,
    })


def get_crypto_intraday(
    symbol: str,
    market: str = "USD",
    interval: str = "5min",
    outputsize: str = "compact",
) -> dict:
    """
    Return intraday OHLCV time series for a digital currency.

    :param symbol: Cryptocurrency symbol, e.g. "BTC" or "ETH".
    :param market: Exchange market currency, e.g. "USD".
    :param interval: One of 1min | 5min | 15min | 30min | 60min.
    :param outputsize: "compact" (latest 100 data points) or "full".
    """
    return _get({
        "function": "CRYPTO_INTRADAY",
        "symbol": symbol,
        "market": market,
        "interval": interval,
        "outputsize": outputsize,
    })


def get_crypto_daily(symbol: str, market: str = "USD") -> dict:
    """
    Return daily OHLCV time series for a digital currency.

    :param symbol: Cryptocurrency symbol, e.g. "BTC".
    :param market: Exchange market currency, e.g. "USD".
    """
    return _get({
        "function": "DIGITAL_CURRENCY_DAILY",
        "symbol": symbol,
        "market": market,
    })


def get_crypto_weekly(symbol: str, market: str = "USD") -> dict:
    """
    Return weekly OHLCV time series for a digital currency.

    :param symbol: Cryptocurrency symbol, e.g. "BTC".
    :param market: Exchange market currency, e.g. "USD".
    """
    return _get({
        "function": "DIGITAL_CURRENCY_WEEKLY",
        "symbol": symbol,
        "market": market,
    })


def get_crypto_monthly(symbol: str, market: str = "USD") -> dict:
    """
    Return monthly OHLCV time series for a digital currency.

    :param symbol: Cryptocurrency symbol, e.g. "BTC".
    :param market: Exchange market currency, e.g. "USD".
    """
    return _get({
        "function": "DIGITAL_CURRENCY_MONTHLY",
        "symbol": symbol,
        "market": market,
    })
