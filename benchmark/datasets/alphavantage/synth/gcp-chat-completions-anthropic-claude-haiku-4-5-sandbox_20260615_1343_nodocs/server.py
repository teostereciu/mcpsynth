#!/usr/bin/env python3
"""
MCP Server for Alpha Vantage Financial Data API

Provides tools for accessing stock data, forex, crypto, technical indicators,
fundamental data, economic indicators, and sector performance.
"""

import os
import json
import requests
from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
server = FastMCP("alphavantage")

# Get API key from environment
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", "")
BASE_URL = "https://www.alphavantage.co/query"


def make_request(params: Dict[str, Any]) -> Dict[str, Any]:
    """Make a request to Alpha Vantage API with error handling."""
    if not API_KEY:
        return {"error": "ALPHAVANTAGE_API_KEY environment variable not set"}
    
    params["apikey"] = API_KEY
    try:
        response = requests.get(BASE_URL, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        # Check for API error messages
        if "Error Message" in data:
            return {"error": data["Error Message"]}
        if "Note" in data:
            return {"error": data["Note"]}
        if "Information" in data:
            return {"error": data["Information"]}
        
        return data
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response from API"}


# ============================================================================
# STOCK TIME SERIES ENDPOINTS
# ============================================================================

@server.tool()
def get_intraday_stock(
    symbol: str,
    interval: str = "5min",
    adjusted: bool = False,
    extended_hours: bool = False,
    output_size: str = "compact"
) -> Dict[str, Any]:
    """
    Get intraday stock price data at specified intervals.
    
    Args:
        symbol: Stock ticker symbol (e.g., "AAPL")
        interval: Time interval - 1min, 5min, 15min, 30min, 60min (default: 5min)
        adjusted: Whether to return adjusted prices (default: False)
        extended_hours: Include pre/post market data (default: False)
        output_size: "compact" (latest 100) or "full" (all available) (default: compact)
    
    Returns:
        Dict with intraday OHLCV data
    """
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "outputsize": output_size
    }
    if adjusted:
        params["adjusted"] = "true"
    if extended_hours:
        params["extended_hours"] = "true"
    
    return make_request(params)


@server.tool()
def get_daily_stock(
    symbol: str,
    adjusted: bool = False,
    output_size: str = "compact"
) -> Dict[str, Any]:
    """
    Get daily stock price data.
    
    Args:
        symbol: Stock ticker symbol (e.g., "AAPL")
        adjusted: Whether to return adjusted prices (default: False)
        output_size: "compact" (latest 100) or "full" (all available) (default: compact)
    
    Returns:
        Dict with daily OHLCV data
    """
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": output_size
    }
    if adjusted:
        params["adjusted"] = "true"
    
    return make_request(params)


@server.tool()
def get_weekly_stock(
    symbol: str,
    output_size: str = "compact"
) -> Dict[str, Any]:
    """
    Get weekly stock price data.
    
    Args:
        symbol: Stock ticker symbol (e.g., "AAPL")
        output_size: "compact" (latest 100) or "full" (all available) (default: compact)
    
    Returns:
        Dict with weekly OHLCV data
    """
    params = {
        "function": "TIME_SERIES_WEEKLY",
        "symbol": symbol,
        "outputsize": output_size
    }
    return make_request(params)


@server.tool()
def get_monthly_stock(
    symbol: str,
    output_size: str = "compact"
) -> Dict[str, Any]:
    """
    Get monthly stock price data.
    
    Args:
        symbol: Stock ticker symbol (e.g., "AAPL")
        output_size: "compact" (latest 100) or "full" (all available) (default: compact)
    
    Returns:
        Dict with monthly OHLCV data
    """
    params = {
        "function": "TIME_SERIES_MONTHLY",
        "symbol": symbol,
        "outputsize": output_size
    }
    return make_request(params)


# ============================================================================
# QUOTE ENDPOINT
# ============================================================================

