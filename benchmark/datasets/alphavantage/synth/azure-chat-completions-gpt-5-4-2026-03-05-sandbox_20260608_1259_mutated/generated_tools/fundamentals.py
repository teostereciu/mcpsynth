from typing import Optional

from generated_tools.common import call_alpha_vantage


def get_company_overview(ticker: str):
    return call_alpha_vantage({"function": "OVERVIEW", "ticker": ticker})


def get_etf_profile(ticker: str):
    return call_alpha_vantage({"function": "ETF_PROFILE", "ticker": ticker})


def get_dividends(ticker: str):
    return call_alpha_vantage({"function": "DIVIDENDS", "ticker": ticker})


def get_splits(ticker: str):
    return call_alpha_vantage({"function": "SPLITS", "ticker": ticker})


def get_income_statement(ticker: str):
    return call_alpha_vantage({"function": "INCOME_STATEMENT", "ticker": ticker})


def get_balance_sheet(ticker: str):
    return call_alpha_vantage({"function": "BALANCE_SHEET", "ticker": ticker})


def get_cash_flow(ticker: str):
    return call_alpha_vantage({"function": "CASH_FLOW", "ticker": ticker})


def get_earnings(ticker: str):
    return call_alpha_vantage({"function": "EARNINGS", "ticker": ticker})


def get_earnings_estimates(ticker: str):
    return call_alpha_vantage({"function": "EARNINGS_ESTIMATES", "ticker": ticker})


def get_earnings_calendar(ticker: Optional[str] = None, horizon: Optional[str] = None):
    return call_alpha_vantage(
        {"function": "EARNINGS_CALENDAR", "ticker": ticker, "horizon": horizon}
    )


def get_listing_status(date: Optional[str] = None, state: Optional[str] = None):
    return call_alpha_vantage({"function": "LISTING_STATUS", "date": date, "state": state})


def get_ipo_calendar():
    return call_alpha_vantage({"function": "IPO_CALENDAR"})
