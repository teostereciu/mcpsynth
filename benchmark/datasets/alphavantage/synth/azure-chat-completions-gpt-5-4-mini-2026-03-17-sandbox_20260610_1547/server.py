import os
from typing import Any, Dict
from urllib.parse import urlencode

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://www.alphavantage.co/query"
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", "")

mcp = FastMCP("alpha-vantage")


def _request(params: Dict[str, Any]) -> Dict[str, Any]:
    if not API_KEY:
        return {"error": "Missing ALPHAVANTAGE_API_KEY environment variable"}
    query = dict(params)
    query["apikey"] = API_KEY
    try:
        resp = requests.get(BASE_URL, params=query, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, dict) and any(k.lower() == "error message" for k in data):
            return {"error": data}
        return data
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def time_series_daily(symbol: str, outputsize: str = "compact"):
    return _request({"function": "TIME_SERIES_DAILY", "symbol": symbol, "outputsize": outputsize})


@mcp.tool()
def time_series_weekly(symbol: str):
    return _request({"function": "TIME_SERIES_WEEKLY", "symbol": symbol})


@mcp.tool()
def time_series_monthly(symbol: str):
    return _request({"function": "TIME_SERIES_MONTHLY", "symbol": symbol})


@mcp.tool()
def quote(symbol: str):
    return _request({"function": "GLOBAL_QUOTE", "symbol": symbol})


@mcp.tool()
def symbol_search(keywords: str):
    return _request({"function": "SYMBOL_SEARCH", "keywords": keywords})


@mcp.tool()
def currency_exchange_rate(from_currency: str, to_currency: str):
    return _request({"function": "CURRENCY_EXCHANGE_RATE", "from_currency": from_currency, "to_currency": to_currency})


@mcp.tool()
def fx_daily(from_symbol: str, to_symbol: str, outputsize: str = "compact"):
    return _request({"function": "FX_DAILY", "from_symbol": from_symbol, "to_symbol": to_symbol, "outputsize": outputsize})


@mcp.tool()
def crypto_exchange_rate(symbol: str, market: str):
    return _request({"function": "CURRENCY_EXCHANGE_RATE", "from_currency": symbol, "to_currency": market})


@mcp.tool()
def crypto_intraday(symbol: str, market: str, interval: str, outputsize: str = "compact"):
    return _request({"function": "CRYPTO_INTRADAY", "symbol": symbol, "market": market, "interval": interval, "outputsize": outputsize})


@mcp.tool()
def sma(symbol: str, interval: str, time_period: int, series_type: str):
    return _request({"function": "SMA", "symbol": symbol, "interval": interval, "time_period": time_period, "series_type": series_type})


@mcp.tool()
def ema(symbol: str, interval: str, time_period: int, series_type: str):
    return _request({"function": "EMA", "symbol": symbol, "interval": interval, "time_period": time_period, "series_type": series_type})


@mcp.tool()
def rsi(symbol: str, interval: str, time_period: int, series_type: str):
    return _request({"function": "RSI", "symbol": symbol, "interval": interval, "time_period": time_period, "series_type": series_type})


@mcp.tool()
def macd(symbol: str, interval: str, series_type: str, fastperiod: int = 12, slowperiod: int = 26, signalperiod: int = 9):
    return _request({"function": "MACD", "symbol": symbol, "interval": interval, "series_type": series_type, "fastperiod": fastperiod, "slowperiod": slowperiod, "signalperiod": signalperiod})


@mcp.tool()
def bollinger_bands(symbol: str, interval: str, time_period: int, series_type: str):
    return _request({"function": "BBANDS", "symbol": symbol, "interval": interval, "time_period": time_period, "series_type": series_type})


@mcp.tool()
def company_overview(symbol: str):
    return _request({"function": "OVERVIEW", "symbol": symbol})


@mcp.tool()
def income_statement(symbol: str):
    return _request({"function": "INCOME_STATEMENT", "symbol": symbol})


@mcp.tool()
def balance_sheet(symbol: str):
    return _request({"function": "BALANCE_SHEET", "symbol": symbol})


@mcp.tool()
def earnings(symbol: str):
    return _request({"function": "EARNINGS", "symbol": symbol})


@mcp.tool()
def real_gdp(interval: str = "annual"):
    return _request({"function": "REAL_GDP", "interval": interval})


@mcp.tool()
def cpi(interval: str = "monthly"):
    return _request({"function": "CPI", "interval": interval})


@mcp.tool()
def inflation():
    return _request({"function": "INFLATION"})


@mcp.tool()
def unemployment():
    return _request({"function": "UNEMPLOYMENT"})


@mcp.tool()
def treasury_yield(interval: str = "monthly", maturity: str = "10year"):
    return _request({"function": "TREASURY_YIELD", "interval": interval, "maturity": maturity})


@mcp.tool()
def sector_performance():
    return _request({"function": "SECTOR"})


if __name__ == "__main__":
    mcp.run(transport="stdio")