@server.tool()
def get_quote(symbol: str) -> Dict[str, Any]:
    """
    Get the latest price and volume for a stock symbol.
    
    Args:
        symbol: Stock ticker symbol (e.g., "AAPL")
    
    Returns:
        Dict with latest quote data including price, volume, and timestamp
    """
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol
    }
    return make_request(params)


# ============================================================================
# SYMBOL SEARCH
# ============================================================================

@server.tool()
def search_symbol(keywords: str) -> Dict[str, Any]:
    """
    Search for stock symbols by company name or keywords.
    
    Args:
        keywords: Company name or keywords to search for
    
    Returns:
        Dict with matching symbols and company information
    """
    params = {
        "function": "SYMBOL_SEARCH",
        "keywords": keywords
    }
    return make_request(params)


# ============================================================================
# FOREX (FX) ENDPOINTS
# ============================================================================

@server.tool()
def get_fx_intraday(
    from_symbol: str,
    to_symbol: str,
    interval: str = "5min",
    output_size: str = "compact"
) -> Dict[str, Any]:
    """
    Get intraday forex exchange rate data.
    
    Args:
        from_symbol: Currency code (e.g., "EUR")
        to_symbol: Currency code (e.g., "USD")
        interval: Time interval - 1min, 5min, 15min, 30min, 60min (default: 5min)
        output_size: "compact" (latest 100) or "full" (all available) (default: compact)
    
    Returns:
        Dict with intraday FX data
    """
    params = {
        "function": "FX_INTRADAY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "interval": interval,
        "outputsize": output_size
    }
    return make_request(params)


@server.tool()
def get_fx_daily(
    from_symbol: str,
    to_symbol: str,
    output_size: str = "compact"
) -> Dict[str, Any]:
    """
    Get daily forex exchange rate data.
    
    Args:
        from_symbol: Currency code (e.g., "EUR")
        to_symbol: Currency code (e.g., "USD")
        output_size: "compact" (latest 100) or "full" (all available) (default: compact)
    
    Returns:
        Dict with daily FX data
    """
    params = {
        "function": "FX_DAILY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "outputsize": output_size
    }
    return make_request(params)


@server.tool()
def get_fx_weekly(
    from_symbol: str,
    to_symbol: str,
    output_size: str = "compact"
) -> Dict[str, Any]:
    """
    Get weekly forex exchange rate data.
    
    Args:
        from_symbol: Currency code (e.g., "EUR")
        to_symbol: Currency code (e.g., "USD")
        output_size: "compact" (latest 100) or "full" (all available) (default: compact)
    
    Returns:
        Dict with weekly FX data
    """
    params = {
        "function": "FX_WEEKLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "outputsize": output_size
    }
    return make_request(params)


@server.tool()
def get_fx_monthly(
    from_symbol: str,
    to_symbol: str,
    output_size: str = "compact"
) -> Dict[str, Any]:
    """
    Get monthly forex exchange rate data.
    
    Args:
        from_symbol: Currency code (e.g., "EUR")
        to_symbol: Currency code (e.g., "USD")
        output_size: "compact" (latest 100) or "full" (all available) (default: compact)
    
    Returns:
        Dict with monthly FX data
    """
    params = {
        "function": "FX_MONTHLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "outputsize": output_size
    }
    return make_request(params)


@server.tool()
def get_currency_exchange_rate(
    from_currency: str,
    to_currency: str
) -> Dict[str, Any]:
    """
    Get the latest exchange rate between two currencies.
    
    Args:
        from_currency: Currency code (e.g., "EUR")
        to_currency: Currency code (e.g., "USD")
    
    Returns:
        Dict with exchange rate and metadata
    """
    params = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": from_currency,
        "to_currency": to_currency
    }
    return make_request(params)


# ============================================================================
# CRYPTOCURRENCY ENDPOINTS
# ============================================================================

