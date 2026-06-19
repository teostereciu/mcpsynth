import os
import requests
from typing import Optional, Dict, Any
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AlphaVantage")

BASE_URL = "https://www.alphavantage.co/query"

def get_api_key() -> str:
    key = os.environ.get("ALPHAVANTAGE_API_KEY")
    if not key:
        return "demo"
    return key

def make_request(params: Dict[str, Any]) -> Dict[str, Any]:
    params["apikey"] = get_api_key()
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if "Error Message" in data:
            return {"error": data["Error Message"]}
        if "Information" in data and "rate limit" in data["Information"].lower():
            return {"error": data["Information"]}
        return data
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_time_series_intraday(symbol: str, interval: str = "5min", outputsize: str = "compact") -> dict:
    """Get intraday stock time series data."""
    return make_request({
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "outputsize": outputsize
    })

@mcp.tool()
def get_time_series_daily(symbol: str, outputsize: str = "compact") -> dict:
    """Get daily stock time series data."""
    return make_request({
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": outputsize
    })

@mcp.tool()
def get_time_series_weekly(symbol: str) -> dict:
    """Get weekly stock time series data."""
    return make_request({
        "function": "TIME_SERIES_WEEKLY",
        "symbol": symbol
    })

@mcp.tool()
def get_time_series_monthly(symbol: str) -> dict:
    """Get monthly stock time series data."""
    return make_request({
        "function": "TIME_SERIES_MONTHLY",
        "symbol": symbol
    })

@mcp.tool()
def get_global_quote(symbol: str) -> dict:
    """Get the latest price and volume for a symbol."""
    return make_request({
        "function": "GLOBAL_QUOTE",
        "symbol": symbol
    })

@mcp.tool()
def search_symbol(keywords: str) -> dict:
    """Search for a symbol or ticker."""
    return make_request({
        "function": "SYMBOL_SEARCH",
        "keywords": keywords
    })

@mcp.tool()
def get_exchange_rate(from_currency: str, to_currency: str) -> dict:
    """Get the real-time exchange rate for any pair of digital currency or fiat currency."""
    return make_request({
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": from_currency,
        "to_currency": to_currency
    })

@mcp.tool()
def get_fx_daily(from_symbol: str, to_symbol: str) -> dict:
    """Get daily forex time series data."""
    return make_request({
        "function": "FX_DAILY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol
    })

@mcp.tool()
def get_fx_weekly(from_symbol: str, to_symbol: str) -> dict:
    """Get weekly forex time series data."""
    return make_request({
        "function": "FX_WEEKLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol
    })

@mcp.tool()
def get_fx_monthly(from_symbol: str, to_symbol: str) -> dict:
    """Get monthly forex time series data."""
    return make_request({
        "function": "FX_MONTHLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol
    })

@mcp.tool()
def get_crypto_daily(symbol: str, market: str = "USD") -> dict:
    """Get daily cryptocurrency time series data."""
    return make_request({
        "function": "DIGITAL_CURRENCY_DAILY",
        "symbol": symbol,
        "market": market
    })

@mcp.tool()
def get_crypto_weekly(symbol: str, market: str = "USD") -> dict:
    """Get weekly cryptocurrency time series data."""
    return make_request({
        "function": "DIGITAL_CURRENCY_WEEKLY",
        "symbol": symbol,
        "market": market
    })

@mcp.tool()
def get_crypto_monthly(symbol: str, market: str = "USD") -> dict:
    """Get monthly cryptocurrency time series data."""
    return make_request({
        "function": "DIGITAL_CURRENCY_MONTHLY",
        "symbol": symbol,
        "market": market
    })

@mcp.tool()
def get_sma(symbol: str, interval: str, time_period: int, series_type: str) -> dict:
    """Get Simple Moving Average (SMA) values."""
    return make_request({
        "function": "SMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type
    })

@mcp.tool()
def get_ema(symbol: str, interval: str, time_period: int, series_type: str) -> dict:
    """Get Exponential Moving Average (EMA) values."""
    return make_request({
        "function": "EMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type
    })

@mcp.tool()
def get_rsi(symbol: str, interval: str, time_period: int, series_type: str) -> dict:
    """Get Relative Strength Index (RSI) values."""
    return make_request({
        "function": "RSI",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type
    })

@mcp.tool()
def get_macd(symbol: str, interval: str, series_type: str) -> dict:
    """Get Moving Average Convergence/Divergence (MACD) values."""
    return make_request({
        "function": "MACD",
        "symbol": symbol,
        "interval": interval,
        "series_type": series_type
    })

@mcp.tool()
def get_bbands(symbol: str, interval: str, time_period: int, series_type: str) -> dict:
    """Get Bollinger Bands (BBANDS) values."""
    return make_request({
        "function": "BBANDS",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type
    })

@mcp.tool()
def get_company_overview(symbol: str) -> dict:
    """Get company overview fundamental data."""
    return make_request({
        "function": "OVERVIEW",
        "symbol": symbol
    })

@mcp.tool()
def get_income_statement(symbol: str) -> dict:
    """Get company income statement."""
    return make_request({
        "function": "INCOME_STATEMENT",
        "symbol": symbol
    })

@mcp.tool()
def get_balance_sheet(symbol: str) -> dict:
    """Get company balance sheet."""
    return make_request({
        "function": "BALANCE_SHEET",
        "symbol": symbol
    })

@mcp.tool()
def get_earnings(symbol: str) -> dict:
    """Get company earnings."""
    return make_request({
        "function": "EARNINGS",
        "symbol": symbol
    })

@mcp.tool()
def get_cpi(interval: str = "monthly") -> dict:
    """Get Consumer Price Index (CPI)."""
    return make_request({
        "function": "CPI",
        "interval": interval
    })

@mcp.tool()
def get_inflation() -> dict:
    """Get inflation rates."""
    return make_request({
        "function": "INFLATION"
    })

@mcp.tool()
def get_real_gdp(interval: str = "annual") -> dict:
    """Get Real Gross Domestic Product (GDP)."""
    return make_request({
        "function": "REAL_GDP",
        "interval": interval
    })

@mcp.tool()
def get_unemployment() -> dict:
    """Get unemployment rates."""
    return make_request({
        "function": "UNEMPLOYMENT"
    })

@mcp.tool()
def get_treasury_yield(interval: str = "monthly", maturity: str = "10year") -> dict:
    """Get treasury yields."""
    return make_request({
        "function": "TREASURY_YIELD",
        "interval": interval,
        "maturity": maturity
    })

@mcp.tool()
def get_sector_performance() -> dict:
    """Get real-time sector performance across S&P 500."""
    return make_request({
        "function": "SECTOR"
    })

if __name__ == "__main__":
    mcp.run()
