from typing import Any, Dict, Optional

from .client import av_get


def stock_time_series_intraday(
    ticker: str,
    time_interval: str,
    adjusted: Optional[bool] = True,
    extended_hours: Optional[bool] = True,
    month: Optional[str] = None,
    output_size: Optional[str] = None,
    format: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": ticker,
        "interval": time_interval,
    }
    if adjusted is not None:
        params["adjusted"] = "true" if adjusted else "false"
    if extended_hours is not None:
        params["extended_hours"] = "true" if extended_hours else "false"
    if month:
        params["month"] = month
    if output_size:
        params["outputsize"] = output_size
    if format:
        params["datatype"] = format
    if entitlement:
        params["entitlement"] = entitlement
    return av_get(params)


def stock_time_series_daily(
    ticker: str,
    output_size: Optional[str] = None,
    format: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "TIME_SERIES_DAILY", "symbol": ticker}
    if output_size:
        params["outputsize"] = output_size
    if format:
        params["datatype"] = format
    return av_get(params)


def stock_time_series_daily_adjusted(
    ticker: str,
    output_size: Optional[str] = None,
    format: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "TIME_SERIES_DAILY_ADJUSTED", "symbol": ticker}
    if output_size:
        params["outputsize"] = output_size
    if format:
        params["datatype"] = format
    if entitlement:
        params["entitlement"] = entitlement
    return av_get(params)


def stock_time_series_weekly(
    ticker: str,
    format: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "TIME_SERIES_WEEKLY", "symbol": ticker}
    if format:
        params["datatype"] = format
    return av_get(params)


def stock_time_series_weekly_adjusted(
    ticker: str,
    format: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "TIME_SERIES_WEEKLY_ADJUSTED", "symbol": ticker}
    if format:
        params["datatype"] = format
    return av_get(params)


def stock_time_series_monthly(
    ticker: str,
    format: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "TIME_SERIES_MONTHLY", "symbol": ticker}
    if format:
        params["datatype"] = format
    return av_get(params)


def stock_time_series_monthly_adjusted(
    ticker: str,
    format: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "TIME_SERIES_MONTHLY_ADJUSTED", "symbol": ticker}
    if format:
        params["datatype"] = format
    return av_get(params)


def stock_quote(ticker: str) -> Dict[str, Any]:
    return av_get({"function": "GLOBAL_QUOTE", "symbol": ticker})


def symbol_search(keywords: str) -> Dict[str, Any]:
    return av_get({"function": "SYMBOL_SEARCH", "keywords": keywords})


def market_status() -> Dict[str, Any]:
    return av_get({"function": "MARKET_STATUS"})
