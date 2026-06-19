from typing import Optional

from generated_tools.common import alpha_vantage_get, build_result


def get_stock_intraday(symbol: str, interval: str, adjusted: Optional[bool] = None, extended_hours: Optional[bool] = None, month: Optional[str] = None, outputsize: Optional[str] = None, entitlement: Optional[str] = None):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "adjusted": str(adjusted).lower() if adjusted is not None else None,
        "extended_hours": str(extended_hours).lower() if extended_hours is not None else None,
        "month": month,
        "outputsize": outputsize,
        "entitlement": entitlement,
    }
    return build_result("get_stock_intraday", params, alpha_vantage_get(params))


def get_stock_daily(symbol: str, outputsize: Optional[str] = None):
    params = {"function": "TIME_SERIES_DAILY", "symbol": symbol, "outputsize": outputsize}
    return build_result("get_stock_daily", params, alpha_vantage_get(params))


def get_stock_weekly(symbol: str):
    params = {"function": "TIME_SERIES_WEEKLY", "symbol": symbol}
    return build_result("get_stock_weekly", params, alpha_vantage_get(params))


def get_stock_monthly(symbol: str):
    params = {"function": "TIME_SERIES_MONTHLY", "symbol": symbol}
    return build_result("get_stock_monthly", params, alpha_vantage_get(params))


def get_global_quote(symbol: str):
    params = {"function": "GLOBAL_QUOTE", "symbol": symbol}
    return build_result("get_global_quote", params, alpha_vantage_get(params))


def search_symbols(keywords: str):
    params = {"function": "SYMBOL_SEARCH", "keywords": keywords}
    return build_result("search_symbols", params, alpha_vantage_get(params))
