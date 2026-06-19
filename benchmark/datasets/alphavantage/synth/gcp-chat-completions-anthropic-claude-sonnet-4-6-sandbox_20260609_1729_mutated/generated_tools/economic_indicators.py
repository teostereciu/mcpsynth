"""
Economic Indicators tools for Alpha Vantage MCP server.
Source: docs/api_economic_indicators.md
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


def register_economic_indicator_tools(mcp: FastMCP):

    @mcp.tool()
    def get_real_gdp(time_interval: Optional[str] = None) -> dict:
        """
        Get annual and quarterly Real GDP of the United States.
        Source: U.S. Bureau of Economic Analysis via FRED.

        Args:
            time_interval: 'annual' (default) or 'quarterly'
        """
        params: dict = {"function": "REAL_GDP"}
        if time_interval is not None:
            params["time_interval"] = time_interval
        return _call(params)

    @mcp.tool()
    def get_real_gdp_per_capita() -> dict:
        """
        Get quarterly Real GDP per Capita data of the United States.
        Source: U.S. Bureau of Economic Analysis via FRED.
        """
        return _call({"function": "REAL_GDP_PER_CAPITA"})

    @mcp.tool()
    def get_treasury_yield(
        time_interval: Optional[str] = None,
        maturity: Optional[str] = None,
    ) -> dict:
        """
        Get daily, weekly, or monthly US Treasury yield for a given maturity.
        Source: Federal Reserve Board via FRED.

        Args:
            time_interval: 'daily', 'weekly', or 'monthly' (default)
            maturity: '3month', '2year', '5year', '7year', '10year' (default), or '30year'
        """
        params: dict = {"function": "TREASURY_YIELD"}
        if time_interval is not None:
            params["time_interval"] = time_interval
        if maturity is not None:
            params["maturity"] = maturity
        return _call(params)

    @mcp.tool()
    def get_federal_funds_rate(time_interval: Optional[str] = None) -> dict:
        """
        Get daily, weekly, or monthly US Federal Funds Rate (interest rate).
        Source: Federal Reserve Board via FRED.

        Args:
            time_interval: 'daily', 'weekly', or 'monthly' (default)
        """
        params: dict = {"function": "FEDERAL_FUNDS_RATE"}
        if time_interval is not None:
            params["time_interval"] = time_interval
        return _call(params)

    @mcp.tool()
    def get_cpi(time_interval: Optional[str] = None) -> dict:
        """
        Get monthly or semiannual Consumer Price Index (CPI) for the United States.
        Source: U.S. Bureau of Labor Statistics via FRED.

        Args:
            time_interval: 'monthly' (default) or 'semiannual'
        """
        params: dict = {"function": "CPI"}
        if time_interval is not None:
            params["time_interval"] = time_interval
        return _call(params)

    @mcp.tool()
    def get_inflation() -> dict:
        """
        Get annual inflation rates (% change in CPI) for the United States.
        Source: World Bank via FRED.
        """
        return _call({"function": "INFLATION"})

    @mcp.tool()
    def get_retail_sales() -> dict:
        """
        Get monthly Advance Retail Sales data for the United States.
        Source: U.S. Census Bureau via FRED.
        """
        return _call({"function": "RETAIL_SALES"})

    @mcp.tool()
    def get_durables() -> dict:
        """
        Get monthly manufacturers' new orders for durable goods in the United States.
        Source: U.S. Census Bureau via FRED.
        """
        return _call({"function": "DURABLES"})

    @mcp.tool()
    def get_unemployment() -> dict:
        """
        Get monthly US unemployment rate data.
        Source: U.S. Bureau of Labor Statistics via FRED.
        """
        return _call({"function": "UNEMPLOYMENT"})

    @mcp.tool()
    def get_nonfarm_payroll() -> dict:
        """
        Get monthly US Total Nonfarm Employees (payroll) data.
        Source: U.S. Bureau of Labor Statistics via FRED.
        """
        return _call({"function": "NONFARM_PAYROLL"})
