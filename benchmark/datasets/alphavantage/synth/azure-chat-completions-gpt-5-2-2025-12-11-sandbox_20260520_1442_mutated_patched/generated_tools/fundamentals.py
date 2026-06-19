from typing import Any, Dict, Optional

from .alphavantage_client import call_alpha_vantage


def company_overview(ticker: str) -> Dict[str, Any]:
    """OVERVIEW.

    Doc: docs/api_fundamentals.md
    """
    return call_alpha_vantage({"function": "OVERVIEW", "symbol": ticker})


def etf_profile(ticker: str) -> Dict[str, Any]:
    """ETF_PROFILE.

    Doc: docs/api_fundamentals.md
    """
    return call_alpha_vantage({"function": "ETF_PROFILE", "symbol": ticker})


def dividends(ticker: str, format: Optional[str] = "json") -> Dict[str, Any]:
    """DIVIDENDS.

    Doc: docs/api_fundamentals.md
    """
    params: Dict[str, Any] = {"function": "DIVIDENDS", "symbol": ticker}
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def splits(ticker: str, format: Optional[str] = "json") -> Dict[str, Any]:
    """SPLITS.

    Doc: docs/api_fundamentals.md
    """
    params: Dict[str, Any] = {"function": "SPLITS", "symbol": ticker}
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def income_statement(ticker: str) -> Dict[str, Any]:
    """INCOME_STATEMENT.

    Doc: docs/api_fundamentals.md
    """
    return call_alpha_vantage({"function": "INCOME_STATEMENT", "symbol": ticker})


def balance_sheet(ticker: str) -> Dict[str, Any]:
    """BALANCE_SHEET.

    Doc: docs/api_fundamentals.md
    """
    return call_alpha_vantage({"function": "BALANCE_SHEET", "symbol": ticker})


def cash_flow(ticker: str) -> Dict[str, Any]:
    """CASH_FLOW.

    Doc: docs/api_fundamentals.md
    """
    return call_alpha_vantage({"function": "CASH_FLOW", "symbol": ticker})


def earnings(ticker: str) -> Dict[str, Any]:
    """EARNINGS.

    Doc: docs/api_fundamentals.md
    """
    return call_alpha_vantage({"function": "EARNINGS", "symbol": ticker})
