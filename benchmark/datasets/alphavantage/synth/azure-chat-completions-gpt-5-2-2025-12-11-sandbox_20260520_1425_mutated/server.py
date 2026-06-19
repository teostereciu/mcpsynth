import os
import json
import asyncio
from typing import Any, Dict, Optional

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

BASE_URL = "https://www.alphavantage.co/query"
DEFAULT_TIMEOUT_S = float(os.getenv("ALPHAVANTAGE_TIMEOUT", "30"))

mcp = FastMCP("alphavantage")


def _get_api_key(explicit: Optional[str] = None) -> str:
    key = explicit or os.getenv("ALPHAVANTAGE_API_KEY") or os.getenv("ALPHA_VANTAGE_API_KEY")
    if not key:
        raise ValueError(
            "Missing API key. Provide `apikey` argument or set ALPHAVANTAGE_API_KEY (or ALPHA_VANTAGE_API_KEY)."
        )
    return key


async def _av_query(params: Dict[str, Any], apikey: Optional[str] = None) -> Dict[str, Any]:
    params = {k: v for k, v in params.items() if v is not None}
    params["apikey"] = _get_api_key(apikey)

    timeout = httpx.Timeout(DEFAULT_TIMEOUT_S)
    async with httpx.AsyncClient(timeout=timeout) as client:
        r = await client.get(BASE_URL, params=params)
        r.raise_for_status()

        ctype = r.headers.get("content-type", "")
        if "application/json" in ctype or "text/json" in ctype or r.text.strip().startswith("{"):
            data = r.json()
        else:
            # CSV or other text
            data = {"raw": r.text, "content_type": ctype}

    # Alpha Vantage error conventions
    if isinstance(data, dict):
        if "Error Message" in data:
            raise ValueError(data["Error Message"])
        if "Information" in data and "Note" not in data:
            # often premium / parameter issues
            raise ValueError(data["Information"])
        if "Note" in data:
            # rate limit
            raise RuntimeError(data["Note"])

    return data


@mcp.tool()
async def alphavantage_query(function: str, params: Optional[Dict[str, Any]] = None, apikey: Optional[str] = None) -> Dict[str, Any]:
    """Generic Alpha Vantage query tool.

    This server provides comprehensive coverage via this generic tool: pass the Alpha Vantage `function` name
    and any additional query parameters.

    Args:
      function: Alpha Vantage function name, e.g. TIME_SERIES_DAILY, SMA, NEWS_SENTIMENT, OVERVIEW.
      params: Additional query parameters (excluding apikey). Example: {"ticker": "IBM", "time_interval": "weekly"}
      apikey: Optional API key override.

    Returns:
      Parsed JSON response, or {raw, content_type} for CSV/text responses.
    """
    q = dict(params or {})
    q["function"] = function
    return await _av_query(q, apikey=apikey)


# Convenience wrappers for common workflows across domains

@mcp.tool()
async def stock_time_series(
    function: str,
    ticker: str,
    interval: Optional[str] = None,
    output_size: Optional[str] = None,
    adjusted: Optional[bool] = None,
    month: Optional[str] = None,
    entitlement: Optional[str] = None,
    datatype: Optional[str] = None,
    apikey: Optional[str] = None,
) -> Dict[str, Any]:
    """Stock time series wrapper.

    Supports common parameters used by TIME_SERIES_* endpoints.

    Args:
      function: e.g. TIME_SERIES_INTRADAY, TIME_SERIES_DAILY, TIME_SERIES_WEEKLY, TIME_SERIES_MONTHLY,
                TIME_SERIES_DAILY_ADJUSTED, TIME_SERIES_WEEKLY_ADJUSTED, TIME_SERIES_MONTHLY_ADJUSTED.
      ticker: Equity ticker symbol.
      interval: Intraday interval (e.g. 1min, 5min, 15min, 30min, 60min) when applicable.
      output_size: compact|full when applicable.
      adjusted: Some endpoints accept adjusted=true/false.
      month: YYYY-MM for intraday extended / some indicator-like endpoints.
      entitlement: realtime|delayed (premium) or omit for historical.
      datatype: json|csv (some endpoints use datatype or format; we pass through as datatype).
      apikey: Optional API key override.
    """
    params: Dict[str, Any] = {"function": function, "ticker": ticker}
    if interval is not None:
        params["interval"] = interval
        params["time_interval"] = interval  # some docs use time_interval
    if output_size is not None:
        params["output_size"] = output_size
    if adjusted is not None:
        params["adjusted"] = str(adjusted).lower()
    if month is not None:
        params["month"] = month
    if entitlement is not None:
        params["entitlement"] = entitlement
    if datatype is not None:
        params["datatype"] = datatype
        params["format"] = datatype
    return await _av_query(params, apikey=apikey)


