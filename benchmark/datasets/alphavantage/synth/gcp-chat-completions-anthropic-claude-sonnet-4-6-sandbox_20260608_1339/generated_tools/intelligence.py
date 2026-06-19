"""
Alpha Intelligence tools for Alpha Vantage MCP server.
Source: docs/api_intelligence.md
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


def register_intelligence_tools(mcp: FastMCP):

    @mcp.tool()
    def get_news_sentiment(
        tickers: Optional[str] = None,
        topics: Optional[str] = None,
        time_from: Optional[str] = None,
        time_to: Optional[str] = None,
        sort: Optional[str] = "LATEST",
        limit: Optional[int] = 50,
    ) -> dict:
        """
        Get live and historical market news and sentiment data from premier news outlets.
        Covers stocks, cryptocurrencies, forex, and topics like fiscal policy, M&A, IPOs.

        Args:
            tickers: Comma-separated ticker symbols to filter by, e.g. 'IBM' or 'COIN,CRYPTO:BTC,FOREX:USD'
            topics: Comma-separated topics to filter by, e.g. 'technology,ipo'.
                    Supported: blockchain, earnings, ipo, mergers_and_acquisitions,
                    financial_markets, economy_fiscal, economy_monetary, economy_macro,
                    energy_transportation, finance, life_sciences, manufacturing,
                    real_estate, retail_wholesale, technology
            time_from: Start time in YYYYMMDDTHHMM format, e.g. '20220410T0130'
            time_to: End time in YYYYMMDDTHHMM format
            sort: 'LATEST' (default), 'EARLIEST', or 'RELEVANCE'
            limit: Number of results to return (default 50, max 1000)
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
    def get_earnings_call_transcript(symbol: str, quarter: str) -> dict:
        """
        Get the earnings call transcript for a company in a specific quarter.
        Covers 15+ years of history, enriched with LLM-based sentiment signals.

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
            quarter: Fiscal quarter in YYYYQM format, e.g. '2024Q1'. Supported since 2010Q1.
        """
        return _fetch({
            "function": "EARNINGS_CALL_TRANSCRIPT",
            "symbol": symbol,
            "quarter": quarter,
        })

    @mcp.tool()
    def get_top_gainers_losers() -> dict:
        """
        Get the top 20 gainers, losers, and most actively traded tickers in the US market.
        Data is updated at the end of each trading day.
        """
        return _fetch({"function": "TOP_GAINERS_LOSERS"})

    @mcp.tool()
    def get_insider_transactions(symbol: str, from_date: Optional[str] = None) -> dict:
        """
        Get the latest and historical insider transactions for a specific company.
        Covers transactions by founders, executives, board members, and other key stakeholders.

        Args:
            symbol: Equity ticker symbol, e.g. 'IBM'
            from_date: Optional date filter in YYYY-MM-DD format to return transactions on or after this date
        """
        params: dict = {"function": "INSIDER_TRANSACTIONS", "symbol": symbol}
        if from_date:
            params["from"] = from_date
        return _fetch(params)

    @mcp.tool()
    def get_analytics_fixed_window(
        symbols: str,
        range: str,
        ohlc: str,
        calculations: str,
    ) -> dict:
        """
        Get advanced analytics (returns, correlations, volatility, etc.) for one or more
        equities over a fixed time window.

        Args:
            symbols: Comma-separated ticker symbols, e.g. 'IBM,AAPL,MSFT'
            range: Time range, e.g. '6month', '1year', '2year', or a date range like '2020-01-01&2021-01-01'
            ohlc: Price type to use: 'open', 'high', 'low', 'close'
            calculations: Comma-separated analytics to compute, e.g. 'MEAN,VARIANCE,CORRELATION'
        """
        return _fetch({
            "function": "ANALYTICS_FIXED_WINDOW",
            "SYMBOLS": symbols,
            "RANGE": range,
            "OHLC": ohlc,
            "CALCULATIONS": calculations,
        })

    @mcp.tool()
    def get_analytics_sliding_window(
        symbols: str,
        range: str,
        ohlc: str,
        window_size: int,
        calculations: str,
    ) -> dict:
        """
        Get advanced analytics computed over a sliding (rolling) window for one or more equities.

        Args:
            symbols: Comma-separated ticker symbols, e.g. 'IBM,AAPL'
            range: Time range, e.g. '6month', '1year'
            ohlc: Price type to use: 'open', 'high', 'low', 'close'
            window_size: Size of the sliding window in trading days, e.g. 20
            calculations: Comma-separated analytics to compute, e.g. 'MEAN,VARIANCE'
        """
        return _fetch({
            "function": "ANALYTICS_SLIDING_WINDOW",
            "SYMBOLS": symbols,
            "RANGE": range,
            "OHLC": ohlc,
            "WINDOW_SIZE": window_size,
            "CALCULATIONS": calculations,
        })
