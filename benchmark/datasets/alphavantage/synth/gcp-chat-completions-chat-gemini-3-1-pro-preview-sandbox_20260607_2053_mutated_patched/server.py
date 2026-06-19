import os
import requests
from typing import Optional, Dict, Any
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("AlphaVantage")

BASE_URL = "https://www.alphavantage.co/query"

def _make_request(params: Dict[str, Any]) -> Dict[str, Any]:
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
    if not api_key:
        return {"error": "ALPHAVANTAGE_API_KEY environment variable is not set"}
    
    params["apikey"] = api_key
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Check for API-level errors
        if "Error Message" in data:
            return {"error": data["Error Message"]}
        if "Information" in data:
            return {"error": data["Information"]}
        if "Note" in data:
            return {"error": data["Note"]}
            
        return data
    except Exception as e:
        return {"error": str(e)}

# 1. Stock Time Series
@mcp.tool()
def get_intraday_time_series(symbol: str, interval: str = "5min", outputsize: str = "compact") -> Dict[str, Any]:
    """Get intraday time series data for a stock symbol."""
    return _make_request({
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "outputsize": outputsize
    })

@mcp.tool()
def get_daily_time_series(symbol: str, outputsize: str = "compact") -> Dict[str, Any]:
    """Get daily time series data for a stock symbol."""
    return _make_request({
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": outputsize
    })

@mcp.tool()
def get_weekly_time_series(symbol: str) -> Dict[str, Any]:
    """Get weekly time series data for a stock symbol."""
    return _make_request({
        "function": "TIME_SERIES_WEEKLY",
        "symbol": symbol
    })

@mcp.tool()
def get_monthly_time_series(symbol: str) -> Dict[str, Any]:
    """Get monthly time series data for a stock symbol."""
    return _make_request({
        "function": "TIME_SERIES_MONTHLY",
        "symbol": symbol
    })

# 2. Quote Endpoint
@mcp.tool()
def get_quote(symbol: str) -> Dict[str, Any]:
    """Get the latest price and volume information for a stock symbol."""
    return _make_request({
        "function": "GLOBAL_QUOTE",
        "symbol": symbol
    })

# 3. Search
@mcp.tool()
def search_symbol(keywords: str) -> Dict[str, Any]:
    """Search for a stock symbol or ticker by keywords."""
    return _make_request({
        "function": "SYMBOL_SEARCH",
        "keywords": keywords
    })

# 4. Forex (FX)
@mcp.tool()
def get_exchange_rate(from_currency: str, to_currency: str) -> Dict[str, Any]:
    """Get the real-time exchange rate for any pair of digital currency or physical currency."""
    return _make_request({
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": from_currency,
        "to_currency": to_currency
    })

@mcp.tool()
def get_fx_daily(from_symbol: str, to_symbol: str, outputsize: str = "compact") -> Dict[str, Any]:
    """Get daily time series data for a forex currency pair."""
    return _make_request({
        "function": "FX_DAILY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "outputsize": outputsize
    })

@mcp.tool()
def get_fx_weekly(from_symbol: str, to_symbol: str) -> Dict[str, Any]:
    """Get weekly time series data for a forex currency pair."""
    return _make_request({
        "function": "FX_WEEKLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol
    })

@mcp.tool()
def get_fx_monthly(from_symbol: str, to_symbol: str) -> Dict[str, Any]:
    """Get monthly time series data for a forex currency pair."""
    return _make_request({
        "function": "FX_MONTHLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol
    })

# 5. Cryptocurrency
@mcp.tool()
def get_crypto_daily(symbol: str, market: str = "USD") -> Dict[str, Any]:
    """Get daily time series data for a cryptocurrency."""
    return _make_request({
        "function": "DIGITAL_CURRENCY_DAILY",
        "symbol": symbol,
        "market": market
    })

@mcp.tool()
def get_crypto_weekly(symbol: str, market: str = "USD") -> Dict[str, Any]:
    """Get weekly time series data for a cryptocurrency."""
    return _make_request({
        "function": "DIGITAL_CURRENCY_WEEKLY",
        "symbol": symbol,
        "market": market
    })

