from .common import alpha_vantage_get


def get_company_overview(symbol: str):
    return alpha_vantage_get({"function": "OVERVIEW", "symbol": symbol})


def get_income_statement(symbol: str):
    return alpha_vantage_get({"function": "INCOME_STATEMENT", "symbol": symbol})


def get_balance_sheet(symbol: str):
    return alpha_vantage_get({"function": "BALANCE_SHEET", "symbol": symbol})


def get_earnings(symbol: str):
    return alpha_vantage_get({"function": "EARNINGS", "symbol": symbol})
