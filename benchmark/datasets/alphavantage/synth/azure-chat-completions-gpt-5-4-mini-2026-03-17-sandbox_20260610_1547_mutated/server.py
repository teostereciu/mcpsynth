import json
import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://www.alphavantage.co/query"
API_KEY_ENV = "ALPHAVANTAGE_API_KEY"

mcp = FastMCP("alpha-vantage")


def _request(function: str, **params: Any) -> Dict[str, Any]:
    api_key = os.getenv(API_KEY_ENV)
    if not api_key:
        return {"error": f"Missing environment variable {API_KEY_ENV}"}
    query = {"function": function, "apikey": api_key}
    query.update({k: v for k, v in params.items() if v is not None})
    try:
        resp = requests.get(BASE_URL, params=query, timeout=30)
        resp.raise_for_status()
        try:
            data = resp.json()
        except Exception:
            return {"error": "Alpha Vantage returned non-JSON response", "text": resp.text}
        if isinstance(data, dict) and ("Error Message" in data or "Note" in data or "Information" in data):
            return {"error": data.get("Error Message") or data.get("Note") or data.get("Information"), "raw": data}
        return data
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def time_series_intraday(ticker: str, time_interval: str, adjusted: bool = True, extended_hours: bool = True, month: str | None = None, output_size: str = "compact", entitlement: str | None = None) -> Dict[str, Any]:
    return _request("TIME_SERIES_INTRADAY", ticker=ticker, time_interval=time_interval, adjusted=str(adjusted).lower(), extended_hours=str(extended_hours).lower(), month=month, output_size=output_size, entitlement=entitlement)


@mcp.tool()
def time_series_daily(ticker: str, output_size: str = "compact") -> Dict[str, Any]:
    return _request("TIME_SERIES_DAILY", ticker=ticker, output_size=output_size)


@mcp.tool()
def quote_endpoint(ticker: str) -> Dict[str, Any]:
    return _request("GLOBAL_QUOTE", ticker=ticker)


@mcp.tool()
def symbol_search(keywords: str) -> Dict[str, Any]:
    return _request("SYMBOL_SEARCH", keywords=keywords)


@mcp.tool()
def currency_exchange_rate(from_currency: str, to_currency: str) -> Dict[str, Any]:
    return _request("CURRENCY_EXCHANGE_RATE", from_currency=from_currency, to_currency=to_currency)


@mcp.tool()
def fx_daily(from_symbol: str, to_symbol: str, output_size: str = "compact") -> Dict[str, Any]:
    return _request("FX_DAILY", from_symbol=from_symbol, to_symbol=to_symbol, output_size=output_size)


@mcp.tool()
def digital_currency_daily(ticker: str, market: str) -> Dict[str, Any]:
    return _request("DIGITAL_CURRENCY_DAILY", ticker=ticker, market=market)


@mcp.tool()
def sma(ticker: str, time_interval: str, time_period: int, price_type: str) -> Dict[str, Any]:
    return _request("SMA", ticker=ticker, time_interval=time_interval, time_period=time_period, price_type=price_type)


@mcp.tool()
def ema(ticker: str, time_interval: str, time_period: int, price_type: str) -> Dict[str, Any]:
    return _request("EMA", ticker=ticker, time_interval=time_interval, time_period=time_period, price_type=price_type)


@mcp.tool()
def rsi(ticker: str, time_interval: str, time_period: int, price_type: str) -> Dict[str, Any]:
    return _request("RSI", ticker=ticker, time_interval=time_interval, time_period=time_period, price_type=price_type)


@mcp.tool()
def macd(ticker: str, time_interval: str, series_type: str, fastperiod: int = 12, slowperiod: int = 26, signalperiod: int = 9) -> Dict[str, Any]:
    return _request("MACD", ticker=ticker, time_interval=time_interval, series_type=series_type, fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)


@mcp.tool()
def bbands(ticker: str, time_interval: str, time_period: int, series_type: str) -> Dict[str, Any]:
    return _request("BBANDS", ticker=ticker, time_interval=time_interval, time_period=time_period, series_type=series_type)


@mcp.tool()
def company_overview(ticker: str) -> Dict[str, Any]:
    return _request("OVERVIEW", ticker=ticker)


@mcp.tool()
def income_statement(ticker: str) -> Dict[str, Any]:
    return _request("INCOME_STATEMENT", ticker=ticker)


@mcp.tool()
def balance_sheet(ticker: str) -> Dict[str, Any]:
    return _request("BALANCE_SHEET", ticker=ticker)


@mcp.tool()
def earnings(ticker: str) -> Dict[str, Any]:
    return _request("EARNINGS", ticker=ticker)


@mcp.tool()
def cpi() -> Dict[str, Any]:
    return _request("CPI")


@mcp.tool()
def inflation() -> Dict[str, Any]:
    return _request("INFLATION")


@mcp.tool()
def gdp() -> Dict[str, Any]:
    return _request("REAL_GDP")


@mcp.tool()
def unemployment() -> Dict[str, Any]:
    return _request("UNEMPLOYMENT")


@mcp.tool()
def treasury_yield(interval: str) -> Dict[str, Any]:
    return _request("TREASURY_YIELD", interval=interval)


@mcp.tool()
def sector_performance() -> Dict[str, Any]:
    return _request("SECTOR")


if __name__ == "__main__":
    mcp.run()
