"""
Sector Performance tools for Alpha Vantage MCP server.
Source: docs/api_intelligence.md (SECTOR function)
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


def register_sector_tools(mcp: FastMCP):

    @mcp.tool()
    def get_sector_performance() -> dict:
        """
        Return real-time and historical sector performance data across S&P 500 sectors.
        Covers performance over 1 day, 5 days, 1 month, 3 months, YTD, 1 year, 3 years,
        5 years, and 10 years.
        """
        params = {"function": "SECTOR"}
        return _fetch(params)
