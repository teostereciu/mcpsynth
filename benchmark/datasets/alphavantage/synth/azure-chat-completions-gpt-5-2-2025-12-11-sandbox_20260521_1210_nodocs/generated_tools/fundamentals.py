from typing import Any, Dict

from .client import av_get


def company_overview(symbol: str) -> Dict[str, Any]:
    return av_get({"function": "OVERVIEW", "symbol": symbol})


def income_statement(symbol: str) -> Dict[str, Any]:
    return av_get({"function": "INCOME_STATEMENT", "symbol": symbol})


def balance_sheet(symbol: str) -> Dict[str, Any]:
    return av_get({"function": "BALANCE_SHEET", "symbol": symbol})


def earnings(symbol: str) -> Dict[str, Any]:
    return av_get({"function": "EARNINGS", "symbol": symbol})
