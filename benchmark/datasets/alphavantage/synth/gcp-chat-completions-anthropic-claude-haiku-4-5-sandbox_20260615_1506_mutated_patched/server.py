#!/usr/bin/env python3
"""
Alpha Vantage MCP Server

A comprehensive MCP server for the Alpha Vantage financial data API.
Provides tools for stock time series, forex, crypto, technical indicators,
fundamental data, economic indicators, commodities, options, and market intelligence.
"""

import os
import requests
from typing import Any, Optional
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
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}
    except ValueError as e:
        return {"error": f"Invalid JSON response: {str(e)}"}


# ============================================================================
# TIME SERIES STOCK DATA ENDPOINTS
# ============================================================================

@mcp.tool()
def get_intraday_data(
    ticker: str,
    time_interval: str,
    adjusted: Optional[bool] = True,
    extended_hours: Optional[bool] = True,
    month: Optional[str] = None,
    output_size: Optional[str] = "compact",
) -> dict:
    """Get intraday OHLCV time series data for a stock.
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
        time_interval: Time interval between data points ('1min', '5min', '15min', '30min', '60min')
        adjusted: Whether to adjust for splits/dividends (default: true)
        extended_hours: Include pre/post-market hours (default: true)
        month: Specific month in YYYY-MM format (optional)
        output_size: 'compact' (latest 100) or 'full' (30 days or full month)
    """
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "ticker": ticker,
        "time_interval": time_interval,
        "adjusted": str(adjusted).lower(),
        "extended_hours": str(extended_hours).lower(),
        "output_size": output_size,
    }
    if month:
        params["month"] = month
    return make_request(params)


@mcp.tool()
def get_daily_data(
    ticker: str,
    output_size: Optional[str] = "compact",
) -> dict:
    """Get daily OHLCV time series data for a stock.
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
        output_size: 'compact' (latest 100) or 'full' (20+ years)
    """
    params = {
        "function": "TIME_SERIES_DAILY",
        "ticker": ticker,
        "output_size": output_size,
    }
    return make_request(params)


@mcp.tool()
def get_daily_adjusted_data(
    ticker: str,
    output_size: Optional[str] = "compact",
) -> dict:
    """Get daily adjusted OHLCV time series data for a stock (includes splits/dividends).
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
        output_size: 'compact' (latest 100) or 'full' (20+ years)
    """
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "ticker": ticker,
        "output_size": output_size,
    }
    return make_request(params)


@mcp.tool()
def get_weekly_data(ticker: str) -> dict:
    """Get weekly OHLCV time series data for a stock.
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "TIME_SERIES_WEEKLY",
        "ticker": ticker,
    }
    return make_request(params)


@mcp.tool()
def get_weekly_adjusted_data(ticker: str) -> dict:
    """Get weekly adjusted OHLCV time series data for a stock (includes splits/dividends).
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "TIME_SERIES_WEEKLY_ADJUSTED",
        "ticker": ticker,
    }
    return make_request(params)


@mcp.tool()
def get_monthly_data(ticker: str) -> dict:
    """Get monthly OHLCV time series data for a stock.
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "TIME_SERIES_MONTHLY",
        "ticker": ticker,
    }
    return make_request(params)


@mcp.tool()
def get_monthly_adjusted_data(ticker: str) -> dict:
    """Get monthly adjusted OHLCV time series data for a stock (includes splits/dividends).
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "TIME_SERIES_MONTHLY_ADJUSTED",
        "ticker": ticker,
    }
    return make_request(params)


@mcp.tool()
def get_quote_endpoint(ticker: str) -> dict:
    """Get the latest price and volume for a stock (quote endpoint).
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "GLOBAL_QUOTE",
        "ticker": ticker,
    }
    return make_request(params)


@mcp.tool()
def search_symbol(keywords: str) -> dict:
    """Search for stock symbols by keywords.
    
    Args:
        keywords: Search keywords (e.g., 'IBM', 'Apple')
    """
    params = {
        "function": "SYMBOL_SEARCH",
        "keywords": keywords,
    }
    return make_request(params)


# ============================================================================
# FOREX (FX) ENDPOINTS
# ============================================================================

@mcp.tool()
def get_currency_exchange_rate(from_currency: str, to_currency: str) -> dict:
    """Get realtime exchange rate between two currencies.
    
    Args:
        from_currency: Source currency code (e.g., 'USD', 'BTC')
        to_currency: Target currency code (e.g., 'JPY', 'EUR')
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
    time_interval: str,
    output_size: Optional[str] = "compact",
) -> dict:
    """Get intraday FX time series data.
    
    Args:
        from_symbol: Source currency code (e.g., 'EUR')
        to_symbol: Target currency code (e.g., 'USD')
        time_interval: Time interval ('1min', '5min', '15min', '30min', '60min')
        output_size: 'compact' (latest 100) or 'full'
    """
    params = {
        "function": "FX_INTRADAY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "time_interval": time_interval,
        "output_size": output_size,
    }
    return make_request(params)


