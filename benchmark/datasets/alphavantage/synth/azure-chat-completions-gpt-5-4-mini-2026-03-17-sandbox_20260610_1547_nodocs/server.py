import os
import requests
from typing import Any, Dict
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://www.alphavantage.co/query"
API_KEY_ENV = "ALPHAVANTAGE_API_KEY"

mcp = FastMCP("alpha-vantage")


def _call_alpha_vantage(params: Dict[str, Any]) -> Dict[str, Any]:
    api_key = os.getenv(API_KEY_ENV)
    if not api_key:
        return {"error": f"Missing environment variable {API_KEY_ENV}"}
    try:
        query = dict(params)
        query["apikey"] = api_key
        resp = requests.get(BASE_URL, params=query, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, dict) and ("Error Message" in data or "Information" in data or "Note" in data):
            return {"error": data.get("Error Message") or data.get("Information") or data.get("Note")}
        return data
    except requests.RequestException as e:
        return {"error": str(e)}
    except ValueError:
        return {"error": "Invalid JSON response from Alpha Vantage"}


@mcp.tool()
def global_quote(symbol: str) -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "GLOBAL_QUOTE", "symbol": symbol})


@mcp.tool()
def symbol_search(keywords: str) -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "SYMBOL_SEARCH", "keywords": keywords})


@mcp.tool()
def time_series_daily(symbol: str, outputsize: str = "compact") -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "TIME_SERIES_DAILY", "symbol": symbol, "outputsize": outputsize})


@mcp.tool()
def time_series_weekly(symbol: str) -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "TIME_SERIES_WEEKLY", "symbol": symbol})


@mcp.tool()
def time_series_monthly(symbol: str) -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "TIME_SERIES_MONTHLY", "symbol": symbol})


@mcp.tool()
def forex_exchange_rate(from_currency: str, to_currency: str) -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "CURRENCY_EXCHANGE_RATE", "from_currency": from_currency, "to_currency": to_currency})


@mcp.tool()
def forex_daily(from_symbol: str, to_symbol: str, outputsize: str = "compact") -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "FX_DAILY", "from_symbol": from_symbol, "to_symbol": to_symbol, "outputsize": outputsize})


@mcp.tool()
def crypto_exchange_rate(symbol: str, market: str) -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "CURRENCY_EXCHANGE_RATE", "from_currency": symbol, "to_currency": market})


@mcp.tool()
def sector_performance() -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "SECTOR"})


if __name__ == "__main__":
    mcp.run(transport="stdio")
