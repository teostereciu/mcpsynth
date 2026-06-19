"""
Alpha Intelligence tools for Alpha Vantage MCP server.
Source: docs/api_intelligence.md
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


def register_intelligence_tools(mcp: FastMCP):

    @mcp.tool()
    def get_news_sentiment(
        tickers: str = "",
        topics: str = "",
        time_from: str = "",
        time_to: str = "",
        sort: str = "LATEST",
        limit: int = 50,
    ) -> dict:
        """
        Return live and historical market news and sentiment data.

        Args:
            tickers: Comma-separated symbols to filter by, e.g. 'IBM' or 'COIN,CRYPTO:BTC'.
            topics: Comma-separated topics, e.g. 'technology' or 'earnings,ipo'.
            time_from: Start datetime in YYYYMMDDTHHMM format, e.g. '20220410T0130'.
            time_to: End datetime in YYYYMMDDTHHMM format.
            sort: 'LATEST' (default), 'EARLIEST', or 'RELEVANCE'.
            limit: Number of results to return (default 50, max 1000).
        """
        params: dict = {"function": "NEWS_SENTIMENT", "sort": sort, "limit": limit}
        if tickers:
            params["tickers"] = tickers
        if topics:
            params["topics"] = topics
        if time_from:
            params["time_from"] = time_from
        if time_to:
            params["time_to"] = time_to
        return _fetch(params)

    @mcp.tool()
    def get_earnings_call_transcript(ticker: str, quarter: str) -> dict:
        """
        Return the earnings call transcript for a company in a specific quarter.

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
            quarter: Fiscal quarter in YYYYQM format, e.g. '2024Q1'.
        """
        params = {
            "function": "EARNINGS_CALL_TRANSCRIPT",
            "symbol": ticker,
            "quarter": quarter,
        }
        return _fetch(params)

    @mcp.tool()
    def get_top_gainers_losers() -> dict:
        """
        Return the top 20 gainers, losers, and most actively traded tickers in the US market.
        """
        params = {"function": "TOP_GAINERS_LOSERS"}
        return _fetch(params)

    @mcp.tool()
    def get_insider_transactions(ticker: str, from_date: str = "") -> dict:
        """
        Return the latest and historical insider transactions for a company.

        Args:
            ticker: Equity symbol, e.g. 'IBM'.
            from_date: Optional start date in YYYY-MM-DD format to filter transactions.
        """
        params = {"function": "INSIDER_TRANSACTIONS", "symbol": ticker}
        if from_date:
            params["from"] = from_date
        return _fetch(params)

    @mcp.tool()
    def get_analytics_fixed_window(
        tickers: str,
        range: str,
        calculations: str,
    ) -> dict:
        """
        Return advanced analytics (e.g. returns, volatility, correlations) over a fixed window.

        Args:
            tickers: Comma-separated symbols, e.g. 'AAPL,MSFT,IBM'.
            range: Date range, e.g. '2month' or 'full' or 'YYYY-MM-DD:YYYY-MM-DD'.
            calculations: Comma-separated analytics, e.g. 'MEAN,VARIANCE,CORRELATION'.
        """
        params = {
            "function": "ANALYTICS_FIXED_WINDOW",
            "TICKERS": tickers,
            "RANGE": range,
            "CALCULATIONS": calculations,
        }
        return _fetch(params)

    @mcp.tool()
    def get_analytics_sliding_window(
        tickers: str,
        range: str,
        calculations: str,
        window_size: int = 20,
    ) -> dict:
        """
        Return advanced analytics computed over a sliding window.

        Args:
            tickers: Comma-separated symbols, e.g. 'AAPL,MSFT'.
            range: Date range, e.g. '6month' or 'YYYY-MM-DD:YYYY-MM-DD'.
            calculations: Comma-separated analytics, e.g. 'MEAN,STDDEV'.
            window_size: Size of the sliding window in trading days (default 20).
        """
        params = {
            "function": "ANALYTICS_SLIDING_WINDOW",
            "TICKERS": tickers,
            "RANGE": range,
            "CALCULATIONS": calculations,
            "WINDOW_SIZE": window_size,
        }
        return _fetch(params)