@mcp.tool()
def get_fx_daily(
    from_symbol: str,
    to_symbol: str,
    output_size: Optional[str] = "compact",
) -> dict:
    """Get daily FX time series data.
    
    Args:
        from_symbol: Source currency code (e.g., 'EUR')
        to_symbol: Target currency code (e.g., 'USD')
        output_size: 'compact' (latest 100) or 'full'
    """
    params = {
        "function": "FX_DAILY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "output_size": output_size,
    }
    return make_request(params)


@mcp.tool()
def get_fx_weekly(
    from_symbol: str,
    to_symbol: str,
) -> dict:
    """Get weekly FX time series data.
    
    Args:
        from_symbol: Source currency code (e.g., 'EUR')
        to_symbol: Target currency code (e.g., 'USD')
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
    """Get monthly FX time series data.
    
    Args:
        from_symbol: Source currency code (e.g., 'EUR')
        to_symbol: Target currency code (e.g., 'USD')
    """
    params = {
        "function": "FX_MONTHLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
    }
    return make_request(params)


# ============================================================================
# DIGITAL CURRENCY (CRYPTO) ENDPOINTS
# ============================================================================

@mcp.tool()
def get_crypto_intraday(
    ticker: str,
    market: str,
    time_interval: str,
    output_size: Optional[str] = "compact",
) -> dict:
    """Get intraday cryptocurrency time series data.
    
    Args:
        ticker: Cryptocurrency symbol (e.g., 'BTC', 'ETH')
        market: Market currency (e.g., 'USD', 'EUR')
        time_interval: Time interval ('1min', '5min', '15min', '30min', '60min')
        output_size: 'compact' (latest 100) or 'full'
    """
    params = {
        "function": "CRYPTO_INTRADAY",
        "ticker": ticker,
        "market": market,
        "time_interval": time_interval,
        "output_size": output_size,
    }
    return make_request(params)


@mcp.tool()
def get_digital_currency_daily(ticker: str, market: str) -> dict:
    """Get daily cryptocurrency time series data.
    
    Args:
        ticker: Cryptocurrency symbol (e.g., 'BTC', 'ETH')
        market: Market currency (e.g., 'USD', 'EUR')
    """
    params = {
        "function": "DIGITAL_CURRENCY_DAILY",
        "ticker": ticker,
        "market": market,
    }
    return make_request(params)


@mcp.tool()
def get_digital_currency_weekly(ticker: str, market: str) -> dict:
    """Get weekly cryptocurrency time series data.
    
    Args:
        ticker: Cryptocurrency symbol (e.g., 'BTC', 'ETH')
        market: Market currency (e.g., 'USD', 'EUR')
    """
    params = {
        "function": "DIGITAL_CURRENCY_WEEKLY",
        "ticker": ticker,
        "market": market,
    }
    return make_request(params)


@mcp.tool()
def get_digital_currency_monthly(ticker: str, market: str) -> dict:
    """Get monthly cryptocurrency time series data.
    
    Args:
        ticker: Cryptocurrency symbol (e.g., 'BTC', 'ETH')
        market: Market currency (e.g., 'USD', 'EUR')
    """
    params = {
        "function": "DIGITAL_CURRENCY_MONTHLY",
        "ticker": ticker,
        "market": market,
    }
    return make_request(params)


# ============================================================================
# TECHNICAL INDICATORS ENDPOINTS
# ============================================================================

@mcp.tool()
def get_sma(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
) -> dict:
    """Get Simple Moving Average (SMA) technical indicator.
    
    Args:
        ticker: Stock or forex symbol (e.g., 'IBM', 'USDEUR')
        time_interval: Time interval ('1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly')
        time_period: Number of data points for calculation (e.g., 10, 200)
        price_type: Price type ('close', 'open', 'high', 'low')
        month: Specific month in YYYY-MM format (optional)
    """
    params = {
        "function": "SMA",
        "ticker": ticker,
        "time_interval": time_interval,
        "time_period": time_period,
        "price_type": price_type,
    }
    if month:
        params["month"] = month
    return make_request(params)


@mcp.tool()
def get_ema(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
) -> dict:
    """Get Exponential Moving Average (EMA) technical indicator.
    
    Args:
        ticker: Stock or forex symbol (e.g., 'IBM', 'USDEUR')
        time_interval: Time interval ('1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly')
        time_period: Number of data points for calculation (e.g., 10, 200)
        price_type: Price type ('close', 'open', 'high', 'low')
        month: Specific month in YYYY-MM format (optional)
    """
    params = {
        "function": "EMA",
        "ticker": ticker,
        "time_interval": time_interval,
        "time_period": time_period,
        "price_type": price_type,
    }
    if month:
        params["month"] = month
    return make_request(params)


@mcp.tool()
def get_wma(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
) -> dict:
    """Get Weighted Moving Average (WMA) technical indicator.
    
    Args:
        ticker: Stock or forex symbol (e.g., 'IBM', 'USDEUR')
        time_interval: Time interval ('1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly')
        time_period: Number of data points for calculation (e.g., 10, 200)
        price_type: Price type ('close', 'open', 'high', 'low')
        month: Specific month in YYYY-MM format (optional)
    """
    params = {
        "function": "WMA",
        "ticker": ticker,
        "time_interval": time_interval,
        "time_period": time_period,
        "price_type": price_type,
    }
    if month:
        params["month"] = month
    return make_request(params)


@mcp.tool()
def get_rsi(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
) -> dict:
    """Get Relative Strength Index (RSI) technical indicator.
    
    Args:
        ticker: Stock or forex symbol (e.g., 'IBM', 'USDEUR')
        time_interval: Time interval ('1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly')
        time_period: Number of data points for calculation (e.g., 14)
        price_type: Price type ('close', 'open', 'high', 'low')
        month: Specific month in YYYY-MM format (optional)
    """
    params = {
        "function": "RSI",
        "ticker": ticker,
        "time_interval": time_interval,
        "time_period": time_period,
        "price_type": price_type,
    }
    if month:
        params["month"] = month
    return make_request(params)


@mcp.tool()
def get_macd(
    ticker: str,
    time_interval: str,
    price_type: str,
    month: Optional[str] = None,
) -> dict:
    """Get MACD (Moving Average Convergence Divergence) technical indicator.
    
    Args:
        ticker: Stock or forex symbol (e.g., 'IBM', 'USDEUR')
        time_interval: Time interval ('1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly')
        price_type: Price type ('close', 'open', 'high', 'low')
        month: Specific month in YYYY-MM format (optional)
    """
    params = {
        "function": "MACD",
        "ticker": ticker,
        "time_interval": time_interval,
        "price_type": price_type,
    }
    if month:
        params["month"] = month
    return make_request(params)


@mcp.tool()
def get_bollinger_bands(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    nbdevup: Optional[int] = 2,
    nbdevdn: Optional[int] = 2,
    month: Optional[str] = None,
) -> dict:
    """Get Bollinger Bands technical indicator.
    
    Args:
        ticker: Stock or forex symbol (e.g., 'IBM', 'USDEUR')
        time_interval: Time interval ('1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly')
        time_period: Number of data points for calculation (e.g., 20)
        price_type: Price type ('close', 'open', 'high', 'low')
        nbdevup: Number of standard deviations for upper band (default: 2)
        nbdevdn: Number of standard deviations for lower band (default: 2)
        month: Specific month in YYYY-MM format (optional)
    """
    params = {
        "function": "BBANDS",
        "ticker": ticker,
        "time_interval": time_interval,
        "time_period": time_period,
        "price_type": price_type,
        "nbdevup": nbdevup,
        "nbdevdn": nbdevdn,
    }
    if month:
        params["month"] = month
    return make_request(params)


# ============================================================================
# FUNDAMENTAL DATA ENDPOINTS
# ============================================================================

@mcp.tool()
def get_company_overview(ticker: str) -> dict:
    """Get company overview and financial metrics.
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "OVERVIEW",
        "ticker": ticker,
    }
    return make_request(params)


