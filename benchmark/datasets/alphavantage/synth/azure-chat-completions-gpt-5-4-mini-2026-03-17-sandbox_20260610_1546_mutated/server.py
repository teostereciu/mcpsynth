import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://www.alphavantage.co/query"
API_KEY_ENV = "ALPHAVANTAGE_API_KEY"

mcp = FastMCP("alpha-vantage")


def _call_alpha_vantage(params: Dict[str, Any]) -> Dict[str, Any]:
    api_key = os.getenv(API_KEY_ENV)
    if not api_key:
        return {"error": f"Missing environment variable {API_KEY_ENV}"}

    query = dict(params)
    query["apikey"] = api_key
    try:
        resp = requests.get(BASE_URL, params=query, timeout=30)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as exc:
        return {"error": str(exc)}
    except ValueError:
        return {"error": "Alpha Vantage returned non-JSON response"}

    if isinstance(data, dict) and ("Error Message" in data or "Note" in data or "Information" in data):
        return {"error": data.get("Error Message") or data.get("Note") or data.get("Information")}
    return data


@mcp.tool()
def time_series_intraday(ticker: str, time_interval: str, adjusted: bool = True, extended_hours: bool = True, month: str | None = None, output_size: str = "compact", format: str = "json", entitlement: str | None = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "TIME_SERIES_INTRADAY", "ticker": ticker, "time_interval": time_interval, "adjusted": str(adjusted).lower(), "extended_hours": str(extended_hours).lower(), "output_size": output_size, "format": format}
    if month is not None:
        params["month"] = month
    if entitlement is not None:
        params["entitlement"] = entitlement
    return _call_alpha_vantage(params)


@mcp.tool()
def time_series_daily(ticker: str, output_size: str = "compact", format: str = "json") -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "TIME_SERIES_DAILY", "ticker": ticker, "output_size": output_size, "format": format})


@mcp.tool()
def time_series_weekly(ticker: str, format: str = "json") -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "TIME_SERIES_WEEKLY", "ticker": ticker, "format": format})


@mcp.tool()
def time_series_monthly(ticker: str, format: str = "json") -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "TIME_SERIES_MONTHLY", "ticker": ticker, "format": format})


@mcp.tool()
def global_quote(symbol: str) -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "GLOBAL_QUOTE", "symbol": symbol})


@mcp.tool()
def symbol_search(keywords: str) -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "SYMBOL_SEARCH", "keywords": keywords})


@mcp.tool()
def currency_exchange_rate(from_currency: str, to_currency: str) -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "CURRENCY_EXCHANGE_RATE", "from_currency": from_currency, "to_currency": to_currency})


@mcp.tool()
def fx_daily(from_symbol: str, to_symbol: str, output_size: str = "compact", format: str = "json") -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "FX_DAILY", "from_symbol": from_symbol, "to_symbol": to_symbol, "output_size": output_size, "format": format})


@mcp.tool()
def digital_currency_daily(ticker: str, market: str, format: str = "json") -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "DIGITAL_CURRENCY_DAILY", "ticker": ticker, "market": market, "format": format})


@mcp.tool()
def sma(ticker: str, time_interval: str, time_period: int, price_type: str, month: str | None = None, format: str = "json", entitlement: str | None = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "SMA", "ticker": ticker, "time_interval": time_interval, "time_period": time_period, "price_type": price_type, "format": format}
    if month is not None:
        params["month"] = month
    if entitlement is not None:
        params["entitlement"] = entitlement
    return _call_alpha_vantage(params)


@mcp.tool()
def ema(ticker: str, time_interval: str, time_period: int, price_type: str, month: str | None = None, format: str = "json", entitlement: str | None = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "EMA", "ticker": ticker, "time_interval": time_interval, "time_period": time_period, "price_type": price_type, "format": format}
    if month is not None:
        params["month"] = month
    if entitlement is not None:
        params["entitlement"] = entitlement
    return _call_alpha_vantage(params)


@mcp.tool()
def rsi(ticker: str, time_interval: str, time_period: int, price_type: str, month: str | None = None, format: str = "json", entitlement: str | None = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "RSI", "ticker": ticker, "time_interval": time_interval, "time_period": time_period, "price_type": price_type, "format": format}
    if month is not None:
        params["month"] = month
    if entitlement is not None:
        params["entitlement"] = entitlement
    return _call_alpha_vantage(params)


@mcp.tool()
def macd(ticker: str, time_interval: str, series_type: str, fastperiod: int = 12, slowperiod: int = 26, signalperiod: int = 9, month: str | None = None, format: str = "json", entitlement: str | None = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "MACD", "ticker": ticker, "time_interval": time_interval, "series_type": series_type, "fastperiod": fastperiod, "slowperiod": slowperiod, "signalperiod": signalperiod, "format": format}
    if month is not None:
        params["month"] = month
    if entitlement is not None:
        params["entitlement"] = entitlement
    return _call_alpha_vantage(params)


@mcp.tool()
def bollinger_bands(ticker: str, time_interval: str, time_period: int, series_type: str, nbdevup: int = 2, nbdevdn: int = 2, month: str | None = None, format: str = "json", entitlement: str | None = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "BBANDS", "ticker": ticker, "time_interval": time_interval, "time_period": time_period, "series_type": series_type, "nbdevup": nbdevup, "nbdevdn": nbdevdn, "format": format}
    if month is not None:
        params["month"] = month
    if entitlement is not None:
        params["entitlement"] = entitlement
    return _call_alpha_vantage(params)


@mcp.tool()
def company_overview(ticker: str) -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "OVERVIEW", "ticker": ticker})


@mcp.tool()
def income_statement(ticker: str) -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "INCOME_STATEMENT", "ticker": ticker})


@mcp.tool()
def balance_sheet(ticker: str) -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "BALANCE_SHEET", "ticker": ticker})


@mcp.tool()
def earnings(ticker: str) -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "EARNINGS", "ticker": ticker})


@mcp.tool()
def real_gdp(time_interval: str = "annual", format: str = "json") -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "REAL_GDP", "time_interval": time_interval, "format": format})


@mcp.tool()
def real_gdp_per_capita(format: str = "json") -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "REAL_GDP_PER_CAPITA", "format": format})


@mcp.tool()
def treasury_yield(time_interval: str = "monthly", maturity: str = "10year", format: str = "json") -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "TREASURY_YIELD", "time_interval": time_interval, "maturity": maturity, "format": format})


@mcp.tool()
def federal_funds_rate(time_interval: str = "monthly", format: str = "json") -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "FEDERAL_FUNDS_RATE", "time_interval": time_interval, "format": format})


@mcp.tool()
def cpi(time_interval: str = "monthly", format: str = "json") -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "CPI", "time_interval": time_interval, "format": format})


@mcp.tool()
def inflation(time_interval: str = "monthly", format: str = "json") -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "INFLATION", "time_interval": time_interval, "format": format})


@mcp.tool()
def unemployment(time_interval: str = "monthly", format: str = "json") -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "UNEMPLOYMENT", "time_interval": time_interval, "format": format})


@mcp.tool()
def sector_performance() -> Dict[str, Any]:
    return _call_alpha_vantage({"function": "SECTOR"})


if __name__ == "__main__":
    mcp.run(transport="stdio")
