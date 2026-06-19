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
        raise ValueError("ALPHAVANTAGE_API_KEY environment variable not set")
    return key


def _call(params: dict) -> dict:
    try:
        params["apikey"] = _get_api_key()
        r = requests.get(BASE_URL, params=params, timeout=30)
        r.raise_for_status()
        return r.json()
    except ValueError as e:
        return {"error": str(e)}
    except requests.RequestException as e:
        return {"error": f"Request failed: {e}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}


def register_crypto_tools(mcp: FastMCP):

    @mcp.tool()
    def get_crypto_exchange_rate(from_currency: str, to_currency: str) -> dict:
        """
        Get the realtime exchange rate for any pair of cryptocurrency or physical currency.

        Args:
            from_currency: Source currency, e.g. 'BTC' or 'USD'
            to_currency: Destination currency, e.g. 'EUR' or 'JPY'
        """
        return _call({
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": from_currency,
            "to_currency": to_currency,
        })

    @mcp.tool()
    def get_crypto_intraday(
        ticker: str,
        market: str,
        time_interval: str,
        output_size: Optional[str] = None,
    ) -> dict:
        """
        Get intraday OHLCV time series for a cryptocurrency, updated realtime.

        Args:
            ticker: Cryptocurrency symbol, e.g. 'ETH' or 'BTC'
            market: Exchange market currency, e.g. 'USD'
            time_interval: One of '1min', '5min', '15min', '30min', '60min'
            output_size: 'compact' (latest 100, default) or 'full'
        """
        params = {
            "function": "CRYPTO_INTRADAY",
            "ticker": ticker,
            "market": market,
            "time_interval": time_interval,
        }
        if output_size is not None:
            params["output_size"] = output_size
        return _call(params)

    @mcp.tool()
    def get_crypto_daily(ticker: str, market: str) -> dict:
        """
        Get daily historical time series for a cryptocurrency traded on a specific market.
        Prices and volumes are quoted in both the market-specific currency and USD.

        Args:
            ticker: Cryptocurrency symbol, e.g. 'BTC'
            market: Exchange market currency, e.g. 'EUR'
        """
        return _call({
            "function": "DIGITAL_CURRENCY_DAILY",
            "ticker": ticker,
            "market": market,
        })

    @mcp.tool()
    def get_crypto_weekly(ticker: str, market: str) -> dict:
        """
        Get weekly historical time series for a cryptocurrency traded on a specific market.
        Prices and volumes are quoted in both the market-specific currency and USD.

        Args:
            ticker: Cryptocurrency symbol, e.g. 'BTC'
            market: Exchange market currency, e.g. 'EUR'
        """
        return _call({
            "function": "DIGITAL_CURRENCY_WEEKLY",
            "ticker": ticker,
            "market": market,
        })

    @mcp.tool()
    def get_crypto_monthly(ticker: str, market: str) -> dict:
        """
        Get monthly historical time series for a cryptocurrency traded on a specific market.
        Prices and volumes are quoted in both the market-specific currency and USD.

        Args:
            ticker: Cryptocurrency symbol, e.g. 'BTC'
            market: Exchange market currency, e.g. 'EUR'
        """
        return _call({
            "function": "DIGITAL_CURRENCY_MONTHLY",
            "ticker": ticker,
            "market": market,
        })