@mcp.tool()
def get_etf_profile(ticker: str) -> dict:
    """Get ETF profile and holdings information.
    
    Args:
        ticker: ETF symbol (e.g., 'QQQ')
    """
    params = {
        "function": "ETF_PROFILE",
        "ticker": ticker,
    }
    return make_request(params)


@mcp.tool()
def get_dividends(ticker: str) -> dict:
    """Get historical and future dividend distributions.
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "DIVIDENDS",
        "ticker": ticker,
    }
    return make_request(params)


@mcp.tool()
def get_splits(ticker: str) -> dict:
    """Get historical stock split events.
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "SPLITS",
        "ticker": ticker,
    }
    return make_request(params)


@mcp.tool()
def get_income_statement(ticker: str) -> dict:
    """Get income statement data.
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "INCOME_STATEMENT",
        "ticker": ticker,
    }
    return make_request(params)


@mcp.tool()
def get_balance_sheet(ticker: str) -> dict:
    """Get balance sheet data.
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "BALANCE_SHEET",
        "ticker": ticker,
    }
    return make_request(params)


@mcp.tool()
def get_cash_flow(ticker: str) -> dict:
    """Get cash flow statement data.
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "CASH_FLOW",
        "ticker": ticker,
    }
    return make_request(params)


@mcp.tool()
def get_earnings(ticker: str) -> dict:
    """Get earnings data (EPS).
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "EARNINGS",
        "ticker": ticker,
    }
    return make_request(params)


