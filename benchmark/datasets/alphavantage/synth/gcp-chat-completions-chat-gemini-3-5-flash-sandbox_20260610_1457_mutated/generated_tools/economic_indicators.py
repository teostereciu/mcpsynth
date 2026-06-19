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

def register_economic_indicators_tools(mcp: FastMCP):
    @mcp.tool()
    async def get_real_gdp(interval: str = "quarterly") -> dict:
        """
        Get Real Gross Domestic Product (GDP) of the United States.
        
        Args:
            interval: 'quarterly' or 'annual'.
        """
        params = {
            "function": "REAL_GDP",
            "interval": interval
        }
        return await make_request(params)

    @mcp.tool()
    async def get_real_gdp_per_capita() -> dict:
        """
        Get Real GDP per Capita of the United States.
        """
        params = {
            "function": "REAL_GDP_PER_CAPITA"
        }
        return await make_request(params)

    @mcp.tool()
    async def get_treasury_yield(
        interval: str = "monthly",
        maturity: str = "10year"
    ) -> dict:
        """
        Get US Treasury constant maturity yields.
        
        Args:
            interval: 'daily', 'weekly', or 'monthly'.
            maturity: '3month', '2year', '5year', '7year', '10year', or '30year'.
        """
        params = {
            "function": "TREASURY_YIELD",
            "interval": interval,
            "maturity": maturity
        }
        return await make_request(params)

    @mcp.tool()
    async def get_federal_funds_rate(interval: str = "monthly") -> dict:
        """
        Get the Federal Funds Rate.
        
        Args:
            interval: 'daily', 'weekly', or 'monthly'.
        """
        params = {
            "function": "FEDERAL_FUNDS_RATE",
            "interval": interval
        }
        return await make_request(params)

    @mcp.tool()
    async def get_cpi(interval: str = "monthly") -> dict:
        """
        Get the Consumer Price Index (CPI) for All Urban Consumers.
        
        Args:
            interval: 'monthly' or 'semiannual'.
        """
        params = {
            "function": "CPI",
            "interval": interval
        }
        return await make_request(params)

    @mcp.tool()
    async def get_inflation() -> dict:
        """
        Get the US inflation rate (CPI-U YoY change).
        """
        params = {
            "function": "INFLATION"
        }
        return await make_request(params)

    @mcp.tool()
    async def get_retail_sales() -> dict:
        """
        Get US Retail Sales (Advance Retail Sales: Retail and Food Services).
        """
        params = {
            "function": "RETAIL_SALES"
        }
        return await make_request(params)

    @mcp.tool()
    async def get_durable_goods() -> dict:
        """
        Get US Durable Goods Orders (Manufacturers' Shipments, Inventories, and Orders).
        """
        params = {
            "function": "DURABLE_GOODS"
        }
        return await make_request(params)

    @mcp.tool()
    async def get_unemployment_rate() -> dict:
        """
        Get the US Unemployment Rate.
        """
        params = {
            "function": "UNEMPLOYMENT"
        }
        return await make_request(params)

    @mcp.tool()
    async def get_nonfarm_payroll() -> dict:
        """
        Get US Nonfarm Payrolls (Total Nonfarm Employees).
        """
        params = {
            "function": "NONFARM_PAYROLL"
        }
        return await make_request(params)
