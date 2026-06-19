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

def register_options_tools(mcp: FastMCP):
    @mcp.tool()
    async def get_historical_options(symbol: str, date: str = None) -> dict:
        """
        Get historical options chain data for a stock.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
            date: Specific date (YYYY-MM-DD) or month (YYYY-MM) to query. If not specified, returns the latest available options chain.
        """
        params = {
            "function": "HISTORICAL_OPTIONS",
            "symbol": symbol
        }
        if date:
            params["date"] = date
        return await make_request(params)
