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

def register_crypto_tools(mcp: FastMCP):
    @mcp.tool()
    async def get_crypto_intraday(
        symbol: str,
        market: str = "USD",
        interval: str = "5min",
        outputsize: str = "compact"
    ) -> dict:
        """
        Get intraday time series for a cryptocurrency.
        
        Args:
            symbol: The cryptocurrency symbol (e.g., BTC, ETH).
            market: The target market/currency (e.g., USD, EUR).
            interval: Time interval between data points (1min, 5min, 15min, 30min, 60min).
            outputsize: 'compact' returns 100 data points, 'full' returns full intraday data.
        """
        params = {
            "function": "CRYPTO_INTRADAY",
            "symbol": symbol,
            "market": market,
            "interval": interval,
            "outputsize": outputsize
        }
        return await make_request(params)

    @mcp.tool()
    async def get_crypto_daily(symbol: str, market: str = "USD") -> dict:
        """
        Get daily time series for a cryptocurrency.
        
        Args:
            symbol: The cryptocurrency symbol (e.g., BTC, ETH).
            market: The target market/currency (e.g., USD, EUR).
        """
        params = {
            "function": "DIGITAL_CURRENCY_DAILY",
            "symbol": symbol,
            "market": market
        }
        return await make_request(params)

    @mcp.tool()
    async def get_crypto_weekly(symbol: str, market: str = "USD") -> dict:
        """
        Get weekly time series for a cryptocurrency.
        
        Args:
            symbol: The cryptocurrency symbol (e.g., BTC, ETH).
            market: The target market/currency (e.g., USD, EUR).
        """
        params = {
            "function": "DIGITAL_CURRENCY_WEEKLY",
            "symbol": symbol,
            "market": market
        }
        return await make_request(params)

    @mcp.tool()
    async def get_crypto_monthly(symbol: str, market: str = "USD") -> dict:
        """
        Get monthly time series for a cryptocurrency.
        
        Args:
            symbol: The cryptocurrency symbol (e.g., BTC, ETH).
            market: The target market/currency (e.g., USD, EUR).
        """
        params = {
            "function": "DIGITAL_CURRENCY_MONTHLY",
            "symbol": symbol,
            "market": market
        }
        return await make_request(params)
