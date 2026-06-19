#!/usr/bin/env python3
"""
MCP Server for Alpha Vantage Financial Data API
Provides comprehensive coverage of stock data, forex, crypto, technical indicators, fundamentals, and economic indicators.
"""

import os
import requests
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("Alpha Vantage")

# Get API key from environment
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", "demo")
BASE_URL = "https://www.alphavantage.co/query"


def make_request(params: dict) -> dict:
    """Make a request to the Alpha Vantage API."""
    params["apikey"] = API_KEY
    try:
        response = requests.get(BASE_URL, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}
    except ValueError as e:
        return {"error": f"Failed to parse response: {str(e)}"}


# ============================================================================
# TIME SERIES STOCK DATA APIs
# ============================================================================

@mcp.tool()
def get_intraday_timeseries(
    symbol: str,
    interval: str,
    adjusted: bool = True,
    extended_hours: bool = True,
    month: str = None,
    outputsize: str = "compact",
) -> dict:
    """
    Get intraday OHLCV time series data for a stock.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
        interval: Time interval ('1min', '5min', '15min', '30min', '60min')
        adjusted: Whether to adjust for splits/dividends (default: True)
        extended_hours: Include pre/post-market hours (default: True)
        month: Specific month in YYYY-MM format (optional)
        outputsize: 'compact' (latest 100) or 'full' (30 days or full month)
    """
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "adjusted": "true" if adjusted else "false",
        "extended_hours": "true" if extended_hours else "false",
        "outputsize": outputsize,
    }
    if month:
        params["month"] = month
    return make_request(params)


@mcp.tool()
def get_daily_timeseries(symbol: str, outputsize: str = "compact") -> dict:
    """
    Get daily OHLCV time series data for a stock (raw, as-traded).
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
        outputsize: 'compact' (latest 100) or 'full' (20+ years)
    """
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": outputsize,
    }
    return make_request(params)


@mcp.tool()
def get_daily_adjusted_timeseries(symbol: str, outputsize: str = "compact") -> dict:
    """
    Get daily OHLCV time series data adjusted for splits/dividends.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
        outputsize: 'compact' (latest 100) or 'full' (20+ years)
    """
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": symbol,
        "outputsize": outputsize,
    }
    return make_request(params)


@mcp.tool()
def get_weekly_timeseries(symbol: str) -> dict:
    """
    Get weekly OHLCV time series data for a stock.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "TIME_SERIES_WEEKLY",
        "symbol": symbol,
    }
    return make_request(params)


@mcp.tool()
def get_weekly_adjusted_timeseries(symbol: str) -> dict:
    """
    Get weekly OHLCV time series data adjusted for splits/dividends.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "TIME_SERIES_WEEKLY_ADJUSTED",
        "symbol": symbol,
    }
    return make_request(params)


@mcp.tool()
def get_monthly_timeseries(symbol: str) -> dict:
    """
    Get monthly OHLCV time series data for a stock.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "TIME_SERIES_MONTHLY",
        "symbol": symbol,
    }
    return make_request(params)


@mcp.tool()
def get_monthly_adjusted_timeseries(symbol: str) -> dict:
    """
    Get monthly OHLCV time series data adjusted for splits/dividends.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "TIME_SERIES_MONTHLY_ADJUSTED",
        "symbol": symbol,
    }
    return make_request(params)


