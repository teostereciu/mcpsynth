"""
Alpha Vantage MCP Server
Runs over stdio using FastMCP.
"""

from mcp.server.fastmcp import FastMCP

# ── domain modules ──────────────────────────────────────────────────────────
from generated_tools.stock_time_series import (
    get_intraday,
    get_daily,
    get_daily_adjusted,
    get_weekly,
    get_weekly_adjusted,
    get_monthly,
    get_monthly_adjusted,
    get_global_quote,
    search_symbol,
)
from generated_tools.forex import (
    get_fx_exchange_rate,
    get_fx_intraday,
    get_fx_daily,
    get_fx_weekly,
    get_fx_monthly,
)
from generated_tools.crypto import (
    get_crypto_exchange_rate,
    get_crypto_intraday,
    get_crypto_daily,
    get_crypto_weekly,
    get_crypto_monthly,
)
from generated_tools.technical_indicators import (
    get_sma,
    get_ema,
    get_rsi,
    get_macd,
    get_bbands,
    get_vwap,
    get_stoch,
    get_adx,
    get_cci,
    get_aroon,
)
from generated_tools.fundamentals import (
    get_company_overview,
    get_income_statement,
    get_balance_sheet,
    get_cash_flow,
    get_earnings,
    get_earnings_calendar,
    get_ipo_calendar,
    get_listing_status,
)
from generated_tools.economic_indicators import (
    get_real_gdp,
    get_real_gdp_per_capita,
    get_treasury_yield,
    get_federal_funds_rate,
    get_cpi,
    get_inflation,
    get_retail_sales,
    get_durables,
    get_unemployment,
    get_nonfarm_payroll,
)
from generated_tools.sector_performance import get_sector_performance

# ── server instance ──────────────────────────────────────────────────────────
mcp = FastMCP("alpha-vantage")

# ============================================================================
# Stock Time Series
# ============================================================================

@mcp.tool()
def stock_intraday(
    symbol: str,
    interval: str = "5min",
    outputsize: str = "compact",
    adjusted: bool = True,
    extended_hours: bool = True,
    month: str = "",
) -> dict:
    """
    Fetch intraday OHLCV time series for a stock symbol.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: One of 1min | 5min | 15min | 30min | 60min.
    :param outputsize: "compact" (latest 100 bars) or "full" (up to 20 years).
    :param adjusted: Return split/dividend-adjusted values.
    :param extended_hours: Include pre/post-market data.
    :param month: Optional YYYY-MM to fetch a specific historical month.
    """
    return get_intraday(symbol, interval, outputsize, adjusted, extended_hours, month)


@mcp.tool()
def stock_daily(symbol: str, outputsize: str = "compact") -> dict:
    """
    Fetch daily OHLCV time series for a stock symbol (unadjusted).

    :param symbol: Ticker symbol, e.g. "IBM".
    :param outputsize: "compact" (latest 100 days) or "full".
    """
    return get_daily(symbol, outputsize)


@mcp.tool()
def stock_daily_adjusted(symbol: str, outputsize: str = "compact") -> dict:
    """
    Fetch daily adjusted OHLCV time series (split & dividend adjusted).

    :param symbol: Ticker symbol, e.g. "IBM".
    :param outputsize: "compact" (latest 100 days) or "full".
    """
    return get_daily_adjusted(symbol, outputsize)


@mcp.tool()
def stock_weekly(symbol: str) -> dict:
    """
    Fetch weekly OHLCV time series for a stock symbol (unadjusted).

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return get_weekly(symbol)


@mcp.tool()
def stock_weekly_adjusted(symbol: str) -> dict:
    """
    Fetch weekly adjusted OHLCV time series for a stock symbol.

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return get_weekly_adjusted(symbol)


@mcp.tool()
def stock_monthly(symbol: str) -> dict:
    """
    Fetch monthly OHLCV time series for a stock symbol (unadjusted).

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return get_monthly(symbol)


@mcp.tool()
def stock_monthly_adjusted(symbol: str) -> dict:
    """
    Fetch monthly adjusted OHLCV time series for a stock symbol.

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return get_monthly_adjusted(symbol)


