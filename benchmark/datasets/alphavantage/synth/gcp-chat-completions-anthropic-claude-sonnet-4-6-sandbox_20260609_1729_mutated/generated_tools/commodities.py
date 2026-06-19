"""
Commodities tools for Alpha Vantage MCP server.
Source: docs/api_commodities.md
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


def register_commodity_tools(mcp: FastMCP):

    @mcp.tool()
    def get_gold_silver_spot(ticker: str) -> dict:
        """
        Get the live spot price of gold or silver.

        Args:
            ticker: 'GOLD' or 'XAU' for gold; 'SILVER' or 'XAG' for silver
        """
        return _call({"function": "GOLD_SILVER_SPOT", "ticker": ticker})

    @mcp.tool()
    def get_gold_silver_history(ticker: str, time_interval: str) -> dict:
        """
        Get historical gold or silver prices in daily, weekly, or monthly horizons.

        Args:
            ticker: 'GOLD' or 'XAU' for gold; 'SILVER' or 'XAG' for silver
            time_interval: 'daily', 'weekly', or 'monthly'
        """
        return _call({
            "function": "GOLD_SILVER_HISTORY",
            "ticker": ticker,
            "time_interval": time_interval,
        })

    @mcp.tool()
    def get_wti_crude_oil(time_interval: Optional[str] = None) -> dict:
        """
        Get West Texas Intermediate (WTI) crude oil prices in daily, weekly, or monthly horizons.
        Source: U.S. Energy Information Administration via FRED.

        Args:
            time_interval: 'daily', 'weekly', or 'monthly' (default)
        """
        params: dict = {"function": "WTI"}
        if time_interval is not None:
            params["time_interval"] = time_interval
        return _call(params)

    @mcp.tool()
    def get_brent_crude_oil(time_interval: Optional[str] = None) -> dict:
        """
        Get Brent (Europe) crude oil prices in daily, weekly, or monthly horizons.
        Source: U.S. Energy Information Administration via FRED.

        Args:
            time_interval: 'daily', 'weekly', or 'monthly' (default)
        """
        params: dict = {"function": "BRENT"}
        if time_interval is not None:
            params["time_interval"] = time_interval
        return _call(params)

    @mcp.tool()
    def get_natural_gas(time_interval: Optional[str] = None) -> dict:
        """
        Get Henry Hub natural gas spot prices in daily, weekly, or monthly horizons.
        Source: U.S. Energy Information Administration via FRED.

        Args:
            time_interval: 'daily', 'weekly', or 'monthly' (default)
        """
        params: dict = {"function": "NATURAL_GAS"}
        if time_interval is not None:
            params["time_interval"] = time_interval
        return _call(params)

    @mcp.tool()
    def get_copper(time_interval: Optional[str] = None) -> dict:
        """
        Get global copper prices in monthly, quarterly, or annual horizons.
        Source: World Bank via FRED.

        Args:
            time_interval: 'monthly' (default), 'quarterly', or 'annual'
        """
        params: dict = {"function": "COPPER"}
        if time_interval is not None:
            params["time_interval"] = time_interval
        return _call(params)

    @mcp.tool()
    def get_aluminum(time_interval: Optional[str] = None) -> dict:
        """
        Get global aluminum prices in monthly, quarterly, or annual horizons.
        Source: World Bank via FRED.

        Args:
            time_interval: 'monthly' (default), 'quarterly', or 'annual'
        """
        params: dict = {"function": "ALUMINUM"}
        if time_interval is not None:
            params["time_interval"] = time_interval
        return _call(params)

    @mcp.tool()
    def get_wheat(time_interval: Optional[str] = None) -> dict:
        """
        Get global wheat prices in monthly, quarterly, or annual horizons.
        Source: World Bank via FRED.

        Args:
            time_interval: 'monthly' (default), 'quarterly', or 'annual'
        """
        params: dict = {"function": "WHEAT"}
        if time_interval is not None:
            params["time_interval"] = time_interval
        return _call(params)

    @mcp.tool()
    def get_corn(time_interval: Optional[str] = None) -> dict:
        """
        Get global corn prices in monthly, quarterly, or annual horizons.
        Source: World Bank via FRED.

        Args:
            time_interval: 'monthly' (default), 'quarterly', or 'annual'
        """
        params: dict = {"function": "CORN"}
        if time_interval is not None:
            params["time_interval"] = time_interval
        return _call(params)

    @mcp.tool()
    def get_cotton(time_interval: Optional[str] = None) -> dict:
        """
        Get global cotton prices in monthly, quarterly, or annual horizons.
        Source: World Bank via FRED.

        Args:
            time_interval: 'monthly' (default), 'quarterly', or 'annual'
        """
        params: dict = {"function": "COTTON"}
        if time_interval is not None:
            params["time_interval"] = time_interval
        return _call(params)

    @mcp.tool()
    def get_sugar(time_interval: Optional[str] = None) -> dict:
        """
        Get global sugar prices in monthly, quarterly, or annual horizons.
        Source: World Bank via FRED.

        Args:
            time_interval: 'monthly' (default), 'quarterly', or 'annual'
        """
        params: dict = {"function": "SUGAR"}
        if time_interval is not None:
            params["time_interval"] = time_interval
        return _call(params)

    @mcp.tool()
    def get_coffee(time_interval: Optional[str] = None) -> dict:
        """
        Get global coffee prices in monthly, quarterly, or annual horizons.
        Source: World Bank via FRED.

        Args:
            time_interval: 'monthly' (default), 'quarterly', or 'annual'
        """
        params: dict = {"function": "COFFEE"}
        if time_interval is not None:
            params["time_interval"] = time_interval
        return _call(params)

    @mcp.tool()
    def get_all_commodities(time_interval: Optional[str] = None) -> dict:
        """
        Get the global price index of all commodities in monthly, quarterly, or annual horizons.
        Source: World Bank via FRED.

        Args:
            time_interval: 'monthly' (default), 'quarterly', or 'annual'
        """
        params: dict = {"function": "ALL_COMMODITIES"}
        if time_interval is not None:
            params["time_interval"] = time_interval
        return _call(params)
