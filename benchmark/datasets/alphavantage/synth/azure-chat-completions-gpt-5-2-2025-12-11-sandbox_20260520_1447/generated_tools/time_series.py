from typing import Any, Dict, Optional, Union

from .client import av_get


def stock_time_series_intraday(
    symbol: str,
    interval: str,
    adjusted: Optional[bool] = True,
    extended_hours: Optional[bool] = True,
    month: Optional[str] = None,
    outputsize: Optional[str] = None,
    datatype: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Union[Dict[str, Any], str]:
    """TIME_SERIES_INTRADAY.

    Doc: docs/api_time_series_data.md
    Endpoint: GET /query?function=TIME_SERIES_INTRADAY
    """
    params: Dict[str, Any] = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
    }
    if adjusted is not None:
        params["adjusted"] = "true" if adjusted else "false"
    if extended_hours is not None:
        params["extended_hours"] = "true" if extended_hours else "false"
    if month:
        params["month"] = month
    if outputsize:
        params["outputsize"] = outputsize
    if datatype:
        params["datatype"] = datatype
    if entitlement:
        params["entitlement"] = entitlement
    return av_get(params)


def stock_time_series_daily(
    symbol: str,
    outputsize: Optional[str] = None,
    datatype: Optional[str] = None,
) -> Union[Dict[str, Any], str]:
    """TIME_SERIES_DAILY.

    Doc: docs/api_time_series_data.md
    Endpoint: GET /query?function=TIME_SERIES_DAILY
    """
    params: Dict[str, Any] = {"function": "TIME_SERIES_DAILY", "symbol": symbol}
    if outputsize:
        params["outputsize"] = outputsize
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def stock_time_series_daily_adjusted(
    symbol: str,
    outputsize: Optional[str] = None,
    datatype: Optional[str] = None,
    entitlement: Optional[str] = None,
) -> Union[Dict[str, Any], str]:
    """TIME_SERIES_DAILY_ADJUSTED.

    Doc: docs/api_time_series_data.md
    Endpoint: GET /query?function=TIME_SERIES_DAILY_ADJUSTED
    """
    params: Dict[str, Any] = {"function": "TIME_SERIES_DAILY_ADJUSTED", "symbol": symbol}
    if outputsize:
        params["outputsize"] = outputsize
    if datatype:
        params["datatype"] = datatype
    if entitlement:
        params["entitlement"] = entitlement
    return av_get(params)


def stock_time_series_weekly(symbol: str, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """TIME_SERIES_WEEKLY.

    Doc: docs/api_time_series_data.md
    Endpoint: GET /query?function=TIME_SERIES_WEEKLY
    """
    params: Dict[str, Any] = {"function": "TIME_SERIES_WEEKLY", "symbol": symbol}
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def stock_time_series_weekly_adjusted(
    symbol: str, datatype: Optional[str] = None
) -> Union[Dict[str, Any], str]:
    """TIME_SERIES_WEEKLY_ADJUSTED.

    Doc: docs/api_time_series_data.md
    Endpoint: GET /query?function=TIME_SERIES_WEEKLY_ADJUSTED
    """
    params: Dict[str, Any] = {"function": "TIME_SERIES_WEEKLY_ADJUSTED", "symbol": symbol}
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def stock_time_series_monthly(symbol: str, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """TIME_SERIES_MONTHLY.

    Doc: docs/api_time_series_data.md
    Endpoint: GET /query?function=TIME_SERIES_MONTHLY
    """
    params: Dict[str, Any] = {"function": "TIME_SERIES_MONTHLY", "symbol": symbol}
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def stock_time_series_monthly_adjusted(
    symbol: str, datatype: Optional[str] = None
) -> Union[Dict[str, Any], str]:
    """TIME_SERIES_MONTHLY_ADJUSTED.

    Doc: docs/api_time_series_data.md
    Endpoint: GET /query?function=TIME_SERIES_MONTHLY_ADJUSTED
    """
    params: Dict[str, Any] = {"function": "TIME_SERIES_MONTHLY_ADJUSTED", "symbol": symbol}
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def stock_quote(symbol: str, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """GLOBAL_QUOTE.

    Doc: docs/api_time_series_data.md
    Endpoint: GET /query?function=GLOBAL_QUOTE
    """
    params: Dict[str, Any] = {"function": "GLOBAL_QUOTE", "symbol": symbol}
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def symbol_search(keywords: str) -> Dict[str, Any]:
    """SYMBOL_SEARCH.

    Doc: docs/api_time_series_data.md
    Endpoint: GET /query?function=SYMBOL_SEARCH
    """
    return av_get({"function": "SYMBOL_SEARCH", "keywords": keywords})  # type: ignore[return-value]


def market_status() -> Dict[str, Any]:
    """MARKET_STATUS.

    Doc: docs/api_time_series_data.md
    Endpoint: GET /query?function=MARKET_STATUS
    """
    return av_get({"function": "MARKET_STATUS"})  # type: ignore[return-value]