# ============================================================================
# ECONOMIC INDICATORS ENDPOINTS
# ============================================================================

@mcp.tool()
def get_real_gdp(time_interval: Optional[str] = "annual") -> dict:
    """Get US Real GDP data.
    
    Args:
        time_interval: 'annual' or 'quarterly'
    """
    params = {
        "function": "REAL_GDP",
        "time_interval": time_interval,
    }
    return make_request(params)


@mcp.tool()
def get_real_gdp_per_capita() -> dict:
    """Get US Real GDP per Capita data."""
    params = {
        "function": "REAL_GDP_PER_CAPITA",
    }
    return make_request(params)


@mcp.tool()
def get_treasury_yield(
    time_interval: Optional[str] = "monthly",
    maturity: Optional[str] = "10year",
) -> dict:
    """Get US Treasury Yield data.
    
    Args:
        time_interval: 'daily', 'weekly', or 'monthly'
        maturity: '3month', '2year', '5year', '7year', '10year', or '30year'
    """
    params = {
        "function": "TREASURY_YIELD",
        "time_interval": time_interval,
        "maturity": maturity,
    }
    return make_request(params)


@mcp.tool()
def get_federal_funds_rate(time_interval: Optional[str] = "monthly") -> dict:
    """Get US Federal Funds Rate data.
    
    Args:
        time_interval: 'daily', 'weekly', or 'monthly'
    """
    params = {
        "function": "FEDERAL_FUNDS_RATE",
        "time_interval": time_interval,
    }
    return make_request(params)


@mcp.tool()
def get_cpi(time_interval: Optional[str] = "monthly") -> dict:
    """Get US Consumer Price Index (CPI) data.
    
    Args:
        time_interval: 'monthly' or 'semiannual'
    """
    params = {
        "function": "CPI",
        "time_interval": time_interval,
    }
    return make_request(params)


@mcp.tool()
def get_inflation() -> dict:
    """Get US Inflation data."""
    params = {
        "function": "INFLATION",
    }
    return make_request(params)


@mcp.tool()
def get_retail_sales() -> dict:
    """Get US Retail Sales data."""
    params = {
        "function": "RETAIL_SALES",
    }
    return make_request(params)


@mcp.tool()
def get_durables() -> dict:
    """Get US Durable Goods Orders data."""
    params = {
        "function": "DURABLES",
    }
    return make_request(params)


@mcp.tool()
def get_unemployment() -> dict:
    """Get US Unemployment Rate data."""
    params = {
        "function": "UNEMPLOYMENT",
    }
    return make_request(params)


