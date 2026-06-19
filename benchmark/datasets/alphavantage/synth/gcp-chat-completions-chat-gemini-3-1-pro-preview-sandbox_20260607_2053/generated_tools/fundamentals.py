from .time_series import make_request

def get_company_overview(symbol: str) -> dict:
    """Get company overview fundamental data."""
    return make_request({
        "function": "OVERVIEW",
        "symbol": symbol
    })

def get_income_statement(symbol: str) -> dict:
    """Get company income statement."""
    return make_request({
        "function": "INCOME_STATEMENT",
        "symbol": symbol
    })

def get_balance_sheet(symbol: str) -> dict:
    """Get company balance sheet."""
    return make_request({
        "function": "BALANCE_SHEET",
        "symbol": symbol
    })

def get_earnings(symbol: str) -> dict:
    """Get company earnings."""
    return make_request({
        "function": "EARNINGS",
        "symbol": symbol
    })
