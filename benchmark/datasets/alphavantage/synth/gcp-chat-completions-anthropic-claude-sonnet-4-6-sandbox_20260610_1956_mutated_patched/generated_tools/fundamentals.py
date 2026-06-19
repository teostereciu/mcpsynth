"""
Fundamental Data tools for Alpha Vantage MCP server.
Source: docs/api_fundamentals.md
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


def register_fundamental_tools(mcp: FastMCP):

    @mcp.tool()
    def get_company_overview(ticker: str) -> dict:
        """
        Return company information, financial ratios, and key metrics for an equity.

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
        """
        params = {"function": "OVERVIEW", "symbol": ticker}
        return _fetch(params)

    @mcp.tool()
    def get_etf_profile(ticker: str) -> dict:
        """
        Return key ETF metrics (net assets, expense ratio, turnover) and holdings.

        Args:
            ticker: ETF symbol, e.g. 'QQQ'.
        """
        params = {"function": "ETF_PROFILE", "symbol": ticker}
        return _fetch(params)

    @mcp.tool()
    def get_dividends(ticker: str) -> dict:
        """
        Return historical and future (declared) dividend distributions for an equity.

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
        """
        params = {"function": "DIVIDENDS", "symbol": ticker}
        return _fetch(params)

    @mcp.tool()
    def get_splits(ticker: str) -> dict:
        """
        Return historical stock split events for an equity.

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
        """
        params = {"function": "SPLITS", "symbol": ticker}
        return _fetch(params)

    @mcp.tool()
    def get_income_statement(ticker: str) -> dict:
        """
        Return annual and quarterly income statements for an equity.

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
        """
        params = {"function": "INCOME_STATEMENT", "symbol": ticker}
        return _fetch(params)

    @mcp.tool()
    def get_balance_sheet(ticker: str) -> dict:
        """
        Return annual and quarterly balance sheets for an equity.

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
        """
        params = {"function": "BALANCE_SHEET", "symbol": ticker}
        return _fetch(params)

    @mcp.tool()
    def get_cash_flow(ticker: str) -> dict:
        """
        Return annual and quarterly cash flow statements for an equity.

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
        """
        params = {"function": "CASH_FLOW", "symbol": ticker}
        return _fetch(params)

    @mcp.tool()
    def get_earnings(ticker: str) -> dict:
        """
        Return annual and quarterly earnings (EPS) data for an equity.

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
        """
        params = {"function": "EARNINGS", "symbol": ticker}
        return _fetch(params)

    @mcp.tool()
    def get_earnings_calendar(
        ticker: str = "",
        horizon: str = "3month",
    ) -> dict:
        """
        Return upcoming earnings dates for a specific ticker or the entire market.

        Args:
            ticker: Optional equity symbol to filter results, e.g. 'IBM'.
            horizon: Lookahead window: '3month', '6month', or '12month'.
        """
        params = {"function": "EARNINGS_CALENDAR", "horizon": horizon}
        if ticker:
            params["symbol"] = ticker
        return _fetch(params)

    @mcp.tool()
    def get_ipo_calendar() -> dict:
        """
        Return upcoming IPO events for the next 3 months.
        """
        params = {"function": "IPO_CALENDAR"}
        return _fetch(params)

    @mcp.tool()
    def get_listing_status(
        date: str = "",
        state: str = "active",
    ) -> dict:
        """
        Return a list of active or delisted US stocks and ETFs.

        Args:
            date: Optional date in YYYY-MM-DD format to query historical listing status.
            state: 'active' (default) or 'delisted'.
        """
        params = {"function": "LISTING_STATUS", "state": state}
        if date:
            params["date"] = date
        return _fetch(params)