@mcp.tool()
def get_nonfarm_payroll() -> dict:
    """Get US Nonfarm Payroll data."""
    params = {
        "function": "NONFARM_PAYROLL",
    }
    return make_request(params)


# ============================================================================
# COMMODITIES ENDPOINTS
# ============================================================================

@mcp.tool()
def get_gold_silver_spot(ticker: str) -> dict:
    """Get live spot prices for gold or silver.
    
    Args:
        ticker: 'GOLD', 'XAU', 'SILVER', or 'XAG'
    """
    params = {
        "function": "GOLD_SILVER_SPOT",
        "ticker": ticker,
    }
    return make_request(params)


@mcp.tool()
def get_gold_silver_history(
    ticker: str,
    time_interval: str,
) -> dict:
    """Get historical gold or silver prices.
    
    Args:
        ticker: 'GOLD', 'XAU', 'SILVER', or 'XAG'
        time_interval: 'daily', 'weekly', or 'monthly'
    """
    params = {
        "function": "GOLD_SILVER_HISTORY",
        "ticker": ticker,
        "time_interval": time_interval,
    }
    return make_request(params)


@mcp.tool()
def get_wti_crude_oil(time_interval: Optional[str] = "monthly") -> dict:
    """Get West Texas Intermediate (WTI) crude oil prices.
    
    Args:
        time_interval: 'daily', 'weekly', or 'monthly'
    """
    params = {
        "function": "WTI",
        "time_interval": time_interval,
    }
    return make_request(params)


@mcp.tool()
def get_brent_crude_oil(time_interval: Optional[str] = "monthly") -> dict:
    """Get Brent crude oil prices.
    
    Args:
        time_interval: 'daily', 'weekly', or 'monthly'
    """
    params = {
        "function": "BRENT",
        "time_interval": time_interval,
    }
    return make_request(params)


@mcp.tool()
def get_natural_gas(time_interval: Optional[str] = "monthly") -> dict:
    """Get natural gas prices.
    
    Args:
        time_interval: 'daily', 'weekly', or 'monthly'
    """
    params = {
        "function": "NATURAL_GAS",
        "time_interval": time_interval,
    }
    return make_request(params)


@mcp.tool()
def get_copper(time_interval: Optional[str] = "monthly") -> dict:
    """Get copper prices.
    
    Args:
        time_interval: 'daily', 'weekly', or 'monthly'
    """
    params = {
        "function": "COPPER",
        "time_interval": time_interval,
    }
    return make_request(params)


@mcp.tool()
def get_aluminum(time_interval: Optional[str] = "monthly") -> dict:
    """Get aluminum prices.
    
    Args:
        time_interval: 'daily', 'weekly', or 'monthly'
    """
    params = {
        "function": "ALUMINUM",
        "time_interval": time_interval,
    }
    return make_request(params)


@mcp.tool()
def get_wheat(time_interval: Optional[str] = "monthly") -> dict:
    """Get wheat prices.
    
    Args:
        time_interval: 'daily', 'weekly', or 'monthly'
    """
    params = {
        "function": "WHEAT",
        "time_interval": time_interval,
    }
    return make_request(params)


@mcp.tool()
def get_corn(time_interval: Optional[str] = "monthly") -> dict:
    """Get corn prices.
    
    Args:
        time_interval: 'daily', 'weekly', or 'monthly'
    """
    params = {
        "function": "CORN",
        "time_interval": time_interval,
    }
    return make_request(params)


@mcp.tool()
def get_cotton(time_interval: Optional[str] = "monthly") -> dict:
    """Get cotton prices.
    
    Args:
        time_interval: 'daily', 'weekly', or 'monthly'
    """
    params = {
        "function": "COTTON",
        "time_interval": time_interval,
    }
    return make_request(params)


@mcp.tool()
def get_sugar(time_interval: Optional[str] = "monthly") -> dict:
    """Get sugar prices.
    
    Args:
        time_interval: 'daily', 'weekly', or 'monthly'
    """
    params = {
        "function": "SUGAR",
        "time_interval": time_interval,
    }
    return make_request(params)


@mcp.tool()
def get_coffee(time_interval: Optional[str] = "monthly") -> dict:
    """Get coffee prices.
    
    Args:
        time_interval: 'daily', 'weekly', or 'monthly'
    """
    params = {
        "function": "COFFEE",
        "time_interval": time_interval,
    }
    return make_request(params)


