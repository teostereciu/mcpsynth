"""
Sector Performance tools for Alpha Vantage MCP server.
Source: docs/api_intelligence.md (SECTOR function)
"""

import os
import requests
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


def register_sector_tools(mcp: FastMCP):

    @mcp.tool()
    def get_sector_performance() -> dict:
        """
        Get real-time and historical sector performance data across all S&P 500 sectors.
        Returns performance metrics for multiple time horizons: real-time, 1 day, 5 days,
        1 month, 3 months, year-to-date, 1 year, 3 years, and 10 years.
        """
        return _fetch({"function": "SECTOR"})
