from mcp.server.fastmcp import FastMCP
from generated_tools.time_series import register_time_series_tools
from generated_tools.fundamentals import register_fundamentals_tools
from generated_tools.fx import register_fx_tools
from generated_tools.crypto import register_crypto_tools
from generated_tools.economic_indicators import register_economic_indicators_tools
from generated_tools.commodities import register_commodities_tools
from generated_tools.technical_indicators import register_technical_indicators_tools
from generated_tools.intelligence import register_intelligence_tools
from generated_tools.options import register_options_tools

# Create the FastMCP server
mcp = FastMCP("Alpha Vantage MCP Server")

# Register all tools
register_time_series_tools(mcp)
register_fundamentals_tools(mcp)
register_fx_tools(mcp)
register_crypto_tools(mcp)
register_economic_indicators_tools(mcp)
register_commodities_tools(mcp)
register_technical_indicators_tools(mcp)
register_intelligence_tools(mcp)
register_options_tools(mcp)

if __name__ == "__main__":
    mcp.run()
