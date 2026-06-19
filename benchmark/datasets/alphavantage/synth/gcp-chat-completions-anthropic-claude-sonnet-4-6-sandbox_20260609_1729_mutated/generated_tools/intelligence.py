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


def register_intelligence_tools(mcp: FastMCP):

    @mcp.tool()
    def get_news_sentiment(
        tickers: Optional[str] = None,
        topics: Optional[str] = None,
        time_from: Optional[str] = None,
        time_to: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> dict:
        """
        Get live and historical market news & sentiment data from premier news outlets.
        Covers stocks, cryptocurrencies, forex, and topics like fiscal policy, M&A, IPOs.

        Args:
            tickers: Comma-separated symbols to filter, e.g. 'IBM' or 'COIN,CRYPTO:BTC,FOREX:USD'
            topics: Comma-separated topics, e.g. 'technology' or 'technology,ipo'.
                    Supported: blockchain, earnings, ipo, mergers_and_acquisitions,
                    financial_markets, economy_fiscal, economy_monetary, economy_macro,
                    energy_transportation, finance, life_sciences, manufacturing,
                    real_estate, retail_wholesale, technology
            time_from: Start time in YYYYMMDDTHHMM format, e.g. '20220410T0130'
            time_to: End time in YYYYMMDDTHHMM format
            sort: 'LATEST' (default), 'EARLIEST', or 'RELEVANCE'
            limit: Max results to return (default 50, max 1000)
        """
        params: dict = {"function": "NEWS_SENTIMENT"}
        if tickers is not None:
            params["tickers"] = tickers
        if topics is not None:
            params["topics"] = topics
        if time_from is not None:
            params["time_from"] = time_from
        if time_to is not None:
            params["time_to"] = time_to
        if sort is not None:
            params["sort"] = sort
        if limit is not None:
            params["limit"] = limit
        return _call(params)

    @mcp.tool()
    def get_earnings_call_transcript(ticker: str, quarter: str) -> dict:
        """
        Get the earnings call transcript for a company in a specific quarter.
        Covers 15+ years of history with LLM-based sentiment signals.

        Args:
            ticker: Equity symbol, e.g. 'IBM'
            quarter: Fiscal quarter in YYYYQM format, e.g. '2024Q1' (supported since 2010Q1)
        """
        return _call({
            "function": "EARNINGS_CALL_TRANSCRIPT",
            "ticker": ticker,
            "quarter": quarter,
        })

    @mcp.tool()
    def get_top_gainers_losers() -> dict:
        """
        Get the top 20 gainers, losers, and most actively traded tickers in the US market.
        """
        return _call({"function": "TOP_GAINERS_LOSERS"})

    @mcp.tool()
    def get_insider_transactions(ticker: str) -> dict:
        """
        Get the latest and historical insider transactions for a specific company.
        Covers key stakeholders such as founders, executives, and board members.

        Args:
            ticker: Equity symbol, e.g. 'IBM'
        """
        return _call({"function": "INSIDER_TRANSACTIONS", "ticker": ticker})

    @mcp.tool()
    def get_analytics_fixed_window(
        ticker: str,
        range: str,
        ohlcv: str,
        calculations: str,
    ) -> dict:
        """
        Get advanced analytics (mean, variance, etc.) for a ticker over a fixed time window.

        Args:
            ticker: Equity symbol, e.g. 'AAPL'
            range: Date range in YYYY-MM-DD:YYYY-MM-DD format, e.g. '2023-01-01:2023-12-31'
            ohlcv: Price type: 'open', 'high', 'low', 'close', or 'volume'
            calculations: Comma-separated analytics, e.g. 'MEAN,VARIANCE,COVARIANCE'
        """
        return _call({
            "function": "ANALYTICS_FIXED_WINDOW",
            "TICKER": ticker,
            "RANGE": range,
            "OHLCV": ohlcv,
            "CALCULATIONS": calculations,
        })

    @mcp.tool()
    def get_analytics_sliding_window(
        ticker: str,
        range: str,
        ohlcv: str,
        window_size: int,
        calculations: str,
    ) -> dict:
        """
        Get advanced analytics for a ticker using a sliding time window.

        Args:
            ticker: Equity symbol, e.g. 'AAPL'
            range: Date range in YYYY-MM-DD:YYYY-MM-DD format, e.g. '2023-01-01:2023-12-31'
            ohlcv: Price type: 'open', 'high', 'low', 'close', or 'volume'
            window_size: Number of data points in each sliding window, e.g. 20
            calculations: Comma-separated analytics, e.g. 'MEAN,VARIANCE'
        """
        return _call({
            "function": "ANALYTICS_SLIDING_WINDOW",
            "TICKER": ticker,
            "RANGE": range,
            "OHLCV": ohlcv,
            "WINDOW_SIZE": window_size,
            "CALCULATIONS": calculations,
        })