@mcp.tool()
def get_quote_endpoint(symbol: str) -> dict:
    """
    Get the latest price and volume for a stock (quote endpoint).
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
    }
    return make_request(params)


@mcp.tool()
def search_symbol(keywords: str) -> dict:
    """
    Search for stock symbols by keywords.
    
    Args:
        keywords: Search keywords (e.g., 'IBM', 'Apple')
    """
    params = {
        "function": "SYMBOL_SEARCH",
        "keywords": keywords,
    }
    return make_request(params)


# ============================================================================
# FOREX (FX) APIs
# ============================================================================

@mcp.tool()
def get_currency_exchange_rate(from_currency: str, to_currency: str) -> dict:
    """
    Get realtime exchange rate between two currencies (fiat or crypto).
    
    Args:
        from_currency: Source currency code (e.g., 'USD', 'BTC')
        to_currency: Target currency code (e.g., 'EUR', 'JPY')
    """
    params = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": from_currency,
        "to_currency": to_currency,
    }
    return make_request(params)


@mcp.tool()
def get_fx_intraday(
    from_symbol: str,
    to_symbol: str,
    interval: str,
    outputsize: str = "compact",
) -> dict:
    """
    Get intraday FX time series data.
    
    Args:
        from_symbol: Source currency (3-letter code, e.g., 'EUR')
        to_symbol: Target currency (3-letter code, e.g., 'USD')
        interval: Time interval ('1min', '5min', '15min', '30min', '60min')
        outputsize: 'compact' (latest 100) or 'full'
    """
    params = {
        "function": "FX_INTRADAY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "interval": interval,
        "outputsize": outputsize,
    }
    return make_request(params)


@mcp.tool()
def get_fx_daily(
    from_symbol: str,
    to_symbol: str,
    outputsize: str = "compact",
) -> dict:
    """
    Get daily FX time series data.
    
    Args:
        from_symbol: Source currency (3-letter code, e.g., 'EUR')
        to_symbol: Target currency (3-letter code, e.g., 'USD')
        outputsize: 'compact' (latest 100) or 'full'
    """
    params = {
        "function": "FX_DAILY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "outputsize": outputsize,
    }
    return make_request(params)


@mcp.tool()
def get_fx_weekly(
    from_symbol: str,
    to_symbol: str,
) -> dict:
    """
    Get weekly FX time series data.
    
    Args:
        from_symbol: Source currency (3-letter code, e.g., 'EUR')
        to_symbol: Target currency (3-letter code, e.g., 'USD')
    """
    params = {
        "function": "FX_WEEKLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
    }
    return make_request(params)


@mcp.tool()
def get_fx_monthly(
    from_symbol: str,
    to_symbol: str,
) -> dict:
    """
    Get monthly FX time series data.
    
    Args:
        from_symbol: Source currency (3-letter code, e.g., 'EUR')
        to_symbol: Target currency (3-letter code, e.g., 'USD')
    """
    params = {
        "function": "FX_MONTHLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
    }
    return make_request(params)


# ============================================================================
# CRYPTOCURRENCY APIs
# ============================================================================

@mcp.tool()
def get_crypto_intraday(
    symbol: str,
    market: str,
    interval: str,
    outputsize: str = "compact",
) -> dict:
    """
    Get intraday cryptocurrency time series data.
    
    Args:
        symbol: Cryptocurrency symbol (e.g., 'BTC', 'ETH')
        market: Market currency (e.g., 'USD', 'EUR')
        interval: Time interval ('1min', '5min', '15min', '30min', '60min')
        outputsize: 'compact' (latest 100) or 'full'
    """
    params = {
        "function": "CRYPTO_INTRADAY",
        "symbol": symbol,
        "market": market,
        "interval": interval,
        "outputsize": outputsize,
    }
    return make_request(params)


@mcp.tool()
def get_digital_currency_daily(symbol: str, market: str) -> dict:
    """
    Get daily cryptocurrency time series data.
    
    Args:
        symbol: Cryptocurrency symbol (e.g., 'BTC', 'ETH')
        market: Market currency (e.g., 'USD', 'EUR')
    """
    params = {
        "function": "DIGITAL_CURRENCY_DAILY",
        "symbol": symbol,
        "market": market,
    }
    return make_request(params)


@mcp.tool()
def get_digital_currency_weekly(symbol: str, market: str) -> dict:
    """
    Get weekly cryptocurrency time series data.
    
    Args:
        symbol: Cryptocurrency symbol (e.g., 'BTC', 'ETH')
        market: Market currency (e.g., 'USD', 'EUR')
    """
    params = {
        "function": "DIGITAL_CURRENCY_WEEKLY",
        "symbol": symbol,
        "market": market,
    }
    return make_request(params)


@mcp.tool()
def get_digital_currency_monthly(symbol: str, market: str) -> dict:
    """
    Get monthly cryptocurrency time series data.
    
    Args:
        symbol: Cryptocurrency symbol (e.g., 'BTC', 'ETH')
        market: Market currency (e.g., 'USD', 'EUR')
    """
    params = {
        "function": "DIGITAL_CURRENCY_MONTHLY",
        "symbol": symbol,
        "market": market,
    }
    return make_request(params)


# ============================================================================
# TECHNICAL INDICATORS APIs
# ============================================================================

@mcp.tool()
def get_sma(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    month: str = None,
) -> dict:
    """
    Get Simple Moving Average (SMA) technical indicator.
    
    Args:
        symbol: Stock or forex symbol (e.g., 'IBM', 'USDEUR')
        interval: Time interval ('1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly')
        time_period: Number of data points for calculation (e.g., 10, 200)
        series_type: Price type ('close', 'open', 'high', 'low')
        month: Specific month in YYYY-MM format (optional)
    """
    params = {
        "function": "SMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    }
    if month:
        params["month"] = month
    return make_request(params)


@mcp.tool()
def get_ema(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    month: str = None,
) -> dict:
    """
    Get Exponential Moving Average (EMA) technical indicator.
    
    Args:
        symbol: Stock or forex symbol (e.g., 'IBM', 'USDEUR')
        interval: Time interval ('1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly')
        time_period: Number of data points for calculation (e.g., 10, 200)
        series_type: Price type ('close', 'open', 'high', 'low')
        month: Specific month in YYYY-MM format (optional)
    """
    params = {
        "function": "EMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    }
    if month:
        params["month"] = month
    return make_request(params)


@mcp.tool()
def get_wma(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    month: str = None,
) -> dict:
    """
    Get Weighted Moving Average (WMA) technical indicator.
    
    Args:
        symbol: Stock or forex symbol (e.g., 'IBM', 'USDEUR')
        interval: Time interval ('1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly')
        time_period: Number of data points for calculation (e.g., 10, 200)
        series_type: Price type ('close', 'open', 'high', 'low')
        month: Specific month in YYYY-MM format (optional)
    """
    params = {
        "function": "WMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    }
    if month:
        params["month"] = month
    return make_request(params)


@mcp.tool()
def get_rsi(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    month: str = None,
) -> dict:
    """
    Get Relative Strength Index (RSI) technical indicator.
    
    Args:
        symbol: Stock or forex symbol (e.g., 'IBM', 'USDEUR')
        interval: Time interval ('1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly')
        time_period: Number of data points for calculation (e.g., 14)
        series_type: Price type ('close', 'open', 'high', 'low')
        month: Specific month in YYYY-MM format (optional)
    """
    params = {
        "function": "RSI",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    }
    if month:
        params["month"] = month
    return make_request(params)


@mcp.tool()
def get_macd(
    symbol: str,
    interval: str,
    series_type: str,
    month: str = None,
) -> dict:
    """
    Get MACD (Moving Average Convergence Divergence) technical indicator.
    
    Args:
        symbol: Stock or forex symbol (e.g., 'IBM', 'USDEUR')
        interval: Time interval ('1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly')
        series_type: Price type ('close', 'open', 'high', 'low')
        month: Specific month in YYYY-MM format (optional)
    """
    params = {
        "function": "MACD",
        "symbol": symbol,
        "interval": interval,
        "series_type": series_type,
    }
    if month:
        params["month"] = month
    return make_request(params)


@mcp.tool()
def get_bbands(
    symbol: str,
    interval: str,
    time_period: int,
    series_type: str,
    nbdevup: float = 2,
    nbdevdn: float = 2,
    month: str = None,
) -> dict:
    """
    Get Bollinger Bands technical indicator.
    
    Args:
        symbol: Stock or forex symbol (e.g., 'IBM', 'USDEUR')
        interval: Time interval ('1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly')
        time_period: Number of data points for calculation (e.g., 20)
        series_type: Price type ('close', 'open', 'high', 'low')
        nbdevup: Standard deviations for upper band (default: 2)
        nbdevdn: Standard deviations for lower band (default: 2)
        month: Specific month in YYYY-MM format (optional)
    """
    params = {
        "function": "BBANDS",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
        "nbdevup": nbdevup,
        "nbdevdn": nbdevdn,
    }
    if month:
        params["month"] = month
    return make_request(params)


# ============================================================================
# FUNDAMENTAL DATA APIs
# ============================================================================

@mcp.tool()
def get_company_overview(symbol: str) -> dict:
    """
    Get company overview and financial metrics.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "OVERVIEW",
        "symbol": symbol,
    }
    return make_request(params)