@mcp.tool()
def get_all_commodities(time_interval: Optional[str] = "monthly") -> dict:
    """Get all commodities data.
    
    Args:
        time_interval: 'daily', 'weekly', or 'monthly'
    """
    params = {
        "function": "ALL_COMMODITIES",
        "time_interval": time_interval,
    }
    return make_request(params)


# ============================================================================
# OPTIONS ENDPOINTS
# ============================================================================

@mcp.tool()
def get_realtime_options(
    ticker: str,
    require_greeks: Optional[bool] = False,
    contract: Optional[str] = None,
    expiration: Optional[str] = None,
) -> dict:
    """Get realtime US options data.
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
        require_greeks: Include Greeks and implied volatility (default: false)
        contract: Specific contract ID (optional)
        expiration: Contract expiration date in YYYY-MM-DD format (optional)
    """
    params = {
        "function": "REALTIME_OPTIONS",
        "ticker": ticker,
        "require_greeks": str(require_greeks).lower(),
    }
    if contract:
        params["contract"] = contract
    if expiration:
        params["expiration"] = expiration
    return make_request(params)


@mcp.tool()
def get_realtime_put_call_ratio(ticker: str) -> dict:
    """Get realtime put-call ratio for options.
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
    """
    params = {
        "function": "REALTIME_PUT_CALL_RATIO",
        "ticker": ticker,
    }
    return make_request(params)


@mcp.tool()
def get_realtime_volume_open_interest_ratio(ticker: str) -> dict:
    """Get realtime volume-to-open-interest ratio for options.
    
    Args:
        ticker: Stock symbol (e.g., 'NVDA')
    """
    params = {
        "function": "REALTIME_VOLUME_OPEN_INTEREST_RATIO",
        "ticker": ticker,
    }
    return make_request(params)


@mcp.tool()
def get_historical_options(
    ticker: str,
    date: Optional[str] = None,
    contract: Optional[str] = None,
) -> dict:
    """Get historical US options data.
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
        date: Date in YYYY-MM-DD format (optional, defaults to previous trading session)
        contract: Specific contract ID (optional)
    """
    params = {
        "function": "HISTORICAL_OPTIONS",
        "ticker": ticker,
    }
    if date:
        params["date"] = date
    if contract:
        params["contract"] = contract
    return make_request(params)


# ============================================================================
# ALPHA INTELLIGENCE ENDPOINTS
# ============================================================================

@mcp.tool()
def get_news_sentiment(
    tickers: Optional[str] = None,
    topics: Optional[str] = None,
    time_from: Optional[str] = None,
    time_to: Optional[str] = None,
    sort: Optional[str] = "LATEST",
    limit: Optional[int] = 50,
) -> dict:
    """Get market news and sentiment data.
    
    Args:
        tickers: Comma-separated symbols (e.g., 'IBM', 'COIN,CRYPTO:BTC,FOREX:USD')
        topics: Comma-separated topics (e.g., 'technology', 'earnings', 'ipo')
        time_from: Start time in YYYYMMDDTHHMM format (optional)
        time_to: End time in YYYYMMDDTHHMM format (optional)
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
def get_earnings_call_transcript(ticker: str, quarter: str) -> dict:
    """Get earnings call transcript.
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
        quarter: Fiscal quarter in YYYYQM format (e.g., '2024Q1')
    """
    params = {
        "function": "EARNINGS_CALL_TRANSCRIPT",
        "ticker": ticker,
        "quarter": quarter,
    }
    return make_request(params)


@mcp.tool()
def get_top_gainers_losers() -> dict:
    """Get top 20 gainers, losers, and most active traded tickers in US market."""
    params = {
        "function": "TOP_GAINERS_LOSERS",
    }
    return make_request(params)


@mcp.tool()
def get_insider_transactions(
    ticker: str,
    from_date: Optional[str] = None,
) -> dict:
    """Get insider transactions for a company.
    
    Args:
        ticker: Stock symbol (e.g., 'IBM')
        from_date: Start date in YYYY-MM-DD format (optional)
    """
    params = {
        "function": "INSIDER_TRANSACTIONS",
        "ticker": ticker,
    }
    if from_date:
        params["from"] = from_date
    return make_request(params)


if __name__ == "__main__":
    mcp.run()
