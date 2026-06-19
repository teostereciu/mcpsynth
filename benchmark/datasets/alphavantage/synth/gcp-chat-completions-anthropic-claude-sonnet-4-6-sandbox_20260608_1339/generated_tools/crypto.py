"""
Digital / Crypto Currency tools for Alpha Vantage MCP server.
Source: docs/api_digital_currency.md
"""

import os
import requests
from typing import Optional
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://www.alphavantage.co/query"


def _get_api_key() -> str:
    key = os.environ.get("ALPHAVANTAGE_API_KEY", "")
    if not key:
        raise ValueError("ALPHAVANTAGE_API_KEY environment variable is not set")
    return key


def _fetch(params: dict) -> dict:
    try:
        params["apikey"] = _get_api_key()
        r = requests.get(BASE_URL, params=params, timeout=30)
        r.raise_for_status()
        return r.json()
    except ValueError as e:
        return {"error": str(e)}
    except requests.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


def register_crypto_tools(mcp: FastMCP):

    @mcp.tool()
    def get_crypto_exchange_rate(from_currency: str, to_currency: str) -> dict:
        """
        Get the realtime exchange rate for any pair of cryptocurrency or physical currency.

        Args:
            from_currency: Source currency code (crypto or fiat), e.g. 'BTC', 'USD'
            to_currency: Destination currency code (crypto or fiat), e.g. 'EUR', 'ETH'
        """
        return _fetch({
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": from_currency,
            "to_currency": to_currency,
        })

    @mcp.tool()
    def get_crypto_intraday(
        symbol: str,
        market: str,
        interval: str,
        outputsize: Optional[str] = "compact",
    ) -> dict:
        """
        Get intraday time series (timestamp, open, high, low, close, volume) for a cryptocurrency.
        Updated realtime.

        Args:
            symbol: Cryptocurrency symbol, e.g. 'ETH', 'BTC'
            market: Exchange market currency, e.g. 'USD', 'EUR'
            interval: Time interval: '1min', '5min', '15min', '30min', '60min'
            outputsize: 'compact' (latest 100 points) or 'full' (full-length series)
        """
        return _fetch({
            "function": "CRYPTO_INTRADAY",
            "symbol": symbol,
            "market": market,
            "interval": interval,
            "outputsize": outputsize,
        })

    @mcp.tool()
    def get_crypto_daily(symbol: str, market: str) -> dict:
        """
        Get daily historical time series for a cryptocurrency traded on a specific market.
        Prices and volumes are quoted in both the market-specific currency and USD.
        Refreshed daily at midnight UTC.

        Args:
            symbol: Cryptocurrency symbol, e.g. 'BTC', 'ETH'
            market: Exchange market currency, e.g. 'EUR', 'USD'
        """
        return _fetch({
            "function": "DIGITAL_CURRENCY_DAILY",
            "symbol": symbol,
            "market": market,
        })

    @mcp.tool()
    def get_crypto_weekly(symbol: str, market: str) -> dict:
        """
        Get weekly historical time series for a cryptocurrency traded on a specific market.
        Prices and volumes are quoted in both the market-specific currency and USD.

        Args:
            symbol: Cryptocurrency symbol, e.g. 'BTC', 'ETH'
            market: Exchange market currency, e.g. 'EUR', 'USD'
        """
        return _fetch({
            "function": "DIGITAL_CURRENCY_WEEKLY",
            "symbol": symbol,
            "market": market,
        })

    @mcp.tool()
    def get_crypto_monthly(symbol: str, market: str) -> dict:
        """
        Get monthly historical time series for a cryptocurrency traded on a specific market.
        Prices and volumes are quoted in both the market-specific currency and USD.

        Args:
            symbol: Cryptocurrency symbol, e.g. 'BTC', 'ETH'
            market: Exchange market currency, e.g. 'EUR', 'USD'
        """
        return _fetch({
            "function": "DIGITAL_CURRENCY_MONTHLY",
            "symbol": symbol,
            "market": market,
        })
