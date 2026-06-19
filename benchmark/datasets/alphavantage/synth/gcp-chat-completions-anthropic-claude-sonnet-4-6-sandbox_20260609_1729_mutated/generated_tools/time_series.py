"""
Stock Time Series tools for Alpha Vantage MCP server.
Source: docs/api_time_series_data.md
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


def register_time_series_tools(mcp: FastMCP):

    @mcp.tool()
    def get_stock_intraday(
        ticker: str,
        time_interval: str,
        adjusted: Optional[str] = None,
        extended_hours: Optional[str] = None,
        month: Optional[str] = None,
        output_size: Optional[str] = None,
    ) -> dict:
        """
        Get intraday OHLCV time series for a stock (20+ years of history).
        Covers pre-market and post-market hours where applicable.

        Args:
            ticker: Equity symbol, e.g. 'IBM'
            time_interval: One of '1min', '5min', '15min', '30min', '60min'
            adjusted: 'true' (default) or 'false' for raw as-traded values
            extended_hours: 'true' (default) includes pre/post market; 'false' for regular hours only
            month: Optional month in YYYY-MM format (e.g. '2009-01') for historical month
            output_size: 'compact' (latest 100, default) or 'full' (trailing 30 days)
        """
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "ticker": ticker,
            "time_interval": time_interval,
        }
        if adjusted is not None:
            params["adjusted"] = adjusted
        if extended_hours is not None:
            params["extended_hours"] = extended_hours
        if month is not None:
            params["month"] = month
        if output_size is not None:
            params["output_size"] = output_size
        return _call(params)

    @mcp.tool()
    def get_stock_daily(
        ticker: str,
        output_size: Optional[str] = None,
    ) -> dict:
        """
        Get raw (as-traded) daily OHLCV time series for a global equity (20+ years).

        Args:
            ticker: Equity symbol, e.g. 'IBM', 'TSCO.LON', 'SHOP.TRT'
            output_size: 'compact' (latest 100, default) or 'full' (20+ years)
        """
        params = {"function": "TIME_SERIES_DAILY", "ticker": ticker}
        if output_size is not None:
            params["output_size"] = output_size
        return _call(params)

    @mcp.tool()
    def get_stock_daily_adjusted(
        ticker: str,
        output_size: Optional[str] = None,
    ) -> dict:
        """
        Get daily OHLCV with adjusted close values and split/dividend events (20+ years).

        Args:
            ticker: Equity symbol, e.g. 'IBM'
            output_size: 'compact' (latest 100, default) or 'full' (20+ years)
        """
        params = {"function": "TIME_SERIES_DAILY_ADJUSTED", "ticker": ticker}
        if output_size is not None:
            params["output_size"] = output_size
        return _call(params)

    @mcp.tool()
    def get_stock_weekly(ticker: str) -> dict:
        """
        Get weekly OHLCV time series for a global equity (20+ years of history).
        The latest data point is the week containing the current trading day.

        Args:
            ticker: Equity symbol, e.g. 'IBM'
        """
        return _call({"function": "TIME_SERIES_WEEKLY", "ticker": ticker})

    @mcp.tool()
    def get_stock_weekly_adjusted(ticker: str) -> dict:
        """
        Get weekly adjusted OHLCV time series with dividend-adjusted close values.

        Args:
            ticker: Equity symbol, e.g. 'IBM'
        """
        return _call({"function": "TIME_SERIES_WEEKLY_ADJUSTED", "ticker": ticker})

    @mcp.tool()
    def get_stock_monthly(ticker: str) -> dict:
        """
        Get monthly OHLCV time series for a global equity (20+ years of history).

        Args:
            ticker: Equity symbol, e.g. 'IBM'
        """
        return _call({"function": "TIME_SERIES_MONTHLY", "ticker": ticker})

    @mcp.tool()
    def get_stock_monthly_adjusted(ticker: str) -> dict:
        """
        Get monthly adjusted OHLCV time series with dividend-adjusted close values.

        Args:
            ticker: Equity symbol, e.g. 'IBM'
        """
        return _call({"function": "TIME_SERIES_MONTHLY_ADJUSTED", "ticker": ticker})

    @mcp.tool()
    def get_stock_quote(ticker: str) -> dict:
        """
        Get the latest price and volume information for a ticker symbol (global quote).

        Args:
            ticker: Equity symbol, e.g. 'IBM'
        """
        return _call({"function": "GLOBAL_QUOTE", "ticker": ticker})

    @mcp.tool()
    def search_ticker(
        keywords: str,
        data_type: Optional[str] = None,
    ) -> dict:
        """
        Search for stock symbols, ETFs, and mutual funds by keyword.

        Args:
            keywords: Search keyword, e.g. 'microsoft' or 'AAPL'
            data_type: Optional filter; 'json' (default) or 'csv'
        """
        params = {"function": "SYMBOL_SEARCH", "keywords": keywords}
        if data_type is not None:
            params["datatype"] = data_type
        return _call(params)

    @mcp.tool()
    def get_market_status() -> dict:
        """
        Get the current market open/close status for major global trading venues.
        """
        return _call({"function": "MARKET_STATUS"})
