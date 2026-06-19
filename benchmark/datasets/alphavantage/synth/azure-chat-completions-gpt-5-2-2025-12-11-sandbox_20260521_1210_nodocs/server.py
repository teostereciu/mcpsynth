from mcp.server.fastmcp import FastMCP

from generated_tools.stocks import (
    stock_intraday,
    stock_daily,
    stock_daily_adjusted,
    stock_weekly,
    stock_weekly_adjusted,
    stock_monthly,
    stock_monthly_adjusted,
    global_quote,
    symbol_search,
)
from generated_tools.forex import fx_exchange_rate, fx_daily, fx_weekly, fx_monthly
from generated_tools.crypto import crypto_exchange_rate, crypto_daily, crypto_weekly, crypto_monthly
from generated_tools.technical import sma, ema, rsi, macd, bbands
from generated_tools.fundamentals import company_overview, income_statement, balance_sheet, earnings
from generated_tools.economics import cpi, inflation, gdp, unemployment, treasury_yield
from generated_tools.sector import sector_performance

mcp = FastMCP("alphavantage")

# Stocks
mcp.tool()(stock_intraday)
mcp.tool()(stock_daily)
mcp.tool()(stock_daily_adjusted)
mcp.tool()(stock_weekly)
mcp.tool()(stock_weekly_adjusted)
mcp.tool()(stock_monthly)
mcp.tool()(stock_monthly_adjusted)
mcp.tool()(global_quote)
mcp.tool()(symbol_search)

# Forex
mcp.tool()(fx_exchange_rate)
mcp.tool()(fx_daily)
mcp.tool()(fx_weekly)
mcp.tool()(fx_monthly)

# Crypto
mcp.tool()(crypto_exchange_rate)
mcp.tool()(crypto_daily)
mcp.tool()(crypto_weekly)
mcp.tool()(crypto_monthly)

# Technical indicators
mcp.tool()(sma)
mcp.tool()(ema)
mcp.tool()(rsi)
mcp.tool()(macd)
mcp.tool()(bbands)

# Fundamentals
mcp.tool()(company_overview)
mcp.tool()(income_statement)
mcp.tool()(balance_sheet)
mcp.tool()(earnings)

# Economics
mcp.tool()(cpi)
mcp.tool()(inflation)
mcp.tool()(gdp)
mcp.tool()(unemployment)
mcp.tool()(treasury_yield)

# Sector
mcp.tool()(sector_performance)


if __name__ == "__main__":
    mcp.run()