@mcp.tool()
def stock_quote(symbol: str) -> dict:
    """
    Fetch the latest price, volume, change, and change-percent for a stock symbol.

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return get_global_quote(symbol)


@mcp.tool()
def symbol_search(keywords: str) -> dict:
    """
    Search for ticker symbols and company names matching the given keywords.

    :param keywords: Search string, e.g. "Microsoft" or "AAPL".
    """
    return search_symbol(keywords)


# ============================================================================
# Forex (FX)
# ============================================================================

@mcp.tool()
def fx_exchange_rate(from_currency: str, to_currency: str) -> dict:
    """
    Fetch the real-time exchange rate for a currency pair (fiat or crypto).

    :param from_currency: Source currency code, e.g. "USD".
    :param to_currency: Destination currency code, e.g. "EUR".
    """
    return get_fx_exchange_rate(from_currency, to_currency)


@mcp.tool()
def fx_intraday(
    from_symbol: str,
    to_symbol: str,
    interval: str = "5min",
    outputsize: str = "compact",
) -> dict:
    """
    Fetch intraday FX OHLCV time series for a currency pair.

    :param from_symbol: Source currency code, e.g. "EUR".
    :param to_symbol: Destination currency code, e.g. "USD".
    :param interval: One of 1min | 5min | 15min | 30min | 60min.
    :param outputsize: "compact" or "full".
    """
    return get_fx_intraday(from_symbol, to_symbol, interval, outputsize)


@mcp.tool()
def fx_daily(
    from_symbol: str,
    to_symbol: str,
    outputsize: str = "compact",
) -> dict:
    """
    Fetch daily FX OHLCV time series for a currency pair.

    :param from_symbol: Source currency code, e.g. "EUR".
    :param to_symbol: Destination currency code, e.g. "USD".
    :param outputsize: "compact" or "full".
    """
    return get_fx_daily(from_symbol, to_symbol, outputsize)


@mcp.tool()
def fx_weekly(from_symbol: str, to_symbol: str) -> dict:
    """
    Fetch weekly FX OHLCV time series for a currency pair.

    :param from_symbol: Source currency code, e.g. "EUR".
    :param to_symbol: Destination currency code, e.g. "USD".
    """
    return get_fx_weekly(from_symbol, to_symbol)


@mcp.tool()
def fx_monthly(from_symbol: str, to_symbol: str) -> dict:
    """
    Fetch monthly FX OHLCV time series for a currency pair.

    :param from_symbol: Source currency code, e.g. "EUR".
    :param to_symbol: Destination currency code, e.g. "USD".
    """
    return get_fx_monthly(from_symbol, to_symbol)


# ============================================================================
# Cryptocurrency
# ============================================================================

@mcp.tool()
def crypto_exchange_rate(from_currency: str, to_currency: str) -> dict:
    """
    Fetch the real-time exchange rate for a cryptocurrency pair.

    :param from_currency: Crypto symbol, e.g. "BTC" or "ETH".
    :param to_currency: Destination currency, e.g. "USD".
    """
    return get_crypto_exchange_rate(from_currency, to_currency)


@mcp.tool()
def crypto_intraday(
    symbol: str,
    market: str = "USD",
    interval: str = "5min",
    outputsize: str = "compact",
) -> dict:
    """
    Fetch intraday OHLCV time series for a cryptocurrency.

    :param symbol: Crypto symbol, e.g. "BTC".
    :param market: Market currency, e.g. "USD".
    :param interval: One of 1min | 5min | 15min | 30min | 60min.
    :param outputsize: "compact" or "full".
    """
    return get_crypto_intraday(symbol, market, interval, outputsize)


@mcp.tool()
def crypto_daily(symbol: str, market: str = "USD") -> dict:
    """
    Fetch daily OHLCV time series for a cryptocurrency.

    :param symbol: Crypto symbol, e.g. "BTC".
    :param market: Market currency, e.g. "USD".
    """
    return get_crypto_daily(symbol, market)


@mcp.tool()
def crypto_weekly(symbol: str, market: str = "USD") -> dict:
    """
    Fetch weekly OHLCV time series for a cryptocurrency.

    :param symbol: Crypto symbol, e.g. "BTC".
    :param market: Market currency, e.g. "USD".
    """
    return get_crypto_weekly(symbol, market)


@mcp.tool()
def crypto_monthly(symbol: str, market: str = "USD") -> dict:
    """
    Fetch monthly OHLCV time series for a cryptocurrency.

    :param symbol: Crypto symbol, e.g. "BTC".
    :param market: Market currency, e.g. "USD".
    """
    return get_crypto_monthly(symbol, market)


# ============================================================================
# Technical Indicators
# ============================================================================

@mcp.tool()
def indicator_sma(
    symbol: str,
    interval: str = "daily",
    time_period: int = 20,
    series_type: str = "close",
) -> dict:
    """
    Fetch Simple Moving Average (SMA) values for a symbol.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: 1min | 5min | 15min | 30min | 60min | daily | weekly | monthly.
    :param time_period: Lookback window (e.g. 20 for 20-day SMA).
    :param series_type: close | open | high | low.
    """
    return get_sma(symbol, interval, time_period, series_type)


@mcp.tool()
def indicator_ema(
    symbol: str,
    interval: str = "daily",
    time_period: int = 20,
    series_type: str = "close",
) -> dict:
    """
    Fetch Exponential Moving Average (EMA) values for a symbol.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: 1min | 5min | 15min | 30min | 60min | daily | weekly | monthly.
    :param time_period: Lookback window (e.g. 20 for 20-day EMA).
    :param series_type: close | open | high | low.
    """
    return get_ema(symbol, interval, time_period, series_type)


@mcp.tool()
def indicator_rsi(
    symbol: str,
    interval: str = "daily",
    time_period: int = 14,
    series_type: str = "close",
) -> dict:
    """
    Fetch Relative Strength Index (RSI) values for a symbol.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: 1min | 5min | 15min | 30min | 60min | daily | weekly | monthly.
    :param time_period: Lookback window (typically 14).
    :param series_type: close | open | high | low.
    """
    return get_rsi(symbol, interval, time_period, series_type)


@mcp.tool()
def indicator_macd(
    symbol: str,
    interval: str = "daily",
    series_type: str = "close",
    fastperiod: int = 12,
    slowperiod: int = 26,
    signalperiod: int = 9,
) -> dict:
    """
    Fetch MACD (Moving Average Convergence/Divergence) values for a symbol.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: 1min | 5min | 15min | 30min | 60min | daily | weekly | monthly.
    :param series_type: close | open | high | low.
    :param fastperiod: Fast EMA period (default 12).
    :param slowperiod: Slow EMA period (default 26).
    :param signalperiod: Signal EMA period (default 9).
    """
    return get_macd(symbol, interval, series_type, fastperiod, slowperiod, signalperiod)


@mcp.tool()
def indicator_bbands(
    symbol: str,
    interval: str = "daily",
    time_period: int = 20,
    series_type: str = "close",
    nbdevup: int = 2,
    nbdevdn: int = 2,
    matype: int = 0,
) -> dict:
    """
    Fetch Bollinger Bands (upper, middle, lower) for a symbol.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: 1min | 5min | 15min | 30min | 60min | daily | weekly | monthly.
    :param time_period: Lookback window (typically 20).
    :param series_type: close | open | high | low.
    :param nbdevup: Std-dev multiplier for upper band (default 2).
    :param nbdevdn: Std-dev multiplier for lower band (default 2).
    :param matype: MA type: 0=SMA, 1=EMA, 2=WMA, …
    """
    return get_bbands(symbol, interval, time_period, series_type, nbdevup, nbdevdn, matype)


@mcp.tool()
def indicator_vwap(symbol: str, interval: str = "5min") -> dict:
    """
    Fetch Volume Weighted Average Price (VWAP) for a symbol.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: Intraday interval: 1min | 5min | 15min | 30min | 60min.
    """
    return get_vwap(symbol, interval)


@mcp.tool()
def indicator_stoch(
    symbol: str,
    interval: str = "daily",
    fastkperiod: int = 5,
    slowkperiod: int = 3,
    slowdperiod: int = 3,
    slowkmatype: int = 0,
    slowdmatype: int = 0,
) -> dict:
    """
    Fetch Stochastic Oscillator (SlowK, SlowD) for a symbol.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: 1min | 5min | 15min | 30min | 60min | daily | weekly | monthly.
    :param fastkperiod: Fast %K period.
    :param slowkperiod: Slow %K period.
    :param slowdperiod: Slow %D period.
    :param slowkmatype: MA type for Slow %K.
    :param slowdmatype: MA type for Slow %D.
    """
    return get_stoch(symbol, interval, fastkperiod, slowkperiod, slowdperiod, slowkmatype, slowdmatype)


@mcp.tool()
def indicator_adx(
    symbol: str,
    interval: str = "daily",
    time_period: int = 14,
) -> dict:
    """
    Fetch Average Directional Movement Index (ADX) for a symbol.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: 1min | 5min | 15min | 30min | 60min | daily | weekly | monthly.
    :param time_period: Lookback window (typically 14).
    """
    return get_adx(symbol, interval, time_period)


@mcp.tool()
def indicator_cci(
    symbol: str,
    interval: str = "daily",
    time_period: int = 20,
) -> dict:
    """
    Fetch Commodity Channel Index (CCI) for a symbol.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: 1min | 5min | 15min | 30min | 60min | daily | weekly | monthly.
    :param time_period: Lookback window (typically 20).
    """
    return get_cci(symbol, interval, time_period)


@mcp.tool()
def indicator_aroon(
    symbol: str,
    interval: str = "daily",
    time_period: int = 14,
) -> dict:
    """
    Fetch Aroon indicator (Aroon Up, Aroon Down) for a symbol.

    :param symbol: Ticker symbol, e.g. "IBM".
    :param interval: 1min | 5min | 15min | 30min | 60min | daily | weekly | monthly.
    :param time_period: Lookback window (typically 14).
    """
    return get_aroon(symbol, interval, time_period)


# ============================================================================
# Fundamental Data
# ============================================================================

@mcp.tool()
def fundamental_company_overview(symbol: str) -> dict:
    """
    Fetch company overview: description, sector, market cap, P/E, EPS, dividend yield, etc.

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return get_company_overview(symbol)


