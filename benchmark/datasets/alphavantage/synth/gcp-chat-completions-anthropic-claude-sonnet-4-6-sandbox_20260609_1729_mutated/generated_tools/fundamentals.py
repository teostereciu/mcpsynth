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


def register_fundamental_tools(mcp: FastMCP):

    @mcp.tool()
    def get_company_overview(ticker: str) -> dict:
        """
        Get company information, financial ratios, and key metrics for an equity.
        Data is refreshed on the same day a company reports its latest earnings.

        Args:
            ticker: Equity symbol, e.g. 'IBM'
        """
        return _call({"function": "OVERVIEW", "ticker": ticker})

    @mcp.tool()
    def get_etf_profile(ticker: str) -> dict:
        """
        Get key ETF metrics (net assets, expense ratio, turnover) and holdings/constituents
        with allocation by asset types and sectors.

        Args:
            ticker: ETF symbol, e.g. 'QQQ'
        """
        return _call({"function": "ETF_PROFILE", "ticker": ticker})

    @mcp.tool()
    def get_dividends(ticker: str) -> dict:
        """
        Get historical and future (declared) dividend distributions for a company.

        Args:
            ticker: Equity symbol, e.g. 'IBM'
        """
        return _call({"function": "DIVIDENDS", "ticker": ticker})

    @mcp.tool()
    def get_splits(ticker: str) -> dict:
        """
        Get historical stock split events for a company.

        Args:
            ticker: Equity symbol, e.g. 'IBM'
        """
        return _call({"function": "SPLITS", "ticker": ticker})

    @mcp.tool()
    def get_income_statement(ticker: str) -> dict:
        """
        Get annual and quarterly income statements for a company.

        Args:
            ticker: Equity symbol, e.g. 'IBM'
        """
        return _call({"function": "INCOME_STATEMENT", "ticker": ticker})

    @mcp.tool()
    def get_balance_sheet(ticker: str) -> dict:
        """
        Get annual and quarterly balance sheets for a company.

        Args:
            ticker: Equity symbol, e.g. 'IBM'
        """
        return _call({"function": "BALANCE_SHEET", "ticker": ticker})

    @mcp.tool()
    def get_cash_flow(ticker: str) -> dict:
        """
        Get annual and quarterly cash flow statements for a company.

        Args:
            ticker: Equity symbol, e.g. 'IBM'
        """
        return _call({"function": "CASH_FLOW", "ticker": ticker})

    @mcp.tool()
    def get_earnings(ticker: str) -> dict:
        """
        Get annual and quarterly earnings (EPS) data for a company.

        Args:
            ticker: Equity symbol, e.g. 'IBM'
        """
        return _call({"function": "EARNINGS", "ticker": ticker})

    @mcp.tool()
    def get_listing_status(
        date: Optional[str] = None,
        state: Optional[str] = None,
    ) -> dict:
        """
        Get a list of active or delisted US stocks and ETFs.

        Args:
            date: Optional date in YYYY-MM-DD format to query historical listing status
            state: 'active' (default) or 'delisted'
        """
        params: dict = {"function": "LISTING_STATUS"}
        if date is not None:
            params["date"] = date
        if state is not None:
            params["state"] = state
        return _call(params)

    @mcp.tool()
    def get_earnings_calendar(
        ticker: Optional[str] = None,
        horizon: Optional[str] = None,
    ) -> dict:
        """
        Get upcoming earnings dates for companies (next 3 or 12 months).

        Args:
            ticker: Optional equity symbol to filter results, e.g. 'IBM'
            horizon: '3month' (default) or '6month' or '12month'
        """
        params: dict = {"function": "EARNINGS_CALENDAR"}
        if ticker is not None:
            params["ticker"] = ticker
        if horizon is not None:
            params["horizon"] = horizon
        return _call(params)

    @mcp.tool()
    def get_ipo_calendar() -> dict:
        """
        Get upcoming IPO events for the next 3 months.
        """
        return _call({"function": "IPO_CALENDAR"})
