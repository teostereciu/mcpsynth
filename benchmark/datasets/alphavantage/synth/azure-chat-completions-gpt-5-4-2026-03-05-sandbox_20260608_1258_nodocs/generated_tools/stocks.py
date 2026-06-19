from typing import Optional

from .common import alpha_vantage_get


def get_global_quote(symbol: str):
    return alpha_vantage_get({"function": "GLOBAL_QUOTE", "symbol": symbol})


def search_symbols(keywords: str):
    return alpha_vantage_get({"function": "SYMBOL_SEARCH", "keywords": keywords})


def get_intraday_time_series(symbol: str, interval: str = "5min", adjusted: bool = True, extended_hours: bool = True, month: Optional[str] = None, outputsize: str = "compact"):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "adjusted": str(adjusted).lower(),
        "extended_hours": str(extended_hours).lower(),
        "outputsize": outputsize,
    }
    if month:
        params["month"] = month
    return alpha_vantage_get(params)


def get_daily_time_series(symbol: str, outputsize: str = "compact"):
    return alpha_vantage_get({"function": "TIME_SERIES_DAILY", "symbol": symbol, "outputsize": outputsize})


def get_daily_adjusted_time_series(symbol: str, outputsize: str = "compact"):
    return alpha_vantage_get({"function": "TIME_SERIES_DAILY_ADJUSTED", "symbol": symbol, "outputsize": outputsize})


def get_weekly_time_series(symbol: str):
    return alpha_vantage_get({"function": "TIME_SERIES_WEEKLY", "symbol": symbol})


def get_weekly_adjusted_time_series(symbol: str):
    return alpha_vantage_get({"function": "TIME_SERIES_WEEKLY_ADJUSTED", "symbol": symbol})


def get_monthly_time_series(symbol: str):
    return alpha_vantage_get({"function": "TIME_SERIES_MONTHLY", "symbol": symbol})


def get_monthly_adjusted_time_series(symbol: str):
    return alpha_vantage_get({"function": "TIME_SERIES_MONTHLY_ADJUSTED", "symbol": symbol})
