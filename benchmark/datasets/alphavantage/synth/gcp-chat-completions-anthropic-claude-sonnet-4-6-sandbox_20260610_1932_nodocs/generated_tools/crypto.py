"""
Alpha Vantage — Cryptocurrency tools
Covers: digital currency exchange rate, crypto daily/weekly/monthly time series
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


def get_crypto_exchange_rate(from_currency: str, to_currency: str) -> dict:
    """
    Fetch the real-time exchange rate for a digital/crypto currency pair.

    Args:
        from_currency: Crypto or fiat currency to convert from (e.g. 'BTC', 'ETH').
        to_currency:   Crypto or fiat currency to convert to   (e.g. 'USD', 'EUR').

    Returns:
        Dict with exchange rate, bid price, ask price, and last refreshed timestamp.
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
    Fetch intraday time series for a digital currency traded on a specific market.

    Args:
        symbol:     Cryptocurrency symbol (e.g. 'BTC', 'ETH').
        market:     Exchange market currency (e.g. 'USD', 'EUR', 'CNY').
        interval:   Time interval between data points.
                    Allowed values: '1min', '5min', '15min', '30min', '60min'.
        outputsize: 'compact' returns the latest 100 data points;
                    'full' returns the full intraday history.

    Returns:
        Dict containing intraday crypto OHLCV time series.
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
    Fetch daily historical time series for a digital currency.

    Args:
        symbol: Cryptocurrency symbol (e.g. 'BTC', 'ETH').
        market: Exchange market currency (e.g. 'USD', 'EUR', 'CNY').

    Returns:
        Dict containing daily crypto OHLCV time series with market cap data.
    """
    return _get({
        "function": "DIGITAL_CURRENCY_DAILY",
        "symbol": symbol,
        "market": market,
    })


def get_crypto_weekly(symbol: str, market: str = "USD") -> dict:
    """
    Fetch weekly historical time series for a digital currency.

    Args:
        symbol: Cryptocurrency symbol (e.g. 'BTC', 'ETH').
        market: Exchange market currency (e.g. 'USD', 'EUR', 'CNY').

    Returns:
        Dict containing weekly crypto OHLCV time series with market cap data.
    """
    return _get({
        "function": "DIGITAL_CURRENCY_WEEKLY",
        "symbol": symbol,
        "market": market,
    })


def get_crypto_monthly(symbol: str, market: str = "USD") -> dict:
    """
    Fetch monthly historical time series for a digital currency.

    Args:
        symbol: Cryptocurrency symbol (e.g. 'BTC', 'ETH').
        market: Exchange market currency (e.g. 'USD', 'EUR', 'CNY').

    Returns:
        Dict containing monthly crypto OHLCV time series with market cap data.
    """
    return _get({
        "function": "DIGITAL_CURRENCY_MONTHLY",
        "symbol": symbol,
        "market": market,
    })
