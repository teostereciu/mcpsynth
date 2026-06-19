from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from generated_tools import stocks, forex, crypto, technical, fundamentals, economics, sector

mcp = FastMCP("alphavantage")


@mcp.tool()
def av_quote(symbol: str) -> Dict[str, Any]:
    return stocks.quote(symbol)


@mcp.tool()
def av_symbol_search(keywords: str) -> Dict[str, Any]:
    return stocks.search_keywords(keywords)


@mcp.tool()
def av_time_series_intraday(
    symbol: str,
    interval: str = "5min",
    adjusted: bool = True,
    outputsize: str = "compact",
    extended_hours: bool = True,
    month: str | None = None,
) -> Dict[str, Any]:
    return stocks.time_series_intraday(symbol, interval, adjusted, outputsize, extended_hours, month)


@mcp.tool()
def av_time_series_daily(symbol: str, adjusted: bool = True, outputsize: str = "compact") -> Dict[str, Any]:
    return stocks.time_series_daily(symbol, adjusted, outputsize)


@mcp.tool()
def av_time_series_weekly(symbol: str, adjusted: bool = True) -> Dict[str, Any]:
    return stocks.time_series_weekly(symbol, adjusted)


@mcp.tool()
def av_time_series_monthly(symbol: str, adjusted: bool = True) -> Dict[str, Any]:
    return stocks.time_series_monthly(symbol, adjusted)


@mcp.tool()
def av_fx_exchange_rate(from_currency: str, to_currency: str) -> Dict[str, Any]:
    return forex.fx_exchange_rate(from_currency, to_currency)


@mcp.tool()
def av_fx_daily(from_symbol: str, to_symbol: str, outputsize: str = "compact") -> Dict[str, Any]:
    return forex.fx_daily(from_symbol, to_symbol, outputsize)


@mcp.tool()
def av_fx_weekly(from_symbol: str, to_symbol: str) -> Dict[str, Any]:
    return forex.fx_weekly(from_symbol, to_symbol)


@mcp.tool()
def av_fx_monthly(from_symbol: str, to_symbol: str) -> Dict[str, Any]:
    return forex.fx_monthly(from_symbol, to_symbol)


@mcp.tool()
def av_crypto_daily(symbol: str, market: str = "USD") -> Dict[str, Any]:
    return crypto.digital_currency_daily(symbol, market)


@mcp.tool()
def av_crypto_weekly(symbol: str, market: str = "USD") -> Dict[str, Any]:
    return crypto.digital_currency_weekly(symbol, market)


@mcp.tool()
def av_crypto_monthly(symbol: str, market: str = "USD") -> Dict[str, Any]:
    return crypto.digital_currency_monthly(symbol, market)


@mcp.tool()
def av_sma(symbol: str, interval: str, time_period: int = 20, series_type: str = "close") -> Dict[str, Any]:
    return technical.sma(symbol, interval, time_period, series_type)


@mcp.tool()
def av_ema(symbol: str, interval: str, time_period: int = 20, series_type: str = "close") -> Dict[str, Any]:
    return technical.ema(symbol, interval, time_period, series_type)


@mcp.tool()
def av_rsi(symbol: str, interval: str, time_period: int = 14, series_type: str = "close") -> Dict[str, Any]:
    return technical.rsi(symbol, interval, time_period, series_type)


@mcp.tool()
def av_macd(
    symbol: str,
    interval: str,
    series_type: str = "close",
    fastperiod: int = 12,
    slowperiod: int = 26,
    signalperiod: int = 9,
) -> Dict[str, Any]:
    return technical.macd(symbol, interval, series_type, fastperiod, slowperiod, signalperiod)


@mcp.tool()
def av_bbands(
    symbol: str,
    interval: str,
    time_period: int = 20,
    series_type: str = "close",
    nbdevup: int = 2,
    nbdevdn: int = 2,
    matype: int = 0,
) -> Dict[str, Any]:
    return technical.bbands(symbol, interval, time_period, series_type, nbdevup, nbdevdn, matype)


@mcp.tool()
def av_company_overview(symbol: str) -> Dict[str, Any]:
    return fundamentals.company_overview(symbol)


@mcp.tool()
def av_income_statement(symbol: str) -> Dict[str, Any]:
    return fundamentals.income_statement(symbol)


@mcp.tool()
def av_balance_sheet(symbol: str) -> Dict[str, Any]:
    return fundamentals.balance_sheet(symbol)


@mcp.tool()
def av_earnings(symbol: str) -> Dict[str, Any]:
    return fundamentals.earnings(symbol)


@mcp.tool()
def av_cpi(interval: str = "monthly") -> Dict[str, Any]:
    return economics.cpi(interval)


@mcp.tool()
def av_inflation() -> Dict[str, Any]:
    return economics.inflation()


@mcp.tool()
def av_real_gdp(interval: str = "quarterly") -> Dict[str, Any]:
    return economics.gdp(interval)


@mcp.tool()
def av_unemployment() -> Dict[str, Any]:
    return economics.unemployment()


@mcp.tool()
def av_treasury_yield(interval: str = "monthly", maturity: str = "10year") -> Dict[str, Any]:
    return economics.treasury_yield(interval, maturity)


@mcp.tool()
def av_sector_performance() -> Dict[str, Any]:
    return sector.sector_performance()


if __name__ == "__main__":
    mcp.run()
