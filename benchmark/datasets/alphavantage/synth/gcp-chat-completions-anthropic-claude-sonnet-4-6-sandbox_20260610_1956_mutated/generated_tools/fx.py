"""
Forex / FX tools for Alpha Vantage MCP server.
Source: docs/api_fx.md
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


def register_fx_tools(mcp: FastMCP):

    @mcp.tool()
    def get_fx_exchange_rate(from_currency: str, to_currency: str) -> dict:
        """
        Return the realtime exchange rate for a pair of fiat or crypto currencies.

        Args:
            from_currency: Source currency code, e.g. 'USD' or 'BTC'.
            to_currency: Destination currency code, e.g. 'JPY' or 'EUR'.
        """
        params = {
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": from_currency,
            "to_currency": to_currency,
        }
        return _fetch(params)

    @mcp.tool()
    def get_fx_intraday(
        from_symbol: str,
        to_symbol: str,
        time_interval: str,
        output_size: str = "compact",
    ) -> dict:
        """
        Return intraday OHLC time series for a forex currency pair.

        Args:
            from_symbol: Three-letter forex ticker, e.g. 'EUR'.
            to_symbol: Three-letter forex ticker, e.g. 'USD'.
            time_interval: One of '1min', '5min', '15min', '30min', '60min'.
            output_size: 'compact' (latest 100 bars) or 'full' (full series).
        """
        params = {
            "function": "FX_INTRADAY",
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
            "time_interval": time_interval,
            "output_size": output_size,
        }
        return _fetch(params)

    @mcp.tool()
    def get_fx_daily(
        from_symbol: str,
        to_symbol: str,
        output_size: str = "compact",
    ) -> dict:
        """
        Return daily OHLC time series for a forex currency pair.

        Args:
            from_symbol: Three-letter forex ticker, e.g. 'EUR'.
            to_symbol: Three-letter forex ticker, e.g. 'USD'.
            output_size: 'compact' (latest 100 data points) or 'full'.
        """
        params = {
            "function": "FX_DAILY",
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
            "output_size": output_size,
        }
        return _fetch(params)

    @mcp.tool()
    def get_fx_weekly(from_symbol: str, to_symbol: str) -> dict:
        """
        Return weekly OHLC time series for a forex currency pair.

        Args:
            from_symbol: Three-letter forex ticker, e.g. 'EUR'.
            to_symbol: Three-letter forex ticker, e.g. 'USD'.
        """
        params = {
            "function": "FX_WEEKLY",
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
        }
        return _fetch(params)

    @mcp.tool()
    def get_fx_monthly(from_symbol: str, to_symbol: str) -> dict:
        """
        Return monthly OHLC time series for a forex currency pair.

        Args:
            from_symbol: Three-letter forex ticker, e.g. 'EUR'.
            to_symbol: Three-letter forex ticker, e.g. 'USD'.
        """
        params = {
            "function": "FX_MONTHLY",
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
        }
        return _fetch(params)