@mcp.tool()
def get_etf_profile(symbol: str) -> dict:
    """
    Get ETF profile, holdings, and metrics.
    
    Args:
        symbol: ETF symbol (e.g., 'QQQ')
    """
    params = {
        "function": "ETF_PROFILE",
        "symbol": symbol,
    }
    return make_request(params)


@mcp.tool()
def get_dividends(symbol: str) -> dict:
    """
    Get historical and future dividend distributions.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "DIVIDENDS",
        "symbol": symbol,
    }
    return make_request(params)


@mcp.tool()
def get_splits(symbol: str) -> dict:
    """
    Get historical stock split events.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "SPLITS",
        "symbol": symbol,
    }
    return make_request(params)


@mcp.tool()
def get_income_statement(symbol: str) -> dict:
    """
    Get income statement data.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "INCOME_STATEMENT",
        "symbol": symbol,
    }
    return make_request(params)


@mcp.tool()
def get_balance_sheet(symbol: str) -> dict:
    """
    Get balance sheet data.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "BALANCE_SHEET",
        "symbol": symbol,
    }
    return make_request(params)


@mcp.tool()
def get_cash_flow(symbol: str) -> dict:
    """
    Get cash flow statement data.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "CASH_FLOW",
        "symbol": symbol,
    }
    return make_request(params)


@mcp.tool()
def get_earnings(symbol: str) -> dict:
    """
    Get earnings data.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "EARNINGS",
        "symbol": symbol,
    }
    return make_request(params)


