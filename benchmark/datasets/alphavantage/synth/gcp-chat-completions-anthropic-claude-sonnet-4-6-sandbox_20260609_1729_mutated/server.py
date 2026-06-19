"""
Alpha Vantage MCP Server
Exposes comprehensive financial data tools via the MCP protocol over stdio.
"""

from mcp.server.fastmcp import FastMCP

from generated_tools.time_series import register_time_series_tools
from generated_tools.forex import register_forex_tools
from generated_tools.crypto import register_crypto_tools
from generated_tools.technical_indicators import register_technical_indicator_tools
from generated_tools.fundamentals import register_fundamental_tools
from generated_tools.economic_indicators import register_economic_indicator_tools
from generated_tools.commodities import register_commodity_tools
from generated_tools.intelligence import register_intelligence_tools
from generated_tools.options import register_options_tools

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
        "RSI, MACD, Bollinger Bands, Stochastic, ADX, CCI, Aroon, ATR, OBV), "
        "fundamental data (company overview, ETF profile, income statement, balance sheet, "
        "cash flow, earnings, dividends, splits), economic indicators (GDP, CPI, inflation, "
        "unemployment, treasury yields, federal funds rate, retail sales, nonfarm payroll), "
        "commodities (gold, silver, crude oil WTI/Brent, natural gas, copper, aluminum, "
        "wheat, corn, cotton, sugar, coffee), options data (realtime & historical chains, "
        "put-call ratio, volume/OI ratio), and Alpha Intelligence (news sentiment, earnings "
        "call transcripts, top gainers/losers, insider transactions, analytics)."
    ),
)

# ---------------------------------------------------------------------------
# Register all domain tools
# ---------------------------------------------------------------------------
register_time_series_tools(mcp)
register_forex_tools(mcp)
register_crypto_tools(mcp)
register_technical_indicator_tools(mcp)
register_fundamental_tools(mcp)
register_economic_indicator_tools(mcp)
register_commodity_tools(mcp)
register_intelligence_tools(mcp)
register_options_tools(mcp)

# ---------------------------------------------------------------------------
# Entry point — runs over stdio for MCP protocol
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    mcp.run(transport="stdio")
