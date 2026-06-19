import json
import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://www.alphavantage.co/query"
API_KEY_ENV = "ALPHAVANTAGE_API_KEY"

mcp = FastMCP("alpha-vantage")


def _request(params: Dict[str, Any]) -> Dict[str, Any]:
    api_key = os.getenv(API_KEY_ENV)
    if not api_key:
        return {"error": f"Missing environment variable {API_KEY_ENV}"}
    query = dict(params)
    query["apikey"] = api_key
    try:
        resp = requests.get(BASE_URL, params=query, timeout=30)
        resp.raise_for_status()
        try:
            data = resp.json()
        except Exception:
            return {"error": "Alpha Vantage returned non-JSON response", "text": resp.text}
        if isinstance(data, dict) and ("Error Message" in data or "Information" in data or "Note" in data):
            return {"error": data.get("Error Message") or data.get("Information") or data.get("Note"), "raw": data}
        return data
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def get_stock_quote(symbol: str) -> Dict[str, Any]:
    return _request({"function": "GLOBAL_QUOTE", "symbol": symbol})


@mcp.tool()
def search_symbol(keywords: str) -> Dict[str, Any]:
    return _request({"function": "SYMBOL_SEARCH", "keywords": keywords})


@mcp.tool()
def get_daily_time_series(symbol: str, outputsize: str = "compact") -> Dict[str, Any]:
    return _request({"function": "TIME_SERIES_DAILY", "symbol": symbol, "outputsize": outputsize})


@mcp.tool()
def get_intraday_time_series(symbol: str, interval: str, outputsize: str = "compact") -> Dict[str, Any]:
    return _request({"function": "TIME_SERIES_INTRADAY", "symbol": symbol, "interval": interval, "outputsize": outputsize})


@mcp.tool()
def get_fx_rate(from_currency: str, to_currency: str) -> Dict[str, Any]:
    return _request({"function": "CURRENCY_EXCHANGE_RATE", "from_currency": from_currency, "to_currency": to_currency})


@mcp.tool()
def get_fx_daily(from_symbol: str, to_symbol: str, outputsize: str = "compact") -> Dict[str, Any]:
    return _request({"function": "FX_DAILY", "from_symbol": from_symbol, "to_symbol": to_symbol, "outputsize": outputsize})


@mcp.tool()
def get_crypto_daily(symbol: str, market: str) -> Dict[str, Any]:
    return _request({"function": "DIGITAL_CURRENCY_DAILY", "symbol": symbol, "market": market})


@mcp.tool()
def get_sma(symbol: str, interval: str, time_period: int, series_type: str) -> Dict[str, Any]:
    return _request({"function": "SMA", "symbol": symbol, "interval": interval, "time_period": time_period, "series_type": series_type})


@mcp.tool()
def get_company_overview(symbol: str) -> Dict[str, Any]:
    return _request({"function": "OVERVIEW", "symbol": symbol})


@mcp.tool()
def get_income_statement(symbol: str) -> Dict[str, Any]:
    return _request({"function": "INCOME_STATEMENT", "symbol": symbol})


@mcp.tool()
def get_balance_sheet(symbol: str) -> Dict[str, Any]:
    return _request({"function": "BALANCE_SHEET", "symbol": symbol})


@mcp.tool()
def get_earnings(symbol: str) -> Dict[str, Any]:
    return _request({"function": "EARNINGS", "symbol": symbol})


@mcp.tool()
def get_real_gdp(interval: str = "annual") -> Dict[str, Any]:
    return _request({"function": "REAL_GDP", "interval": interval})


@mcp.tool()
def get_cpi() -> Dict[str, Any]:
    return _request({"function": "CPI"})


@mcp.tool()
def get_unemployment() -> Dict[str, Any]:
    return _request({"function": "UNEMPLOYMENT"})


@mcp.tool()
def get_treasury_yield(interval: str = "monthly", maturity: str = "10year") -> Dict[str, Any]:
    return _request({"function": "TREASURY_YIELD", "interval": interval, "maturity": maturity})


@mcp.tool()
def get_sector_performance() -> Dict[str, Any]:
    return _request({"function": "SECTOR"})


if __name__ == "__main__":
    mcp.run()
