from typing import Optional

from generated_tools.common import alpha_vantage_get, build_result


def get_company_overview(symbol: str):
    params = {"function": "OVERVIEW", "symbol": symbol}
    return build_result("get_company_overview", params, alpha_vantage_get(params))


def get_etf_profile(symbol: str):
    params = {"function": "ETF_PROFILE", "symbol": symbol}
    return build_result("get_etf_profile", params, alpha_vantage_get(params))


def get_dividends(symbol: str):
    params = {"function": "DIVIDENDS", "symbol": symbol}
    return build_result("get_dividends", params, alpha_vantage_get(params))


def get_splits(symbol: str):
    params = {"function": "SPLITS", "symbol": symbol}
    return build_result("get_splits", params, alpha_vantage_get(params))


def get_income_statement(symbol: str):
    params = {"function": "INCOME_STATEMENT", "symbol": symbol}
    return build_result("get_income_statement", params, alpha_vantage_get(params))


def get_balance_sheet(symbol: str):
    params = {"function": "BALANCE_SHEET", "symbol": symbol}
    return build_result("get_balance_sheet", params, alpha_vantage_get(params))


def get_cash_flow(symbol: str):
    params = {"function": "CASH_FLOW", "symbol": symbol}
    return build_result("get_cash_flow", params, alpha_vantage_get(params))


def get_earnings(symbol: str):
    params = {"function": "EARNINGS", "symbol": symbol}
    return build_result("get_earnings", params, alpha_vantage_get(params))


def get_earnings_estimates(symbol: str):
    params = {"function": "EARNINGS_ESTIMATES", "symbol": symbol}
    return build_result("get_earnings_estimates", params, alpha_vantage_get(params))


def get_earnings_calendar(symbol: Optional[str] = None, horizon: Optional[str] = None):
    params = {"function": "EARNINGS_CALENDAR", "symbol": symbol, "horizon": horizon}
    return build_result("get_earnings_calendar", params, alpha_vantage_get(params))