@mcp.tool()
def get_crypto_monthly(symbol: str, market: str = "USD") -> Dict[str, Any]:
    """Get monthly time series data for a cryptocurrency."""
    return _make_request({
        "function": "DIGITAL_CURRENCY_MONTHLY",
        "symbol": symbol,
        "market": market
    })

# 6. Technical Indicators
@mcp.tool()
def get_sma(symbol: str, interval: str, time_period: int, series_type: str) -> Dict[str, Any]:
    """Get Simple Moving Average (SMA) values."""
    return _make_request({
        "function": "SMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type
    })

@mcp.tool()
def get_ema(symbol: str, interval: str, time_period: int, series_type: str) -> Dict[str, Any]:
    """Get Exponential Moving Average (EMA) values."""
    return _make_request({
        "function": "EMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type
    })

@mcp.tool()
def get_rsi(symbol: str, interval: str, time_period: int, series_type: str) -> Dict[str, Any]:
    """Get Relative Strength Index (RSI) values."""
    return _make_request({
        "function": "RSI",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type
    })

@mcp.tool()
def get_macd(symbol: str, interval: str, series_type: str) -> Dict[str, Any]:
    """Get Moving Average Convergence/Divergence (MACD) values."""
    return _make_request({
        "function": "MACD",
        "symbol": symbol,
        "interval": interval,
        "series_type": series_type
    })

@mcp.tool()
def get_bbands(symbol: str, interval: str, time_period: int, series_type: str) -> Dict[str, Any]:
    """Get Bollinger Bands (BBANDS) values."""
    return _make_request({
        "function": "BBANDS",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type
    })

# 7. Fundamental Data
@mcp.tool()
def get_company_overview(symbol: str) -> Dict[str, Any]:
    """Get company overview and fundamental data."""
    return _make_request({
        "function": "OVERVIEW",
        "symbol": symbol
    })

@mcp.tool()
def get_income_statement(symbol: str) -> Dict[str, Any]:
    """Get annual and quarterly income statements for a company."""
    return _make_request({
        "function": "INCOME_STATEMENT",
        "symbol": symbol
    })

@mcp.tool()
def get_balance_sheet(symbol: str) -> Dict[str, Any]:
    """Get annual and quarterly balance sheets for a company."""
    return _make_request({
        "function": "BALANCE_SHEET",
        "symbol": symbol
    })

@mcp.tool()
def get_earnings(symbol: str) -> Dict[str, Any]:
    """Get annual and quarterly earnings (EPS) for a company."""
    return _make_request({
        "function": "EARNINGS",
        "symbol": symbol
    })

# 8. Economic Indicators
@mcp.tool()
def get_cpi(interval: str = "monthly") -> Dict[str, Any]:
    """Get Consumer Price Index (CPI) data."""
    return _make_request({
        "function": "CPI",
        "interval": interval
    })

@mcp.tool()
def get_inflation() -> Dict[str, Any]:
    """Get annual inflation rates."""
    return _make_request({
        "function": "INFLATION"
    })

@mcp.tool()
def get_real_gdp(interval: str = "annual") -> Dict[str, Any]:
    """Get Real Gross Domestic Product (GDP) data."""
    return _make_request({
        "function": "REAL_GDP",
        "interval": interval
    })

@mcp.tool()
def get_unemployment() -> Dict[str, Any]:
    """Get unemployment rates."""
    return _make_request({
        "function": "UNEMPLOYMENT"
    })

@mcp.tool()
def get_treasury_yield(interval: str = "monthly", maturity: str = "10year") -> Dict[str, Any]:
    """Get treasury yield data."""
    return _make_request({
        "function": "TREASURY_YIELD",
        "interval": interval,
        "maturity": maturity
    })

# 9. Sector Performance
@mcp.tool()
def get_sector_performance() -> Dict[str, Any]:
    """Get real-time sector performance across the S&P 500."""
    return _make_request({
        "function": "SECTOR"
    })

if __name__ == "__main__":
    mcp.run()
