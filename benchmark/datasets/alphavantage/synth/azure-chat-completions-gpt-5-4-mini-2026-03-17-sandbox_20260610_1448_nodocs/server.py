import json
import os
from typing import Any, Dict

import requests
from fastmcp import FastMCP

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
        data = resp.json()
        if isinstance(data, dict) and ("Error Message" in data or "Note" in data or "Information" in data):
            return {"error": data.get("Error Message") or data.get("Note") or data.get("Information")}
        return data
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_intraday(symbol: str, interval: str = "5min", outputsize: str = "compact", adjusted: bool = True, datatype: str = "json"):
    return _request("TIME_SERIES_INTRADAY", symbol=symbol, interval=interval, outputsize=outputsize, adjusted=str(adjusted).lower(), datatype=datatype)


@mcp.tool()
def get_daily(symbol: str, outputsize: str = "compact", datatype: str = "json"):
    return _request("TIME_SERIES_DAILY", symbol=symbol, outputsize=outputsize, datatype=datatype)


@mcp.tool()
def get_daily_adjusted(symbol: str, outputsize: str = "compact", datatype: str = "json"):
    return _request("TIME_SERIES_DAILY_ADJUSTED", symbol=symbol, outputsize=outputsize, datatype=datatype)


@mcp.tool()
def get_weekly(symbol: str, datatype: str = "json"):
    return _request("TIME_SERIES_WEEKLY", symbol=symbol, datatype=datatype)


@mcp.tool()
def get_weekly_adjusted(symbol: str, datatype: str = "json"):
    return _request("TIME_SERIES_WEEKLY_ADJUSTED", symbol=symbol, datatype=datatype)


@mcp.tool()
def get_monthly(symbol: str, datatype: str = "json"):
    return _request("TIME_SERIES_MONTHLY", symbol=symbol, datatype=datatype)


@mcp.tool()
def get_monthly_adjusted(symbol: str, datatype: str = "json"):
    return _request("TIME_SERIES_MONTHLY_ADJUSTED", symbol=symbol, datatype=datatype)


@mcp.tool()
def get_quote(symbol: str):
    return _request("GLOBAL_QUOTE", symbol=symbol)


@mcp.tool()
def search_symbols(keywords: str):
    return _request("SYMBOL_SEARCH", keywords=keywords)


@mcp.tool()
def get_fx_rate(from_currency: str, to_currency: str):
    return _request("CURRENCY_EXCHANGE_RATE", from_currency=from_currency, to_currency=to_currency)


@mcp.tool()
def get_fx_daily(from_symbol: str, to_symbol: str, outputsize: str = "compact", datatype: str = "json"):
    return _request("FX_DAILY", from_symbol=from_symbol, to_symbol=to_symbol, outputsize=outputsize, datatype=datatype)


@mcp.tool()
def get_fx_weekly(from_symbol: str, to_symbol: str, datatype: str = "json"):
    return _request("FX_WEEKLY", from_symbol=from_symbol, to_symbol=to_symbol, datatype=datatype)


@mcp.tool()
def get_fx_monthly(from_symbol: str, to_symbol: str, datatype: str = "json"):
    return _request("FX_MONTHLY", from_symbol=from_symbol, to_symbol=to_symbol, datatype=datatype)


@mcp.tool()
def get_crypto_rate(from_currency: str, to_currency: str):
    return _request("CURRENCY_EXCHANGE_RATE", from_currency=from_currency, to_currency=to_currency)


@mcp.tool()
def get_crypto_daily(symbol: str, market: str = "USD", outputsize: str = "compact", datatype: str = "json"):
    return _request("DIGITAL_CURRENCY_DAILY", symbol=symbol, market=market, outputsize=outputsize, datatype=datatype)


@mcp.tool()
def get_crypto_weekly(symbol: str, market: str = "USD", datatype: str = "json"):
    return _request("DIGITAL_CURRENCY_WEEKLY", symbol=symbol, market=market, datatype=datatype)


@mcp.tool()
def get_crypto_monthly(symbol: str, market: str = "USD", datatype: str = "json"):
    return _request("DIGITAL_CURRENCY_MONTHLY", symbol=symbol, market=market, datatype=datatype)


@mcp.tool()
def get_sma(symbol: str, interval: str, time_period: int, series_type: str, datatype: str = "json"):
    return _request("SMA", symbol=symbol, interval=interval, time_period=time_period, series_type=series_type, datatype=datatype)


@mcp.tool()
def get_ema(symbol: str, interval: str, time_period: int, series_type: str, datatype: str = "json"):
    return _request("EMA", symbol=symbol, interval=interval, time_period=time_period, series_type=series_type, datatype=datatype)


@mcp.tool()
def get_rsi(symbol: str, interval: str, time_period: int, series_type: str, datatype: str = "json"):
    return _request("RSI", symbol=symbol, interval=interval, time_period=time_period, series_type=series_type, datatype=datatype)


@mcp.tool()
def get_macd(symbol: str, interval: str, series_type: str, fastperiod: int = 12, slowperiod: int = 26, signalperiod: int = 9, datatype: str = "json"):
    return _request("MACD", symbol=symbol, interval=interval, series_type=series_type, fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod, datatype=datatype)


@mcp.tool()
def get_bbands(symbol: str, interval: str, time_period: int, series_type: str, nbdevup: int = 2, nbdevdn: int = 2, matype: int = 0, datatype: str = "json"):
    return _request("BBANDS", symbol=symbol, interval=interval, time_period=time_period, series_type=series_type, nbdevup=nbdevup, nbdevdn=nbdevdn, matype=matype, datatype=datatype)


@mcp.tool()
def get_company_overview(symbol: str):
    return _request("OVERVIEW", symbol=symbol)


@mcp.tool()
def get_income_statement(symbol: str):
    return _request("INCOME_STATEMENT", symbol=symbol)


@mcp.tool()
def get_balance_sheet(symbol: str):
    return _request("BALANCE_SHEET", symbol=symbol)


@mcp.tool()
def get_earnings(symbol: str):
    return _request("EARNINGS", symbol=symbol)


@mcp.tool()
def get_cpi(interval: str = "monthly"):
    return _request("CPI", interval=interval)


@mcp.tool()
def get_inflation():
    return _request("INFLATION")


@mcp.tool()
def get_gdp(interval: str = "quarterly"):
    return _request("REAL_GDP", interval=interval)


@mcp.tool()
def get_unemployment():
    return _request("UNEMPLOYMENT")


@mcp.tool()
def get_treasury_yield(interval: str = "monthly", maturity: str = "10year"):
    return _request("TREASURY_YIELD", interval=interval, maturity=maturity)


@mcp.tool()
def get_sector_performance():
    return _request("SECTOR")


if __name__ == "__main__":
    mcp.run()
