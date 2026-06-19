import asyncio

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
from generated_tools.technical_indicators import bbands, ema, macd, rsi, sma
from generated_tools.time_series import (
    market_status,
    realtime_bulk_quotes,
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


# --- Time series / quotes / search ---
@mcp.tool()
def stock_time_series_intraday_tool(
    ticker: str,
    time_interval: str,
    adjusted: bool = True,
    extended_hours: bool = True,
    month: str | None = None,
    output_size: str = "compact",
    entitlement: str | None = None,
    format: str = "json",
):
    return stock_time_series_intraday(
        ticker=ticker,
        time_interval=time_interval,
        adjusted=adjusted,
        extended_hours=extended_hours,
        month=month,
        output_size=output_size,
        entitlement=entitlement,
        format=format,
    )


@mcp.tool()
def stock_time_series_daily_tool(ticker: str, output_size: str = "compact", format: str = "json"):
    return stock_time_series_daily(ticker=ticker, output_size=output_size, format=format)


@mcp.tool()
def stock_time_series_daily_adjusted_tool(
    ticker: str,
    output_size: str = "compact",
    format: str = "json",
    entitlement: str | None = None,
):
    return stock_time_series_daily_adjusted(ticker=ticker, output_size=output_size, format=format, entitlement=entitlement)


@mcp.tool()
def stock_time_series_weekly_tool(ticker: str, format: str = "json"):
    return stock_time_series_weekly(ticker=ticker, format=format)


@mcp.tool()
def stock_time_series_weekly_adjusted_tool(ticker: str, format: str = "json"):
    return stock_time_series_weekly_adjusted(ticker=ticker, format=format)


@mcp.tool()
def stock_time_series_monthly_tool(ticker: str, format: str = "json"):
    return stock_time_series_monthly(ticker=ticker, format=format)


@mcp.tool()
def stock_time_series_monthly_adjusted_tool(ticker: str, format: str = "json"):
    return stock_time_series_monthly_adjusted(ticker=ticker, format=format)


@mcp.tool()
def stock_quote_tool(ticker: str):
    return stock_quote(ticker=ticker)


@mcp.tool()
def realtime_bulk_quotes_tool(ticker: str):
    return realtime_bulk_quotes(ticker=ticker)


@mcp.tool()
def symbol_search_tool(keywords: str):
    return symbol_search(keywords=keywords)


@mcp.tool()
def market_status_tool():
    return market_status()


# --- FX ---
@mcp.tool()
def fx_exchange_rate_tool(from_currency: str, to_currency: str):
    return fx_exchange_rate(from_currency=from_currency, to_currency=to_currency)


@mcp.tool()
def fx_intraday_tool(
    from_symbol: str,
    to_symbol: str,
    time_interval: str,
    output_size: str = "compact",
    format: str = "json",
):
    return fx_intraday(
        from_symbol=from_symbol,
        to_symbol=to_symbol,
        time_interval=time_interval,
        output_size=output_size,
        format=format,
    )


@mcp.tool()
def fx_daily_tool(from_symbol: str, to_symbol: str, output_size: str = "compact", format: str = "json"):
    return fx_daily(from_symbol=from_symbol, to_symbol=to_symbol, output_size=output_size, format=format)


@mcp.tool()
def fx_weekly_tool(from_symbol: str, to_symbol: str, format: str = "json"):
    return fx_weekly(from_symbol=from_symbol, to_symbol=to_symbol, format=format)


@mcp.tool()
def fx_monthly_tool(from_symbol: str, to_symbol: str, format: str = "json"):
    return fx_monthly(from_symbol=from_symbol, to_symbol=to_symbol, format=format)


# --- Digital currency ---
@mcp.tool()
def crypto_intraday_tool(
    ticker: str,
    market: str,
    time_interval: str,
    output_size: str = "compact",
    format: str = "json",
):
    return crypto_intraday(ticker=ticker, market=market, time_interval=time_interval, output_size=output_size, format=format)


@mcp.tool()
def digital_currency_daily_tool(ticker: str, market: str, format: str = "json"):
    return digital_currency_daily(ticker=ticker, market=market, format=format)


@mcp.tool()
def digital_currency_weekly_tool(ticker: str, market: str, format: str = "json"):
    return digital_currency_weekly(ticker=ticker, market=market, format=format)


@mcp.tool()
def digital_currency_monthly_tool(ticker: str, market: str, format: str = "json"):
    return digital_currency_monthly(ticker=ticker, market=market, format=format)


# --- Technical indicators ---
@mcp.tool()
def sma_tool(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: str | None = None,
    format: str = "json",
    entitlement: str | None = None,
):
    return sma(
        ticker=ticker,
        time_interval=time_interval,
        time_period=time_period,
        price_type=price_type,
        month=month,
        format=format,
        entitlement=entitlement,
    )


@mcp.tool()
def ema_tool(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: str | None = None,
    format: str = "json",
    entitlement: str | None = None,
):
    return ema(
        ticker=ticker,
        time_interval=time_interval,
        time_period=time_period,
        price_type=price_type,
        month=month,
        format=format,
        entitlement=entitlement,
    )


@mcp.tool()
def rsi_tool(
    ticker: str,
    time_interval: str,
    time_period: int,
    month: str | None = None,
    format: str = "json",
    entitlement: str | None = None,
):
    return rsi(ticker=ticker, time_interval=time_interval, time_period=time_period, month=month, format=format, entitlement=entitlement)


@mcp.tool()
def macd_tool(
    ticker: str,
    time_interval: str,
    series_type: str = "close",
    fastperiod: int = 12,
    slowperiod: int = 26,
    signalperiod: int = 9,
    month: str | None = None,
    format: str = "json",
    entitlement: str | None = None,
):
    return macd(
        ticker=ticker,
        time_interval=time_interval,
        series_type=series_type,
        fastperiod=fastperiod,
        slowperiod=slowperiod,
        signalperiod=signalperiod,
        month=month,
        format=format,
        entitlement=entitlement,
    )


@mcp.tool()
def bbands_tool(
    ticker: str,
    time_interval: str,
    time_period: int,
    series_type: str = "close",
    nbdevup: int = 2,
    nbdevdn: int = 2,
    matype: int = 0,
    month: str | None = None,
    format: str = "json",
    entitlement: str | None = None,
):
    return bbands(
        ticker=ticker,
        time_interval=time_interval,
        time_period=time_period,
        series_type=series_type,
        nbdevup=nbdevup,
        nbdevdn=nbdevdn,
        matype=matype,
        month=month,
        format=format,
        entitlement=entitlement,
    )


# --- Fundamentals ---
@mcp.tool()
def company_overview_tool(ticker: str):
    return company_overview(ticker=ticker)


@mcp.tool()
def income_statement_tool(ticker: str):
    return income_statement(ticker=ticker)


@mcp.tool()
def balance_sheet_tool(ticker: str):
    return balance_sheet(ticker=ticker)


@mcp.tool()
def cash_flow_tool(ticker: str):
    return cash_flow(ticker=ticker)


@mcp.tool()
def earnings_tool(ticker: str):
    return earnings(ticker=ticker)


@mcp.tool()
def etf_profile_tool(ticker: str):
    return etf_profile(ticker=ticker)


@mcp.tool()
def dividends_tool(ticker: str, format: str = "json"):
    return dividends(ticker=ticker, format=format)


@mcp.tool()
def splits_tool(ticker: str, format: str = "json"):
    return splits(ticker=ticker, format=format)


# --- Economic indicators ---
@mcp.tool()
def real_gdp_tool(time_interval: str = "annual", format: str = "json"):
    return real_gdp(time_interval=time_interval, format=format)


@mcp.tool()
def real_gdp_per_capita_tool(format: str = "json"):
    return real_gdp_per_capita(format=format)


@mcp.tool()
def treasury_yield_tool(time_interval: str = "monthly", maturity: str = "10year", format: str = "json"):
    return treasury_yield(time_interval=time_interval, maturity=maturity, format=format)


@mcp.tool()
def federal_funds_rate_tool(time_interval: str = "monthly", format: str = "json"):
    return federal_funds_rate(time_interval=time_interval, format=format)


@mcp.tool()
def cpi_tool(time_interval: str = "monthly", format: str = "json"):
    return cpi(time_interval=time_interval, format=format)


@mcp.tool()
def inflation_tool(format: str = "json"):
    return inflation(format=format)


@mcp.tool()
def unemployment_tool(format: str = "json"):
    return unemployment(format=format)


# --- Commodities ---
@mcp.tool()
def gold_silver_spot_tool(ticker: str):
    return gold_silver_spot(ticker=ticker)


@mcp.tool()
def gold_silver_history_tool(ticker: str, time_interval: str):
    return gold_silver_history(ticker=ticker, time_interval=time_interval)


@mcp.tool()
def wti_tool(time_interval: str = "monthly", format: str = "json"):
    return wti(time_interval=time_interval, format=format)


@mcp.tool()
def brent_tool(time_interval: str = "monthly", format: str = "json"):
    return brent(time_interval=time_interval, format=format)


@mcp.tool()
def natural_gas_tool(time_interval: str = "monthly", format: str = "json"):
    return natural_gas(time_interval=time_interval, format=format)


@mcp.tool()
def copper_tool(time_interval: str = "monthly", format: str = "json"):
    return copper(time_interval=time_interval, format=format)


@mcp.tool()
def aluminum_tool(time_interval: str = "monthly", format: str = "json"):
    return aluminum(time_interval=time_interval, format=format)


@mcp.tool()
def wheat_tool(time_interval: str = "monthly", format: str = "json"):
    return wheat(time_interval=time_interval, format=format)


@mcp.tool()
def corn_tool(time_interval: str = "monthly", format: str = "json"):
    return corn(time_interval=time_interval, format=format)


@mcp.tool()
def cotton_tool(time_interval: str = "monthly", format: str = "json"):
    return cotton(time_interval=time_interval, format=format)


@mcp.tool()
def sugar_tool(time_interval: str = "monthly", format: str = "json"):
    return sugar(time_interval=time_interval, format=format)


@mcp.tool()
def coffee_tool(time_interval: str = "monthly", format: str = "json"):
    return coffee(time_interval=time_interval, format=format)


@mcp.tool()
def all_commodities_tool(time_interval: str = "monthly", format: str = "json"):
    return all_commodities(time_interval=time_interval, format=format)


# --- Options ---
@mcp.tool()
def realtime_options_tool(
    ticker: str,
    require_greeks: bool = False,
    contract: str | None = None,
    expiration: str | None = None,
    format: str = "json",
):
    return realtime_options(
        ticker=ticker,
        require_greeks=require_greeks,
        contract=contract,
        expiration=expiration,
        format=format,
    )


@mcp.tool()
def historical_options_tool(ticker: str, date: str | None = None, contract: str | None = None, format: str = "json"):
    return historical_options(ticker=ticker, date=date, contract=contract, format=format)


@mcp.tool()
def realtime_put_call_ratio_tool(ticker: str):
    return realtime_put_call_ratio(ticker=ticker)


@mcp.tool()
def realtime_volume_open_interest_ratio_tool(ticker: str):
    return realtime_volume_open_interest_ratio(ticker=ticker)


# --- Intelligence ---
@mcp.tool()
def news_sentiment_tool(
    tickers: str | None = None,
    topics: str | None = None,
    time_from: str | None = None,
    time_to: str | None = None,
    sort: str | None = None,
    limit: int | None = None,
):
    return news_sentiment(tickers=tickers, topics=topics, time_from=time_from, time_to=time_to, sort=sort, limit=limit)


@mcp.tool()
def earnings_call_transcript_tool(ticker: str, quarter: str):
    return earnings_call_transcript(ticker=ticker, quarter=quarter)


@mcp.tool()
def top_gainers_losers_tool(entitlement: str | None = None):
    return top_gainers_losers(entitlement=entitlement)


@mcp.tool()
def insider_transactions_tool(ticker: str, from_date: str | None = None):
    return insider_transactions(ticker=ticker, from_date=from_date)


async def main():
    await mcp.run_stdio_async()


if __name__ == "__main__":
    asyncio.run(main())
