from mcp.server.fastmcp import FastMCP

from generated_tools.commodities import (
    all_commodities,
    aluminum,
    brent,
    coffee,
    copper,
    corn,
    cotton,
    gold_silver_history,
    gold_silver_spot,
    natural_gas,
    sugar,
    wheat,
    wti,
)
from generated_tools.digital_currency import (
    crypto_intraday,
    digital_currency_daily,
    digital_currency_monthly,
    digital_currency_weekly,
)
from generated_tools.economic_indicators import (
    cpi,
    durables,
    federal_funds_rate,
    inflation,
    nonfarm_payroll,
    real_gdp,
    real_gdp_per_capita,
    retail_sales,
    treasury_yield,
    unemployment,
)
from generated_tools.fundamentals import (
    balance_sheet,
    cash_flow,
    company_overview,
    dividends,
    earnings,
    earnings_calendar,
    earnings_estimates,
    etf_profile,
    income_statement,
    splits,
)
from generated_tools.fx import fx_daily, fx_exchange_rate, fx_intraday, fx_monthly, fx_weekly
from generated_tools.intelligence import (
    earnings_call_transcript,
    insider_transactions,
    news_sentiment,
    top_gainers_losers,
)
from generated_tools.options import (
    historical_options,
    realtime_options,
    realtime_put_call_ratio,
    realtime_volume_open_interest_ratio,
)
from generated_tools.technical_indicators import bbands, ema, macd, rsi, sma
from generated_tools.time_series import (
    market_status,
    sector_performance,
    stock_quote,
    stock_time_series_daily,
    stock_time_series_daily_adjusted,
    stock_time_series_intraday,
    stock_time_series_monthly,
    stock_time_series_monthly_adjusted,
    stock_time_series_weekly,
    stock_time_series_weekly_adjusted,
    symbol_search,
)

mcp = FastMCP("alphavantage")

# --- Time series / utilities ---
mcp.tool()(stock_time_series_intraday)
mcp.tool()(stock_time_series_daily)
mcp.tool()(stock_time_series_daily_adjusted)
mcp.tool()(stock_time_series_weekly)
mcp.tool()(stock_time_series_weekly_adjusted)
mcp.tool()(stock_time_series_monthly)
mcp.tool()(stock_time_series_monthly_adjusted)
mcp.tool()(stock_quote)
mcp.tool()(symbol_search)
mcp.tool()(market_status)
mcp.tool()(sector_performance)

# --- FX ---
mcp.tool()(fx_exchange_rate)
mcp.tool()(fx_intraday)
mcp.tool()(fx_daily)
mcp.tool()(fx_weekly)
mcp.tool()(fx_monthly)

# --- Digital currency ---
mcp.tool()(crypto_intraday)
mcp.tool()(digital_currency_daily)
mcp.tool()(digital_currency_weekly)
mcp.tool()(digital_currency_monthly)

# --- Technical indicators ---
mcp.tool()(sma)
mcp.tool()(ema)
mcp.tool()(rsi)
mcp.tool()(macd)
mcp.tool()(bbands)

# --- Fundamentals ---
mcp.tool()(company_overview)
mcp.tool()(etf_profile)
mcp.tool()(dividends)
mcp.tool()(splits)
mcp.tool()(income_statement)
mcp.tool()(balance_sheet)
mcp.tool()(cash_flow)
mcp.tool()(earnings)
mcp.tool()(earnings_estimates)
mcp.tool()(earnings_calendar)

# --- Economic indicators ---
mcp.tool()(real_gdp)
mcp.tool()(real_gdp_per_capita)
mcp.tool()(treasury_yield)
mcp.tool()(federal_funds_rate)
mcp.tool()(cpi)
mcp.tool()(inflation)
mcp.tool()(unemployment)
mcp.tool()(retail_sales)
mcp.tool()(durables)
mcp.tool()(nonfarm_payroll)

# --- Commodities ---
mcp.tool()(gold_silver_spot)
mcp.tool()(gold_silver_history)
mcp.tool()(wti)
mcp.tool()(brent)
mcp.tool()(natural_gas)
mcp.tool()(copper)
mcp.tool()(aluminum)
mcp.tool()(wheat)
mcp.tool()(corn)
mcp.tool()(cotton)
mcp.tool()(sugar)
mcp.tool()(coffee)
mcp.tool()(all_commodities)

# --- Intelligence ---
mcp.tool()(news_sentiment)
mcp.tool()(earnings_call_transcript)
mcp.tool()(top_gainers_losers)
mcp.tool()(insider_transactions)

# --- Options ---
mcp.tool()(realtime_options)
mcp.tool()(realtime_put_call_ratio)
mcp.tool()(realtime_volume_open_interest_ratio)
mcp.tool()(historical_options)


if __name__ == "__main__":
    mcp.run()
