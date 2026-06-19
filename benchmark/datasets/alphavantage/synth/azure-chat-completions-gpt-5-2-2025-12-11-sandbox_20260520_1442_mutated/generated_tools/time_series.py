from typing import Any, Dict, Optional

from .alphavantage_client import call_alpha_vantage


def stock_time_series_intraday(
    ticker: str,
    time_interval: str,
    adjusted: Optional[bool] = True,
    extended_hours: Optional[bool] = True,
    month: Optional[str] = None,
    output_size: Optional[str] = "compact",
    entitlement: Optional[str] = None,
    format: Optional[str] = "json",
) -> Dict[str, Any]:
    """TIME_SERIES_INTRADAY.

    Doc: docs/api_time_series_data.md
    """
    params: Dict[str, Any] = {
        "function": "TIME_SERIES_INTRADAY",
        "ticker": ticker,
        "time_interval": time_interval,
    }
    if adjusted is not None:
        params["adjusted"] = "true" if adjusted else "false"
    if extended_hours is not None:
        params["extended_hours"] = "true" if extended_hours else "false"
    if month:
        params["month"] = month
    if output_size:
        params["output_size"] = output_size
    if entitlement:
        params["entitlement"] = entitlement
    if format:
        params["format"] = format
    return call_alpha_vantage(params)


def stock_time_series_daily(
    ticker: str,
    output_size: Optional[str] = "compact",
    format: Optional[str] = "json",
) -> Dict[str, Any]:
    """TIME_SERIES_DAILY.

    Doc: docs/api_time_series_data.md
    """
    params: Dict[str, Any] = {"function": "TIME_SERIES_DAILY", "ticker": ticker}
    if output_size:
        params["output_size"] = output_size
    if format:
        params["format"] = format
    return call_alpha_vantage(params)


def stock_time_series_daily_adjusted(
    ticker: str,
    output_size: Optional[str] = "compact",
    format: Optional[str] = "json",
    entitlement: Optional[str] = None,
) -> Dict[str, Any]:
    """TIME_SERIES_DAILY_ADJUSTED.

    Doc: docs/api_time_series_data.md
    """
    params: Dict[str, Any] = {"function": "TIME_SERIES_DAILY_ADJUSTED", "ticker": ticker}
    if output_size:
        params["output_size"] = output_size
    if format:
        params["format"] = format
    if entitlement:
        params["entitlement"] = entitlement
    return call_alpha_vantage(params)


def stock_time_series_weekly(
    ticker: str,
    format: Optional[str] = "json",
) -> Dict[str, Any]:
    """TIME_SERIES_WEEKLY.

    Doc: docs/api_time_series_data.md
    """
    params: Dict[str, Any] = {"function": "TIME_SERIES_WEEKLY", "ticker": ticker}
    if format:
        params["format"] = format
    return call_alpha_vantage(params)


def stock_time_series_weekly_adjusted(
    ticker: str,
    format: Optional[str] = "json",
) -> Dict[str, Any]:
    """TIME_SERIES_WEEKLY_ADJUSTED.

    Doc: docs/api_time_series_data.md
    """
    params: Dict[str, Any] = {"function": "TIME_SERIES_WEEKLY_ADJUSTED", "ticker": ticker}
    if format:
        params["format"] = format
    return call_alpha_vantage(params)


def stock_time_series_monthly(
    ticker: str,
    format: Optional[str] = "json",
) -> Dict[str, Any]:
    """TIME_SERIES_MONTHLY.

    Doc: docs/api_time_series_data.md
    """
    params: Dict[str, Any] = {"function": "TIME_SERIES_MONTHLY", "ticker": ticker}
    if format:
        params["format"] = format
    return call_alpha_vantage(params)


def stock_time_series_monthly_adjusted(
    ticker: str,
    format: Optional[str] = "json",
) -> Dict[str, Any]:
    """TIME_SERIES_MONTHLY_ADJUSTED.

    Doc: docs/api_time_series_data.md
    """
    params: Dict[str, Any] = {"function": "TIME_SERIES_MONTHLY_ADJUSTED", "ticker": ticker}
    if format:
        params["format"] = format
    return call_alpha_vantage(params)


def stock_quote(ticker: str) -> Dict[str, Any]:
    """GLOBAL_QUOTE.

    Doc: docs/api_time_series_data.md
    """
    return call_alpha_vantage({"function": "GLOBAL_QUOTE", "ticker": ticker})


def symbol_search(keywords: str) -> Dict[str, Any]:
    """SYMBOL_SEARCH.

    Doc: docs/api_time_series_data.md
    """
    return call_alpha_vantage({"function": "SYMBOL_SEARCH", "keywords": keywords})


def market_status() -> Dict[str, Any]:
    """MARKET_STATUS.

    Doc: docs/api_time_series_data.md
    """
    return call_alpha_vantage({"function": "MARKET_STATUS"})


def realtime_bulk_quotes(ticker: str) -> Dict[str, Any]:
    """REALTIME_BULK_QUOTES.

    Doc: docs/api_time_series_data.md
    """
    return call_alpha_vantage({"function": "REALTIME_BULK_QUOTES", "ticker": ticker})
