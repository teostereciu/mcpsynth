from typing import Any, Dict, Optional

from .client import av_get


def stock_intraday(symbol: str, interval: str = "5min", adjusted: bool = True, extended_hours: bool = True,
                   month: Optional[str] = None, outputsize: str = "compact", datatype: str = "json") -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "adjusted": "true" if adjusted else "false",
        "extended_hours": "true" if extended_hours else "false",
        "outputsize": outputsize,
        "datatype": datatype,
    }
    if month:
        params["month"] = month
    return av_get(params)


def stock_daily(symbol: str, outputsize: str = "compact", datatype: str = "json") -> Dict[str, Any]:
    return av_get({
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": outputsize,
        "datatype": datatype,
    })


def stock_daily_adjusted(symbol: str, outputsize: str = "compact", datatype: str = "json") -> Dict[str, Any]:
    return av_get({
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": symbol,
        "outputsize": outputsize,
        "datatype": datatype,
    })


def stock_weekly(symbol: str, datatype: str = "json") -> Dict[str, Any]:
    return av_get({"function": "TIME_SERIES_WEEKLY", "symbol": symbol, "datatype": datatype})


def stock_weekly_adjusted(symbol: str, datatype: str = "json") -> Dict[str, Any]:
    return av_get({"function": "TIME_SERIES_WEEKLY_ADJUSTED", "symbol": symbol, "datatype": datatype})


def stock_monthly(symbol: str, datatype: str = "json") -> Dict[str, Any]:
    return av_get({"function": "TIME_SERIES_MONTHLY", "symbol": symbol, "datatype": datatype})


def stock_monthly_adjusted(symbol: str, datatype: str = "json") -> Dict[str, Any]:
    return av_get({"function": "TIME_SERIES_MONTHLY_ADJUSTED", "symbol": symbol, "datatype": datatype})


def global_quote(symbol: str, datatype: str = "json") -> Dict[str, Any]:
    return av_get({"function": "GLOBAL_QUOTE", "symbol": symbol, "datatype": datatype})


def symbol_search(keywords: str, datatype: str = "json") -> Dict[str, Any]:
    return av_get({"function": "SYMBOL_SEARCH", "keywords": keywords, "datatype": datatype})
