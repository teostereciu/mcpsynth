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

def register_fx_tools(mcp: FastMCP):
    @mcp.tool()
    async def get_exchange_rate(from_currency: str, to_currency: str) -> dict:
        """
        Get the real-time exchange rate for any pair of digital or physical currencies.
        
        Args:
            from_currency: The currency you want to convert from (e.g., USD, BTC).
            to_currency: The currency you want to convert to (e.g., EUR, JPY).
        """
        params = {
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": from_currency,
            "to_currency": to_currency
        }
        return await make_request(params)

    @mcp.tool()
    async def get_fx_intraday(
        from_symbol: str,
        to_symbol: str,
        interval: str = "5min",
        outputsize: str = "compact"
    ) -> dict:
        """
        Get intraday time series of the foreign exchange (FX) rate.
        
        Args:
            from_symbol: The physical currency you want to convert from (e.g., EUR).
            to_symbol: The physical currency you want to convert to (e.g., USD).
            interval: Time interval between data points (1min, 5min, 15min, 30min, 60min).
            outputsize: 'compact' returns 100 data points, 'full' returns full intraday data.
        """
        params = {
            "function": "FX_INTRADAY",
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
            "interval": interval,
            "outputsize": outputsize
        }
        return await make_request(params)

    @mcp.tool()
    async def get_fx_daily(
        from_symbol: str,
        to_symbol: str,
        outputsize: str = "compact"
    ) -> dict:
        """
        Get daily time series of the foreign exchange (FX) rate.
        
        Args:
            from_symbol: The physical currency you want to convert from (e.g., EUR).
            to_symbol: The physical currency you want to convert to (e.g., USD).
            outputsize: 'compact' returns 100 data points, 'full' returns up to 20+ years of historical data.
        """
        params = {
            "function": "FX_DAILY",
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
            "outputsize": outputsize
        }
        return await make_request(params)

    @mcp.tool()
    async def get_fx_weekly(from_symbol: str, to_symbol: str) -> dict:
        """
        Get weekly time series of the foreign exchange (FX) rate.
        
        Args:
            from_symbol: The physical currency you want to convert from (e.g., EUR).
            to_symbol: The physical currency you want to convert to (e.g., USD).
        """
        params = {
            "function": "FX_WEEKLY",
            "from_symbol": from_symbol,
            "to_symbol": to_symbol
        }
        return await make_request(params)

    @mcp.tool()
    async def get_fx_monthly(from_symbol: str, to_symbol: str) -> dict:
        """
        Get monthly time series of the foreign exchange (FX) rate.
        
        Args:
            from_symbol: The physical currency you want to convert from (e.g., EUR).
            to_symbol: The physical currency you want to convert to (e.g., USD).
        """
        params = {
            "function": "FX_MONTHLY",
            "from_symbol": from_symbol,
            "to_symbol": to_symbol
        }
        return await make_request(params)
