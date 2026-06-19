from typing import Any, Dict, Optional

from .client import av_get


def company_overview(ticker: str) -> Dict[str, Any]:
    return av_get({"function": "OVERVIEW", "symbol": ticker})


def etf_profile(ticker: str) -> Dict[str, Any]:
    return av_get({"function": "ETF_PROFILE", "symbol": ticker})


def dividends(ticker: str, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "DIVIDENDS", "symbol": ticker}
    if format:
        params["datatype"] = format
    return av_get(params)


def splits(ticker: str, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "SPLITS", "symbol": ticker}
    if format:
        params["datatype"] = format
    return av_get(params)


def income_statement(ticker: str) -> Dict[str, Any]:
    return av_get({"function": "INCOME_STATEMENT", "symbol": ticker})


def balance_sheet(ticker: str) -> Dict[str, Any]:
    return av_get({"function": "BALANCE_SHEET", "symbol": ticker})


def cash_flow(ticker: str) -> Dict[str, Any]:
    return av_get({"function": "CASH_FLOW", "symbol": ticker})


def earnings(ticker: str) -> Dict[str, Any]:
    return av_get({"function": "EARNINGS", "symbol": ticker})
