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


def register_commodities_tools(mcp: FastMCP):

    @mcp.tool()
    def get_gold_silver_spot(symbol: str) -> dict:
        """
        Get the live spot price of gold or silver.

        Args:
            symbol: 'GOLD' or 'XAU' for gold; 'SILVER' or 'XAG' for silver
        """
        return _fetch({"function": "GOLD_SILVER_SPOT", "symbol": symbol})

    @mcp.tool()
    def get_gold_silver_history(symbol: str, interval: str) -> dict:
        """
        Get historical gold or silver prices in daily, weekly, or monthly horizons.

        Args:
            symbol: 'GOLD' or 'XAU' for gold; 'SILVER' or 'XAG' for silver
            interval: 'daily', 'weekly', or 'monthly'
        """
        return _fetch({
            "function": "GOLD_SILVER_HISTORY",
            "symbol": symbol,
            "interval": interval,
        })

    @mcp.tool()
    def get_wti_crude_oil(interval: Optional[str] = "monthly") -> dict:
        """
        Get West Texas Intermediate (WTI) crude oil prices in daily, weekly, or monthly horizons.
        Source: U.S. Energy Information Administration via FRED.

        Args:
            interval: 'daily', 'weekly', or 'monthly' (default)
        """
        return _fetch({"function": "WTI", "interval": interval})

    @mcp.tool()
    def get_brent_crude_oil(interval: Optional[str] = "monthly") -> dict:
        """
        Get Brent (Europe) crude oil prices in daily, weekly, or monthly horizons.
        Source: U.S. Energy Information Administration via FRED.

        Args:
            interval: 'daily', 'weekly', or 'monthly' (default)
        """
        return _fetch({"function": "BRENT", "interval": interval})

    @mcp.tool()
    def get_natural_gas(interval: Optional[str] = "monthly") -> dict:
        """
        Get Henry Hub natural gas spot prices in daily, weekly, or monthly horizons.
        Source: U.S. Energy Information Administration via FRED.

        Args:
            interval: 'daily', 'weekly', or 'monthly' (default)
        """
        return _fetch({"function": "NATURAL_GAS", "interval": interval})

    @mcp.tool()
    def get_copper(interval: Optional[str] = "monthly") -> dict:
        """
        Get global copper prices in monthly, quarterly, or annual horizons.
        Source: World Bank via FRED.

        Args:
            interval: 'monthly' (default), 'quarterly', or 'annual'
        """
        return _fetch({"function": "COPPER", "interval": interval})

    @mcp.tool()
    def get_aluminum(interval: Optional[str] = "monthly") -> dict:
        """
        Get global aluminum prices in monthly, quarterly, or annual horizons.
        Source: World Bank via FRED.

        Args:
            interval: 'monthly' (default), 'quarterly', or 'annual'
        """
        return _fetch({"function": "ALUMINUM", "interval": interval})

    @mcp.tool()
    def get_wheat(interval: Optional[str] = "monthly") -> dict:
        """
        Get global wheat prices in monthly, quarterly, or annual horizons.
        Source: World Bank via FRED.

        Args:
            interval: 'monthly' (default), 'quarterly', or 'annual'
        """
        return _fetch({"function": "WHEAT", "interval": interval})

    @mcp.tool()
    def get_corn(interval: Optional[str] = "monthly") -> dict:
        """
        Get global corn prices in monthly, quarterly, or annual horizons.
        Source: World Bank via FRED.

        Args:
            interval: 'monthly' (default), 'quarterly', or 'annual'
        """
        return _fetch({"function": "CORN", "interval": interval})

    @mcp.tool()
    def get_cotton(interval: Optional[str] = "monthly") -> dict:
        """
        Get global cotton prices in monthly, quarterly, or annual horizons.
        Source: World Bank via FRED.

        Args:
            interval: 'monthly' (default), 'quarterly', or 'annual'
        """
        return _fetch({"function": "COTTON", "interval": interval})

    @mcp.tool()
    def get_sugar(interval: Optional[str] = "monthly") -> dict:
        """
        Get global sugar prices in monthly, quarterly, or annual horizons.
        Source: World Bank via FRED.

        Args:
            interval: 'monthly' (default), 'quarterly', or 'annual'
        """
        return _fetch({"function": "SUGAR", "interval": interval})

    @mcp.tool()
    def get_coffee(interval: Optional[str] = "monthly") -> dict:
        """
        Get global coffee prices in monthly, quarterly, or annual horizons.
        Source: World Bank via FRED.

        Args:
            interval: 'monthly' (default), 'quarterly', or 'annual'
        """
        return _fetch({"function": "COFFEE", "interval": interval})

    @mcp.tool()
    def get_all_commodities(interval: Optional[str] = "monthly") -> dict:
        """
        Get the global price index of all commodities in monthly, quarterly, or annual horizons.
        Source: World Bank via FRED.

        Args:
            interval: 'monthly' (default), 'quarterly', or 'annual'
        """
        return _fetch({"function": "ALL_COMMODITIES", "interval": interval})
