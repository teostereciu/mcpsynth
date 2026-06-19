import json
import os
from typing import Any, Dict
from urllib.parse import urlencode

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://www.alphavantage.co/query"
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

mcp = FastMCP("alpha-vantage")


def _request(params: Dict[str, Any]) -> Dict[str, Any]:
    if not API_KEY:
        return {"error": "Missing ALPHAVANTAGE_API_KEY environment variable"}
    query = dict(params)
    query["apikey"] = API_KEY
    try:
        resp = requests.get(BASE_URL, params=query, timeout=30)
        resp.raise_for_status()
        try:
            return resp.json()
        except Exception:
            return {"data": resp.text}
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def time_series_daily(ticker: str, output_size: str = "compact", format: str = "json"):
    return _request({"function": "TIME_SERIES_DAILY", "ticker": ticker, "output_size": output_size, "format": format})


@mcp.tool()
def time_series_intraday(ticker: str, time_interval: str, output_size: str = "compact", adjusted: bool = True, extended_hours: bool = True, month: str | None = None, format: str = "json"):
    params: Dict[str, Any] = {"function": "TIME_SERIES_INTRADAY", "ticker": ticker, "time_interval": time_interval, "output_size": output_size, "adjusted": str(adjusted).lower(), "extended_hours": str(extended_hours).lower(), "format": format}
    if month:
        params["month"] = month
    return _request(params)


@mcp.tool()
def quote(symbol: str):
    return _request({"function": "GLOBAL_QUOTE", "symbol": symbol})


@mcp.tool()
def symbol_search(keywords: str):
    return _request({"function": "SYMBOL_SEARCH", "keywords": keywords})


@mcp.tool()
def fx_exchange_rate(from_currency: str, to_currency: str):
    return _request({"function": "CURRENCY_EXCHANGE_RATE", "from_currency": from_currency, "to_currency": to_currency})


@mcp.tool()
def company_overview(ticker: str):
    return _request({"function": "OVERVIEW", "ticker": ticker})


@mcp.tool()
def income_statement(ticker: str):
    return _request({"function": "INCOME_STATEMENT", "ticker": ticker})


@mcp.tool()
def balance_sheet(ticker: str):
    return _request({"function": "BALANCE_SHEET", "ticker": ticker})


@mcp.tool()
def earnings(ticker: str):
    return _request({"function": "EARNINGS", "ticker": ticker})


@mcp.tool()
def cpi():
    return _request({"function": "CPI"})


@mcp.tool()
def unemployment():
    return _request({"function": "UNEMPLOYMENT"})


@mcp.tool()
def treasury_yield(time_interval: str = "monthly", maturity: str = "10year"):
    return _request({"function": "TREASURY_YIELD", "time_interval": time_interval, "maturity": maturity})


@mcp.tool()
def sector_performance():
    return _request({"function": "SECTOR"})


if __name__ == "__main__":
    mcp.run()
