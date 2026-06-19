"""
Commodities tools for Alpha Vantage MCP server.
Source: docs/api_commodities.md
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


def register_commodity_tools(mcp: FastMCP):

    @mcp.tool()
    def get_gold_silver_spot(ticker: str) -> dict:
        """
        Return the live spot price of gold or silver.

        Args:
            ticker: 'GOLD' or 'XAU' for gold; 'SILVER' or 'XAG' for silver.
        """
        params = {"function": "GOLD_SILVER_SPOT", "ticker": ticker}
        return _fetch(params)

    @mcp.tool()
    def get_gold_silver_history(ticker: str, time_interval: str) -> dict:
        """
        Return historical gold or silver prices in daily, weekly, or monthly horizons.

        Args:
            ticker: 'GOLD' or 'XAU' for gold; 'SILVER' or 'XAG' for silver.
            time_interval: 'daily', 'weekly', or 'monthly'.
        """
        params = {
            "function": "GOLD_SILVER_HISTORY",
            "ticker": ticker,
            "time_interval": time_interval,
        }
        return _fetch(params)

    @mcp.tool()
    def get_wti_crude_oil(time_interval: str = "monthly") -> dict:
        """
        Return West Texas Intermediate (WTI) crude oil prices.

        Args:
            time_interval: 'daily', 'weekly', or 'monthly' (default).
        """
        params = {"function": "WTI", "time_interval": time_interval}
        return _fetch(params)

    @mcp.tool()
    def get_brent_crude_oil(time_interval: str = "monthly") -> dict:
        """
        Return Brent (Europe) crude oil prices.

        Args:
            time_interval: 'daily', 'weekly', or 'monthly' (default).
        """
        params = {"function": "BRENT", "time_interval": time_interval}
        return _fetch(params)

    @mcp.tool()
    def get_natural_gas(time_interval: str = "monthly") -> dict:
        """
        Return Henry Hub natural gas spot prices.

        Args:
            time_interval: 'daily', 'weekly', or 'monthly' (default).
        """
        params = {"function": "NATURAL_GAS", "time_interval": time_interval}
        return _fetch(params)

    @mcp.tool()
    def get_copper(time_interval: str = "monthly") -> dict:
        """
        Return global copper prices.

        Args:
            time_interval: 'monthly' (default), 'quarterly', or 'annual'.
        """
        params = {"function": "COPPER", "time_interval": time_interval}
        return _fetch(params)

    @mcp.tool()
    def get_aluminum(time_interval: str = "monthly") -> dict:
        """
        Return global aluminum prices.

        Args:
            time_interval: 'monthly' (default), 'quarterly', or 'annual'.
        """
        params = {"function": "ALUMINUM", "time_interval": time_interval}
        return _fetch(params)

    @mcp.tool()
    def get_wheat(time_interval: str = "monthly") -> dict:
        """
        Return global wheat prices.

        Args:
            time_interval: 'monthly' (default), 'quarterly', or 'annual'.
        """
        params = {"function": "WHEAT", "time_interval": time_interval}
        return _fetch(params)

    @mcp.tool()
    def get_corn(time_interval: str = "monthly") -> dict:
        """
        Return global corn prices.

        Args:
            time_interval: 'monthly' (default), 'quarterly', or 'annual'.
        """
        params = {"function": "CORN", "time_interval": time_interval}
        return _fetch(params)

    @mcp.tool()
    def get_cotton(time_interval: str = "monthly") -> dict:
        """
        Return global cotton prices.

        Args:
            time_interval: 'monthly' (default), 'quarterly', or 'annual'.
        """
        params = {"function": "COTTON", "time_interval": time_interval}
        return _fetch(params)

    @mcp.tool()
    def get_sugar(time_interval: str = "monthly") -> dict:
        """
        Return global sugar prices.

        Args:
            time_interval: 'monthly' (default), 'quarterly', or 'annual'.
        """
        params = {"function": "SUGAR", "time_interval": time_interval}
        return _fetch(params)

    @mcp.tool()
    def get_coffee(time_interval: str = "monthly") -> dict:
        """
        Return global coffee prices.

        Args:
            time_interval: 'monthly' (default), 'quarterly', or 'annual'.
        """
        params = {"function": "COFFEE", "time_interval": time_interval}
        return _fetch(params)

    @mcp.tool()
    def get_all_commodities(time_interval: str = "monthly") -> dict:
        """
        Return the global price index of all commodities.

        Args:
            time_interval: 'monthly' (default), 'quarterly', or 'annual'.
        """
        params = {"function": "ALL_COMMODITIES", "time_interval": time_interval}
        return _fetch(params)