@server.tool()
def get_crypto_intraday(
    symbol: str,
    market: str = "USD",
    interval: str = "5min",
    output_size: str = "compact"
) -> Dict[str, Any]:
    """
    Get intraday cryptocurrency price data.
    
    Args:
        symbol: Cryptocurrency code (e.g., "BTC", "ETH")
        market: Market currency (e.g., "USD", "EUR") (default: USD)
        interval: Time interval - 1min, 5min, 15min, 30min, 60min (default: 5min)
        output_size: "compact" (latest 100) or "full" (all available) (default: compact)
    
    Returns:
        Dict with intraday crypto data
    """
    params = {
        "function": "CRYPTO_INTRADAY",
        "symbol": symbol,
        "market": market,
        "interval": interval,
        "outputsize": output_size
    }
    return make_request(params)


@server.tool()
def get_crypto_daily(
    symbol: str,
    market: str = "USD",
    output_size: str = "compact"
) -> Dict[str, Any]:
    """
    Get daily cryptocurrency price data.
    
    Args:
        symbol: Cryptocurrency code (e.g., "BTC", "ETH")
        market: Market currency (e.g., "USD", "EUR") (default: USD)
        output_size: "compact" (latest 100) or "full" (all available) (default: compact)
    
    Returns:
        Dict with daily crypto data
    """
    params = {
        "function": "CRYPTO_DAILY",
        "symbol": symbol,
        "market": market,
        "outputsize": output_size
    }
    return make_request(params)


@server.tool()
def get_crypto_weekly(
    symbol: str,
    market: str = "USD",
    output_size: str = "compact"
) -> Dict[str, Any]:
    """
    Get weekly cryptocurrency price data.
    
    Args:
        symbol: Cryptocurrency code (e.g., "BTC", "ETH")
        market: Market currency (e.g., "USD", "EUR") (default: USD)
        output_size: "compact" (latest 100) or "full" (all available) (default: compact)
    
    Returns:
        Dict with weekly crypto data
    """
    params = {
        "function": "CRYPTO_WEEKLY",
        "symbol": symbol,
        "market": market,
        "outputsize": output_size
    }
    return make_request(params)


@server.tool()
def get_crypto_monthly(
    symbol: str,
    market: str = "USD",
    output_size: str = "compact"
) -> Dict[str, Any]:
    """
    Get monthly cryptocurrency price data.
    
    Args:
        symbol: Cryptocurrency code (e.g., "BTC", "ETH")
        market: Market currency (e.g., "USD", "EUR") (default: USD)
        output_size: "compact" (latest 100) or "full" (all available) (default: compact)
    
    Returns:
        Dict with monthly crypto data
    """
    params = {
        "function": "CRYPTO_MONTHLY",
        "symbol": symbol,
        "market": market,
        "outputsize": output_size
    }
    return make_request(params)


@server.tool()
def get_crypto_rating(symbol: str) -> Dict[str, Any]:
    """
    Get cryptocurrency rating and technical analysis.
    
    Args:
        symbol: Cryptocurrency code (e.g., "BTC", "ETH")
    
    Returns:
        Dict with crypto rating data
    """
    params = {
        "function": "CRYPTO_RATING",
        "symbol": symbol
    }
    return make_request(params)


# ============================================================================
# TECHNICAL INDICATORS
# ============================================================================

@server.tool()
def get_sma(
    symbol: str,
    interval: str = "daily",
    time_period: int = 20,
    series_type: str = "close"
) -> Dict[str, Any]:
    """
    Get Simple Moving Average (SMA) technical indicator.
    
    Args:
        symbol: Stock or crypto symbol
        interval: Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)
        time_period: Number of periods for the moving average (default: 20)
        series_type: Price type - close, open, high, low (default: close)
    
    Returns:
        Dict with SMA values
    """
    params = {
        "function": "SMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type
    }
    return make_request(params)


@server.tool()
def get_ema(
    symbol: str,
    interval: str = "daily",
    time_period: int = 20,
    series_type: str = "close"
) -> Dict[str, Any]:
    """
    Get Exponential Moving Average (EMA) technical indicator.
    
    Args:
        symbol: Stock or crypto symbol
        interval: Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)
        time_period: Number of periods for the moving average (default: 20)
        series_type: Price type - close, open, high, low (default: close)
    
    Returns:
        Dict with EMA values
    """
    params = {
        "function": "EMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type
    }
    return make_request(params)


