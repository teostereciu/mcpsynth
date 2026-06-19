from mcp.server.fastmcp import FastMCP

from generated_tools.commodities import *
from generated_tools.crypto import *
from generated_tools.economic import *
from generated_tools.fundamentals import *
from generated_tools.fx import *
from generated_tools.intelligence import *
from generated_tools.options import *
from generated_tools.technical import *
from generated_tools.time_series import *

mcp = FastMCP("alphavantage")


mcp.tool()(get_stock_intraday)
mcp.tool()(get_stock_daily)
mcp.tool()(get_stock_daily_adjusted)
mcp.tool()(get_stock_weekly)
mcp.tool()(get_stock_weekly_adjusted)
mcp.tool()(get_stock_monthly)
mcp.tool()(get_stock_monthly_adjusted)
mcp.tool()(get_global_quote)
mcp.tool()(search_symbols)

mcp.tool()(get_currency_exchange_rate)
mcp.tool()(get_fx_intraday)
mcp.tool()(get_fx_daily)
mcp.tool()(get_fx_weekly)
mcp.tool()(get_fx_monthly)

mcp.tool()(get_crypto_intraday)
mcp.tool()(get_digital_currency_daily)
mcp.tool()(get_digital_currency_weekly)
mcp.tool()(get_digital_currency_monthly)

mcp.tool()(get_sma)
mcp.tool()(get_ema)
mcp.tool()(get_rsi)
mcp.tool()(get_macd)
mcp.tool()(get_bbands)

mcp.tool()(get_company_overview)
mcp.tool()(get_etf_profile)
mcp.tool()(get_dividends)
mcp.tool()(get_splits)
mcp.tool()(get_income_statement)
mcp.tool()(get_balance_sheet)
mcp.tool()(get_cash_flow)
mcp.tool()(get_earnings)
mcp.tool()(get_earnings_estimates)
mcp.tool()(get_earnings_calendar)
mcp.tool()(get_listing_status)
mcp.tool()(get_ipo_calendar)

mcp.tool()(get_real_gdp)
mcp.tool()(get_real_gdp_per_capita)
mcp.tool()(get_treasury_yield)
mcp.tool()(get_federal_funds_rate)
mcp.tool()(get_cpi)
mcp.tool()(get_inflation)
mcp.tool()(get_retail_sales)
mcp.tool()(get_durables)
mcp.tool()(get_unemployment)
mcp.tool()(get_nonfarm_payroll)

mcp.tool()(get_gold_silver_spot)
mcp.tool()(get_gold_silver_history)
mcp.tool()(get_wti)
mcp.tool()(get_brent)
mcp.tool()(get_natural_gas)
mcp.tool()(get_copper)
mcp.tool()(get_aluminum)
mcp.tool()(get_wheat)
mcp.tool()(get_corn)
mcp.tool()(get_cotton)
mcp.tool()(get_sugar)
mcp.tool()(get_coffee)

mcp.tool()(get_realtime_options)
mcp.tool()(get_realtime_put_call_ratio)
mcp.tool()(get_realtime_volume_open_interest_ratio)
mcp.tool()(get_historical_options)

mcp.tool()(get_news_sentiment)
mcp.tool()(get_earnings_call_transcript)
mcp.tool()(get_top_gainers_losers)
mcp.tool()(get_insider_transactions)


if __name__ == "__main__":
    mcp.run()
