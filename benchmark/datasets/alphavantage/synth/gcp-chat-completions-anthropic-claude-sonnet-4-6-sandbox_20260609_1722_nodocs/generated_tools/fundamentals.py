"""
Alpha Vantage – Fundamental Data tools
Covers: company overview, income statement, balance sheet, cash flow, earnings,
        earnings calendar, IPO calendar, listing status
"""

import os
import requests

BASE_URL = "https://www.alphavantage.co/query"


def _get(params: dict) -> dict:
    params["apikey"] = os.environ.get("ALPHAVANTAGE_API_KEY", "")
    try:
        resp = requests.get(BASE_URL, params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        if "Error Message" in data:
            return {"error": data["Error Message"]}
        if "Note" in data:
            return {"error": "API rate limit reached", "note": data["Note"]}
        if "Information" in data:
            return {"error": "API limit / info", "information": data["Information"]}
        return data
    except requests.RequestException as exc:
        return {"error": str(exc)}


def get_company_overview(symbol: str) -> dict:
    """
    Return company overview including description, sector, market cap, P/E ratio,
    dividend yield, 52-week high/low, and many other fundamental metrics.

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return _get({"function": "OVERVIEW", "symbol": symbol})


def get_income_statement(symbol: str) -> dict:
    """
    Return annual and quarterly income statements for *symbol*.

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return _get({"function": "INCOME_STATEMENT", "symbol": symbol})


def get_balance_sheet(symbol: str) -> dict:
    """
    Return annual and quarterly balance sheets for *symbol*.

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return _get({"function": "BALANCE_SHEET", "symbol": symbol})


def get_cash_flow(symbol: str) -> dict:
    """
    Return annual and quarterly cash flow statements for *symbol*.

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return _get({"function": "CASH_FLOW", "symbol": symbol})


def get_earnings(symbol: str) -> dict:
    """
    Return annual and quarterly earnings (EPS) data for *symbol*.

    :param symbol: Ticker symbol, e.g. "IBM".
    """
    return _get({"function": "EARNINGS", "symbol": symbol})


def get_earnings_calendar(
    symbol: str = "",
    horizon: str = "3month",
) -> dict:
    """
    Return a list of company earnings expected in the next 3, 6, or 12 months.

    :param symbol: Optional ticker to filter results, e.g. "IBM". Leave empty for all.
    :param horizon: Forecast horizon: "3month" | "6month" | "12month".
    """
    params: dict = {"function": "EARNINGS_CALENDAR", "horizon": horizon}
    if symbol:
        params["symbol"] = symbol
    return _get(params)


def get_ipo_calendar() -> dict:
    """
    Return a list of IPOs expected in the next three months.
    """
    return _get({"function": "IPO_CALENDAR"})


def get_listing_status(
    date: str = "",
    state: str = "active",
) -> dict:
    """
    Return a list of active or delisted US stocks and ETFs.

    :param date: Optional date in YYYY-MM-DD format to query historical listing status.
    :param state: "active" or "delisted".
    """
    params: dict = {"function": "LISTING_STATUS", "state": state}
    if date:
        params["date"] = date
    return _get(params)
