from typing import Any, Dict, Optional

from .client import call_alpha_vantage


def stock_time_series_intraday(
    symbol: str,
    interval: str,
    adjusted: Optional[bool] = None,
    extended_hours: Optional[bool] = None,
    month: Optional[str] = None,
    outputsize: Optional[str] = None,
    datatype: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
    }
    if adjusted is not None:
        params["adjusted"] = "true" if adjusted else "false"
    if extended_hours is not None:
        params["extended_hours"] = "true" if extended_hours else "false"
    if month is not None:
        params["month"] = month
    if outputsize is not None:
        params["outputsize"] = outputsize
    if datatype is not None:
        params["datatype"] = datatype
    if entitlement is not None:
        params["entitlement"] = entitlement
    return call_alpha_vantage(params)


def stock_time_series_daily(
    symbol: str,
    outputsize: Optional[str] = None,
    datatype: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "TIME_SERIES_DAILY", "symbol": symbol}
    if outputsize is not None:
        params["outputsize"] = outputsize
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def stock_time_series_daily_adjusted(
    symbol: str,
    outputsize: Optional[str] = None,
    datatype: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "TIME_SERIES_DAILY_ADJUSTED", "symbol": symbol}
    if outputsize is not None:
        params["outputsize"] = outputsize
    if datatype is not None:
        params["datatype"] = datatype
    if entitlement is not None:
        params["entitlement"] = entitlement
    return call_alpha_vantage(params)


def stock_time_series_weekly(
    symbol: str,
    datatype: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "TIME_SERIES_WEEKLY", "symbol": symbol}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def stock_time_series_weekly_adjusted(
    symbol: str,
    datatype: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "TIME_SERIES_WEEKLY_ADJUSTED", "symbol": symbol}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def stock_time_series_monthly(
    symbol: str,
    datatype: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "TIME_SERIES_MONTHLY", "symbol": symbol}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def stock_time_series_monthly_adjusted(
    symbol: str,
    datatype: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "TIME_SERIES_MONTHLY_ADJUSTED", "symbol": symbol}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def stock_quote(symbol: str, datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "GLOBAL_QUOTE", "symbol": symbol}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def symbol_search(keywords: str) -> Dict[str, Any]:
    return call_alpha_vantage({"function": "SYMBOL_SEARCH", "keywords": keywords})


def market_status() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "MARKET_STATUS"})


def sector_performance() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "SECTOR"})