# ============================================================================
# ECONOMIC INDICATORS APIs
# ============================================================================

@mcp.tool()
def get_real_gdp(interval: str = "annual") -> dict:
    """
    Get Real GDP economic indicator.
    
    Args:
        interval: 'annual' or 'quarterly'
    """
    params = {
        "function": "REAL_GDP",
        "interval": interval,
    }
    return make_request(params)


@mcp.tool()
def get_real_gdp_per_capita() -> dict:
    """
    Get Real GDP per Capita economic indicator.
    """
    params = {
        "function": "REAL_GDP_PER_CAPITA",
    }
    return make_request(params)


@mcp.tool()
def get_treasury_yield(interval: str, maturity: str) -> dict:
    """
    Get US Treasury Yield economic indicator.
    
    Args:
        interval: 'daily', 'weekly', or 'monthly'
        maturity: '3month', '2year', '5year', '7year', '10year', '30year'
    """
    params = {
        "function": "TREASURY_YIELD",
        "interval": interval,
        "maturity": maturity,
    }
    return make_request(params)


@mcp.tool()
def get_federal_funds_rate(interval: str = "monthly") -> dict:
    """
    Get Federal Funds Rate economic indicator.
    
    Args:
        interval: 'daily', 'weekly', or 'monthly'
    """
    params = {
        "function": "FEDERAL_FUNDS_RATE",
        "interval": interval,
    }
    return make_request(params)


@mcp.tool()
def get_cpi(interval: str = "monthly") -> dict:
    """
    Get Consumer Price Index (CPI) economic indicator.
    
    Args:
        interval: 'monthly' or 'semiannual'
    """
    params = {
        "function": "CPI",
        "interval": interval,
    }
    return make_request(params)


@mcp.tool()
def get_inflation() -> dict:
    """
    Get Inflation Rate economic indicator.
    """
    params = {
        "function": "INFLATION",
    }
    return make_request(params)


@mcp.tool()
def get_retail_sales() -> dict:
    """
    Get Retail Sales economic indicator.
    """
    params = {
        "function": "RETAIL_SALES",
    }
    return make_request(params)


@mcp.tool()
def get_durables() -> dict:
    """
    Get Durable Goods Orders economic indicator.
    """
    params = {
        "function": "DURABLES",
    }
    return make_request(params)


@mcp.tool()
def get_unemployment() -> dict:
    """
    Get Unemployment Rate economic indicator.
    """
    params = {
        "function": "UNEMPLOYMENT",
    }
    return make_request(params)


@mcp.tool()
def get_nonfarm_payroll() -> dict:
    """
    Get Nonfarm Payroll economic indicator.
    """
    params = {
        "function": "NONFARM_PAYROLL",
    }
    return make_request(params)


