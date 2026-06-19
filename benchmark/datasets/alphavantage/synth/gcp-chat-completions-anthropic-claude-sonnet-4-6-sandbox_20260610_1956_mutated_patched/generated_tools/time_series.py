"""
Stock Time Series tools for Alpha Vantage MCP server.
Source: docs/api_time_series_data.md
"""

import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://www.alphavantage.co/query"


def _get_api_key() -> str:
    key = os.environ.get("ALPHAVANTAGE_API_KEY", "")
    return key


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


def register_time_series_tools(mcp: FastMCP):

    @mcp.tool()
    def get_stock_intraday(
        ticker: str,
        time_interval: str,
        adjusted: bool = True,
        extended_hours: bool = True,
        month: str = "",
        output_size: str = "compact",
    ) -> dict:
        """
        Return intraday OHLCV time series for a given equity.

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
            time_interval: One of '1min', '5min', '15min', '30min', '60min'.
            adjusted: If True (default), data is split/dividend-adjusted.
            extended_hours: If True (default), includes pre/post-market hours.
            month: Optional month in YYYY-MM format for historical intraday data.
            output_size: 'compact' (latest 100 bars) or 'full' (trailing 30 days).
        """
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": ticker,
            "interval": time_interval,
            "adjusted": "true" if adjusted else "false",
            "extended_hours": "true" if extended_hours else "false",
            "outputsize": output_size,
        }
        if month:
            params["month"] = month
        return _fetch(params)

    @mcp.tool()
    def get_stock_daily(
        ticker: str,
        output_size: str = "compact",
    ) -> dict:
        """
        Return raw (as-traded) daily OHLCV time series for a global equity.

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
            output_size: 'compact' (latest 100 data points) or 'full' (20+ years).
        """
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": ticker,
            "outputsize": output_size,
        }
        return _fetch(params)

    @mcp.tool()
    def get_stock_daily_adjusted(
        ticker: str,
        output_size: str = "compact",
    ) -> dict:
        """
        Return daily OHLCV data with adjusted close, split and dividend events.

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
            output_size: 'compact' (latest 100 data points) or 'full' (20+ years).
        """
        params = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": ticker,
            "outputsize": output_size,
        }
        return _fetch(params)

    @mcp.tool()
    def get_stock_weekly(ticker: str) -> dict:
        """
        Return weekly OHLCV time series for a global equity (20+ years of history).

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
        """
        params = {
            "function": "TIME_SERIES_WEEKLY",
            "symbol": ticker,
        }
        return _fetch(params)

    @mcp.tool()
    def get_stock_weekly_adjusted(ticker: str) -> dict:
        """
        Return weekly adjusted OHLCV time series including dividend-adjusted close.

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
        """
        params = {
            "function": "TIME_SERIES_WEEKLY_ADJUSTED",
            "symbol": ticker,
        }
        return _fetch(params)

    @mcp.tool()
    def get_stock_monthly(ticker: str) -> dict:
        """
        Return monthly OHLCV time series for a global equity (20+ years of history).

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
        """
        params = {
            "function": "TIME_SERIES_MONTHLY",
            "symbol": ticker,
        }
        return _fetch(params)

    @mcp.tool()
    def get_stock_monthly_adjusted(ticker: str) -> dict:
        """
        Return monthly adjusted OHLCV time series including dividend-adjusted close.

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
        """
        params = {
            "function": "TIME_SERIES_MONTHLY_ADJUSTED",
            "symbol": ticker,
        }
        return _fetch(params)

    @mcp.tool()
    def get_stock_quote(ticker: str) -> dict:
        """
        Return the latest price and volume information for a ticker (global quote).

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
        """
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": ticker,
        }
        return _fetch(params)

    @mcp.tool()
    def search_ticker(keywords: str) -> dict:
        """
        Search for stock symbols / tickers by keyword.

        Args:
            keywords: Search keywords, e.g. 'Microsoft' or 'AAPL'.
        """
        params = {
            "function": "SYMBOL_SEARCH",
            "keywords": keywords,
        }
        return _fetch(params)

    @mcp.tool()
    def get_market_status() -> dict:
        """
        Return the current market open/close status for major global trading venues.
        """
        params = {"function": "MARKET_STATUS"}
        return _fetch(params)
