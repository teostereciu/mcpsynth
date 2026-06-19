from typing import Optional

from generated_tools.common import call_alpha_vantage


def get_stock_intraday(
    ticker: str,
    time_interval: str,
    adjusted: Optional[bool] = None,
    extended_hours: Optional[bool] = None,
    month: Optional[str] = None,
    output_size: Optional[str] = None,
    entitlement: Optional[str] = None,
):
    return call_alpha_vantage(
        {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": ticker,
            "interval": time_interval,
            "adjusted": str(adjusted).lower() if adjusted is not None else None,
            "extended_hours": str(extended_hours).lower() if extended_hours is not None else None,
            "month": month,
            "outputsize": output_size,
            "entitlement": entitlement,
        }
    )


def get_stock_daily(ticker: str, output_size: Optional[str] = None):
    return call_alpha_vantage(
        {
            "function": "TIME_SERIES_DAILY",
            "symbol": ticker,
            "outputsize": output_size,
        }
    )


def get_stock_daily_adjusted(
    ticker: str, output_size: Optional[str] = None, entitlement: Optional[str] = None
):
    return call_alpha_vantage(
        {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": ticker,
            "outputsize": output_size,
            "entitlement": entitlement,
        }
    )


def get_stock_weekly(ticker: str):
    return call_alpha_vantage({"function": "TIME_SERIES_WEEKLY", "symbol": ticker})


def get_stock_weekly_adjusted(ticker: str):
    return call_alpha_vantage({"function": "TIME_SERIES_WEEKLY_ADJUSTED", "symbol": ticker})


def get_stock_monthly(ticker: str):
    return call_alpha_vantage({"function": "TIME_SERIES_MONTHLY", "symbol": ticker})


def get_stock_monthly_adjusted(ticker: str):
    return call_alpha_vantage({"function": "TIME_SERIES_MONTHLY_ADJUSTED", "symbol": ticker})


def get_global_quote(ticker: str):
    return call_alpha_vantage({"function": "GLOBAL_QUOTE", "symbol": ticker})


def search_symbols(keywords: str):
    return call_alpha_vantage({"function": "SYMBOL_SEARCH", "keywords": keywords})