# ============================================================================
# COMMODITIES APIs
# ============================================================================

@mcp.tool()
def get_gold_silver_spot(symbol: str) -> dict:
    """
    Get Gold or Silver spot prices.
    
    Args:
        symbol: 'GOLD' or 'SILVER'
    """
    params = {
        "function": "GOLD_SILVER_SPOT",
        "symbol": symbol,
    }
    return make_request(params)


@mcp.tool()
def get_gold_silver_history(symbol: str, interval: str = "daily") -> dict:
    """
    Get Gold or Silver historical prices.
    
    Args:
        symbol: 'GOLD' or 'SILVER'
        interval: 'daily', 'weekly', or 'monthly'
    """
    params = {
        "function": "GOLD_SILVER_HISTORY",
        "symbol": symbol,
        "interval": interval,
    }
    return make_request(params)


@mcp.tool()
def get_wti(interval: str = "monthly") -> dict:
    """
    Get WTI Crude Oil prices.
    
    Args:
        interval: 'monthly' or 'weekly'
    """
    params = {
        "function": "WTI",
        "interval": interval,
    }
    return make_request(params)


@mcp.tool()
def get_brent(interval: str = "monthly") -> dict:
    """
    Get Brent Crude Oil prices.
    
    Args:
        interval: 'monthly' or 'weekly'
    """
    params = {
        "function": "BRENT",
        "interval": interval,
    }
    return make_request(params)


@mcp.tool()
def get_natural_gas(interval: str = "monthly") -> dict:
    """
    Get Natural Gas prices.
    
    Args:
        interval: 'monthly' or 'weekly'
    """
    params = {
        "function": "NATURAL_GAS",
        "interval": interval,
    }
    return make_request(params)


@mcp.tool()
def get_copper(interval: str = "monthly") -> dict:
    """
    Get Copper prices.
    
    Args:
        interval: 'monthly' or 'weekly'
    """
    params = {
        "function": "COPPER",
        "interval": interval,
    }
    return make_request(params)


@mcp.tool()
def get_aluminum(interval: str = "monthly") -> dict:
    """
    Get Aluminum prices.
    
    Args:
        interval: 'monthly' or 'weekly'
    """
    params = {
        "function": "ALUMINUM",
        "interval": interval,
    }
    return make_request(params)


@mcp.tool()
def get_wheat(interval: str = "monthly") -> dict:
    """
    Get Wheat prices.
    
    Args:
        interval: 'monthly' or 'weekly'
    """
    params = {
        "function": "WHEAT",
        "interval": interval,
    }
    return make_request(params)


@mcp.tool()
def get_corn(interval: str = "monthly") -> dict:
    """
    Get Corn prices.
    
    Args:
        interval: 'monthly' or 'weekly'
    """
    params = {
        "function": "CORN",
        "interval": interval,
    }
    return make_request(params)


@mcp.tool()
def get_cotton(interval: str = "monthly") -> dict:
    """
    Get Cotton prices.
    
    Args:
        interval: 'monthly' or 'weekly'
    """
    params = {
        "function": "COTTON",
        "interval": interval,
    }
    return make_request(params)


@mcp.tool()
def get_sugar(interval: str = "monthly") -> dict:
    """
    Get Sugar prices.
    
    Args:
        interval: 'monthly' or 'weekly'
    """
    params = {
        "function": "SUGAR",
        "interval": interval,
    }
    return make_request(params)


@mcp.tool()
def get_coffee(interval: str = "monthly") -> dict:
    """
    Get Coffee prices.
    
    Args:
        interval: 'monthly' or 'weekly'
    """
    params = {
        "function": "COFFEE",
        "interval": interval,
    }
    return make_request(params)


@mcp.tool()
def get_all_commodities(interval: str = "monthly") -> dict:
    """
    Get all commodities prices.
    
    Args:
        interval: 'monthly' or 'weekly'
    """
    params = {
        "function": "ALL_COMMODITIES",
        "interval": interval,
    }
    return make_request(params)


# ============================================================================
# OPTIONS DATA APIs
# ============================================================================

