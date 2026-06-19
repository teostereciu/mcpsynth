from mcp.server.fastmcp import FastMCP

from generated_tools import stocks, forex, crypto, technical, fundamentals, economics, sector

mcp = FastMCP("alpha-vantage")

# Stocks
mcp.tool()(stocks.stock_intraday)
mcp.tool()(stocks.stock_daily)
mcp.tool()(stocks.stock_daily_adjusted)
mcp.tool()(stocks.stock_weekly)
mcp.tool()(stocks.stock_weekly_adjusted)
mcp.tool()(stocks.stock_monthly)
mcp.tool()(stocks.stock_monthly_adjusted)
mcp.tool()(stocks.global_quote)
mcp.tool()(stocks.symbol_search)

# Forex
mcp.tool()(forex.fx_exchange_rate)
mcp.tool()(forex.fx_daily)
mcp.tool()(forex.fx_weekly)
mcp.tool()(forex.fx_monthly)

# Crypto
mcp.tool()(crypto.crypto_exchange_rate)
mcp.tool()(crypto.crypto_daily)
mcp.tool()(crypto.crypto_weekly)
mcp.tool()(crypto.crypto_monthly)

# Technical indicators
mcp.tool()(technical.sma)
mcp.tool()(technical.ema)
mcp.tool()(technical.rsi)
mcp.tool()(technical.macd)
mcp.tool()(technical.bbands)

# Fundamentals
mcp.tool()(fundamentals.company_overview)
mcp.tool()(fundamentals.income_statement)
mcp.tool()(fundamentals.balance_sheet)
mcp.tool()(fundamentals.earnings)

# Economics
mcp.tool()(economics.cpi)
mcp.tool()(economics.inflation)
mcp.tool()(economics.gdp)
mcp.tool()(economics.unemployment)
mcp.tool()(economics.treasury_yield)
mcp.tool()(economics.federal_funds_rate)
mcp.tool()(economics.retail_sales)
mcp.tool()(economics.durables)
mcp.tool()(economics.nonfarm_payroll)
mcp.tool()(economics.real_gdp_per_capita)
mcp.tool()(economics.treasury_yield_spread)
mcp.tool()(economics.consumer_sentiment)
mcp.tool()(economics.wti)
mcp.tool()(economics.brent)
mcp.tool()(economics.natural_gas)
mcp.tool()(economics.copper)
mcp.tool()(economics.aluminum)
mcp.tool()(economics.wheat)
mcp.tool()(economics.corn)
mcp.tool()(economics.cotton)
mcp.tool()(economics.sugar)
mcp.tool()(economics.coffee)
mcp.tool()(economics.all_commodities)

# Sector
mcp.tool()(sector.sector_performance)


if __name__ == "__main__":
    mcp.run()
