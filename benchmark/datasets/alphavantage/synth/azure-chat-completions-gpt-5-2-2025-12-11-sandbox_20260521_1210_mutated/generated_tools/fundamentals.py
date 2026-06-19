from typing import Any, Dict, Optional

from .client import av_get


def company_overview(ticker: str) -> Dict[str, Any]:
    return av_get({"function": "OVERVIEW", "ticker": ticker})


def etf_profile(ticker: str) -> Dict[str, Any]:
    return av_get({"function": "ETF_PROFILE", "ticker": ticker})


def dividends(ticker: str, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "DIVIDENDS", "ticker": ticker}
    if format:
        params["format"] = format
    return av_get(params)


def splits(ticker: str, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "SPLITS", "ticker": ticker}
    if format:
        params["format"] = format
    return av_get(params)


def income_statement(ticker: str) -> Dict[str, Any]:
    return av_get({"function": "INCOME_STATEMENT", "ticker": ticker})


def balance_sheet(ticker: str) -> Dict[str, Any]:
    return av_get({"function": "BALANCE_SHEET", "ticker": ticker})


def cash_flow(ticker: str) -> Dict[str, Any]:
    return av_get({"function": "CASH_FLOW", "ticker": ticker})


def earnings(ticker: str) -> Dict[str, Any]:
    return av_get({"function": "EARNINGS", "ticker": ticker})
