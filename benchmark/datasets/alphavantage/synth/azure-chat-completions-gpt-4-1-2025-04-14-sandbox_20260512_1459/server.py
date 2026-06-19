import os
from mcp.server.fastmcp import FastMCP
import generated_tools.time_series as time_series
import generated_tools.fx as fx
import generated_tools.digital_currency as digital_currency
import generated_tools.technical_indicators as technical_indicators
import generated_tools.fundamentals as fundamentals
import generated_tools.economic_indicators as economic_indicators
import generated_tools.commodities as commodities

TOOLS = {
    "get_intraday_time_series": time_series.get_intraday_time_series,
    "get_daily_time_series": time_series.get_daily_time_series,
    "get_daily_adjusted_time_series": time_series.get_daily_adjusted_time_series,
    "get_currency_exchange_rate": fx.get_currency_exchange_rate,
    "get_fx_intraday": fx.get_fx_intraday,
    "get_fx_daily": fx.get_fx_daily,
    "get_crypto_exchange_rate": digital_currency.get_crypto_exchange_rate,
    "get_crypto_intraday": digital_currency.get_crypto_intraday,
    "get_crypto_daily": digital_currency.get_crypto_daily,
    "get_sma": technical_indicators.get_sma,
    "get_ema": technical_indicators.get_ema,
    "get_company_overview": fundamentals.get_company_overview,
    "get_etf_profile": fundamentals.get_etf_profile,
    "get_dividends": fundamentals.get_dividends,
    "get_splits": fundamentals.get_splits,
    "get_real_gdp": economic_indicators.get_real_gdp,
    "get_real_gdp_per_capita": economic_indicators.get_real_gdp_per_capita,
    "get_treasury_yield": economic_indicators.get_treasury_yield,
    "get_federal_funds_rate": economic_indicators.get_federal_funds_rate,
    "get_gold_silver_spot": commodities.get_gold_silver_spot,
    "get_gold_silver_history": commodities.get_gold_silver_history,
    "get_wti_crude_oil": commodities.get_wti_crude_oil,
    "get_brent_crude_oil": commodities.get_brent_crude_oil,
}

def list_tools():
    """Return all available tool names."""
    return list(TOOLS.keys())

class MCPAlphaVantageServer(FastMCP):
    def list_tools(self):
        return list_tools()

    def call_tool(self, tool_name, params):
        tool = TOOLS.get(tool_name)
        if not tool:
            return {"error": f"Tool '{tool_name}' not found."}
        try:
            return tool(**params)
        except Exception as e:
            return {"error": str(e)}

if __name__ == "__main__":
    MCPAlphaVantageServer().run_stdio()
