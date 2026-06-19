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


def register_time_series_tools(mcp: FastMCP):

    @mcp.tool()
    def get_stock_intraday(
        symbol: str,
        interval: str,
        adjusted: Optional[bool] = True,
        extended_hours: Optional[bool] = True,
        month: Optional[str] = None,
        outputsize: Optional[str] = "compact",
    ) -> dict:
        """
        Get intraday OHLCV time series for a stock symbol (20+ years of history).
        Covers pre-market and post-market hours where applicable.

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
            interval: Time interval between data points: '1min', '5min', '15min', '30min', '60min'
            adjusted: If True (default), output is adjusted for splits/dividends
            extended_hours: If True (default), includes pre/post-market hours
            month: Optional month in YYYY-MM format to query a specific historical month
            outputsize: 'compact' (latest 100 points) or 'full' (trailing 30 days or full month)
        """
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": interval,
            "adjusted": str(adjusted).lower(),
            "extended_hours": str(extended_hours).lower(),
            "outputsize": outputsize,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_stock_daily(
        symbol: str,
        outputsize: Optional[str] = "compact",
    ) -> dict:
        """
        Get raw (as-traded) daily OHLCV time series for a global equity (20+ years of history).

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM', 'TSCO.LON', 'SHOP.TRT'
            outputsize: 'compact' (latest 100 data points) or 'full' (full 20+ year history)
        """
        return _fetch({
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "outputsize": outputsize,
        })

    @mcp.tool()
    def get_stock_daily_adjusted(
        symbol: str,
        outputsize: Optional[str] = "compact",
    ) -> dict:
        """
        Get daily OHLCV time series with adjusted close values and split/dividend events (20+ years).

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
            outputsize: 'compact' (latest 100 data points) or 'full' (full 20+ year history)
        """
        return _fetch({
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": symbol,
            "outputsize": outputsize,
        })

    @mcp.tool()
    def get_stock_weekly(symbol: str) -> dict:
        """
        Get weekly OHLCV time series for a global equity (20+ years of history).
        Each data point covers the week ending on the given date.

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
        """
        return _fetch({
            "function": "TIME_SERIES_WEEKLY",
            "symbol": symbol,
        })

    @mcp.tool()
    def get_stock_weekly_adjusted(symbol: str) -> dict:
        """
        Get weekly adjusted OHLCV time series including adjusted close and dividend amounts.

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
        """
        return _fetch({
            "function": "TIME_SERIES_WEEKLY_ADJUSTED",
            "symbol": symbol,
        })

    @mcp.tool()
    def get_stock_monthly(symbol: str) -> dict:
        """
        Get monthly OHLCV time series for a global equity (20+ years of history).
        Each data point covers the month ending on the given date.

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
        """
        return _fetch({
            "function": "TIME_SERIES_MONTHLY",
            "symbol": symbol,
        })

    @mcp.tool()
    def get_stock_monthly_adjusted(symbol: str) -> dict:
        """
        Get monthly adjusted OHLCV time series including adjusted close and dividend amounts.

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
        """
        return _fetch({
            "function": "TIME_SERIES_MONTHLY_ADJUSTED",
            "symbol": symbol,
        })

    @mcp.tool()
    def get_stock_quote(symbol: str) -> dict:
        """
        Get the latest price and volume information for a stock ticker (global quote).

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
        """
        return _fetch({
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
        })

    @mcp.tool()
    def search_ticker(keywords: str) -> dict:
        """
        Search for stock symbols and company names matching the given keywords.
        Returns best-matching symbols and market information.

        Args:
            keywords: Search keywords, e.g. 'Microsoft', 'AAPL', 'Tesla'
        """
        return _fetch({
            "function": "SYMBOL_SEARCH",
            "keywords": keywords,
        })

    @mcp.tool()
    def get_market_status() -> dict:
        """
        Get the current market open/closed status for major trading venues worldwide.
        """
        return _fetch({
            "function": "MARKET_STATUS",
        })
