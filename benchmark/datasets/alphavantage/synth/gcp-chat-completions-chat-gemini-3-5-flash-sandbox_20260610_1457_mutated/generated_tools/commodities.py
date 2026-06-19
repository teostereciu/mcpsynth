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

def register_commodities_tools(mcp: FastMCP):
    @mcp.tool()
    async def get_crude_oil_wti(interval: str = "monthly") -> dict:
        """
        Get West Texas Intermediate (WTI) crude oil prices.
        
        Args:
            interval: 'daily', 'weekly', or 'monthly'.
        """
        params = {
            "function": "WTI",
            "interval": interval
        }
        return await make_request(params)

    @mcp.tool()
    async def get_crude_oil_brent(interval: str = "monthly") -> dict:
        """
        Get Brent crude oil prices.
        
        Args:
            interval: 'daily', 'weekly', or 'monthly'.
        """
        params = {
            "function": "BRENT",
            "interval": interval
        }
        return await make_request(params)

    @mcp.tool()
    async def get_natural_gas(interval: str = "monthly") -> dict:
        """
        Get Henry Hub natural gas prices.
        
        Args:
            interval: 'daily', 'weekly', or 'monthly'.
        """
        params = {
            "function": "NATURAL_GAS",
            "interval": interval
        }
        return await make_request(params)

    @mcp.tool()
    async def get_copper(interval: str = "monthly") -> dict:
        """
        Get global copper prices.
        
        Args:
            interval: 'daily', 'weekly', or 'monthly'.
        """
        params = {
            "function": "COPPER",
            "interval": interval
        }
        return await make_request(params)

    @mcp.tool()
    async def get_aluminum(interval: str = "monthly") -> dict:
        """
        Get global aluminum prices.
        
        Args:
            interval: 'daily', 'weekly', or 'monthly'.
        """
        params = {
            "function": "ALUMINUM",
            "interval": interval
        }
        return await make_request(params)

    @mcp.tool()
    async def get_wheat(interval: str = "monthly") -> dict:
        """
        Get global wheat prices.
        
        Args:
            interval: 'monthly', 'quarterly', or 'annual'.
        """
        params = {
            "function": "WHEAT",
            "interval": interval
        }
        return await make_request(params)

    @mcp.tool()
    async def get_corn(interval: str = "monthly") -> dict:
        """
        Get global corn prices.
        
        Args:
            interval: 'monthly', 'quarterly', or 'annual'.
        """
        params = {
            "function": "CORN",
            "interval": interval
        }
        return await make_request(params)

    @mcp.tool()
    async def get_cotton(interval: str = "monthly") -> dict:
        """
        Get global cotton prices.
        
        Args:
            interval: 'monthly', 'quarterly', or 'annual'.
        """
        params = {
            "function": "COTTON",
            "interval": interval
        }
        return await make_request(params)

    @mcp.tool()
    async def get_sugar(interval: str = "monthly") -> dict:
        """
        Get global sugar prices.
        
        Args:
            interval: 'monthly', 'quarterly', or 'annual'.
        """
        params = {
            "function": "SUGAR",
            "interval": interval
        }
        return await make_request(params)

    @mcp.tool()
    async def get_coffee(interval: str = "monthly") -> dict:
        """
        Get global coffee prices.
        
        Args:
            interval: 'monthly', 'quarterly', or 'annual'.
        """
        params = {
            "function": "COFFEE",
            "interval": interval
        }
        return await make_request(params)

    @mcp.tool()
    async def get_all_commodities(interval: str = "monthly") -> dict:
        """
        Get Global Price Index of All Commodities.
        
        Args:
            interval: 'monthly', 'quarterly', or 'annual'.
        """
        params = {
            "function": "ALL_COMMODITIES",
            "interval": interval
        }
        return await make_request(params)