@server.tool()
def get_rsi(
    symbol: str,
    interval: str = "daily",
    time_period: int = 14,
    series_type: str = "close"
) -> Dict[str, Any]:
    """
    Get Relative Strength Index (RSI) technical indicator.
    
    Args:
        symbol: Stock or crypto symbol
        interval: Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)
        time_period: Number of periods for RSI (default: 14)
        series_type: Price type - close, open, high, low (default: close)
    
    Returns:
        Dict with RSI values
    """
    params = {
        "function": "RSI",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type
    }
    return make_request(params)


@server.tool()
def get_macd(
    symbol: str,
    interval: str = "daily",
    series_type: str = "close",
    fastperiod: int = 12,
    slowperiod: int = 26,
    signalperiod: int = 9
) -> Dict[str, Any]:
    """
    Get MACD (Moving Average Convergence Divergence) technical indicator.
    
    Args:
        symbol: Stock or crypto symbol
        interval: Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)
        series_type: Price type - close, open, high, low (default: close)
        fastperiod: Fast EMA period (default: 12)
        slowperiod: Slow EMA period (default: 26)
        signalperiod: Signal line period (default: 9)
    
    Returns:
        Dict with MACD values
    """
    params = {
        "function": "MACD",
        "symbol": symbol,
        "interval": interval,
        "series_type": series_type,
        "fastperiod": fastperiod,
        "slowperiod": slowperiod,
        "signalperiod": signalperiod
    }
    return make_request(params)


@server.tool()
def get_bbands(
    symbol: str,
    interval: str = "daily",
    time_period: int = 20,
    series_type: str = "close",
    nbdevup: float = 2.0,
    nbdevdn: float = 2.0
) -> Dict[str, Any]:
    """
    Get Bollinger Bands technical indicator.
    
    Args:
        symbol: Stock or crypto symbol
        interval: Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)
        time_period: Number of periods (default: 20)
        series_type: Price type - close, open, high, low (default: close)
        nbdevup: Standard deviations for upper band (default: 2.0)
        nbdevdn: Standard deviations for lower band (default: 2.0)
    
    Returns:
        Dict with Bollinger Bands values
    """
    params = {
        "function": "BBANDS",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
        "nbdevup": nbdevup,
        "nbdevdn": nbdevdn
    }
    return make_request(params)


@server.tool()
def get_stoch(
    symbol: str,
    interval: str = "daily",
    fastkperiod: int = 5,
    slowkperiod: int = 3,
    slowdperiod: int = 3,
    slowkmatype: int = 0,
    slowdmatype: int = 0
) -> Dict[str, Any]:
    """
    Get Stochastic Oscillator technical indicator.
    
    Args:
        symbol: Stock or crypto symbol
        interval: Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)
        fastkperiod: Fast K period (default: 5)
        slowkperiod: Slow K period (default: 3)
        slowdperiod: Slow D period (default: 3)
        slowkmatype: Slow K MA type (default: 0)
        slowdmatype: Slow D MA type (default: 0)
    
    Returns:
        Dict with Stochastic Oscillator values
    """
    params = {
        "function": "STOCH",
        "symbol": symbol,
        "interval": interval,
        "fastkperiod": fastkperiod,
        "slowkperiod": slowkperiod,
        "slowdperiod": slowdperiod,
        "slowkmatype": slowkmatype,
        "slowdmatype": slowdmatype
    }
    return make_request(params)


@server.tool()
def get_adx(
    symbol: str,
    interval: str = "daily",
    time_period: int = 14
) -> Dict[str, Any]:
    """
    Get Average Directional Index (ADX) technical indicator.
    
    Args:
        symbol: Stock or crypto symbol
        interval: Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)
        time_period: Number of periods (default: 14)
    
    Returns:
        Dict with ADX values
    """
    params = {
        "function": "ADX",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period
    }
    return make_request(params)


