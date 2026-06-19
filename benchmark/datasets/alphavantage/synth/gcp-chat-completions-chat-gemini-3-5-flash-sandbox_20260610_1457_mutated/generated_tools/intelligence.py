import os
import httpx
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://www.alphavantage.co/query"

def get_api_key():
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
    if not api_key:
        raise ValueError("ALPHAVANTAGE_API_KEY environment variable is not set")
    return api_key

async def make_request(params: dict) -> dict:
    try:
        params["apikey"] = get_api_key()
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(BASE_URL, params=params)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": str(e)}

def register_intelligence_tools(mcp: FastMCP):
    @mcp.tool()
    async def get_news_sentiment(
        tickers: str = None,
        topics: str = None,
        time_from: str = None,
        time_to: str = None,
        sort: str = "LATEST",
        limit: int = 50
    ) -> dict:
        """
        Get live and historical news articles, sentiment scores, and ticker relevance.
        
        Args:
            tickers: Filter by stock ticker(s) (e.g., AAPL or AAPL,MSFT).
            topics: Filter by topic(s) (e.g., technology, earnings, ipo).
            time_from: Start time of the news articles (format: YYYYMMDDTHHMM).
            time_to: End time of the news articles (format: YYYYMMDDTHHMM).
            sort: Sorting order ('LATEST', 'EARLIEST', 'RELEVANCE').
            limit: Number of results to return (max 1000).
        """
        params = {
            "function": "NEWS_SENTIMENT",
            "sort": sort,
            "limit": str(limit)
        }
        if tickers:
            params["tickers"] = tickers
        if topics:
            params["topics"] = topics
        if time_from:
            params["time_from"] = time_from
        if time_to:
            params["time_to"] = time_to
            
        return await make_request(params)

    @mcp.tool()
    async def get_top_gainers_losers() -> dict:
        """
        Get the top gainers, top losers, and most active tickers in the US market.
        """
        params = {
            "function": "TOP_GAINERS_LOSERS"
        }
        return await make_request(params)
