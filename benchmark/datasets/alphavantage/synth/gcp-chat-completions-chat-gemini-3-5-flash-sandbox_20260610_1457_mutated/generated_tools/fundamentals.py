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

def register_fundamentals_tools(mcp: FastMCP):
    @mcp.tool()
    async def get_company_overview(symbol: str) -> dict:
        """
        Get company information, financial ratios, and other key metrics for a stock.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
        """
        params = {
            "function": "OVERVIEW",
            "symbol": symbol
        }
        return await make_request(params)

    @mcp.tool()
    async def get_income_statement(symbol: str) -> dict:
        """
        Get annual and quarterly income statements for a company.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
        """
        params = {
            "function": "INCOME_STATEMENT",
            "symbol": symbol
        }
        return await make_request(params)

    @mcp.tool()
    async def get_balance_sheet(symbol: str) -> dict:
        """
        Get annual and quarterly balance sheets for a company.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
        """
        params = {
            "function": "BALANCE_SHEET",
            "symbol": symbol
        }
        return await make_request(params)

    @mcp.tool()
    async def get_cash_flow(symbol: str) -> dict:
        """
        Get annual and quarterly cash flow statements for a company.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
        """
        params = {
            "function": "CASH_FLOW",
            "symbol": symbol
        }
        return await make_request(params)

    @mcp.tool()
    async def get_earnings(symbol: str) -> dict:
        """
        Get annual and quarterly earnings (EPS) data for a company.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
        """
        params = {
            "function": "EARNINGS",
            "symbol": symbol
        }
        return await make_request(params)

    @mcp.tool()
    async def get_listing_status(state: str = "active", date: str = None) -> dict:
        """
        Get the list of active or delisted stocks/ETFs.
        Note: This endpoint returns CSV data.
        
        Args:
            state: 'active' or 'delisted'.
            date: Specific date (YYYY-MM-DD) to query listing status.
        """
        params = {
            "function": "LISTING_STATUS",
            "state": state
        }
        if date:
            params["date"] = date
        
        # Since this returns CSV, we handle it separately
        try:
            params["apikey"] = get_api_key()
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.get(BASE_URL, params=params)
                response.raise_for_status()
                # Return as text or parse CSV
                return {"csv_data": response.text}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    async def get_earnings_calendar(symbol: str = None, horizon: str = "3month") -> dict:
        """
        Get the earnings calendar for the next 3, 6, or 12 months.
        Note: This endpoint returns CSV data.
        
        Args:
            symbol: Optional stock ticker symbol to filter.
            horizon: '3month', '6month', or '12month'.
        """
        params = {
            "function": "EARNINGS_CALENDAR",
            "horizon": horizon
        }
        if symbol:
            params["symbol"] = symbol
            
        try:
            params["apikey"] = get_api_key()
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.get(BASE_URL, params=params)
                response.raise_for_status()
                return {"csv_data": response.text}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    async def get_ipo_calendar() -> dict:
        """
        Get the list of upcoming IPOs.
        Note: This endpoint returns CSV data.
        """
        params = {
            "function": "IPO_CALENDAR"
        }
        try:
            params["apikey"] = get_api_key()
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.get(BASE_URL, params=params)
                response.raise_for_status()
                return {"csv_data": response.text}
        except Exception as e:
            return {"error": str(e)}
