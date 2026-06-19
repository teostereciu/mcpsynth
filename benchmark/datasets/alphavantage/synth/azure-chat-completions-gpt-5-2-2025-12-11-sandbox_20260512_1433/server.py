from typing import Any, Dict, Optional

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
    earnings_calendar,
    earnings_estimates,
    etf_profile,
    income_statement,
    splits,
)
from generated_tools.fx import fx_daily, fx_exchange_rate, fx_intraday, fx_monthly, fx_weekly
from generated_tools.intelligence import insider_transactions, news_sentiment, top_gainers_losers
from generated_tools.options import (
    historical_options,
    realtime_options,
    realtime_put_call_ratio,
    realtime_volume_open_interest_ratio,
)
from generated_tools.technical_indicators import bbands, ema, macd, rsi, sma
from generated_tools.time_series import (
    global_quote,
    market_status,
    symbol_search,
    time_series_daily,
    time_series_daily_adjusted,
    time_series_intraday,
    time_series_monthly,
    time_series_monthly_adjusted,
    time_series_weekly,
    time_series_weekly_adjusted,
)

mcp = FastMCP("alphavantage")


@mcp.tool()
def stocks_time_series_intraday(
    symbol: str,
    interval: str,
    adjusted: Optional[bool] = None,
    extended_hours: Optional[bool] = None,
    month: Optional[str] = None,
    outputsize: Optional[str] = None,
    datatype: str = "json",
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    return time_series_intraday(
        symbol=symbol,
        interval=interval,
        adjusted=adjusted,
        extended_hours=extended_hours,
        month=month,
        outputsize=outputsize,
        datatype=datatype,
        entitlement=entitlement,
    )


@mcp.tool()
def stocks_time_series_daily(symbol: str, outputsize: Optional[str] = None, datatype: str = "json") -> Dict[str, Any]:
    return time_series_daily(symbol=symbol, outputsize=outputsize, datatype=datatype)


@mcp.tool()
def stocks_time_series_daily_adjusted(
    symbol: str, outputsize: Optional[str] = None, datatype: str = "json", entitlement: Optional[str] = None
) -> Dict[str, Any]:
    return time_series_daily_adjusted(symbol=symbol, outputsize=outputsize, datatype=datatype, entitlement=entitlement)


@mcp.tool()
def stocks_time_series_weekly(symbol: str, datatype: str = "json") -> Dict[str, Any]:
    return time_series_weekly(symbol=symbol, datatype=datatype)


@mcp.tool()
def stocks_time_series_weekly_adjusted(symbol: str, datatype: str = "json") -> Dict[str, Any]:
    return time_series_weekly_adjusted(symbol=symbol, datatype=datatype)


@mcp.tool()
def stocks_time_series_monthly(symbol: str, datatype: str = "json") -> Dict[str, Any]:
    return time_series_monthly(symbol=symbol, datatype=datatype)


@mcp.tool()
def stocks_time_series_monthly_adjusted(symbol: str, datatype: str = "json") -> Dict[str, Any]:
    return time_series_monthly_adjusted(symbol=symbol, datatype=datatype)


@mcp.tool()
def stocks_global_quote(symbol: str, datatype: str = "json") -> Dict[str, Any]:
    return global_quote(symbol=symbol, datatype=datatype)


@mcp.tool()
def stocks_symbol_search(keywords: str) -> Dict[str, Any]:
    return symbol_search(keywords=keywords)


@mcp.tool()
def stocks_market_status() -> Dict[str, Any]:
    return market_status()


@mcp.tool()
def fx_rate(from_currency: str, to_currency: str) -> Dict[str, Any]:
    return fx_exchange_rate(from_currency=from_currency, to_currency=to_currency)


@mcp.tool()
def fx_time_series_intraday(
    from_symbol: str, to_symbol: str, interval: str, outputsize: Optional[str] = None, datatype: str = "json"
) -> Dict[str, Any]:
    return fx_intraday(from_symbol=from_symbol, to_symbol=to_symbol, interval=interval, outputsize=outputsize, datatype=datatype)


@mcp.tool()
def fx_time_series_daily(
    from_symbol: str, to_symbol: str, outputsize: Optional[str] = None, datatype: str = "json"
) -> Dict[str, Any]:
    return fx_daily(from_symbol=from_symbol, to_symbol=to_symbol, outputsize=outputsize, datatype=datatype)


@mcp.tool()
def fx_time_series_weekly(from_symbol: str, to_symbol: str, datatype: str = "json") -> Dict[str, Any]:
    return fx_weekly(from_symbol=from_symbol, to_symbol=to_symbol, datatype=datatype)


@mcp.tool()
def fx_time_series_monthly(from_symbol: str, to_symbol: str, datatype: str = "json") -> Dict[str, Any]:
    return fx_monthly(from_symbol=from_symbol, to_symbol=to_symbol, datatype=datatype)


@mcp.tool()
def crypto_time_series_intraday(
    symbol: str, market: str, interval: str, outputsize: Optional[str] = None, datatype: str = "json"
) -> Dict[str, Any]:
    return crypto_intraday(symbol=symbol, market=market, interval=interval, outputsize=outputsize, datatype=datatype)


@mcp.tool()
def crypto_time_series_daily(symbol: str, market: str, datatype: str = "json") -> Dict[str, Any]:
    return digital_currency_daily(symbol=symbol, market=market, datatype=datatype)


@mcp.tool()
def crypto_time_series_weekly(symbol: str, market: str, datatype: str = "json") -> Dict[str, Any]:
    return digital_currency_weekly(symbol=symbol, market=market, datatype=datatype)


@mcp.tool()
def crypto_time_series_monthly(symbol: str, market: str, datatype: str = "json") -> Dict[str, Any]:
    return digital_currency_monthly(symbol=symbol, market=market, datatype=datatype)


@mcp.tool()
def technical_sma(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    month: Optional[str] = None,
    datatype: str = "json",
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    return sma(
        symbol=symbol,
        interval=interval,
        time_period=time_period,
        series_type=series_type,
        month=month,
        datatype=datatype,
        entitlement=entitlement,
    )


@mcp.tool()
def technical_ema(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    month: Optional[str] = None,
    datatype: str = "json",
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    return ema(
        symbol=symbol,
        interval=interval,
        time_period=time_period,
        series_type=series_type,
        month=month,
        datatype=datatype,
        entitlement=entitlement,
    )


@mcp.tool()
def technical_rsi(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    month: Optional[str] = None,
    datatype: str = "json",
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    return rsi(
        symbol=symbol,
        interval=interval,
        time_period=time_period,
        series_type=series_type,
        month=month,
        datatype=datatype,
        entitlement=entitlement,
    )


@mcp.tool()
def technical_macd(
    symbol: str,
    interval: str,
    series_type: str,
    fastperiod: int = 12,
    slowperiod: int = 26,
    signalperiod: int = 9,
    month: Optional[str] = None,
    datatype: str = "json",
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    return macd(
        symbol=symbol,
        interval=interval,
        series_type=series_type,
        fastperiod=fastperiod,
        slowperiod=slowperiod,
        signalperiod=signalperiod,
        month=month,
        datatype=datatype,
        entitlement=entitlement,
    )


@mcp.tool()
def technical_bbands(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    nbdevup: int = 2,
    nbdevdn: int = 2,
    matype: int = 0,
    month: Optional[str] = None,
    datatype: str = "json",
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    return bbands(
        symbol=symbol,
        interval=interval,
        time_period=time_period,
        series_type=series_type,
        nbdevup=nbdevup,
        nbdevdn=nbdevdn,
        matype=matype,
        month=month,
        datatype=datatype,
        entitlement=entitlement,
    )


@mcp.tool()
def fundamentals_company_overview(symbol: str) -> Dict[str, Any]:
    return company_overview(symbol=symbol)


@mcp.tool()
def fundamentals_income_statement(symbol: str) -> Dict[str, Any]:
    return income_statement(symbol=symbol)


@mcp.tool()
def fundamentals_balance_sheet(symbol: str) -> Dict[str, Any]:
    return balance_sheet(symbol=symbol)


@mcp.tool()
def fundamentals_cash_flow(symbol: str) -> Dict[str, Any]:
    return cash_flow(symbol=symbol)


@mcp.tool()
def fundamentals_earnings(symbol: str) -> Dict[str, Any]:
    return earnings(symbol=symbol)


@mcp.tool()
def fundamentals_earnings_estimates(symbol: str) -> Dict[str, Any]:
    return earnings_estimates(symbol=symbol)


@mcp.tool()
def fundamentals_earnings_calendar(horizon: str = "3month", symbol: Optional[str] = None) -> Dict[str, Any]:
    return earnings_calendar(horizon=horizon, symbol=symbol)


@mcp.tool()
def fundamentals_etf_profile(symbol: str) -> Dict[str, Any]:
    return etf_profile(symbol=symbol)


@mcp.tool()
def fundamentals_dividends(symbol: str, datatype: str = "json") -> Dict[str, Any]:
    return dividends(symbol=symbol, datatype=datatype)


@mcp.tool()
def fundamentals_splits(symbol: str, datatype: str = "json") -> Dict[str, Any]:
    return splits(symbol=symbol, datatype=datatype)


@mcp.tool()
def econ_real_gdp(interval: str = "annual", datatype: str = "json") -> Dict[str, Any]:
    return real_gdp(interval=interval, datatype=datatype)


@mcp.tool()
def econ_real_gdp_per_capita(datatype: str = "json") -> Dict[str, Any]:
    return real_gdp_per_capita(datatype=datatype)


@mcp.tool()
def econ_treasury_yield(interval: str = "monthly", maturity: str = "10year", datatype: str = "json") -> Dict[str, Any]:
    return treasury_yield(interval=interval, maturity=maturity, datatype=datatype)


@mcp.tool()
def econ_cpi(interval: str = "monthly", datatype: str = "json") -> Dict[str, Any]:
    return cpi(interval=interval, datatype=datatype)


@mcp.tool()
def econ_inflation(datatype: str = "json") -> Dict[str, Any]:
    return inflation(datatype=datatype)


@mcp.tool()
def econ_unemployment(datatype: str = "json") -> Dict[str, Any]:
    return unemployment(datatype=datatype)


@mcp.tool()
def intelligence_news_sentiment(
    tickers: Optional[str] = None,
    topics: Optional[str] = None,
    time_from: Optional[str] = None,
    time_to: Optional[str] = None,
    sort: str = "LATEST",
    limit: int = 50,
) -> Dict[str, Any]:
    return news_sentiment(tickers=tickers, topics=topics, time_from=time_from, time_to=time_to, sort=sort, limit=limit)


@mcp.tool()
def intelligence_top_gainers_losers(entitlement: Optional[str] = None) -> Dict[str, Any]:
    return top_gainers_losers(entitlement=entitlement)


@mcp.tool()
def intelligence_insider_transactions(symbol: str, from_date: Optional[str] = None, to_date: Optional[str] = None) -> Dict[str, Any]:
    return insider_transactions(symbol=symbol, from_date=from_date, to_date=to_date)


@mcp.tool()
def commodities_gold_silver_spot(symbol: str) -> Dict[str, Any]:
    return gold_silver_spot(symbol=symbol)


@mcp.tool()
def commodities_gold_silver_history(symbol: str, interval: str) -> Dict[str, Any]:
    return gold_silver_history(symbol=symbol, interval=interval)


@mcp.tool()
def commodities_wti(interval: str = "monthly", datatype: str = "json") -> Dict[str, Any]:
    return wti(interval=interval, datatype=datatype)


@mcp.tool()
def commodities_brent(interval: str = "monthly", datatype: str = "json") -> Dict[str, Any]:
    return brent(interval=interval, datatype=datatype)


@mcp.tool()
def commodities_natural_gas(interval: str = "monthly", datatype: str = "json") -> Dict[str, Any]:
    return natural_gas(interval=interval, datatype=datatype)


@mcp.tool()
def commodities_copper(interval: str = "monthly", datatype: str = "json") -> Dict[str, Any]:
    return copper(interval=interval, datatype=datatype)


@mcp.tool()
def commodities_aluminum(interval: str = "monthly", datatype: str = "json") -> Dict[str, Any]:
    return aluminum(interval=interval, datatype=datatype)


@mcp.tool()
def commodities_wheat(interval: str = "monthly", datatype: str = "json") -> Dict[str, Any]:
    return wheat(interval=interval, datatype=datatype)


@mcp.tool()
def commodities_corn(interval: str = "monthly", datatype: str = "json") -> Dict[str, Any]:
    return corn(interval=interval, datatype=datatype)


@mcp.tool()
def commodities_cotton(interval: str = "monthly", datatype: str = "json") -> Dict[str, Any]:
    return cotton(interval=interval, datatype=datatype)


@mcp.tool()
def commodities_sugar(interval: str = "monthly", datatype: str = "json") -> Dict[str, Any]:
    return sugar(interval=interval, datatype=datatype)


@mcp.tool()
def commodities_coffee(interval: str = "monthly", datatype: str = "json") -> Dict[str, Any]:
    return coffee(interval=interval, datatype=datatype)


@mcp.tool()
def commodities_all_commodities(interval: str = "monthly", datatype: str = "json") -> Dict[str, Any]:
    return all_commodities(interval=interval, datatype=datatype)


@mcp.tool()
def options_realtime_options(
    symbol: str,
    require_greeks: bool = False,
    contract: Optional[str] = None,
    expiration: Optional[str] = None,
    datatype: str = "json",
) -> Dict[str, Any]:
    return realtime_options(
        symbol=symbol,
        require_greeks=require_greeks,
        contract=contract,
        expiration=expiration,
        datatype=datatype,
    )


@mcp.tool()
def options_historical_options(
    symbol: str,
    date: Optional[str] = None,
    contract: Optional[str] = None,
    datatype: str = "json",
) -> Dict[str, Any]:
    return historical_options(symbol=symbol, date=date, contract=contract, datatype=datatype)


@mcp.tool()
def options_realtime_put_call_ratio(symbol: str) -> Dict[str, Any]:
    return realtime_put_call_ratio(symbol=symbol)


@mcp.tool()
def options_realtime_volume_open_interest_ratio(symbol: str) -> Dict[str, Any]:
    return realtime_volume_open_interest_ratio(symbol=symbol)


if __name__ == "__main__":
    mcp.run()
