"""
Economic Indicator tools for Alpha Vantage MCP server.
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


def register_economic_indicators_tools(mcp: FastMCP):

    @mcp.tool()
    def get_real_gdp(interval: Optional[str] = "annual") -> dict:
        """
        Get annual and quarterly Real GDP of the United States.
        Source: U.S. Bureau of Economic Analysis via FRED.

        Args:
            interval: 'annual' (default) or 'quarterly'
        """
        return _fetch({"function": "REAL_GDP", "interval": interval})

    @mcp.tool()
    def get_real_gdp_per_capita() -> dict:
        """
        Get quarterly Real GDP per Capita data of the United States.
        Source: U.S. Bureau of Economic Analysis via FRED.
        """
        return _fetch({"function": "REAL_GDP_PER_CAPITA"})

    @mcp.tool()
    def get_treasury_yield(
        interval: Optional[str] = "monthly",
        maturity: Optional[str] = "10year",
    ) -> dict:
        """
        Get daily, weekly, or monthly US Treasury yield for a given maturity.
        Source: Board of Governors of the Federal Reserve System via FRED.

        Args:
            interval: 'daily', 'weekly', or 'monthly' (default)
            maturity: '3month', '2year', '5year', '7year', '10year' (default), or '30year'
        """
        return _fetch({
            "function": "TREASURY_YIELD",
            "interval": interval,
            "maturity": maturity,
        })

    @mcp.tool()
    def get_federal_funds_rate(interval: Optional[str] = "monthly") -> dict:
        """
        Get daily, weekly, or monthly Federal Funds Rate (interest rate) of the United States.
        Source: Board of Governors of the Federal Reserve System via FRED.

        Args:
            interval: 'daily', 'weekly', or 'monthly' (default)
        """
        return _fetch({"function": "FEDERAL_FUNDS_RATE", "interval": interval})

    @mcp.tool()
    def get_cpi(interval: Optional[str] = "monthly") -> dict:
        """
        Get monthly or semiannual Consumer Price Index (CPI) data for the United States.
        Source: U.S. Bureau of Labor Statistics via FRED.

        Args:
            interval: 'monthly' (default) or 'semiannual'
        """
        return _fetch({"function": "CPI", "interval": interval})

    @mcp.tool()
    def get_inflation() -> dict:
        """
        Get annual inflation rates (percentage change in CPI) for the United States.
        Source: World Bank via FRED.
        """
        return _fetch({"function": "INFLATION"})

    @mcp.tool()
    def get_retail_sales() -> dict:
        """
        Get monthly Advance Retail Sales data for the United States.
        Measures the total receipts of retail stores.
        Source: U.S. Census Bureau via FRED.
        """
        return _fetch({"function": "RETAIL_SALES"})

    @mcp.tool()
    def get_durable_goods_orders() -> dict:
        """
        Get monthly manufacturers' new orders for durable goods in the United States.
        Source: U.S. Census Bureau via FRED.
        """
        return _fetch({"function": "DURABLES"})

    @mcp.tool()
    def get_unemployment_rate() -> dict:
        """
        Get monthly unemployment rate data for the United States.
        Source: U.S. Bureau of Labor Statistics via FRED.
        """
        return _fetch({"function": "UNEMPLOYMENT"})

    @mcp.tool()
    def get_nonfarm_payroll() -> dict:
        """
        Get monthly US Total Nonfarm Employees (nonfarm payroll) data.
        A key indicator of economic health and labor market conditions.
        Source: U.S. Bureau of Labor Statistics via FRED.
        """
        return _fetch({"function": "NONFARM_PAYROLL"})
