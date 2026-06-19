"""
Options Data tools for Alpha Vantage MCP server.
Source: docs/api_options.md
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


def register_options_tools(mcp: FastMCP):

    @mcp.tool()
    def get_realtime_options(
        ticker: str,
        require_greeks: bool = False,
        contract: str = "",
        expiration: str = "",
    ) -> dict:
        """
        Return realtime US options data (full option chain or a specific contract).

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
            require_greeks: If True, include Greeks and implied volatility fields.
            contract: Optional specific contract ID, e.g. 'IBM270115C00390000'.
            expiration: Optional expiration date filter in YYYY-MM-DD format.
        """
        params: dict = {
            "function": "REALTIME_OPTIONS",
            "symbol": ticker,
            "require_greeks": "true" if require_greeks else "false",
        }
        if contract:
            params["contract"] = contract
        if expiration:
            params["expiration"] = expiration
        return _fetch(params)

    @mcp.tool()
    def get_historical_options(
        ticker: str,
        date: str = "",
        contract: str = "",
    ) -> dict:
        """
        Return the full historical options chain for a ticker on a specific date.

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
            date: Optional date in YYYY-MM-DD format (defaults to previous trading session).
            contract: Optional specific contract ID to narrow results.
        """
        params: dict = {
            "function": "HISTORICAL_OPTIONS",
            "symbol": ticker,
        }
        if date:
            params["date"] = date
        if contract:
            params["contract"] = contract
        return _fetch(params)

    @mcp.tool()
    def get_realtime_put_call_ratio(ticker: str) -> dict:
        """
        Return realtime put-call ratios for the full option chain of a ticker.

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
        """
        params = {"function": "REALTIME_PUT_CALL_RATIO", "symbol": ticker}
        return _fetch(params)

    @mcp.tool()
    def get_realtime_volume_open_interest_ratio(ticker: str) -> dict:
        """
        Return realtime volume-to-open-interest ratios within an option chain.

        Args:
            ticker: Equity symbol, e.g. 'NVDA'.
        """
        params = {
            "function": "REALTIME_VOLUME_OPEN_INTEREST_RATIO",
            "symbol": ticker,
        }
        return _fetch(params)
