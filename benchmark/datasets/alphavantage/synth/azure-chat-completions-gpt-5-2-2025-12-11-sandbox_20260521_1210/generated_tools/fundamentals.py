from typing import Any, Dict, Optional

from .client import call_alpha_vantage


def company_overview(symbol: str) -> Dict[str, Any]:
    return call_alpha_vantage({"function": "OVERVIEW", "symbol": symbol})


def etf_profile(symbol: str) -> Dict[str, Any]:
    return call_alpha_vantage({"function": "ETF_PROFILE", "symbol": symbol})


def dividends(symbol: str, datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "DIVIDENDS", "symbol": symbol}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def splits(symbol: str, datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "SPLITS", "symbol": symbol}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def income_statement(symbol: str) -> Dict[str, Any]:
    return call_alpha_vantage({"function": "INCOME_STATEMENT", "symbol": symbol})


def balance_sheet(symbol: str) -> Dict[str, Any]:
    return call_alpha_vantage({"function": "BALANCE_SHEET", "symbol": symbol})


def cash_flow(symbol: str) -> Dict[str, Any]:
    return call_alpha_vantage({"function": "CASH_FLOW", "symbol": symbol})


def earnings(symbol: str) -> Dict[str, Any]:
    return call_alpha_vantage({"function": "EARNINGS", "symbol": symbol})


def earnings_estimates(symbol: str) -> Dict[str, Any]:
    return call_alpha_vantage({"function": "EARNINGS_ESTIMATES", "symbol": symbol})


def earnings_calendar(horizon: str = "3month", symbol: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "EARNINGS_CALENDAR", "horizon": horizon}
    if symbol is not None:
        params["symbol"] = symbol
    return call_alpha_vantage(params)