@mcp.tool()
async def technical_indicator(
    function: str,
    ticker: str,
    time_interval: str,
    time_period: Optional[int] = None,
    price_type: Optional[str] = None,
    series_type: Optional[str] = None,
    month: Optional[str] = None,
    fastperiod: Optional[int] = None,
    slowperiod: Optional[int] = None,
    signalperiod: Optional[int] = None,
    nbdevup: Optional[int] = None,
    nbdevdn: Optional[int] = None,
    matype: Optional[int] = None,
    acceleration: Optional[float] = None,
    maximum: Optional[float] = None,
    format: Optional[str] = None,
    entitlement: Optional[str] = None,
    apikey: Optional[str] = None,
) -> Dict[str, Any]:
    """Technical indicator wrapper.

    Many indicators share a common parameter set. Provide what you have; unused params are ignored.

    Docs examples: SMA/EMA/WMA require time_period and price_type; others may use series_type.
    """
    params: Dict[str, Any] = {
        "function": function,
        "ticker": ticker,
        "time_interval": time_interval,
    }
    if month is not None:
        params["month"] = month
    if time_period is not None:
        params["time_period"] = time_period
    if price_type is not None:
        params["price_type"] = price_type
    if series_type is not None:
        params["series_type"] = series_type

    # common optional knobs
    if fastperiod is not None:
        params["fastperiod"] = fastperiod
    if slowperiod is not None:
        params["slowperiod"] = slowperiod
    if signalperiod is not None:
        params["signalperiod"] = signalperiod
    if nbdevup is not None:
        params["nbdevup"] = nbdevup
    if nbdevdn is not None:
        params["nbdevdn"] = nbdevdn
    if matype is not None:
        params["matype"] = matype
    if acceleration is not None:
        params["acceleration"] = acceleration
    if maximum is not None:
        params["maximum"] = maximum

    if format is not None:
        params["format"] = format
        params["datatype"] = format
    if entitlement is not None:
        params["entitlement"] = entitlement

    return await _av_query(params, apikey=apikey)


@mcp.tool()
async def fx_exchange_rate(from_currency: str, to_currency: str, apikey: Optional[str] = None) -> Dict[str, Any]:
    """Realtime FX exchange rate (CURRENCY_EXCHANGE_RATE)."""
    return await _av_query(
        {"function": "CURRENCY_EXCHANGE_RATE", "from_currency": from_currency, "to_currency": to_currency},
        apikey=apikey,
    )


@mcp.tool()
async def crypto_exchange_rate(from_currency: str, to_currency: str, apikey: Optional[str] = None) -> Dict[str, Any]:
    """Realtime crypto/physical exchange rate (CURRENCY_EXCHANGE_RATE)."""
    return await fx_exchange_rate(from_currency=from_currency, to_currency=to_currency, apikey=apikey)


@mcp.tool()
async def fundamentals(function: str, ticker: str, format: Optional[str] = None, apikey: Optional[str] = None) -> Dict[str, Any]:
    """Fundamental data wrapper.

    Examples: OVERVIEW, ETF_PROFILE, DIVIDENDS, SPLITS, INCOME_STATEMENT, BALANCE_SHEET, CASH_FLOW, EARNINGS.
    """
    params: Dict[str, Any] = {"function": function, "ticker": ticker}
    if format is not None:
        params["format"] = format
    return await _av_query(params, apikey=apikey)


@mcp.tool()
async def news_sentiment(
    tickers: Optional[str] = None,
    topics: Optional[str] = None,
    time_from: Optional[str] = None,
    time_to: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    apikey: Optional[str] = None,
) -> Dict[str, Any]:
    """Market News & Sentiment (NEWS_SENTIMENT)."""
    params: Dict[str, Any] = {
        "function": "NEWS_SENTIMENT",
        "tickers": tickers,
        "topics": topics,
        "time_from": time_from,
        "time_to": time_to,
        "sort": sort,
        "limit": limit,
    }
    return await _av_query(params, apikey=apikey)


@mcp.tool()
async def economic_indicator(function: str, params: Optional[Dict[str, Any]] = None, apikey: Optional[str] = None) -> Dict[str, Any]:
    """Economic indicators wrapper.

    Examples: REAL_GDP, TREASURY_YIELD, FEDERAL_FUNDS_RATE, CPI, INFLATION, UNEMPLOYMENT, RETAIL_SALES, etc.
    Pass any documented parameters via `params` (e.g., time_interval, maturity, interval, format).
    """
    q = dict(params or {})
    q["function"] = function
    return await _av_query(q, apikey=apikey)


@mcp.tool()
async def commodities(function: str, params: Optional[Dict[str, Any]] = None, apikey: Optional[str] = None) -> Dict[str, Any]:
    """Commodities wrapper.

    Examples: GOLD_SILVER_SPOT, GOLD_SILVER_HISTORY, WTI, BRENT, NATURAL_GAS, COPPER, WHEAT, CORN, etc.
    """
    q = dict(params or {})
    q["function"] = function
    return await _av_query(q, apikey=apikey)


@mcp.tool()
async def options_data(function: str, ticker: str, params: Optional[Dict[str, Any]] = None, apikey: Optional[str] = None) -> Dict[str, Any]:
    """Options data wrapper.

    Examples: REALTIME_OPTIONS, HISTORICAL_OPTIONS, REALTIME_PUT_CALL_RATIO, REALTIME_VOLUME_OPEN_INTEREST_RATIO.
    """
    q = dict(params or {})
    q["function"] = function
    q["ticker"] = ticker
    return await _av_query(q, apikey=apikey)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
