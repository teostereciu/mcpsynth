"""
Alpha Vantage — Fundamental Data tools
Covers: company overview, income statement, balance sheet, cash flow, earnings
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
        if "Information" in data:
            return {"error": data["Information"]}
        if "Note" in data:
            return {"error": data["Note"]}
        return data
    except requests.exceptions.RequestException as exc:
        return {"error": str(exc)}
    except ValueError as exc:
        return {"error": f"JSON decode error: {exc}"}


def get_company_overview(symbol: str) -> dict:
    """
    Fetch company overview and key financial metrics for a given equity.

    Returns a comprehensive snapshot including: description, sector, industry,
    market cap, P/E ratio, EPS, dividend yield, 52-week high/low, beta,
    analyst target price, and many more fundamental metrics.

    Args:
        symbol: Ticker symbol (e.g. 'IBM', 'AAPL').

    Returns:
        Dict with company profile and fundamental financial data.
    """
    return _get({
        "function": "OVERVIEW",
        "symbol": symbol,
    })


def get_income_statement(symbol: str) -> dict:
    """
    Fetch annual and quarterly income statements for a given equity.

    Includes revenue, gross profit, operating income, net income, EBITDA,
    EPS, and other income statement line items.

    Args:
        symbol: Ticker symbol (e.g. 'IBM').

    Returns:
        Dict with 'annualReports' and 'quarterlyReports' lists.
    """
    return _get({
        "function": "INCOME_STATEMENT",
        "symbol": symbol,
    })


def get_balance_sheet(symbol: str) -> dict:
    """
    Fetch annual and quarterly balance sheets for a given equity.

    Includes total assets, total liabilities, shareholder equity, cash,
    short/long-term debt, and other balance sheet line items.

    Args:
        symbol: Ticker symbol (e.g. 'IBM').

    Returns:
        Dict with 'annualReports' and 'quarterlyReports' lists.
    """
    return _get({
        "function": "BALANCE_SHEET",
        "symbol": symbol,
    })


def get_cash_flow(symbol: str) -> dict:
    """
    Fetch annual and quarterly cash flow statements for a given equity.

    Includes operating cash flow, capital expenditures, free cash flow,
    dividends paid, and other cash flow line items.

    Args:
        symbol: Ticker symbol (e.g. 'IBM').

    Returns:
        Dict with 'annualReports' and 'quarterlyReports' lists.
    """
    return _get({
        "function": "CASH_FLOW",
        "symbol": symbol,
    })


def get_earnings(symbol: str) -> dict:
    """
    Fetch annual and quarterly earnings (EPS) data for a given equity.

    Includes reported EPS, estimated EPS, surprise amount, and surprise
    percentage for each reporting period.

    Args:
        symbol: Ticker symbol (e.g. 'IBM').

    Returns:
        Dict with 'annualEarnings' and 'quarterlyEarnings' lists.
    """
    return _get({
        "function": "EARNINGS",
        "symbol": symbol,
    })


def get_earnings_calendar(symbol: str = "", horizon: str = "3month") -> dict:
    """
    Fetch upcoming earnings release dates for one or all equities.

    Args:
        symbol:  Optional ticker symbol to filter results (e.g. 'IBM').
                 Leave empty to get the full earnings calendar.
        horizon: Forecast horizon. Allowed: '3month', '6month', '12month'.

    Returns:
        CSV-formatted string (returned as-is) or dict with earnings dates,
        estimated EPS, and currency.
    """
    params: dict = {
        "function": "EARNINGS_CALENDAR",
        "horizon": horizon,
    }
    if symbol:
        params["symbol"] = symbol

    api_key = os.environ.get("ALPHAVANTAGE_API_KEY", "")
    params["apikey"] = api_key
    try:
        resp = requests.get(BASE_URL, params=params, timeout=15)
        resp.raise_for_status()
        # Earnings calendar returns CSV
        content_type = resp.headers.get("Content-Type", "")
        if "json" in content_type:
            data = resp.json()
            if "Error Message" in data:
                return {"error": data["Error Message"]}
            if "Information" in data:
                return {"error": data["Information"]}
            return data
        return {"csv": resp.text}
    except requests.exceptions.RequestException as exc:
        return {"error": str(exc)}


def get_ipo_calendar() -> dict:
    """
    Fetch upcoming IPO listings for the next 3 months.

    Returns:
        CSV-formatted string wrapped in a dict with key 'csv', containing
        symbol, name, IPO date, price range, currency, and exchange.
    """
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY", "")
    try:
        resp = requests.get(
            BASE_URL,
            params={"function": "IPO_CALENDAR", "apikey": api_key},
            timeout=15,
        )
        resp.raise_for_status()
        return {"csv": resp.text}
    except requests.exceptions.RequestException as exc:
        return {"error": str(exc)}


def get_listing_status(date: str = "", state: str = "active") -> dict:
    """
    Fetch a list of active or delisted US stocks and ETFs.

    Args:
        date:  Optional date in YYYY-MM-DD format to query historical listing status.
               Defaults to the latest trading day.
        state: 'active' for currently listed securities, 'delisted' for removed ones.

    Returns:
        Dict with key 'csv' containing the raw CSV data (symbol, name, exchange,
        assetType, ipoDate, delistingDate, status).
    """
    params: dict = {"function": "LISTING_STATUS", "state": state}
    if date:
        params["date"] = date
    params["apikey"] = os.environ.get("ALPHAVANTAGE_API_KEY", "")
    try:
        resp = requests.get(BASE_URL, params=params, timeout=15)
        resp.raise_for_status()
        return {"csv": resp.text}
    except requests.exceptions.RequestException as exc:
        return {"error": str(exc)}