@mcp.tool()
def fundamental_income_statement(symbol: str) -> dict:
    """
    Fetch annual and quarterly income statements for a company.

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return get_income_statement(symbol)


@mcp.tool()
def fundamental_balance_sheet(symbol: str) -> dict:
    """
    Fetch annual and quarterly balance sheets for a company.

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return get_balance_sheet(symbol)


@mcp.tool()
def fundamental_cash_flow(symbol: str) -> dict:
    """
    Fetch annual and quarterly cash flow statements for a company.

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return get_cash_flow(symbol)


@mcp.tool()
def fundamental_earnings(symbol: str) -> dict:
    """
    Fetch annual and quarterly EPS (earnings per share) data for a company.

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return get_earnings(symbol)


@mcp.tool()
def fundamental_earnings_calendar(
    symbol: str = "",
    horizon: str = "3month",
) -> dict:
    """
    Fetch upcoming earnings announcements for the next 3, 6, or 12 months.

    :param symbol: Optional ticker to filter, e.g. "IBM". Leave empty for all companies.
    :param horizon: "3month" | "6month" | "12month".
    """
    return get_earnings_calendar(symbol, horizon)


@mcp.tool()
def fundamental_ipo_calendar() -> dict:
    """
    Fetch a list of IPOs expected in the next three months.
    """
    return get_ipo_calendar()


