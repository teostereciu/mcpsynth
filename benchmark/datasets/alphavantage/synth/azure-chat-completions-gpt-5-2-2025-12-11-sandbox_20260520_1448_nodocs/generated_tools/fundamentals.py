from typing import Any, Dict

from .client import call_alpha_vantage


def company_overview(symbol: str) -> Dict[str, Any]:
    return call_alpha_vantage({"function": "OVERVIEW", "symbol": symbol})


def income_statement(symbol: str) -> Dict[str, Any]:
    return call_alpha_vantage({"function": "INCOME_STATEMENT", "symbol": symbol})


def balance_sheet(symbol: str) -> Dict[str, Any]:
    return call_alpha_vantage({"function": "BALANCE_SHEET", "symbol": symbol})


def earnings(symbol: str) -> Dict[str, Any]:
    return call_alpha_vantage({"function": "EARNINGS", "symbol": symbol})
