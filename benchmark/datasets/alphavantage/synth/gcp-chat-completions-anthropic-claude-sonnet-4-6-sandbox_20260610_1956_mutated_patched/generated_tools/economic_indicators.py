"""
Economic Indicator tools for Alpha Vantage MCP server.
Source: docs/api_economic_indicators.md
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


def register_economic_indicator_tools(mcp: FastMCP):

    @mcp.tool()
    def get_real_gdp(time_interval: str = "annual") -> dict:
        """
        Return annual or quarterly Real GDP of the United States.

        Args:
            time_interval: 'annual' (default) or 'quarterly'.
        """
        params = {"function": "REAL_GDP", "interval": time_interval}
        return _fetch(params)

    @mcp.tool()
    def get_real_gdp_per_capita() -> dict:
        """
        Return quarterly Real GDP per Capita data of the United States.
        """
        params = {"function": "REAL_GDP_PER_CAPITA"}
        return _fetch(params)

    @mcp.tool()
    def get_treasury_yield(
        time_interval: str = "monthly",
        maturity: str = "10year",
    ) -> dict:
        """
        Return daily, weekly, or monthly US Treasury yield for a given maturity.

        Args:
            time_interval: 'daily', 'weekly', or 'monthly' (default).
            maturity: '3month', '2year', '5year', '7year', '10year' (default), or '30year'.
        """
        params = {
            "function": "TREASURY_YIELD",
            "interval": time_interval,
            "maturity": maturity,
        }
        return _fetch(params)

    @mcp.tool()
    def get_federal_funds_rate(time_interval: str = "monthly") -> dict:
        """
        Return daily, weekly, or monthly US Federal Funds Rate (interest rate).

        Args:
            time_interval: 'daily', 'weekly', or 'monthly' (default).
        """
        params = {
            "function": "FEDERAL_FUNDS_RATE",
            "interval": time_interval,
        }
        return _fetch(params)

    @mcp.tool()
    def get_cpi(time_interval: str = "monthly") -> dict:
        """
        Return monthly or semiannual Consumer Price Index (CPI) for the United States.

        Args:
            time_interval: 'monthly' (default) or 'semiannual'.
        """
        params = {"function": "CPI", "interval": time_interval}
        return _fetch(params)

    @mcp.tool()
    def get_inflation() -> dict:
        """
        Return annual inflation rates (CPI-based) for the United States.
        """
        params = {"function": "INFLATION"}
        return _fetch(params)

    @mcp.tool()
    def get_retail_sales() -> dict:
        """
        Return monthly US Advance Retail Sales data.
        """
        params = {"function": "RETAIL_SALES"}
        return _fetch(params)

    @mcp.tool()
    def get_durables() -> dict:
        """
        Return monthly US Manufacturers' New Orders for Durable Goods.
        """
        params = {"function": "DURABLES"}
        return _fetch(params)

    @mcp.tool()
    def get_unemployment() -> dict:
        """
        Return monthly US unemployment rate data.
        """
        params = {"function": "UNEMPLOYMENT"}
        return _fetch(params)

    @mcp.tool()
    def get_nonfarm_payroll() -> dict:
        """
        Return monthly US Total Nonfarm Employees (payroll) data.
        """
        params = {"function": "NONFARM_PAYROLL"}
        return _fetch(params)
