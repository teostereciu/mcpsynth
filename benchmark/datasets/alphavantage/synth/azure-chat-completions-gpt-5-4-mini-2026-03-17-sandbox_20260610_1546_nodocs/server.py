import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://www.alphavantage.co/query"
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", "")

mcp = FastMCP("alpha-vantage")


def _request(function: str, **params: Any) -> Dict[str, Any]:
    if not API_KEY:
        return {"error": "Missing ALPHAVANTAGE_API_KEY environment variable"}
    query = {"function": function, "apikey": API_KEY}
    query.update({k: v for k, v in params.items() if v is not None})
    try:
        resp = requests.get(BASE_URL, params=query, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, dict) and ("Error Message" in data or "Note" in data or "Information" in data):
            return {"error": data.get("Error Message") or data.get("Note") or data.get("Information")}
        return data
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_global_quote(symbol: str) -> Dict[str, Any]:
    return _request("GLOBAL_QUOTE", symbol=symbol)


@mcp.tool()
def search_symbol(keywords: str) -> Dict[str, Any]:
    return _request("SYMBOL_SEARCH", keywords=keywords)


@mcp.tool()
def get_intraday_time_series(symbol: str, interval: str = "5min", outputsize: str = "compact") -> Dict[str, Any]:
    return _request("TIME_SERIES_INTRADAY", symbol=symbol, interval=interval, outputsize=outputsize)


@mcp.tool()
def get_daily_time_series(symbol: str, outputsize: str = "compact") -> Dict[str, Any]:
    return _request("TIME_SERIES_DAILY", symbol=symbol, outputsize=outputsize)


@mcp.tool()
def get_weekly_time_series(symbol: str) -> Dict[str, Any]:
    return _request("TIME_SERIES_WEEKLY", symbol=symbol)


@mcp.tool()
def get_monthly_time_series(symbol: str) -> Dict[str, Any]:
    return _request("TIME_SERIES_MONTHLY", symbol=symbol)


@mcp.tool()
def get_fx_exchange_rate(from_currency: str, to_currency: str) -> Dict[str, Any]:
    return _request("CURRENCY_EXCHANGE_RATE", from_currency=from_currency, to_currency=to_currency)


@mcp.tool()
def get_fx_daily(from_symbol: str, to_symbol: str, outputsize: str = "compact") -> Dict[str, Any]:
    return _request("FX_DAILY", from_symbol=from_symbol, to_symbol=to_symbol, outputsize=outputsize)


@mcp.tool()
def get_fx_weekly(from_symbol: str, to_symbol: str) -> Dict[str, Any]:
    return _request("FX_WEEKLY", from_symbol=from_symbol, to_symbol=to_symbol)


@mcp.tool()
def get_fx_monthly(from_symbol: str, to_symbol: str) -> Dict[str, Any]:
    return _request("FX_MONTHLY", from_symbol=from_symbol, to_symbol=to_symbol)


@mcp.tool()
def get_crypto_exchange_rate(from_currency: str, to_currency: str) -> Dict[str, Any]:
    return _request("CURRENCY_EXCHANGE_RATE", from_currency=from_currency, to_currency=to_currency)


@mcp.tool()
def get_crypto_daily(symbol: str, market: str = "USD") -> Dict[str, Any]:
    return _request("DIGITAL_CURRENCY_DAILY", symbol=symbol, market=market)


@mcp.tool()
def get_crypto_weekly(symbol: str, market: str = "USD") -> Dict[str, Any]:
    return _request("DIGITAL_CURRENCY_WEEKLY", symbol=symbol, market=market)


@mcp.tool()
def get_crypto_monthly(symbol: str, market: str = "USD") -> Dict[str, Any]:
    return _request("DIGITAL_CURRENCY_MONTHLY", symbol=symbol, market=market)


@mcp.tool()
def get_sma(symbol: str, interval: str, time_period: int, series_type: str = "close") -> Dict[str, Any]:
    return _request("SMA", symbol=symbol, interval=interval, time_period=time_period, series_type=series_type)


@mcp.tool()
def get_ema(symbol: str, interval: str, time_period: int, series_type: str = "close") -> Dict[str, Any]:
    return _request("EMA", symbol=symbol, interval=interval, time_period=time_period, series_type=series_type)


@mcp.tool()
def get_rsi(symbol: str, interval: str, time_period: int, series_type: str = "close") -> Dict[str, Any]:
    return _request("RSI", symbol=symbol, interval=interval, time_period=time_period, series_type=series_type)


@mcp.tool()
def get_macd(symbol: str, interval: str, series_type: str = "close", fastperiod: int = 12, slowperiod: int = 26, signalperiod: int = 9) -> Dict[str, Any]:
    return _request("MACD", symbol=symbol, interval=interval, series_type=series_type, fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)


@mcp.tool()
def get_bbands(symbol: str, interval: str, time_period: int, series_type: str = "close") -> Dict[str, Any]:
    return _request("BBANDS", symbol=symbol, interval=interval, time_period=time_period, series_type=series_type)


@mcp.tool()
def get_company_overview(symbol: str) -> Dict[str, Any]:
    return _request("OVERVIEW", symbol=symbol)


@mcp.tool()
def get_income_statement(symbol: str) -> Dict[str, Any]:
    return _request("INCOME_STATEMENT", symbol=symbol)


@mcp.tool()
def get_balance_sheet(symbol: str) -> Dict[str, Any]:
    return _request("BALANCE_SHEET", symbol=symbol)


@mcp.tool()
def get_earnings(symbol: str) -> Dict[str, Any]:
    return _request("EARNINGS", symbol=symbol)


@mcp.tool()
def get_cpi() -> Dict[str, Any]:
    return _request("CPI")


@mcp.tool()
def get_inflation() -> Dict[str, Any]:
    return _request("INFLATION")


@mcp.tool()
def get_gdp() -> Dict[str, Any]:
    return _request("GDP")


@mcp.tool()
def get_unemployment() -> Dict[str, Any]:
    return _request("UNEMPLOYMENT")


@mcp.tool()
def get_treasury_yield(interval: str = "monthly") -> Dict[str, Any]:
    return _request("TREASURY_YIELD", interval=interval)


@mcp.tool()
def get_sector_performance() -> Dict[str, Any]:
    return _request("SECTOR")


if __name__ == "__main__":
    mcp.run(transport="stdio")
