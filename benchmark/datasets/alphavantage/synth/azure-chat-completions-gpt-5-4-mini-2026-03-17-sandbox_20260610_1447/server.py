import csv
import io
import json
import os
from typing import Any, Dict, Optional
from urllib.parse import urlencode

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://www.alphavantage.co/query"
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", "")

mcp = FastMCP("alpha-vantage")


def _request(params: Dict[str, Any]) -> Any:
    if not API_KEY:
        return {"error": "Missing ALPHAVANTAGE_API_KEY environment variable"}
    query = dict(params)
    query["apikey"] = API_KEY
    try:
        resp = requests.get(BASE_URL, params=query, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        return {"error": str(e)}
    datatype = str(params.get("datatype", "json")).lower()
    if datatype == "csv":
        reader = csv.DictReader(io.StringIO(resp.text))
        return list(reader)
    try:
        data = resp.json()
    except ValueError:
        return {"error": "Invalid JSON response", "raw": resp.text}
    if isinstance(data, dict) and ("Error Message" in data or "Note" in data or "Information" in data):
        return {"error": data.get("Error Message") or data.get("Note") or data.get("Information"), "raw": data}
    return data


@mcp.tool()
def time_series_intraday(symbol: str, interval: str, adjusted: bool = True, extended_hours: bool = True, month: Optional[str] = None, outputsize: str = "compact", datatype: str = "json", entitlement: Optional[str] = None) -> Any:
    return _request({"function": "TIME_SERIES_INTRADAY", "symbol": symbol, "interval": interval, "adjusted": str(adjusted).lower(), "extended_hours": str(extended_hours).lower(), "month": month, "outputsize": outputsize, "datatype": datatype, "entitlement": entitlement})


@mcp.tool()
def time_series_daily(symbol: str, outputsize: str = "compact", datatype: str = "json") -> Any:
    return _request({"function": "TIME_SERIES_DAILY", "symbol": symbol, "outputsize": outputsize, "datatype": datatype})


@mcp.tool()
def time_series_weekly(symbol: str, datatype: str = "json") -> Any:
    return _request({"function": "TIME_SERIES_WEEKLY", "symbol": symbol, "datatype": datatype})


@mcp.tool()
def time_series_monthly(symbol: str, datatype: str = "json") -> Any:
    return _request({"function": "TIME_SERIES_MONTHLY", "symbol": symbol, "datatype": datatype})


@mcp.tool()
def global_quote(symbol: str) -> Any:
    return _request({"function": "GLOBAL_QUOTE", "symbol": symbol})


@mcp.tool()
def symbol_search(keywords: str) -> Any:
    return _request({"function": "SYMBOL_SEARCH", "keywords": keywords})


@mcp.tool()
def currency_exchange_rate(from_currency: str, to_currency: str) -> Any:
    return _request({"function": "CURRENCY_EXCHANGE_RATE", "from_currency": from_currency, "to_currency": to_currency})


@mcp.tool()
def fx_daily(from_symbol: str, to_symbol: str, outputsize: str = "compact", datatype: str = "json") -> Any:
    return _request({"function": "FX_DAILY", "from_symbol": from_symbol, "to_symbol": to_symbol, "outputsize": outputsize, "datatype": datatype})


@mcp.tool()
def digital_currency_daily(symbol: str, market: str) -> Any:
    return _request({"function": "DIGITAL_CURRENCY_DAILY", "symbol": symbol, "market": market})


@mcp.tool()
def sma(symbol: str, interval: str, time_period: int, series_type: str, month: Optional[str] = None, datatype: str = "json", entitlement: Optional[str] = None) -> Any:
    return _request({"function": "SMA", "symbol": symbol, "interval": interval, "time_period": time_period, "series_type": series_type, "month": month, "datatype": datatype, "entitlement": entitlement})


@mcp.tool()
def ema(symbol: str, interval: str, time_period: int, series_type: str, month: Optional[str] = None, datatype: str = "json", entitlement: Optional[str] = None) -> Any:
    return _request({"function": "EMA", "symbol": symbol, "interval": interval, "time_period": time_period, "series_type": series_type, "month": month, "datatype": datatype, "entitlement": entitlement})


@mcp.tool()
def rsi(symbol: str, interval: str, time_period: int, series_type: str, month: Optional[str] = None, datatype: str = "json", entitlement: Optional[str] = None) -> Any:
    return _request({"function": "RSI", "symbol": symbol, "interval": interval, "time_period": time_period, "series_type": series_type, "month": month, "datatype": datatype, "entitlement": entitlement})


@mcp.tool()
def macd(symbol: str, interval: str, series_type: str, fastperiod: int = 12, slowperiod: int = 26, signalperiod: int = 9, month: Optional[str] = None, datatype: str = "json", entitlement: Optional[str] = None) -> Any:
    return _request({"function": "MACD", "symbol": symbol, "interval": interval, "series_type": series_type, "fastperiod": fastperiod, "slowperiod": slowperiod, "signalperiod": signalperiod, "month": month, "datatype": datatype, "entitlement": entitlement})


@mcp.tool()
def bollinger_bands(symbol: str, interval: str, time_period: int, series_type: str, nbdevup: int = 2, nbdevdn: int = 2, matype: int = 0, month: Optional[str] = None, datatype: str = "json", entitlement: Optional[str] = None) -> Any:
    return _request({"function": "BBANDS", "symbol": symbol, "interval": interval, "time_period": time_period, "series_type": series_type, "nbdevup": nbdevup, "nbdevdn": nbdevdn, "matype": matype, "month": month, "datatype": datatype, "entitlement": entitlement})


@mcp.tool()
def company_overview(symbol: str) -> Any:
    return _request({"function": "OVERVIEW", "symbol": symbol})


@mcp.tool()
def income_statement(symbol: str) -> Any:
    return _request({"function": "INCOME_STATEMENT", "symbol": symbol})


@mcp.tool()
def balance_sheet(symbol: str) -> Any:
    return _request({"function": "BALANCE_SHEET", "symbol": symbol})


@mcp.tool()
def earnings(symbol: str) -> Any:
    return _request({"function": "EARNINGS", "symbol": symbol})


@mcp.tool()
def real_gdp(interval: str = "annual", datatype: str = "json") -> Any:
    return _request({"function": "REAL_GDP", "interval": interval, "datatype": datatype})


@mcp.tool()
def real_gdp_per_capita(datatype: str = "json") -> Any:
    return _request({"function": "REAL_GDP_PER_CAPITA", "datatype": datatype})


@mcp.tool()
def treasury_yield(interval: str = "monthly", maturity: str = "10year", datatype: str = "json") -> Any:
    return _request({"function": "TREASURY_YIELD", "interval": interval, "maturity": maturity, "datatype": datatype})


@mcp.tool()
def federal_funds_rate(interval: str = "monthly", datatype: str = "json") -> Any:
    return _request({"function": "FEDERAL_FUNDS_RATE", "interval": interval, "datatype": datatype})


@mcp.tool()
def cpi(interval: str = "monthly", datatype: str = "json") -> Any:
    return _request({"function": "CPI", "interval": interval, "datatype": datatype})


@mcp.tool()
def sector_performance() -> Any:
    return _request({"function": "SECTOR"})


if __name__ == "__main__":
    mcp.run(transport="stdio")