@mcp.tool()
def get_realtime_options(
    symbol: str,
    require_greeks: bool = False,
    contract: str = None,
    expiration: str = None,
) -> dict:
    """
    Get realtime US options data with full market coverage.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
        require_greeks: Enable greeks & implied volatility fields (default: False)
        contract: Specific options contract ID (optional)
        expiration: Contract expiration date in YYYY-MM-DD format (optional)
    """
    params = {
        "function": "REALTIME_OPTIONS",
        "symbol": symbol,
        "require_greeks": "true" if require_greeks else "false",
    }
    if contract:
        params["contract"] = contract
    if expiration:
        params["expiration"] = expiration
    return make_request(params)


@mcp.tool()
def get_realtime_put_call_ratio(symbol: str) -> dict:
    """
    Get realtime put-call ratios for an option chain.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "REALTIME_PUT_CALL_RATIO",
        "symbol": symbol,
    }
    return make_request(params)


@mcp.tool()
def get_realtime_volume_open_interest_ratio(symbol: str) -> dict:
    """
    Get realtime volume-to-open-interest ratios within an option chain.
    
    Args:
        symbol: Stock symbol (e.g., 'NVDA')
    """
    params = {
        "function": "REALTIME_VOLUME_OPEN_INTEREST_RATIO",
        "symbol": symbol,
    }
    return make_request(params)


@mcp.tool()
def get_historical_options(
    symbol: str,
    date: str = None,
    contract: str = None,
) -> dict:
    """
    Get historical options chain data for a specific symbol and date.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
        date: Date in YYYY-MM-DD format (optional, defaults to previous trading session)
        contract: Specific options contract ID (optional)
    """
    params = {
        "function": "HISTORICAL_OPTIONS",
        "symbol": symbol,
    }
    if date:
        params["date"] = date
    if contract:
        params["contract"] = contract
    return make_request(params)


# ============================================================================
# ALPHA INTELLIGENCE APIs
# ============================================================================

@mcp.tool()
def get_news_sentiment(
    tickers: str = None,
    topics: str = None,
    time_from: str = None,
    time_to: str = None,
    sort: str = "LATEST",
    limit: int = 50,
) -> dict:
    """
    Get market news and sentiment data.
    
    Args:
        tickers: Comma-separated list of tickers (e.g., 'IBM', 'COIN,CRYPTO:BTC,FOREX:USD')
        topics: Comma-separated topics (e.g., 'technology', 'earnings', 'ipo', 'mergers_and_acquisitions')
        time_from: Start time in YYYYMMDDTHHMM format (e.g., '20220410T0130')
        time_to: End time in YYYYMMDDTHHMM format
        sort: 'LATEST', 'EARLIEST', or 'RELEVANCE'
        limit: Number of results (1-1000, default: 50)
    """
    params = {
        "function": "NEWS_SENTIMENT",
        "sort": sort,
        "limit": limit,
    }
    if tickers:
        params["tickers"] = tickers
    if topics:
        params["topics"] = topics
    if time_from:
        params["time_from"] = time_from
    if time_to:
        params["time_to"] = time_to
    return make_request(params)


@mcp.tool()
def get_earnings_call_transcript(symbol: str, quarter: str) -> dict:
    """
    Get earnings call transcript for a company in a specific quarter.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
        quarter: Fiscal quarter in YYYYQM format (e.g., '2024Q1')
    """
    params = {
        "function": "EARNINGS_CALL_TRANSCRIPT",
        "symbol": symbol,
        "quarter": quarter,
    }
    return make_request(params)


@mcp.tool()
def get_top_gainers_losers() -> dict:
    """
    Get top 20 gainers, losers, and most actively traded tickers in the US market.
    """
    params = {
        "function": "TOP_GAINERS_LOSERS",
    }
    return make_request(params)


@mcp.tool()
def get_insider_transactions(
    symbol: str,
    from_date: str = None,
    to_date: str = None,
) -> dict:
    """
    Get insider transactions for a company.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM')
        from_date: Start date in YYYY-MM-DD format (optional)
        to_date: End date in YYYY-MM-DD format (optional)
    """
    params = {
        "function": "INSIDER_TRANSACTIONS",
        "symbol": symbol,
    }
    if from_date:
        params["from"] = from_date
    if to_date:
        params["to"] = to_date
    return make_request(params)


if __name__ == "__main__":
    mcp.run()
