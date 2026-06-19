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

def register_time_series_tools(mcp: FastMCP):
    @mcp.tool()
    async def get_stock_intraday(
        symbol: str,
        interval: str = "5min",
        adjusted: bool = True,
        extended_hours: bool = True,
        month: str = None,
        outputsize: str = "compact"
    ) -> dict:
        """
        Get intraday OHLCV time series for a stock.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
            interval: Time interval between data points (1min, 5min, 15min, 30min, 60min).
            adjusted: Whether the output should be adjusted for splits.
            extended_hours: Whether to include pre-market and post-market trading hours.
            month: Query historical intraday data for a specific month (format: YYYY-MM).
            outputsize: 'compact' returns 100 data points, 'full' returns trailing 1-2 months of data.
        """
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": interval,
            "adjusted": "true" if adjusted else "false",
            "extended_hours": "true" if extended_hours else "false",
            "outputsize": outputsize
        }
        if month:
            params["month"] = month
        return await make_request(params)

    @mcp.tool()
    async def get_stock_daily(
        symbol: str,
        outputsize: str = "compact"
    ) -> dict:
        """
        Get daily OHLCV time series for a stock (unadjusted).
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
            outputsize: 'compact' returns 100 data points, 'full' returns up to 20+ years of historical data.
        """
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "outputsize": outputsize
        }
        return await make_request(params)

    @mcp.tool()
    async def get_stock_daily_adjusted(
        symbol: str,
        outputsize: str = "compact"
    ) -> dict:
        """
        Get daily adjusted OHLCV time series for a stock (split/dividend adjusted).
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
            outputsize: 'compact' returns 100 data points, 'full' returns up to 20+ years of historical data.
        """
        params = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": symbol,
            "outputsize": outputsize
        }
        return await make_request(params)

    @mcp.tool()
    async def get_stock_weekly(symbol: str) -> dict:
        """
        Get weekly OHLCV time series for a stock.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
        """
        params = {
            "function": "TIME_SERIES_WEEKLY",
            "symbol": symbol
        }
        return await make_request(params)

    @mcp.tool()
    async def get_stock_weekly_adjusted(symbol: str) -> dict:
        """
        Get weekly adjusted OHLCV time series for a stock.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
        """
        params = {
            "function": "TIME_SERIES_WEEKLY_ADJUSTED",
            "symbol": symbol
        }
        return await make_request(params)

    @mcp.tool()
    async def get_stock_monthly(symbol: str) -> dict:
        """
        Get monthly OHLCV time series for a stock.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
        """
        params = {
            "function": "TIME_SERIES_MONTHLY",
            "symbol": symbol
        }
        return await make_request(params)

    @mcp.tool()
    async def get_stock_monthly_adjusted(symbol: str) -> dict:
        """
        Get monthly adjusted OHLCV time series for a stock.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
        """
        params = {
            "function": "TIME_SERIES_MONTHLY_ADJUSTED",
            "symbol": symbol
        }
        return await make_request(params)

    @mcp.tool()
    async def get_stock_quote(symbol: str) -> dict:
        """
        Get a lightweight, real-time quote for a stock.
        
        Args:
            symbol: The stock ticker symbol (e.g., AAPL).
        """
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol
        }
        return await make_request(params)

    @mcp.tool()
    async def search_ticker(keywords: str) -> dict:
        """
        Search for stock symbols and company information matching keywords.
        
        Args:
            keywords: The search term (e.g., 'microsoft' or 'MSFT').
        """
        params = {
            "function": "SYMBOL_SEARCH",
            "keywords": keywords
        }
        return await make_request(params)

    @mcp.tool()
    async def get_market_status() -> dict:
        """
        Get the current open/close status of major global financial markets.
        """
        params = {
            "function": "MARKET_STATUS"
        }
        return await make_request(params)