@mcp.tool()
def fundamental_listing_status(date: str = "", state: str = "active") -> dict:
    """
    Fetch a list of active or delisted US stocks and ETFs.

    :param date: Optional date YYYY-MM-DD for historical listing status.
    :param state: "active" or "delisted".
    """
    return get_listing_status(date, state)


# ============================================================================
# Economic Indicators
# ============================================================================

@mcp.tool()
def economic_real_gdp(interval: str = "annual") -> dict:
    """
    Fetch US Real GDP data.

    :param interval: "annual" or "quarterly".
    """
    return get_real_gdp(interval)


@mcp.tool()
def economic_real_gdp_per_capita() -> dict:
    """
    Fetch US quarterly Real GDP per Capita data.
    """
    return get_real_gdp_per_capita()


@mcp.tool()
def economic_treasury_yield(
    interval: str = "monthly",
    maturity: str = "10year",
) -> dict:
    """
    Fetch US Treasury yield for a given maturity and interval.

    :param interval: "daily" | "weekly" | "monthly".
    :param maturity: "3month" | "2year" | "5year" | "7year" | "10year" | "30year".
    """
    return get_treasury_yield(interval, maturity)


@mcp.tool()
def economic_federal_funds_rate(interval: str = "monthly") -> dict:
    """
    Fetch the US Federal Funds Rate (interest rate).

    :param interval: "daily" | "weekly" | "monthly".
    """
    return get_federal_funds_rate(interval)


@mcp.tool()
def economic_cpi(interval: str = "monthly") -> dict:
    """
    Fetch US Consumer Price Index (CPI).

    :param interval: "monthly" or "semiannual".
    """
    return get_cpi(interval)


@mcp.tool()
def economic_inflation() -> dict:
    """
    Fetch annual US inflation rate (year-over-year CPI change).
    """
    return get_inflation()


@mcp.tool()
def economic_retail_sales() -> dict:
    """
    Fetch monthly US Advance Retail Sales data.
    """
    return get_retail_sales()


@mcp.tool()
def economic_durables() -> dict:
    """
    Fetch monthly US manufacturers' new orders for durable goods.
    """
    return get_durables()


@mcp.tool()
def economic_unemployment() -> dict:
    """
    Fetch monthly US unemployment rate.
    """
    return get_unemployment()


@mcp.tool()
def economic_nonfarm_payroll() -> dict:
    """
    Fetch monthly US Total Nonfarm Employees (nonfarm payroll).
    """
    return get_nonfarm_payroll()


# ============================================================================
# Sector Performance
# ============================================================================

@mcp.tool()
def sector_performance() -> dict:
    """
    Fetch real-time and historical S&P 500 sector performance across multiple
    time horizons (real-time, 1-day, 5-day, 1-month, 3-month, YTD, 1-year,
    3-year, 5-year, 10-year).
    """
    return get_sector_performance()


# ============================================================================
# Entry point
# ============================================================================

if __name__ == "__main__":
    mcp.run()
