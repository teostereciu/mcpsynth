import os
from typing import Any, Dict

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
    federal_funds_rate,
    inflation,
    real_gdp,
    real_gdp_per_capita,
    treasury_yield,
    unemployment,
)
from generated_tools.fundamentals import (
    balance_sheet,
    cash_flow,
    company_overview,
    dividends,
    earnings,
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
from generated_tools.technical_indicators import bollinger_bands, ema, macd, rsi, sma
from generated_tools.time_series import (
    market_status,
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


@mcp.tool()
def alphavantage_api_key_status() -> Dict[str, Any]:
    """Check whether ALPHAVANTAGE_API_KEY is set."""
    return {"configured": bool(os.getenv("ALPHAVANTAGE_API_KEY"))}


# --- Time series ---
@mcp.tool()
def stock_time_series_intraday_tool(**kwargs):
    return stock_time_series_intraday(**kwargs)


@mcp.tool()
def stock_time_series_daily_tool(**kwargs):
    return stock_time_series_daily(**kwargs)


@mcp.tool()
def stock_time_series_daily_adjusted_tool(**kwargs):
    return stock_time_series_daily_adjusted(**kwargs)


@mcp.tool()
def stock_time_series_weekly_tool(**kwargs):
    return stock_time_series_weekly(**kwargs)


@mcp.tool()
def stock_time_series_weekly_adjusted_tool(**kwargs):
    return stock_time_series_weekly_adjusted(**kwargs)


@mcp.tool()
def stock_time_series_monthly_tool(**kwargs):
    return stock_time_series_monthly(**kwargs)


@mcp.tool()
def stock_time_series_monthly_adjusted_tool(**kwargs):
    return stock_time_series_monthly_adjusted(**kwargs)


@mcp.tool()
def stock_quote_tool(**kwargs):
    return stock_quote(**kwargs)


@mcp.tool()
def symbol_search_tool(**kwargs):
    return symbol_search(**kwargs)


@mcp.tool()
def market_status_tool():
    return market_status()


# --- FX ---
@mcp.tool()
def fx_exchange_rate_tool(**kwargs):
    return fx_exchange_rate(**kwargs)


@mcp.tool()
def fx_intraday_tool(**kwargs):
    return fx_intraday(**kwargs)


@mcp.tool()
def fx_daily_tool(**kwargs):
    return fx_daily(**kwargs)


@mcp.tool()
def fx_weekly_tool(**kwargs):
    return fx_weekly(**kwargs)


@mcp.tool()
def fx_monthly_tool(**kwargs):
    return fx_monthly(**kwargs)


# --- Digital currency ---
@mcp.tool()
def crypto_intraday_tool(**kwargs):
    return crypto_intraday(**kwargs)


@mcp.tool()
def digital_currency_daily_tool(**kwargs):
    return digital_currency_daily(**kwargs)


@mcp.tool()
def digital_currency_weekly_tool(**kwargs):
    return digital_currency_weekly(**kwargs)


@mcp.tool()
def digital_currency_monthly_tool(**kwargs):
    return digital_currency_monthly(**kwargs)


# --- Technical indicators ---
@mcp.tool()
def sma_tool(**kwargs):
    return sma(**kwargs)


@mcp.tool()
def ema_tool(**kwargs):
    return ema(**kwargs)


@mcp.tool()
def rsi_tool(**kwargs):
    return rsi(**kwargs)


@mcp.tool()
def macd_tool(**kwargs):
    return macd(**kwargs)


@mcp.tool()
def bollinger_bands_tool(**kwargs):
    return bollinger_bands(**kwargs)


# --- Fundamentals ---
@mcp.tool()
def company_overview_tool(**kwargs):
    return company_overview(**kwargs)


@mcp.tool()
def etf_profile_tool(**kwargs):
    return etf_profile(**kwargs)


@mcp.tool()
def dividends_tool(**kwargs):
    return dividends(**kwargs)


@mcp.tool()
def splits_tool(**kwargs):
    return splits(**kwargs)


@mcp.tool()
def income_statement_tool(**kwargs):
    return income_statement(**kwargs)


@mcp.tool()
def balance_sheet_tool(**kwargs):
    return balance_sheet(**kwargs)


@mcp.tool()
def cash_flow_tool(**kwargs):
    return cash_flow(**kwargs)


@mcp.tool()
def earnings_tool(**kwargs):
    return earnings(**kwargs)


# --- Economic indicators ---
@mcp.tool()
def real_gdp_tool(**kwargs):
    return real_gdp(**kwargs)


@mcp.tool()
def real_gdp_per_capita_tool(**kwargs):
    return real_gdp_per_capita(**kwargs)


@mcp.tool()
def treasury_yield_tool(**kwargs):
    return treasury_yield(**kwargs)


@mcp.tool()
def federal_funds_rate_tool(**kwargs):
    return federal_funds_rate(**kwargs)


@mcp.tool()
def cpi_tool(**kwargs):
    return cpi(**kwargs)


@mcp.tool()
def inflation_tool(**kwargs):
    return inflation(**kwargs)


@mcp.tool()
def unemployment_tool(**kwargs):
    return unemployment(**kwargs)


# --- Commodities ---
@mcp.tool()
def gold_silver_spot_tool(**kwargs):
    return gold_silver_spot(**kwargs)


@mcp.tool()
def gold_silver_history_tool(**kwargs):
    return gold_silver_history(**kwargs)


@mcp.tool()
def wti_tool(**kwargs):
    return wti(**kwargs)


@mcp.tool()
def brent_tool(**kwargs):
    return brent(**kwargs)


@mcp.tool()
def natural_gas_tool(**kwargs):
    return natural_gas(**kwargs)


@mcp.tool()
def copper_tool(**kwargs):
    return copper(**kwargs)


@mcp.tool()
def aluminum_tool(**kwargs):
    return aluminum(**kwargs)


@mcp.tool()
def wheat_tool(**kwargs):
    return wheat(**kwargs)


@mcp.tool()
def corn_tool(**kwargs):
    return corn(**kwargs)


@mcp.tool()
def cotton_tool(**kwargs):
    return cotton(**kwargs)


@mcp.tool()
def sugar_tool(**kwargs):
    return sugar(**kwargs)


@mcp.tool()
def coffee_tool(**kwargs):
    return coffee(**kwargs)


@mcp.tool()
def all_commodities_tool(**kwargs):
    return all_commodities(**kwargs)


# --- Intelligence ---
@mcp.tool()
def news_sentiment_tool(**kwargs):
    return news_sentiment(**kwargs)


@mcp.tool()
def earnings_call_transcript_tool(**kwargs):
    return earnings_call_transcript(**kwargs)


@mcp.tool()
def top_gainers_losers_tool(**kwargs):
    return top_gainers_losers(**kwargs)


@mcp.tool()
def insider_transactions_tool(**kwargs):
    return insider_transactions(**kwargs)


# --- Options ---
@mcp.tool()
def realtime_options_tool(**kwargs):
    return realtime_options(**kwargs)


@mcp.tool()
def realtime_put_call_ratio_tool(**kwargs):
    return realtime_put_call_ratio(**kwargs)


@mcp.tool()
def realtime_volume_open_interest_ratio_tool(**kwargs):
    return realtime_volume_open_interest_ratio(**kwargs)


@mcp.tool()
def historical_options_tool(**kwargs):
    return historical_options(**kwargs)


if __name__ == "__main__":
    mcp.run()
