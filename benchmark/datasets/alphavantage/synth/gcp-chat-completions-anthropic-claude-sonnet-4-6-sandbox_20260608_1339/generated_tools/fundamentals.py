"""
Fundamental Data tools for Alpha Vantage MCP server.
Source: docs/api_fundamentals.md
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


def register_fundamentals_tools(mcp: FastMCP):

    @mcp.tool()
    def get_company_overview(symbol: str) -> dict:
        """
        Get company information, financial ratios, and key metrics for a stock.
        Includes sector, industry, market cap, P/E ratio, EPS, dividend yield, and more.
        Data is refreshed when a company reports earnings.

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
        """
        return _fetch({"function": "OVERVIEW", "symbol": symbol})

    @mcp.tool()
    def get_etf_profile(symbol: str) -> dict:
        """
        Get key ETF metrics (net assets, expense ratio, turnover) and holdings/constituents
        with allocation by asset types and sectors.

        Args:
            symbol: ETF ticker symbol, e.g. 'QQQ'
        """
        return _fetch({"function": "ETF_PROFILE", "symbol": symbol})

    @mcp.tool()
    def get_dividends(symbol: str) -> dict:
        """
        Get historical and future (declared) dividend distributions for a stock.

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
        """
        return _fetch({"function": "DIVIDENDS", "symbol": symbol})

    @mcp.tool()
    def get_splits(symbol: str) -> dict:
        """
        Get historical stock split events for a company.

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
        """
        return _fetch({"function": "SPLITS", "symbol": symbol})

    @mcp.tool()
    def get_income_statement(symbol: str) -> dict:
        """
        Get annual and quarterly income statements for a company.
        Includes revenue, gross profit, operating income, net income, EPS, and more.

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
        """
        return _fetch({"function": "INCOME_STATEMENT", "symbol": symbol})

    @mcp.tool()
    def get_balance_sheet(symbol: str) -> dict:
        """
        Get annual and quarterly balance sheets for a company.
        Includes total assets, liabilities, equity, cash, debt, and more.

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
        """
        return _fetch({"function": "BALANCE_SHEET", "symbol": symbol})

    @mcp.tool()
    def get_cash_flow(symbol: str) -> dict:
        """
        Get annual and quarterly cash flow statements for a company.
        Includes operating, investing, and financing cash flows.

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
        """
        return _fetch({"function": "CASH_FLOW", "symbol": symbol})

    @mcp.tool()
    def get_earnings(symbol: str) -> dict:
        """
        Get annual and quarterly earnings (EPS) data for a company,
        including reported vs. estimated EPS and surprise percentages.

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
        """
        return _fetch({"function": "EARNINGS", "symbol": symbol})

    @mcp.tool()
    def get_listing_status(
        date: Optional[str] = None,
        state: Optional[str] = "active",
    ) -> dict:
        """
        Get a list of active or delisted US stocks and ETFs.

        Args:
            date: Optional date in YYYY-MM-DD format to query historical listing status
            state: 'active' (default) or 'delisted'
        """
        params: dict = {"function": "LISTING_STATUS", "state": state}
        if date:
            params["date"] = date
        return _fetch(params)

    @mcp.tool()
    def get_earnings_calendar(
        symbol: Optional[str] = None,
        horizon: Optional[str] = "3month",
    ) -> dict:
        """
        Get upcoming earnings release dates for companies.

        Args:
            symbol: Optional ticker to filter for a specific company, e.g. 'IBM'
            horizon: Time horizon: '3month' (default), '6month', or '12month'
        """
        params: dict = {"function": "EARNINGS_CALENDAR", "horizon": horizon}
        if symbol:
            params["symbol"] = symbol
        return _fetch(params)

    @mcp.tool()
    def get_ipo_calendar() -> dict:
        """
        Get upcoming IPO events in the US market for the next 3 months.
        """
        return _fetch({"function": "IPO_CALENDAR"})
