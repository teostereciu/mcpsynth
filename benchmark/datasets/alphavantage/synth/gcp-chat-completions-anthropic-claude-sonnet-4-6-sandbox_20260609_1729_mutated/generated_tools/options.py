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


def register_options_tools(mcp: FastMCP):

    @mcp.tool()
    def get_realtime_options(
        ticker: str,
        require_greeks: Optional[bool] = None,
        contract: Optional[str] = None,
        expiration: Optional[str] = None,
    ) -> dict:
        """
        Get realtime US options data with full market coverage.
        Option chains are sorted by expiration date then strike price.

        Args:
            ticker: Equity symbol, e.g. 'IBM'
            require_greeks: Set True to include Greeks & implied volatility fields
            contract: Specific contract ID, e.g. 'IBM270115C00390000' (optional)
            expiration: Filter by expiration date in YYYY-MM-DD format (optional)
        """
        params: dict = {"function": "REALTIME_OPTIONS", "ticker": ticker}
        if require_greeks is not None:
            params["require_greeks"] = "true" if require_greeks else "false"
        if contract is not None:
            params["contract"] = contract
        if expiration is not None:
            params["expiration"] = expiration
        return _call(params)

    @mcp.tool()
    def get_historical_options(
        ticker: str,
        date: Optional[str] = None,
        contract: Optional[str] = None,
    ) -> dict:
        """
        Get the full historical options chain for a ticker on a specific date.
        Covers 15+ years of history with IV and Greeks (delta, gamma, theta, vega, rho).

        Args:
            ticker: Equity symbol, e.g. 'IBM'
            date: Trading date in YYYY-MM-DD format (default: previous trading session)
            contract: Specific contract ID to filter (optional)
        """
        params: dict = {"function": "HISTORICAL_OPTIONS", "ticker": ticker}
        if date is not None:
            params["date"] = date
        if contract is not None:
            params["contract"] = contract
        return _call(params)

    @mcp.tool()
    def get_realtime_put_call_ratio(ticker: str) -> dict:
        """
        Get realtime put-call ratios for an equity's option chain.
        A ratio <=0.6 signals bullish sentiment; >=1.0 signals bearish sentiment.

        Args:
            ticker: Equity symbol, e.g. 'IBM'
        """
        return _call({"function": "REALTIME_PUT_CALL_RATIO", "ticker": ticker})

    @mcp.tool()
    def get_realtime_volume_open_interest_ratio(ticker: str) -> dict:
        """
        Get realtime volume-to-open-interest ratios within an option chain.
        A high ratio suggests heavy trading activity; a low ratio implies stable conditions.

        Args:
            ticker: Equity symbol, e.g. 'NVDA'
        """
        return _call({"function": "REALTIME_VOLUME_OPEN_INTEREST_RATIO", "ticker": ticker})
