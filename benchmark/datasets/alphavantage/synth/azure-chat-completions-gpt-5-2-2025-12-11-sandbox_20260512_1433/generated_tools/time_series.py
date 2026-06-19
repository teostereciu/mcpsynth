from typing import Any, Dict, Optional

from .client import AlphaVantageClient


def time_series_intraday(
    symbol: str,
    interval: str,
    adjusted: Optional[bool] = None,
    extended_hours: Optional[bool] = None,
    month: Optional[str] = None,
    outputsize: Optional[str] = None,
    datatype: str = "json",
    entitlement: Optional[str] = None,
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Intraday OHLCV time series for an equity.

    function=TIME_SERIES_INTRADAY
    """
    c = client or AlphaVantageClient()
    params: Dict[str, Any] = {"function": "TIME_SERIES_INTRADAY", "symbol": symbol, "interval": interval, "datatype": datatype}
    if adjusted is not None:
        params["adjusted"] = "true" if adjusted else "false"
    if extended_hours is not None:
        params["extended_hours"] = "true" if extended_hours else "false"
    if month:
        params["month"] = month
    if outputsize:
        params["outputsize"] = outputsize
    if entitlement:
        params["entitlement"] = entitlement
    return c.request(params)


def time_series_daily(
    symbol: str,
    outputsize: Optional[str] = None,
    datatype: str = "json",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Raw daily OHLCV time series.

    function=TIME_SERIES_DAILY
    """
    c = client or AlphaVantageClient()
    params: Dict[str, Any] = {"function": "TIME_SERIES_DAILY", "symbol": symbol, "datatype": datatype}
    if outputsize:
        params["outputsize"] = outputsize
    return c.request(params)


def time_series_daily_adjusted(
    symbol: str,
    outputsize: Optional[str] = None,
    datatype: str = "json",
    entitlement: Optional[str] = None,
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Daily adjusted time series (adjusted close + splits/dividends).

    function=TIME_SERIES_DAILY_ADJUSTED
    """
    c = client or AlphaVantageClient()
    params: Dict[str, Any] = {"function": "TIME_SERIES_DAILY_ADJUSTED", "symbol": symbol, "datatype": datatype}
    if outputsize:
        params["outputsize"] = outputsize
    if entitlement:
        params["entitlement"] = entitlement
    return c.request(params)


def time_series_weekly(
    symbol: str,
    datatype: str = "json",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Weekly OHLCV time series.

    function=TIME_SERIES_WEEKLY
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "TIME_SERIES_WEEKLY", "symbol": symbol, "datatype": datatype})


def time_series_weekly_adjusted(
    symbol: str,
    datatype: str = "json",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Weekly adjusted time series.

    function=TIME_SERIES_WEEKLY_ADJUSTED
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "TIME_SERIES_WEEKLY_ADJUSTED", "symbol": symbol, "datatype": datatype})


def time_series_monthly(
    symbol: str,
    datatype: str = "json",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Monthly OHLCV time series.

    function=TIME_SERIES_MONTHLY
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "TIME_SERIES_MONTHLY", "symbol": symbol, "datatype": datatype})


def time_series_monthly_adjusted(
    symbol: str,
    datatype: str = "json",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Monthly adjusted time series.

    function=TIME_SERIES_MONTHLY_ADJUSTED
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "TIME_SERIES_MONTHLY_ADJUSTED", "symbol": symbol, "datatype": datatype})


def global_quote(
    symbol: str,
    datatype: str = "json",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Latest price/volume for a symbol.

    function=GLOBAL_QUOTE
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "GLOBAL_QUOTE", "symbol": symbol, "datatype": datatype})


def symbol_search(
    keywords: str,
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Search for symbols/tickers.

    function=SYMBOL_SEARCH
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "SYMBOL_SEARCH", "keywords": keywords})


def market_status(client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Market open/closure status.

    function=MARKET_STATUS
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "MARKET_STATUS"})
