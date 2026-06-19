"""
Digital / Crypto Currency tools for Alpha Vantage MCP server.
Source: docs/api_digital_currency.md
"""

import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://www.alphavantage.co/query"


def _get_api_key() -> str:
    return os.environ.get("ALPHAVANTAGE_API_KEY", "")


def _fetch(params: dict) -> dict:
    params["apikey"] = _get_api_key()
    try:
        r = requests.get(BASE_URL, params=params, timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}


def register_crypto_tools(mcp: FastMCP):

    @mcp.tool()
    def get_crypto_exchange_rate(from_currency: str, to_currency: str) -> dict:
        """
        Return the realtime exchange rate for any pair of cryptocurrency or fiat currency.

        Args:
            from_currency: Source currency code, e.g. 'BTC' or 'USD'.
            to_currency: Destination currency code, e.g. 'EUR' or 'USD'.
        """
        params = {
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": from_currency,
            "to_currency": to_currency,
        }
        return _fetch(params)

    @mcp.tool()
    def get_crypto_intraday(
        ticker: str,
        market: str,
        time_interval: str,
        output_size: str = "compact",
    ) -> dict:
        """
        Return intraday OHLCV time series for a cryptocurrency.

        Args:
            ticker: Cryptocurrency symbol, e.g. 'ETH'.
            market: Exchange market currency, e.g. 'USD'.
            time_interval: One of '1min', '5min', '15min', '30min', '60min'.
            output_size: 'compact' (latest 100 bars) or 'full'.
        """
        params = {
            "function": "CRYPTO_INTRADAY",
            "ticker": ticker,
            "market": market,
            "time_interval": time_interval,
            "output_size": output_size,
        }
        return _fetch(params)

    @mcp.tool()
    def get_crypto_daily(ticker: str, market: str) -> dict:
        """
        Return daily historical time series for a cryptocurrency in a specific market.

        Args:
            ticker: Cryptocurrency symbol, e.g. 'BTC'.
            market: Exchange market currency, e.g. 'EUR'.
        """
        params = {
            "function": "DIGITAL_CURRENCY_DAILY",
            "ticker": ticker,
            "market": market,
        }
        return _fetch(params)

    @mcp.tool()
    def get_crypto_weekly(ticker: str, market: str) -> dict:
        """
        Return weekly historical time series for a cryptocurrency in a specific market.

        Args:
            ticker: Cryptocurrency symbol, e.g. 'BTC'.
            market: Exchange market currency, e.g. 'EUR'.
        """
        params = {
            "function": "DIGITAL_CURRENCY_WEEKLY",
            "ticker": ticker,
            "market": market,
        }
        return _fetch(params)

    @mcp.tool()
    def get_crypto_monthly(ticker: str, market: str) -> dict:
        """
        Return monthly historical time series for a cryptocurrency in a specific market.

        Args:
            ticker: Cryptocurrency symbol, e.g. 'BTC'.
            market: Exchange market currency, e.g. 'EUR'.
        """
        params = {
            "function": "DIGITAL_CURRENCY_MONTHLY",
            "ticker": ticker,
            "market": market,
        }
        return _fetch(params)