@server.tool()
def get_atr(
    symbol: str,
    interval: str = "daily",
    time_period: int = 14
) -> Dict[str, Any]:
    """
    Get Average True Range (ATR) technical indicator.
    
    Args:
        symbol: Stock or crypto symbol
        interval: Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)
        time_period: Number of periods (default: 14)
    
    Returns:
        Dict with ATR values
    """
    params = {
        "function": "ATR",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period
    }
    return make_request(params)


# ============================================================================
# FUNDAMENTAL DATA
# ============================================================================

@server.tool()
def get_company_overview(symbol: str) -> Dict[str, Any]:
    """
    Get company overview and fundamental information.
    
    Args:
        symbol: Stock ticker symbol (e.g., "AAPL")
    
    Returns:
        Dict with company information including sector, industry, market cap, etc.
    """
    params = {
        "function": "OVERVIEW",
        "symbol": symbol
    }
    return make_request(params)


@server.tool()
def get_income_statement(symbol: str) -> Dict[str, Any]:
    """
    Get company income statement data.
    
    Args:
        symbol: Stock ticker symbol (e.g., "AAPL")
    
    Returns:
        Dict with income statement data
    """
    params = {
        "function": "INCOME_STATEMENT",
        "symbol": symbol
    }
    return make_request(params)


@server.tool()
def get_balance_sheet(symbol: str) -> Dict[str, Any]:
    """
    Get company balance sheet data.
    
    Args:
        symbol: Stock ticker symbol (e.g., "AAPL")
    
    Returns:
        Dict with balance sheet data
    """
    params = {
        "function": "BALANCE_SHEET",
        "symbol": symbol
    }
    return make_request(params)


@server.tool()
def get_cash_flow(symbol: str) -> Dict[str, Any]:
    """
    Get company cash flow statement data.
    
    Args:
        symbol: Stock ticker symbol (e.g., "AAPL")
    
    Returns:
        Dict with cash flow statement data
    """
    params = {
        "function": "CASH_FLOW",
        "symbol": symbol
    }
    return make_request(params)


@server.tool()
def get_earnings(symbol: str) -> Dict[str, Any]:
    """
    Get company earnings data.
    
    Args:
        symbol: Stock ticker symbol (e.g., "AAPL")
    
    Returns:
        Dict with earnings data including quarterly and annual reports
    """
    params = {
        "function": "EARNINGS",
        "symbol": symbol
    }
    return make_request(params)


# ============================================================================
# ECONOMIC INDICATORS
# ============================================================================

@server.tool()
def get_cpi(
    interval: str = "monthly",
    datatype: str = "float"
) -> Dict[str, Any]:
    """
    Get Consumer Price Index (CPI) economic indicator.
    
    Args:
        interval: "monthly" or "semiannual" (default: monthly)
        datatype: "float" or "integer" (default: float)
    
    Returns:
        Dict with CPI data
    """
    params = {
        "function": "CPI",
        "interval": interval,
        "datatype": datatype
    }
    return make_request(params)


@server.tool()
def get_inflation(datatype: str = "float") -> Dict[str, Any]:
    """
    Get inflation rate data.
    
    Args:
        datatype: "float" or "integer" (default: float)
    
    Returns:
        Dict with inflation data
    """
    params = {
        "function": "INFLATION",
        "datatype": datatype
    }
    return make_request(params)


@server.tool()
def get_inflation_expectation(datatype: str = "float") -> Dict[str, Any]:
    """
    Get inflation expectation data.
    
    Args:
        datatype: "float" or "integer" (default: float)
    
    Returns:
        Dict with inflation expectation data
    """
    params = {
        "function": "INFLATION_EXPECTATION",
        "datatype": datatype
    }
    return make_request(params)


