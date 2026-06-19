#!/usr/bin/env python3
"""
MCP Server for Alpha Vantage Financial Data API
"""

import os
import requests
from typing import Any, Dict, List, Optional
from fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP(
    name="alpha-vantage",
    version="1.0.0",
    description="Financial data API server providing stock, forex, crypto, and economic data"
)

# Base URL for Alpha Vantage API
ALPHA_VANTAGE_BASE_URL = "https://www.alphavantage.co/query"


def _make_api_request(function: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """Make a request to the Alpha Vantage API."""
    try:
        params["function"] = function
        params["apikey"] = os.environ.get("ALPHAVANTAGE_API_KEY", "")
        
        response = requests.get(ALPHA_VANTAGE_BASE_URL, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        # Check for API errors
        if "Error Message" in data:
            return {"error": data["Error Message"]}
        if "Information" in data:
            return {"error": data["Information"]}
        if "Note" in data:
            # This is just a note about rate limiting, not an error
            return data
        
        return data
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


# Stock Time Series Endpoints

@mcp.tool()
def get_intraday_stock_data(
    symbol: str,
    interval: str = "60min",
    outputsize: str = "compact",
    datatype: str = "json"
) -> Dict[str, Any]:
    """
    Get intraday time series data for a stock symbol.
    
    Args:
        symbol: The stock symbol to query
        interval: Time interval between data points (1min, 5min, 15min, 30min, 60min)
        outputsize: Size of the output (compact or full)
        datatype: Response format (json or csv)
    
    Returns:
        Time series data including open, high, low, close, volume
    """
    return _make_api_request(
        "TIME_SERIES_INTRADAY",
        {
            "symbol": symbol,
            "interval": interval,
            "outputsize": outputsize,
            "datatype": datatype
        }
    )


@mcp.tool()
def get_daily_stock_data(
    symbol: str,
    outputsize: str = "compact",
    datatype: str = "json"
) -> Dict[str, Any]:
    """
    Get daily time series data for a stock symbol.
    
    Args:
        symbol: The stock symbol to query
        outputsize: Size of the output (compact or full)
        datatype: Response format (json or csv)
    
    Returns:
        Daily time series data including open, high, low, close, volume
    """
    return _make_api_request(
        "TIME_SERIES_DAILY",
        {
            "symbol": symbol,
            "outputsize": outputsize,
            "datatype": datatype
        }
    )


@mcp.tool()
def get_daily_adjusted_stock_data(
    symbol: str,
    outputsize: str = "compact",
    datatype: str = "json"
) -> Dict[str, Any]:
    """
    Get daily adjusted time series data for a stock symbol.
    
    Args:
        symbol: The stock symbol to query
        outputsize: Size of the output (compact or full)
        datatype: Response format (json or csv)
    
    Returns:
        Daily adjusted time series data including open, high, low, close, volume,
        adjusted close, and dividend amount
    """
    return _make_api_request(
        "TIME_SERIES_DAILY_ADJUSTED",
        {
            "symbol": symbol,
            "outputsize": outputsize,
            "datatype": datatype
        }
    )


@mcp.tool()
def get_weekly_stock_data(
    symbol: str,
    datatype: str = "json"
) -> Dict[str, Any]:
    """
    Get weekly time series data for a stock symbol.
    
    Args:
        symbol: The stock symbol to query
        datatype: Response format (json or csv)
    
    Returns:
        Weekly time series data including open, high, low, close, volume
    """
    return _make_api_request(
        "TIME_SERIES_WEEKLY",
        {
            "symbol": symbol,
            "datatype": datatype
        }
    )


@mcp.tool()
def get_weekly_adjusted_stock_data(
    symbol: str,
    datatype: str = "json"
) -> Dict[str, Any]:
    """
    Get weekly adjusted time series data for a stock symbol.
    
    Args:
        symbol: The stock symbol to query
        datatype: Response format (json or csv)
    
    Returns:
        Weekly adjusted time series data including open, high, low, close,
        adjusted close, volume, and dividend amount
    """
    return _make_api_request(
        "TIME_SERIES_WEEKLY_ADJUSTED",
        {
            "symbol": symbol,
            "datatype": datatype
        }
    )


@mcp.tool()
def get_monthly_stock_data(
    symbol: str,
    datatype: str = "json"
) -> Dict[str, Any]:
    """
    Get monthly time series data for a stock symbol.
    
    Args:
        symbol: The stock symbol to query
        datatype: Response format (json or csv)
    
    Returns:
        Monthly time series data including open, high, low, close, volume
    """
    return _make_api_request(
        "TIME_SERIES_MONTHLY",
        {
            "symbol": symbol,
            "datatype": datatype
        }
    )


@mcp.tool()
def get_monthly_adjusted_stock_data(
    symbol: str,
    datatype: str = "json"
) -> Dict[str, Any]:
    """
    Get monthly adjusted time series data for a stock symbol.
    
    Args:
        symbol: The stock symbol to query
        datatype: Response format (json or csv)
    
    Returns:
        Monthly adjusted time series data including open, high, low, close,
        adjusted close, volume, and dividend amount
    """
    return _make_api_request(
        "TIME_SERIES_MONTHLY_ADJUSTED",
        {
            "symbol": symbol,
            "datatype": datatype
        }
    )


# Quote Endpoint

@mcp.tool()
def get_quote_endpoint(symbol: str) -> Dict[str, Any]:
    """
    Get the latest price and volume for a stock symbol.
    
    Args:
        symbol: The stock symbol to query
    
    Returns:
        Latest quote data including price, volume, and other metrics
    """
    return _make_api_request(
        "GLOBAL_QUOTE",
        {
            "symbol": symbol
        }
    )


# Search Endpoint

@mcp.tool()
def search_symbols(
    keywords: str,
    datatype: str = "json"
) -> Dict[str, Any]:
    """
    Search for stock symbols using keywords.
    
    Args:
        keywords: Search keywords (company name, ticker symbol, etc.)
        datatype: Response format (json or csv)
    
    Returns:
        List of matching symbols with metadata
    """
    return _make_api_request(
        "SYMBOL_SEARCH",
        {
            "keywords": keywords,
            "datatype": datatype
        }
    )


# Forex Endpoints

@mcp.tool()
def get_fx_intraday(
    from_symbol: str,
    to_symbol: str,
    interval: str = "60min",
    outputsize: str = "compact",
    datatype: str = "json"
) -> Dict[str, Any]:
    """
    Get intraday forex exchange rate data.
    
    Args:
        from_symbol: The source currency (e.g., USD)
        to_symbol: The target currency (e.g., EUR)
        interval: Time interval between data points (1min, 5min, 15min, 30min, 60min)
        outputsize: Size of the output (compact or full)
        datatype: Response format (json or csv)
    
    Returns:
        Intraday FX time series data
    """
    return _make_api_request(
        "FX_INTRADAY",
        {
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
            "interval": interval,
            "outputsize": outputsize,
            "datatype": datatype
        }
    )


@mcp.tool()
def get_fx_daily(
    from_symbol: str,
    to_symbol: str,
    outputsize: str = "compact",
    datatype: str = "json"
) -> Dict[str, Any]:
    """
    Get daily forex exchange rate data.
    
    Args:
        from_symbol: The source currency (e.g., USD)
        to_symbol: The target currency (e.g., EUR)
        outputsize: Size of the output (compact or full)
        datatype: Response format (json or csv)
    
    Returns:
        Daily FX time series data
    """
    return _make_api_request(
        "FX_DAILY",
        {
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
            "outputsize": outputsize,
            "datatype": datatype
        }
    )


@mcp.tool()
def get_fx_weekly(
    from_symbol: str,
    to_symbol: str,
    datatype: str = "json"
) -> Dict[str, Any]:
    """
    Get weekly forex exchange rate data.
    
    Args:
        from_symbol: The source currency (e.g., USD)
        to_symbol: The target currency (e.g., EUR)
        datatype: Response format (json or csv)
    
    Returns:
        Weekly FX time series data
    """
    return _make_api_request(
        "FX_WEEKLY",
        {
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
            "datatype": datatype
        }
    )


@mcp.tool()
def get_fx_monthly(
    from_symbol: str,
    to_symbol: str,
    datatype: str = "json"
) -> Dict[str, Any]:
    """
    Get monthly forex exchange rate data.
    
    Args:
        from_symbol: The source currency (e.g., USD)
        to_symbol: The target currency (e.g., EUR)
        datatype: Response format (json or csv)
    
    Returns:
        Monthly FX time series data
    """
    return _make_api_request(
        "FX_MONTHLY",
        {
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
            "datatype": datatype
        }
    )


# Crypto Endpoints

@mcp.tool()
def get_crypto_intraday(
    from_symbol: str,
    to_symbol: str,
    interval: str = "60min",
    outputsize: str = "compact",
    datatype: str = "json"
) -> Dict[str, Any]:
    """
    Get intraday cryptocurrency exchange rate data.
    
    Args:
        from_symbol: The source currency (e.g., BTC)
        to_symbol: The target currency (e.g., USD)
        interval: Time interval between data points (1min, 5min, 15min, 30min, 60min)
        outputsize: Size of the output (compact or full)
        datatype: Response format (json or csv)
    
    Returns:
        Intraday crypto time series data
    """
    return _make_api_request(
        "CRYPTO_INTRADAY",
        {
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
            "interval": interval,
            "outputsize": outputsize,
            "datatype": datatype
        }
    )


@mcp.tool()
def get_crypto_daily(
    from_symbol: str,
    to_symbol: str,
    outputsize: str = "compact",
    datatype: str = "json"
) -> Dict[str, Any]:
    """
    Get daily cryptocurrency exchange rate data.
    
    Args:
        from_symbol: The source currency (e.g., BTC)
        to_symbol: The target currency (e.g., USD)
        outputsize: Size of the output (compact or full)
        datatype: Response format (json or csv)
    
    Returns:
        Daily crypto time series data
    """
    return _make_api_request(
        "CRYPTO_DAILY",
        {
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
            "outputsize": outputsize,
            "datatype": datatype
        }
    )


@mcp.tool()
def get_crypto_weekly(
    from_symbol: str,
    to_symbol: str,
    datatype: str = "json"
) -> Dict[str, Any]:
    """
    Get weekly cryptocurrency exchange rate data.
    
    Args:
        from_symbol: The source currency (e.g., BTC)
        to_symbol: The target currency (e.g., USD)
        datatype: Response format (json or csv)
    
    Returns:
        Weekly crypto time series data
    """
    return _make_api_request(
        "CRYPTO_WEEKLY",
        {
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
            "datatype": datatype
        }
    )


@mcp.tool()
def get_crypto_monthly(
    from_symbol: str,
    to_symbol: str,
    datatype: str = "json"
) -> Dict[str, Any]:
    """
    Get monthly cryptocurrency exchange rate data.
    
    Args:
        from_symbol: The source currency (e.g., BTC)
        to_symbol: The target currency (e.g., USD)
        datatype: Response format (json or csv)
    
    Returns:
        Monthly crypto time series data
    """
    return _make_api_request(
        "CRYPTO_MONTHLY",
        {
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
            "datatype": datatype
        }
    )


# Technical Indicators

@mcp.tool()
def get_sma(
    symbol: str,
    interval: str = "daily",
    time_period: int = 20,
    series_type: str = "close"
) -> Dict[str, Any]:
    """
    Get Simple Moving Average (SMA) technical indicator.
    
    Args:
        symbol: The stock symbol to query
        interval: Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)
        time_period: Number of data points to average (e.g., 20, 50, 200)
        series_type: Price type (close, open, high, low)
    
    Returns:
        SMA indicator data
    """
    return _make_api_request(
        "SMA",
        {
            "symbol": symbol,
            "interval": interval,
            "time_period": time_period,
            "series_type": series_type
        }
    )


@mcp.tool()
def get_ema(
    symbol: str,
    interval: str = "daily",
    time_period: int = 20,
    series_type: str = "close"
) -> Dict[str, Any]:
    """
    Get Exponential Moving Average (EMA) technical indicator.
    
    Args:
        symbol: The stock symbol to query
        interval: Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)
        time_period: Number of data points to average (e.g., 20, 50, 200)
        series_type: Price type (close, open, high, low)
    
    Returns:
        EMA indicator data
    """
    return _make_api_request(
        "EMA",
        {
            "symbol": symbol,
            "interval": interval,
            "time_period": time_period,
            "series_type": series_type
        }
    )


@mcp.tool()
def get_rsi(
    symbol: str,
    interval: str = "daily",
    time_period: int = 14,
    series_type: str = "close"
) -> Dict[str, Any]:
    """
    Get Relative Strength Index (RSI) technical indicator.
    
    Args:
        symbol: The stock symbol to query
        interval: Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)
        time_period: Number of data points for calculation (e.g., 14)
        series_type: Price type (close, open, high, low)
    
    Returns:
        RSI indicator data
    """
    return _make_api_request(
        "RSI",
        {
            "symbol": symbol,
            "interval": interval,
            "time_period": time_period,
            "series_type": series_type
        }
    )


@mcp.tool()
def get_macd(
    symbol: str,
    interval: str = "daily",
    series_type: str = "close"
) -> Dict[str, Any]:
    """
    Get Moving Average Convergence Divergence (MACD) technical indicator.
    
    Args:
        symbol: The stock symbol to query
        interval: Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)
        series_type: Price type (close, open, high, low)
    
    Returns:
        MACD indicator data
    """
    return _make_api_request(
        "MACD",
        {
            "symbol": symbol,
            "interval": interval,
            "series_type": series_type
        }
    )


@mcp.tool()
def get_bollinger_bands(
    symbol: str,
    interval: str = "daily",
    time_period: int = 20,
    series_type: str = "close",
    nbdevup: int = 2,
    nbdevdn: int = 2
) -> Dict[str, Any]:
    """
    Get Bollinger Bands technical indicator.
    
    Args:
        symbol: The stock symbol to query
        interval: Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)
        time_period: Number of data points (e.g., 20)
        series_type: Price type (close, open, high, low)
        nbdevup: Number of standard deviations above the moving average
        nbdevdn: Number of standard deviations below the moving average
    
    Returns:
        Bollinger Bands indicator data
    """
    return _make_api_request(
        "BBANDS",
        {
            "symbol": symbol,
            "interval": interval,
            "time_period": time_period,
            "series_type": series_type,
            "nbdevup": nbdevup,
            "nbdevdn": nbdevdn
        }
    )


# Fundamental Data

@mcp.tool()
def get_company_overview(symbol: str) -> Dict[str, Any]:
    """
    Get company overview and fundamentals.
    
    Args:
        symbol: The stock symbol to query
    
    Returns:
        Company overview including market cap, P/E ratio, EPS, and more
    """
    return _make_api_request(
        "OVERVIEW",
        {
            "symbol": symbol
        }
    )


@mcp.tool()
def get_income_statement(symbol: str, datatype: str = "json") -> Dict[str, Any]:
    """
    Get company income statement.
    
    Args:
        symbol: The stock symbol to query
        datatype: Response format (json or csv)
    
    Returns:
        Income statement data including revenue, net income, EPS, etc.
    """
    return _make_api_request(
        "INCOME_STATEMENT",
        {
            "symbol": symbol,
            "datatype": datatype
        }
    )


@mcp.tool()
def get_balance_sheet(symbol: str, datatype: str = "json") -> Dict[str, Any]:
    """
    Get company balance sheet.
    
    Args:
        symbol: The stock symbol to query
        datatype: Response format (json or csv)
    
    Returns:
        Balance sheet data including assets, liabilities, equity, etc.
    """
    return _make_api_request(
        "BALANCE_SHEET",
        {
            "symbol": symbol,
            "datatype": datatype
        }
    )


@mcp.tool()
def get_cash_flow(symbol: str, datatype: str = "json") -> Dict[str, Any]:
    """
    Get company cash flow statement.
    
    Args:
        symbol: The stock symbol to query
        datatype: Response format (json or csv)
    
    Returns:
        Cash flow data including operating cash flow, capital expenditures, etc.
    """
    return _make_api_request(
        "CASH_FLOW",
        {
            "symbol": symbol,
            "datatype": datatype
        }
    )


@mcp.tool()
def get_earnings(symbol: str, datatype: str = "json") -> Dict[str, Any]:
    """
    Get company earnings data.
    
    Args:
        symbol: The stock symbol to query
        datatype: Response format (json or csv)
    
    Returns:
        Earnings data including quarterly and annual EPS
    """
    return _make_api_request(
        "EARNINGS",
        {
            "symbol": symbol,
            "datatype": datatype
        }
    )


# Economic Indicators

@mcp.tool()
def get_cpi(
    interval: str = "monthly",
    seasonally_adjusted: bool = True
) -> Dict[str, Any]:
    """
    Get Consumer Price Index (CPI) data.
    
    Args:
        interval: Data frequency (monthly, quarterly, annually)
        seasonally_adjusted: Whether to return seasonally adjusted data
    
    Returns:
        CPI data series
    """
    function = "CPI" if seasonally_adjusted else "CPI"
    return _make_api_request(
        function,
        {
            "interval": interval,
            "seasonally_adjusted": "true" if seasonally_adjusted else "false"
        }
    )


@mcp.tool()
def get_inflation() -> Dict[str, Any]:
    """
    Get inflation data.
    
    Returns:
        Inflation data series including monthly and annual rates
    """
    return _make_api_request("INFLATION", {})


@mcp.tool()
def get_gdp() -> Dict[str, Any]:
    """
    Get Gross Domestic Product (GDP) data.
    
    Returns:
        GDP data series including quarterly and annual values
    """
    return _make_api_request("GDP", {})


@mcp.tool()
def get_unemployment() -> Dict[str, Any]:
    """
    Get unemployment rate data.
    
    Returns:
        Unemployment rate data series
    """
    return _make_api_request("UNEMPLOYMENT", {})


@mcp.tool()
def get_treasury_rates(
    maturity: str = "daily",
    datatype: str = "json"
) -> Dict[str, Any]:
    """
    Get Treasury constant maturity rates.
    
    Args:
        maturity: Interest rate maturity (daily, monthly)
        datatype: Response format (json or csv)
    
    Returns:
        Treasury rates for various maturities
    """
    return _make_api_request(
        "TREASURY_CONSTANT_MATURITY",
        {
            "datatype": datatype
        }
    )


# Sector Performance

@mcp.tool()
def get_sector_performance() -> Dict[str, Any]:
    """
    Get real-time sector performance across S&P 500.
    
    Returns:
        Sector performance data including 1-day, 1-week, 1-month, and 1-year returns
        for all 11 GICS sectors
    """
    return _make_api_request("SECTOR", {})


# Run the server
if __name__ == "__main__":
    mcp.run()
