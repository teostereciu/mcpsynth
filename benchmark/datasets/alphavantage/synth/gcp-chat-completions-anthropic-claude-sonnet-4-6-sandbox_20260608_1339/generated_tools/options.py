"""
Options Data tools for Alpha Vantage MCP server.
Source: docs/api_options.md
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


def register_options_tools(mcp: FastMCP):

    @mcp.tool()
    def get_realtime_options(
        symbol: str,
        require_greeks: Optional[bool] = False,
        contract: Optional[str] = None,
        expiration: Optional[str] = None,
    ) -> dict:
        """
        Get realtime US options data with full market coverage.
        Option chains are sorted by expiration date then strike price.

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
            require_greeks: If True, include greeks and implied volatility (IV) fields
            contract: Optional specific contract ID, e.g. 'IBM270115C00390000'
            expiration: Optional expiration date filter in YYYY-MM-DD format
        """
        params: dict = {
            "function": "REALTIME_OPTIONS",
            "symbol": symbol,
            "require_greeks": str(require_greeks).lower(),
        }
        if contract:
            params["contract"] = contract
        if expiration:
            params["expiration"] = expiration
        return _fetch(params)

    @mcp.tool()
    def get_historical_options(
        symbol: str,
        date: Optional[str] = None,
        contract: Optional[str] = None,
    ) -> dict:
        """
        Get the full historical options chain for a symbol on a specific date.
        Covers 15+ years of history with implied volatility and Greeks (delta, gamma, theta, vega, rho).

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
            date: Optional date in YYYY-MM-DD format (any date after 2008-01-01).
                  Defaults to the previous trading session.
            contract: Optional specific contract ID to filter results
        """
        params: dict = {"function": "HISTORICAL_OPTIONS", "symbol": symbol}
        if date:
            params["date"] = date
        if contract:
            params["contract"] = contract
        return _fetch(params)

    @mcp.tool()
    def get_realtime_put_call_ratio(symbol: str) -> dict:
        """
        Get realtime put-call ratios for a stock's entire option chain and by expiration date.
        A ratio <= 0.6 typically signals bullish sentiment; >= 1.0 suggests bearish sentiment.

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
        """
        return _fetch({"function": "REALTIME_PUT_CALL_RATIO", "symbol": symbol})

    @mcp.tool()
    def get_realtime_volume_open_interest_ratio(symbol: str) -> dict:
        """
        Get realtime volume-to-open-interest ratios within an option chain.
        A high ratio suggests heavy trading activity relative to existing positions.
        A low ratio implies most positions are being held rather than actively traded.

        Args:
            symbol: Equity ticker symbol, e.g. 'NVDA'
        """
        return _fetch({
            "function": "REALTIME_VOLUME_OPEN_INTEREST_RATIO",
            "symbol": symbol,
        })