@server.tool()
def get_consumer_sentiment(datatype: str = "float") -> Dict[str, Any]:
    """
    Get consumer sentiment index data.
    
    Args:
        datatype: "float" or "integer" (default: float)
    
    Returns:
        Dict with consumer sentiment data
    """
    params = {
        "function": "CONSUMER_SENTIMENT",
        "datatype": datatype
    }
    return make_request(params)


@server.tool()
def get_retail_sales(datatype: str = "float") -> Dict[str, Any]:
    """
    Get retail sales data.
    
    Args:
        datatype: "float" or "integer" (default: float)
    
    Returns:
        Dict with retail sales data
    """
    params = {
        "function": "RETAIL_SALES",
        "datatype": datatype
    }
    return make_request(params)


@server.tool()
def get_durables(datatype: str = "float") -> Dict[str, Any]:
    """
    Get durable goods orders data.
    
    Args:
        datatype: "float" or "integer" (default: float)
    
    Returns:
        Dict with durable goods data
    """
    params = {
        "function": "DURABLES",
        "datatype": datatype
    }
    return make_request(params)


@server.tool()
def get_unemployment(datatype: str = "float") -> Dict[str, Any]:
    """
    Get unemployment rate data.
    
    Args:
        datatype: "float" or "integer" (default: float)
    
    Returns:
        Dict with unemployment data
    """
    params = {
        "function": "UNEMPLOYMENT",
        "datatype": datatype
    }
    return make_request(params)


@server.tool()
def get_nonfarm_payroll(datatype: str = "float") -> Dict[str, Any]:
    """
    Get nonfarm payroll data.
    
    Args:
        datatype: "float" or "integer" (default: float)
    
    Returns:
        Dict with nonfarm payroll data
    """
    params = {
        "function": "NONFARM_PAYROLL",
        "datatype": datatype
    }
    return make_request(params)


@server.tool()
def get_treasury_yield(
    interval: str = "monthly",
    maturity: str = "10year",
    datatype: str = "float"
) -> Dict[str, Any]:
    """
    Get US Treasury yield data.
    
    Args:
        interval: "monthly" or "daily" (default: monthly)
        maturity: "3month", "2year", "5year", "7year", "10year", "30year" (default: 10year)
        datatype: "float" or "integer" (default: float)
    
    Returns:
        Dict with treasury yield data
    """
    params = {
        "function": "TREASURY_YIELD",
        "interval": interval,
        "maturity": maturity,
        "datatype": datatype
    }
    return make_request(params)


@server.tool()
def get_federal_funds_rate(
    interval: str = "monthly",
    datatype: str = "float"
) -> Dict[str, Any]:
    """
    Get Federal Funds Rate data.
    
    Args:
        interval: "monthly" or "daily" (default: monthly)
        datatype: "float" or "integer" (default: float)
    
    Returns:
        Dict with federal funds rate data
    """
    params = {
        "function": "FEDERAL_FUNDS_RATE",
        "interval": interval,
        "datatype": datatype
    }
    return make_request(params)


@server.tool()
def get_real_gdp(datatype: str = "float") -> Dict[str, Any]:
    """
    Get real GDP data.
    
    Args:
        datatype: "float" or "integer" (default: float)
    
    Returns:
        Dict with real GDP data
    """
    params = {
        "function": "REAL_GDP",
        "datatype": datatype
    }
    return make_request(params)


@server.tool()
def get_real_gdp_per_capita(datatype: str = "float") -> Dict[str, Any]:
    """
    Get real GDP per capita data.
    
    Args:
        datatype: "float" or "integer" (default: float)
    
    Returns:
        Dict with real GDP per capita data
    """
    params = {
        "function": "REAL_GDP_PER_CAPITA",
        "datatype": datatype
    }
    return make_request(params)


# ============================================================================
# SECTOR PERFORMANCE
# ============================================================================

@server.tool()
def get_sector_performance() -> Dict[str, Any]:
    """
    Get real-time sector performance across S&P 500.
    
    Returns:
        Dict with sector performance data including percentage changes
    """
    params = {
        "function": "SECTOR"
    }
    return make_request(params)


if __name__ == "__main__":
    server.run()
