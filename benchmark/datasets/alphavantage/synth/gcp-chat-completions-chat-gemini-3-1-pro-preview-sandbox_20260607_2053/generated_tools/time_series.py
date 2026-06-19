import os
import requests
from typing import Dict, Any

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

def get_time_series_intraday(symbol: str, interval: str = "5min", outputsize: str = "compact") -> dict:
    """Get intraday stock time series data."""
    return make_request({
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "outputsize": outputsize
    })

def get_time_series_daily(symbol: str, outputsize: str = "compact") -> dict:
    """Get daily stock time series data."""
    return make_request({
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": outputsize
    })

def get_time_series_weekly(symbol: str) -> dict:
    """Get weekly stock time series data."""
    return make_request({
        "function": "TIME_SERIES_WEEKLY",
        "symbol": symbol
    })

def get_time_series_monthly(symbol: str) -> dict:
    """Get monthly stock time series data."""
    return make_request({
        "function": "TIME_SERIES_MONTHLY",
        "symbol": symbol
    })

def get_global_quote(symbol: str) -> dict:
    """Get the latest price and volume for a symbol."""
    return make_request({
        "function": "GLOBAL_QUOTE",
        "symbol": symbol
    })

def search_symbol(keywords: str) -> dict:
    """Search for a symbol or ticker."""
    return make_request({
        "function": "SYMBOL_SEARCH",
        "keywords": keywords
    })
