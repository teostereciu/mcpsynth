from typing import Any, Dict

from .client import av_get


def fx_exchange_rate(from_currency: str, to_currency: str) -> Dict[str, Any]:
    return av_get({
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": from_currency,
        "to_currency": to_currency,
    })


def fx_daily(from_symbol: str, to_symbol: str, outputsize: str = "compact", datatype: str = "json") -> Dict[str, Any]:
    return av_get({
        "function": "FX_DAILY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "outputsize": outputsize,
        "datatype": datatype,
    })


def fx_weekly(from_symbol: str, to_symbol: str, datatype: str = "json") -> Dict[str, Any]:
    return av_get({
        "function": "FX_WEEKLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "datatype": datatype,
    })


def fx_monthly(from_symbol: str, to_symbol: str, datatype: str = "json") -> Dict[str, Any]:
    return av_get({
        "function": "FX_MONTHLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "datatype": datatype,
    })
