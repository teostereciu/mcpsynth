"""
Alpha Vantage MCP Server
Exposes comprehensive financial data tools via the Model Context Protocol (MCP).
Runs over stdio using FastMCP.
"""

from mcp.server.fastmcp import FastMCP

from generated_tools.time_series import register_time_series_tools
from generated_tools.fundamentals import register_fundamentals_tools
from generated_tools.forex import register_forex_tools
from generated_tools.crypto import register_crypto_tools
from generated_tools.technical_indicators import register_technical_indicators_tools
from generated_tools.economic_indicators import register_economic_indicators_tools
from generated_tools.commodities import register_commodities_tools
from generated_tools.intelligence import register_intelligence_tools
from generated_tools.options import register_options_tools
from generated_tools.sector import register_sector_tools

# ---------------------------------------------------------------------------
# Create the MCP application
# ---------------------------------------------------------------------------
mcp = FastMCP(
    name="alpha-vantage",
    instructions=(
        "This server provides comprehensive financial market data via the Alpha Vantage API. "
        "Available domains: stock time series (intraday/daily/weekly/monthly OHLCV), "
        "real-time quotes, symbol search, forex exchange rates and time series, "
        "cryptocurrency exchange rates and time series, technical indicators (SMA, EMA, WMA, "
        "MACD, RSI, Bollinger Bands, Stochastic, ADX, CCI, Aroon, OBV, ATR), "
        "fundamental data (company overview, ETF profile, income statement, balance sheet, "
        "cash flow, earnings, dividends, splits), economic indicators (GDP, CPI, inflation, "
        "unemployment, treasury yields, federal funds rate, retail sales, nonfarm payroll), "
        "commodities (gold, silver, crude oil, natural gas, copper, wheat, corn, cotton, "
        "sugar, coffee), options data (realtime and historical chains, put-call ratios), "
        "sector performance, and Alpha Intelligence (news sentiment, earnings call transcripts, "
        "top gainers/losers, insider transactions, analytics)."
    ),
)

# ---------------------------------------------------------------------------
# Register all domain tools
# ---------------------------------------------------------------------------
register_time_series_tools(mcp)
register_fundamentals_tools(mcp)
register_forex_tools(mcp)
register_crypto_tools(mcp)
register_technical_indicators_tools(mcp)
register_economic_indicators_tools(mcp)
register_commodities_tools(mcp)
register_intelligence_tools(mcp)
register_options_tools(mcp)
register_sector_tools(mcp)

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    mcp.run(transport="stdio")
