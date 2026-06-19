#!/usr/bin/env python3
"""
Alpha Vantage MCP Server

An MCP server providing comprehensive access to Alpha Vantage financial data API.
"""

import os
import requests
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP

# Create MCP server instance
mcp = FastMCP("alphavantage")

# Base URL for Alpha Vantage API
BASE_URL = "https://www.alphavantage.co/query"


def make_api_request(function: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """Make a request to the Alpha Vantage API and return the response."""
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
    if not api_key:
        return {"error": "ALPHAVANTAGE_API_KEY environment variable not set"}
    
    # Build request parameters
    request_params = {
        "function": function,
        "apikey": api_key,
    }
    request_params.update(params)
    
    try:
        response = requests.get(BASE_URL, params=request_params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}
    except ValueError as e:
        return {"error": f"Failed to parse JSON response: {str(e)}"}


# =============================================================================
# STOCK TIME SERIES
# =============================================================================

@mcp.tool()
def get_intraday_stock_data(
    ticker: str,
    time_interval: str = "5min",
    adjusted: bool = True,
    extended_hours: bool = True,
    month: Optional[str] = None,
    output_size: str = "compact",
    format: str = "json",
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get intraday time series data for a stock.
    
    Returns current and 20+ years of historical intraday OHLCV time series of the equity specified,
    covering pre-market and post-market hours where applicable.
    
    Args:
        ticker: The name of the equity (e.g., "IBM")
        time_interval: Time interval between data points ("1min", "5min", "15min", "30min", "60min")
        adjusted: If True, return split/dividend-adjusted data
        extended_hours: If True, include extended trading hours
        month: Specific month in YYYY-MM format to query
        output_size: "compact" for latest 100 points, "full" for 30 days or full month data
        format: Output format ("json" or "csv")
        entitlement: Data freshness ("realtime", "delayed", or None for historical)
    
    Returns:
        Time series data with timestamp, OHLCV values
    """
    params = {
        "ticker": ticker,
        "time_interval": time_interval,
        "adjusted": str(adjusted).lower(),
        "extended_hours": str(extended_hours).lower(),
        "output_size": output_size,
        "format": format,
    }
    
    if month:
        params["month"] = month
    if entitlement:
        params["entitlement"] = entitlement
    
    return make_api_request("TIME_SERIES_INTRADAY", params)


@mcp.tool()
def get_daily_stock_data(
    ticker: str,
    output_size: str = "compact",
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get daily time series data for a stock.
    
    Returns raw (as-traded) daily time series with date, open, high, low, close, volume.
    
    Args:
        ticker: The name of the equity (e.g., "IBM")
        output_size: "compact" for latest 100 points, "full" for 20+ years of data
        format: Output format ("json" or "csv")
    
    Returns:
        Daily time series data
    """
    params = {
        "ticker": ticker,
        "output_size": output_size,
        "format": format,
    }
    
    return make_api_request("TIME_SERIES_DAILY", params)


@mcp.tool()
def get_daily_adjusted_stock_data(
    ticker: str,
    output_size: str = "compact",
    format: str = "json",
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get daily adjusted time series data for a stock.
    
    Returns daily OHLCV values with adjusted close values and historical split/dividend events.
    
    Args:
        ticker: The name of the equity (e.g., "IBM")
        output_size: "compact" for latest 100 points, "full" for 20+ years of data
        format: Output format ("json" or "csv")
        entitlement: Data freshness ("realtime", "delayed", or None for historical)
    
    Returns:
        Daily adjusted time series data
    """
    params = {
        "ticker": ticker,
        "output_size": output_size,
        "format": format,
    }
    
    if entitlement:
        params["entitlement"] = entitlement
    
    return make_api_request("TIME_SERIES_DAILY_ADJUSTED", params)


@mcp.tool()
def get_weekly_stock_data(
    ticker: str,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get weekly time series data for a stock.
    
    Returns weekly time series with date, open, high, low, close, volume.
    
    Args:
        ticker: The name of the equity (e.g., "IBM")
        format: Output format ("json" or "csv")
    
    Returns:
        Weekly time series data
    """
    params = {
        "ticker": ticker,
        "format": format,
    }
    
    return make_api_request("TIME_SERIES_WEEKLY", params)


@mcp.tool()
def get_weekly_adjusted_stock_data(
    ticker: str,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get weekly adjusted time series data for a stock.
    
    Returns weekly OHLCV values with adjusted close values and historical split/dividend events.
    
    Args:
        ticker: The name of the equity (e.g., "IBM")
        format: Output format ("json" or "csv")
    
    Returns:
        Weekly adjusted time series data
    """
    params = {
        "ticker": ticker,
        "format": format,
    }
    
    return make_api_request("TIME_SERIES_WEEKLY_ADJUSTED", params)


@mcp.tool()
def get_monthly_stock_data(
    ticker: str,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get monthly time series data for a stock.
    
    Returns monthly time series with date, open, high, low, close, volume.
    
    Args:
        ticker: The name of the equity (e.g., "IBM")
        format: Output format ("json" or "csv")
    
    Returns:
        Monthly time series data
    """
    params = {
        "ticker": ticker,
        "format": format,
    }
    
    return make_api_request("TIME_SERIES_MONTHLY", params)


@mcp.tool()
def get_monthly_adjusted_stock_data(
    ticker: str,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get monthly adjusted time series data for a stock.
    
    Returns monthly OHLCV values with adjusted close values and historical split/dividend events.
    
    Args:
        ticker: The name of the equity (e.g., "IBM")
        format: Output format ("json" or "csv")
    
    Returns:
        Monthly adjusted time series data
    """
    params = {
        "ticker": ticker,
        "format": format,
    }
    
    return make_api_request("TIME_SERIES_MONTHLY_ADJUSTED", params)


@mcp.tool()
def get_stock_quote(ticker: str, format: str = "json") -> Dict[str, Any]:
    """
    Get the latest quote (price and volume) for a stock.
    
    Args:
        ticker: The name of the equity (e.g., "IBM")
        format: Output format ("json" or "csv")
    
    Returns:
        Latest quote data with price, volume, and other metrics
    """
    params = {
        "ticker": ticker,
        "format": format,
    }
    
    return make_api_request("GLOBAL_QUOTE", params)


# =============================================================================
# SEARCH
# =============================================================================

@mcp.tool()
def search_symbols(
    keywords: str,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Search for stock symbols/tickers.
    
    Returns matching symbols with full description, type, and market information.
    
    Args:
        keywords: Search keywords (company name, ticker symbol, etc.)
        format: Output format ("json" or "csv")
    
    Returns:
        List of matching symbols with metadata
    """
    params = {
        "keywords": keywords,
        "format": format,
    }
    
    return make_api_request("SYMBOL_SEARCH", params)


# =============================================================================
# FOREX (FX)
# =============================================================================

@mcp.tool()
def get_forex_exchange_rate(
    from_currency: str,
    to_currency: str,
) -> Dict[str, Any]:
    """
    Get the current exchange rate between two currencies.
    
    Args:
        from_currency: Source currency (e.g., "USD", "EUR", "BTC")
        to_currency: Target currency (e.g., "USD", "EUR", "JPY")
    
    Returns:
        Current exchange rate data
    """
    params = {
        "from_currency": from_currency,
        "to_currency": to_currency,
    }
    
    return make_api_request("CURRENCY_EXCHANGE_RATE", params)


@mcp.tool()
def get_forex_intraday(
    from_symbol: str,
    to_symbol: str,
    time_interval: str = "5min",
    output_size: str = "compact",
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get intraday FX time series data.
    
    Args:
        from_symbol: Source currency (e.g., "EUR")
        to_symbol: Target currency (e.g., "USD")
        time_interval: Time interval ("1min", "5min", "15min", "30min", "60min")
        output_size: "compact" for latest 100 points, "full" for full time series
        format: Output format ("json" or "csv")
    
    Returns:
        Intraday FX time series data
    """
    params = {
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "time_interval": time_interval,
        "output_size": output_size,
        "format": format,
    }
    
    return make_api_request("FX_INTRADAY", params)


@mcp.tool()
def get_forex_daily(
    from_symbol: str,
    to_symbol: str,
    output_size: str = "compact",
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get daily FX time series data.
    
    Args:
        from_symbol: Source currency (e.g., "EUR")
        to_symbol: Target currency (e.g., "USD")
        output_size: "compact" for latest 100 points, "full" for full time series
        format: Output format ("json" or "csv")
    
    Returns:
        Daily FX time series data
    """
    params = {
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "output_size": output_size,
        "format": format,
    }
    
    return make_api_request("FX_DAILY", params)


@mcp.tool()
def get_forex_weekly(
    from_symbol: str,
    to_symbol: str,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get weekly FX time series data.
    
    Args:
        from_symbol: Source currency (e.g., "EUR")
        to_symbol: Target currency (e.g., "USD")
        format: Output format ("json" or "csv")
    
    Returns:
        Weekly FX time series data
    """
    params = {
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "format": format,
    }
    
    return make_api_request("FX_WEEKLY", params)


@mcp.tool()
def get_forex_monthly(
    from_symbol: str,
    to_symbol: str,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get monthly FX time series data.
    
    Args:
        from_symbol: Source currency (e.g., "EUR")
        to_symbol: Target currency (e.g., "USD")
        format: Output format ("json" or "csv")
    
    Returns:
        Monthly FX time series data
    """
    params = {
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "format": format,
    }
    
    return make_api_request("FX_MONTHLY", params)


# =============================================================================
# CRYPTO/CURRENCY
# =============================================================================

@mcp.tool()
def get_crypto_exchange_rate(
    from_currency: str,
    to_currency: str,
) -> Dict[str, Any]:
    """
    Get the current exchange rate between two currencies (crypto or fiat).
    
    Args:
        from_currency: Source currency (e.g., "BTC", "ETH", "USD")
        to_currency: Target currency (e.g., "BTC", "EUR", "JPY")
    
    Returns:
        Current exchange rate data
    """
    params = {
        "from_currency": from_currency,
        "to_currency": to_currency,
    }
    
    return make_api_request("CURRENCY_EXCHANGE_RATE", params)


@mcp.tool()
def get_crypto_intraday(
    ticker: str,
    market: str = "USD",
    time_interval: str = "5min",
    output_size: str = "compact",
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get intraday cryptocurrency time series data.
    
    Args:
        ticker: Cryptocurrency (e.g., "ETH", "BTC")
        market: Exchange market (e.g., "USD", "EUR")
        time_interval: Time interval ("1min", "5min", "15min", "30min", "60min")
        output_size: "compact" for latest 100 points, "full" for full time series
        format: Output format ("json" or "csv")
    
    Returns:
        Intraday crypto time series data
    """
    params = {
        "ticker": ticker,
        "market": market,
        "time_interval": time_interval,
        "output_size": output_size,
        "format": format,
    }
    
    return make_api_request("CRYPTO_INTRADAY", params)


@mcp.tool()
def get_crypto_daily(
    ticker: str,
    market: str = "USD",
) -> Dict[str, Any]:
    """
    Get daily cryptocurrency time series data.
    
    Args:
        ticker: Cryptocurrency (e.g., "BTC", "ETH")
        market: Exchange market (e.g., "USD", "EUR")
    
    Returns:
        Daily crypto time series data
    """
    params = {
        "ticker": ticker,
        "market": market,
    }
    
    return make_api_request("DIGITAL_CURRENCY_DAILY", params)


@mcp.tool()
def get_crypto_weekly(
    ticker: str,
    market: str = "USD",
) -> Dict[str, Any]:
    """
    Get weekly cryptocurrency time series data.
    
    Args:
        ticker: Cryptocurrency (e.g., "BTC", "ETH")
        market: Exchange market (e.g., "USD", "EUR")
    
    Returns:
        Weekly crypto time series data
    """
    params = {
        "ticker": ticker,
        "market": market,
    }
    
    return make_api_request("DIGITAL_CURRENCY_WEEKLY", params)


@mcp.tool()
def get_crypto_monthly(
    ticker: str,
    market: str = "USD",
) -> Dict[str, Any]:
    """
    Get monthly cryptocurrency time series data.
    
    Args:
        ticker: Cryptocurrency (e.g., "BTC", "ETH")
        market: Exchange market (e.g., "USD", "EUR")
    
    Returns:
        Monthly crypto time series data
    """
    params = {
        "ticker": ticker,
        "market": market,
    }
    
    return make_api_request("DIGITAL_CURRENCY_MONTHLY", params)


# =============================================================================
# TECHNICAL INDICATORS
# =============================================================================

def _build_technical_indicator_request(
    function: str,
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
    entitlement: Optional[str] = None,
    format: str = "json",
) -> Dict[str, Any]:
    """Helper to build technical indicator requests."""
    params = {
        "ticker": ticker,
        "time_interval": time_interval,
        "time_period": str(time_period),
        "price_type": price_type,
        "format": format,
    }
    
    if month:
        params["month"] = month
    if entitlement:
        params["entitlement"] = entitlement
    
    return make_api_request(function, params)


@mcp.tool()
def get_sma(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
    entitlement: Optional[str] = None,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get Simple Moving Average (SMA) technical indicator.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
        time_interval: Time interval ("1min", "5min", "15min", "30min", "60min", "daily", "weekly", "monthly")
        time_period: Number of data points (e.g., 60, 200)
        price_type: Price type ("close", "open", "high", "low")
        month: Specific month in YYYY-MM format
        entitlement: Data freshness ("realtime", "delayed", or None)
        format: Output format ("json" or "csv")
    
    Returns:
        SMA time series data
    """
    return _build_technical_indicator_request(
        "SMA", ticker, time_interval, time_period, price_type,
        month, entitlement, format
    )


@mcp.tool()
def get_ema(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
    entitlement: Optional[str] = None,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get Exponential Moving Average (EMA) technical indicator.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
        time_interval: Time interval ("1min", "5min", "15min", "30min", "60min", "daily", "weekly", "monthly")
        time_period: Number of data points (e.g., 60, 200)
        price_type: Price type ("close", "open", "high", "low")
        month: Specific month in YYYY-MM format
        entitlement: Data freshness ("realtime", "delayed", or None)
        format: Output format ("json" or "csv")
    
    Returns:
        EMA time series data
    """
    return _build_technical_indicator_request(
        "EMA", ticker, time_interval, time_period, price_type,
        month, entitlement, format
    )


@mcp.tool()
def get_wma(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
    entitlement: Optional[str] = None,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get Weighted Moving Average (WMA) technical indicator.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
        time_interval: Time interval ("1min", "5min", "15min", "30min", "60min", "daily", "weekly", "monthly")
        time_period: Number of data points (e.g., 60, 200)
        price_type: Price type ("close", "open", "high", "low")
        month: Specific month in YYYY-MM format
        entitlement: Data freshness ("realtime", "delayed", or None)
        format: Output format ("json" or "csv")
    
    Returns:
        WMA time series data
    """
    return _build_technical_indicator_request(
        "WMA", ticker, time_interval, time_period, price_type,
        month, entitlement, format
    )


@mcp.tool()
def get_dema(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
    entitlement: Optional[str] = None,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get Double Exponential Moving Average (DEMA) technical indicator.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
        time_interval: Time interval ("1min", "5min", "15min", "30min", "60min", "daily", "weekly", "monthly")
        time_period: Number of data points (e.g., 60, 200)
        price_type: Price type ("close", "open", "high", "low")
        month: Specific month in YYYY-MM format
        entitlement: Data freshness ("realtime", "delayed", or None)
        format: Output format ("json" or "csv")
    
    Returns:
        DEMA time series data
    """
    return _build_technical_indicator_request(
        "DEMA", ticker, time_interval, time_period, price_type,
        month, entitlement, format
    )


@mcp.tool()
def get_tema(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
    entitlement: Optional[str] = None,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get Triple Exponential Moving Average (TEMA) technical indicator.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
        time_interval: Time interval ("1min", "5min", "15min", "30min", "60min", "daily", "weekly", "monthly")
        time_period: Number of data points (e.g., 60, 200)
        price_type: Price type ("close", "open", "high", "low")
        month: Specific month in YYYY-MM format
        entitlement: Data freshness ("realtime", "delayed", or None)
        format: Output format ("json" or "csv")
    
    Returns:
        TEMA time series data
    """
    return _build_technical_indicator_request(
        "TEMA", ticker, time_interval, time_period, price_type,
        month, entitlement, format
    )


@mcp.tool()
def get_trima(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
    entitlement: Optional[str] = None,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get Triangular Moving Average (TRIMA) technical indicator.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
        time_interval: Time interval ("1min", "5min", "15min", "30min", "60min", "daily", "weekly", "monthly")
        time_period: Number of data points (e.g., 60, 200)
        price_type: Price type ("close", "open", "high", "low")
        month: Specific month in YYYY-MM format
        entitlement: Data freshness ("realtime", "delayed", or None)
        format: Output format ("json" or "csv")
    
    Returns:
        TRIMA time series data
    """
    return _build_technical_indicator_request(
        "TRIMA", ticker, time_interval, time_period, price_type,
        month, entitlement, format
    )


@mcp.tool()
def get_kama(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
    entitlement: Optional[str] = None,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get Kaufman Adaptive Moving Average (KAMA) technical indicator.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
        time_interval: Time interval ("1min", "5min", "15min", "30min", "60min", "daily", "weekly", "monthly")
        time_period: Number of data points (e.g., 60, 200)
        price_type: Price type ("close", "open", "high", "low")
        month: Specific month in YYYY-MM format
        entitlement: Data freshness ("realtime", "delayed", or None)
        format: Output format ("json" or "csv")
    
    Returns:
        KAMA time series data
    """
    return _build_technical_indicator_request(
        "KAMA", ticker, time_interval, time_period, price_type,
        month, entitlement, format
    )


@mcp.tool()
def get_mama(
    ticker: str,
    time_interval: str,
    price_type: str,
    month: Optional[str] = None,
    entitlement: Optional[str] = None,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get MESA Adaptive Moving Average (MAMA) technical indicator.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
        time_interval: Time interval ("1min", "5min", "15min", "30min", "60min", "daily", "weekly", "monthly")
        price_type: Price type ("close", "open", "high", "low")
        month: Specific month in YYYY-MM format
        entitlement: Data freshness ("realtime", "delayed", or None)
        format: Output format ("json" or "csv")
    
    Returns:
        MAMA time series data
    """
    params = {
        "ticker": ticker,
        "time_interval": time_interval,
        "price_type": price_type,
        "format": format,
    }
    
    if month:
        params["month"] = month
    if entitlement:
        params["entitlement"] = entitlement
    
    return make_api_request("MAMA", params)


@mcp.tool()
def get_rsi(
    ticker: str,
    time_interval: str,
    time_period: int = 14,
    price_type: str = "close",
    month: Optional[str] = None,
    entitlement: Optional[str] = None,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get Relative Strength Index (RSI) technical indicator.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
        time_interval: Time interval ("1min", "5min", "15min", "30min", "60min", "daily", "weekly", "monthly")
        time_period: Number of data points (default: 14)
        price_type: Price type ("close", "open", "high", "low")
        month: Specific month in YYYY-MM format
        entitlement: Data freshness ("realtime", "delayed", or None)
        format: Output format ("json" or "csv")
    
    Returns:
        RSI time series data
    """
    params = {
        "ticker": ticker,
        "time_interval": time_interval,
        "time_period": str(time_period),
        "price_type": price_type,
        "format": format,
    }
    
    if month:
        params["month"] = month
    if entitlement:
        params["entitlement"] = entitlement
    
    return make_api_request("RSI", params)


@mcp.tool()
def get_macd(
    ticker: str,
    time_interval: str,
    time_period: int = 20,
    price_type: str = "close",
    month: Optional[str] = None,
    entitlement: Optional[str] = None,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get Moving Average Convergence Divergence (MACD) technical indicator.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
        time_interval: Time interval ("1min", "5min", "15min", "30min", "60min", "daily", "weekly", "monthly")
        time_period: Number of data points (default: 20)
        price_type: Price type ("close", "open", "high", "low")
        month: Specific month in YYYY-MM format
        entitlement: Data freshness ("realtime", "delayed", or None)
        format: Output format ("json" or "csv")
    
    Returns:
        MACD time series data
    """
    params = {
        "ticker": ticker,
        "time_interval": time_interval,
        "time_period": str(time_period),
        "price_type": price_type,
        "format": format,
    }
    
    if month:
        params["month"] = month
    if entitlement:
        params["entitlement"] = entitlement
    
    return make_api_request("MACD", params)


@mcp.tool()
def get_bbands(
    ticker: str,
    time_interval: str,
    time_period: int = 20,
    price_type: str = "close",
    nbdevup: int = 2,
    nbdevdn: int = 2,
    matype: int = 0,
    month: Optional[str] = None,
    entitlement: Optional[str] = None,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get Bollinger Bands technical indicator.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
        time_interval: Time interval ("1min", "5min", "15min", "30min", "60min", "daily", "weekly", "monthly")
        time_period: Number of data points (default: 20)
        price_type: Price type ("close", "open", "high", "low")
        nbdevup: Number of standard deviations above the moving average (default: 2)
        nbdevdn: Number of standard deviations below the moving average (default: 2)
        matype: Moving average type (0=SMA, 1=EMA, 2=WMA, 3=DEMA, 4=TEMA, 5=TRIMA, 6=KAMA, 7=MAMA)
        month: Specific month in YYYY-MM format
        entitlement: Data freshness ("realtime", "delayed", or None)
        format: Output format ("json" or "csv")
    
    Returns:
        Bollinger Bands time series data
    """
    params = {
        "ticker": ticker,
        "time_interval": time_interval,
        "time_period": str(time_period),
        "price_type": price_type,
        "nbdevup": str(nbdevup),
        "nbdevdn": str(nbdevdn),
        "matype": str(matype),
        "format": format,
    }
    
    if month:
        params["month"] = month
    if entitlement:
        params["entitlement"] = entitlement
    
    return make_api_request("BBANDS", params)


# =============================================================================
# FUNDAMENTAL DATA
# =============================================================================

@mcp.tool()
def get_company_overview(ticker: str) -> Dict[str, Any]:
    """
    Get company overview including financial ratios and key metrics.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
    
    Returns:
        Company information, financial ratios, and key metrics
    """
    params = {
        "ticker": ticker,
    }
    
    return make_api_request("OVERVIEW", params)


@mcp.tool()
def get_ETF_profile(ticker: str) -> Dict[str, Any]:
    """
    Get ETF profile including metrics and holdings.
    
    Args:
        ticker: ETF symbol (e.g., "QQQ")
    
    Returns:
        ETF metrics and holdings data
    """
    params = {
        "ticker": ticker,
    }
    
    return make_api_request("ETF_PROFILE", params)


@mcp.tool()
def get_dividends(ticker: str, format: str = "json") -> Dict[str, Any]:
    """
    Get dividend history for a stock.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
        format: Output format ("json" or "csv")
    
    Returns:
        Historical dividend data
    """
    params = {
        "ticker": ticker,
        "format": format,
    }
    
    return make_api_request("DIVIDENDS", params)


@mcp.tool()
def get_splits(ticker: str, format: str = "json") -> Dict[str, Any]:
    """
    Get stock split history for a stock.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
        format: Output format ("json" or "csv")
    
    Returns:
        Historical split data
    """
    params = {
        "ticker": ticker,
        "format": format,
    }
    
    return make_api_request("SPLITS", params)


# =============================================================================
# ECONOMIC INDICATORS
# =============================================================================

@mcp.tool()
def get_real_gdp(
    time_interval: str = "annual",
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get US Real GDP data.
    
    Args:
        time_interval: "annual" or "quarterly"
        format: Output format ("json" or "csv")
    
    Returns:
        Real GDP time series data
    """
    params = {
        "time_interval": time_interval,
        "format": format,
    }
    
    return make_api_request("REAL_GDP", params)


@mcp.tool()
def get_real_gdp_per_capita(
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get US Real GDP per Capita data.
    
    Args:
        format: Output format ("json" or "csv")
    
    Returns:
        Real GDP per Capita time series data
    """
    params = {
        "format": format,
    }
    
    return make_api_request("REAL_GDP_PER_CAPITA", params)


@mcp.tool()
def get_treasury_yield(
    time_interval: str = "monthly",
    maturity: str = "10year",
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get US Treasury yield data.
    
    Args:
        time_interval: "daily", "weekly", or "monthly"
        maturity: "3month", "2year", "5year", "7year", "10year", or "30year"
        format: Output format ("json" or "csv")
    
    Returns:
        Treasury yield time series data
    """
    params = {
        "time_interval": time_interval,
        "maturity": maturity,
        "format": format,
    }
    
    return make_api_request("TREASURY_YIELD", params)


@mcp.tool()
def get_federal_funds_rate(
    time_interval: str = "monthly",
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get US Federal Funds Rate data.
    
    Args:
        time_interval: "daily", "weekly", or "monthly"
        format: Output format ("json" or "csv")
    
    Returns:
        Federal Funds Rate time series data
    """
    params = {
        "time_interval": time_interval,
        "format": format,
    }
    
    return make_api_request("FEDERAL_FUNDS_RATE", params)


@mcp.tool()
def get_cpi(
    time_interval: str = "monthly",
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get US Consumer Price Index (CPI) data.
    
    Args:
        time_interval: "monthly" or "annual"
        format: Output format ("json" or "csv")
    
    Returns:
        CPI time series data
    """
    params = {
        "time_interval": time_interval,
        "format": format,
    }
    
    return make_api_request("CPI", params)


@mcp.tool()
def get_inflation(
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get US inflation rate data.
    
    Args:
        format: Output format ("json" or "csv")
    
    Returns:
        Inflation rate time series data
    """
    params = {
        "format": format,
    }
    
    return make_api_request("INFLATION", params)


@mcp.tool()
def get_retail_sales(
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get US Retail Sales data.
    
    Args:
        format: Output format ("json" or "csv")
    
    Returns:
        Retail Sales time series data
    """
    params = {
        "format": format,
    }
    
    return make_api_request("RETAIL_SALES", params)


@mcp.tool()
def get_durable_goods(
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get US Durable Goods Orders data.
    
    Args:
        format: Output format ("json" or "csv")
    
    Returns:
        Durable Goods Orders time series data
    """
    params = {
        "format": format,
    }
    
    return make_api_request("DURABLES", params)


@mcp.tool()
def get_unemployment(
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get US Unemployment Rate data.
    
    Args:
        format: Output format ("json" or "csv")
    
    Returns:
        Unemployment Rate time series data
    """
    params = {
        "format": format,
    }
    
    return make_api_request("UNEMPLOYMENT", params)


# =============================================================================
# ALPHA INTELLIGENCE
# =============================================================================

@mcp.tool()
def get_market_news_sentiment(
    tickers: Optional[str] = None,
    topics: Optional[str] = None,
    time_from: Optional[str] = None,
    time_to: Optional[str] = None,
    sort: str = "LATEST",
    limit: int = 50,
) -> Dict[str, Any]:
    """
    Get market news and sentiment data.
    
    Args:
        tickers: Stock/crypto/forex symbols to filter (comma-separated)
        topics: News topics to filter (comma-separated)
        time_from: Start time in YYYYMMDDTHHMM format
        time_to: End time in YYYYMMDDTHHMM format
        sort: Sort order ("LATEST", "EARLIEST", or "RELEVANCE")
        limit: Maximum results (default: 50, max: 1000)
    
    Returns:
        Market news and sentiment data
    """
    params = {
        "sort": sort,
        "limit": str(limit),
    }
    
    if tickers:
        params["tickers"] = tickers
    if topics:
        params["topics"] = topics
    if time_from:
        params["time_from"] = time_from
    if time_to:
        params["time_to"] = time_to
    
    return make_api_request("NEWS_SENTIMENT", params)


@mcp.tool()
def get_earnings_call_transcript(
    ticker: str,
    quarter: str,
) -> Dict[str, Any]:
    """
    Get earnings call transcript for a company.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
        quarter: Quarter in YYYYQM format (e.g., "2024Q1")
    
    Returns:
        Earnings call transcript with sentiment signals
    """
    params = {
        "ticker": ticker,
        "quarter": quarter,
    }
    
    return make_api_request("EARNINGS_CALL_TRANSCRIPT", params)


@mcp.tool()
def get_top_gainers_losers(
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get top gainers, losers, and most active tickers (US market).
    
    Args:
        entitlement: Data freshness ("realtime", "delayed", or None for daily updates)
    
    Returns:
        Top gainers, losers, and most active tickers data
    """
    params = {}
    
    if entitlement:
        params["entitlement"] = entitlement
    
    return make_api_request("TOP_GAINERS_LOSERS", params)


@mcp.tool()
def get_insider_transactions(
    ticker: str,
    from_date: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get insider transactions for a company.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
        from_date: Start date in YYYY-MM-DD format
    
    Returns:
        Insider transactions data
    """
    params = {
        "ticker": ticker,
    }
    
    if from_date:
        params["from"] = from_date
    
    return make_api_request("INSIDER_TRANSACTIONS", params)


# =============================================================================
# COMMODITIES
# =============================================================================

@mcp.tool()
def get_gold_silver_spot_price(ticker: str) -> Dict[str, Any]:
    """
    Get live spot prices for gold or silver.
    
    Args:
        ticker: "GOLD", "XAU" for gold; "SILVER", "XAG" for silver
    
    Returns:
        Live spot price data
    """
    params = {
        "ticker": ticker,
    }
    
    return make_api_request("GOLD_SILVER_SPOT", params)


@mcp.tool()
def get_gold_silver_history(
    ticker: str,
    time_interval: str,
) -> Dict[str, Any]:
    """
    Get historical gold or silver prices.
    
    Args:
        ticker: "GOLD", "XAU" for gold; "SILVER", "XAG" for silver
        time_interval: "daily", "weekly", or "monthly"
    
    Returns:
        Historical price data
    """
    params = {
        "ticker": ticker,
        "time_interval": time_interval,
    }
    
    return make_api_request("GOLD_SILVER_HISTORY", params)


@mcp.tool()
def get_wti_crude_oil(
    time_interval: str = "monthly",
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get West Texas Intermediate (WTI) crude oil prices.
    
    Args:
        time_interval: "daily", "weekly", or "monthly"
        format: Output format ("json" or "csv")
    
    Returns:
        WTI crude oil price time series data
    """
    params = {
        "time_interval": time_interval,
        "format": format,
    }
    
    return make_api_request("WTI", params)


@mcp.tool()
def get_brent_crude_oil(
    time_interval: str = "monthly",
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get Brent (Europe) crude oil prices.
    
    Args:
        time_interval: "daily", "weekly", or "monthly"
        format: Output format ("json" or "csv")
    
    Returns:
        Brent crude oil price time series data
    """
    params = {
        "time_interval": time_interval,
        "format": format,
    }
    
    return make_api_request("BRENT", params)


# =============================================================================
# OPTIONS DATA
# =============================================================================

@mcp.tool()
def get_realtime_options(
    ticker: str,
    require_greeks: bool = False,
    contract: Optional[str] = None,
    expiration: Optional[str] = None,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get realtime US options data.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
        require_greeks: If True, include greeks and implied volatility
        contract: Specific options contract ID
        expiration: Expiration date in YYYY-MM-DD format
        format: Output format ("json" or "csv")
    
    Returns:
        Options chain data
    """
    params = {
        "ticker": ticker,
        "require_greeks": str(require_greeks).lower(),
        "format": format,
    }
    
    if contract:
        params["contract"] = contract
    if expiration:
        params["expiration"] = expiration
    
    return make_api_request("REALTIME_OPTIONS", params)


@mcp.tool()
def get_realtime_put_call_ratio(ticker: str) -> Dict[str, Any]:
    """
    Get realtime put-call ratio for an option chain.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
    
    Returns:
        Put-call ratio data
    """
    params = {
        "ticker": ticker,
    }
    
    return make_api_request("REALTIME_PUT_CALL_RATIO", params)


@mcp.tool()
def get_realtime_volume_open_interest_ratio(ticker: str) -> Dict[str, Any]:
    """
    Get realtime volume-to-open-interest ratio for an option chain.
    
    Args:
        ticker: Stock symbol (e.g., "NVDA")
    
    Returns:
        Volume-to-open-interest ratio data
    """
    params = {
        "ticker": ticker,
    }
    
    return make_api_request("REALTIME_VOLUME_OPEN_INTEREST_RATIO", params)


@mcp.tool()
def get_historical_options(
    ticker: str,
    date: Optional[str] = None,
    contract: Optional[str] = None,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get historical US options data.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
        date: Date in YYYY-MM-DD format (defaults to previous trading session)
        contract: Specific options contract ID
        format: Output format ("json" or "csv")
    
    Returns:
        Historical options chain data
    """
    params = {
        "ticker": ticker,
        "format": format,
    }
    
    if date:
        params["date"] = date
    if contract:
        params["contract"] = contract
    
    return make_api_request("HISTORICAL_OPTIONS", params)


# =============================================================================
# RUN SERVER
# =============================================================================

if __name__ == "__main__":
    mcp.run()


@mcp.tool()
def get_historical_options(
    ticker: str,
    date: Optional[str] = None,
    contract: Optional[str] = None,
    format: str = "json",
) -> Dict[str, Any]:
    """
    Get historical US options data.
    
    Args:
        ticker: Stock symbol (e.g., "IBM")
        date: Date in YYYY-MM-DD format (defaults to previous trading session)
        contract: Specific options contract ID
        format: Output format ("json" or "csv")
    
    Returns:
        Historical options chain data
    """
    params = {
        "ticker": ticker,
        "format": format,
    }
    
    if date:
        params["date"] = date
    if contract:
        params["contract"] = contract
    
    return make_api_request("HISTORICAL_OPTIONS", params)


# =============================================================================
# RUN SERVER
# =============================================================================

if __name__ == "__main__":
    mcp.run()
