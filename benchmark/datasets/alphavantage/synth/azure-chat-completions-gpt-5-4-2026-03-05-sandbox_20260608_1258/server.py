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

for fn in [
    get_stock_intraday,
    get_stock_daily,
    get_stock_weekly,
    get_stock_monthly,
    get_global_quote,
    search_symbols,
    get_currency_exchange_rate,
    get_fx_intraday,
    get_fx_daily,
    get_fx_weekly,
    get_fx_monthly,
    get_crypto_exchange_rate,
    get_crypto_intraday,
    get_crypto_daily,
    get_crypto_weekly,
    get_crypto_monthly,
    get_company_overview,
    get_etf_profile,
    get_dividends,
    get_splits,
    get_income_statement,
    get_balance_sheet,
    get_cash_flow,
    get_earnings,
    get_earnings_estimates,
    get_earnings_calendar,
    get_real_gdp,
    get_real_gdp_per_capita,
    get_treasury_yield,
    get_federal_funds_rate,
    get_cpi,
    get_inflation,
    get_unemployment,
    get_sma,
    get_ema,
    get_rsi,
    get_macd,
    get_bbands,
    get_gold_silver_spot,
    get_gold_silver_history,
    get_wti,
    get_brent,
    get_natural_gas,
    get_copper,
    get_aluminum,
    get_wheat,
    get_corn,
    get_cotton,
    get_sugar,
    get_coffee,
    get_realtime_options,
    get_realtime_put_call_ratio,
    get_realtime_volume_open_interest_ratio,
    get_historical_options,
    get_news_sentiment,
    get_earnings_call_transcript,
    get_top_gainers_losers,
    get_insider_transactions,
]:
    mcp.tool()(fn)


if __name__ == "__main__":
    mcp.run()
