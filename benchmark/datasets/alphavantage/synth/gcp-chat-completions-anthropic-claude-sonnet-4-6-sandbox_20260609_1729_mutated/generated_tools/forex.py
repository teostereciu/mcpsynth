"""
Forex / FX tools for Alpha Vantage MCP server.
Source: docs/api_fx.md
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


def register_forex_tools(mcp: FastMCP):

    @mcp.tool()
    def get_fx_exchange_rate(from_currency: str, to_currency: str) -> dict:
        """
        Get the realtime exchange rate for a pair of currencies (fiat or crypto).

        Args:
            from_currency: Source currency code, e.g. 'USD' or 'BTC'
            to_currency: Destination currency code, e.g. 'JPY' or 'EUR'
        """
        return _call({
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": from_currency,
            "to_currency": to_currency,
        })

    @mcp.tool()
    def get_fx_intraday(
        from_symbol: str,
        to_symbol: str,
        time_interval: str,
        output_size: Optional[str] = None,
    ) -> dict:
        """
        Get intraday time series (timestamp, open, high, low, close) for a forex pair.

        Args:
            from_symbol: Three-letter forex currency code, e.g. 'EUR'
            to_symbol: Three-letter forex currency code, e.g. 'USD'
            time_interval: One of '1min', '5min', '15min', '30min', '60min'
            output_size: 'compact' (latest 100, default) or 'full'
        """
        params = {
            "function": "FX_INTRADAY",
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
            "time_interval": time_interval,
        }
        if output_size is not None:
            params["output_size"] = output_size
        return _call(params)

    @mcp.tool()
    def get_fx_daily(
        from_symbol: str,
        to_symbol: str,
        output_size: Optional[str] = None,
    ) -> dict:
        """
        Get daily time series (timestamp, open, high, low, close) for a forex pair.

        Args:
            from_symbol: Three-letter forex currency code, e.g. 'EUR'
            to_symbol: Three-letter forex currency code, e.g. 'USD'
            output_size: 'compact' (latest 100, default) or 'full'
        """
        params = {
            "function": "FX_DAILY",
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
        }
        if output_size is not None:
            params["output_size"] = output_size
        return _call(params)

    @mcp.tool()
    def get_fx_weekly(from_symbol: str, to_symbol: str) -> dict:
        """
        Get weekly time series (timestamp, open, high, low, close) for a forex pair.

        Args:
            from_symbol: Three-letter forex currency code, e.g. 'EUR'
            to_symbol: Three-letter forex currency code, e.g. 'USD'
        """
        return _call({
            "function": "FX_WEEKLY",
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
        })

    @mcp.tool()
    def get_fx_monthly(from_symbol: str, to_symbol: str) -> dict:
        """
        Get monthly time series (timestamp, open, high, low, close) for a forex pair.

        Args:
            from_symbol: Three-letter forex currency code, e.g. 'EUR'
            to_symbol: Three-letter forex currency code, e.g. 'USD'
        """
        return _call({
            "function": "FX_MONTHLY",
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
        })
