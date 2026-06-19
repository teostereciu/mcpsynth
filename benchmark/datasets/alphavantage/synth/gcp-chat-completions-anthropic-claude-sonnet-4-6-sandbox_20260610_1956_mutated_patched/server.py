"""
Alpha Vantage MCP Server
Runs over stdio using FastMCP and exposes comprehensive financial data tools.
"""

from mcp.server.fastmcp import FastMCP

from generated_tools.time_series import register_time_series_tools
from generated_tools.fx import register_fx_tools
from generated_tools.crypto import register_crypto_tools
from generated_tools.technical_indicators import register_technical_indicator_tools
from generated_tools.fundamentals import register_fundamental_tools
from generated_tools.economic_indicators import register_economic_indicator_tools
from generated_tools.commodities import register_commodity_tools
from generated_tools.intelligence import register_intelligence_tools
from generated_tools.options import register_options_tools
from generated_tools.sector import register_sector_tools

mcp = FastMCP("alpha-vantage")

# Register all domain tool groups
register_time_series_tools(mcp)
register_fx_tools(mcp)
register_crypto_tools(mcp)
register_technical_indicator_tools(mcp)
register_fundamental_tools(mcp)
register_economic_indicator_tools(mcp)
register_commodity_tools(mcp)
register_intelligence_tools(mcp)
register_options_tools(mcp)
register_sector_tools(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")
