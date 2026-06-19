from typing import Any, Dict

from .client import av_get


def crypto_exchange_rate(from_currency: str, to_currency: str) -> Dict[str, Any]:
    return av_get({
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": from_currency,
        "to_currency": to_currency,
    })


def crypto_daily(symbol: str, market: str, datatype: str = "json") -> Dict[str, Any]:
    return av_get({
        "function": "DIGITAL_CURRENCY_DAILY",
        "symbol": symbol,
        "market": market,
        "datatype": datatype,
    })


def crypto_weekly(symbol: str, market: str, datatype: str = "json") -> Dict[str, Any]:
    return av_get({
        "function": "DIGITAL_CURRENCY_WEEKLY",
        "symbol": symbol,
        "market": market,
        "datatype": datatype,
    })


def crypto_monthly(symbol: str, market: str, datatype: str = "json") -> Dict[str, Any]:
    return av_get({
        "function": "DIGITAL_CURRENCY_MONTHLY",
        "symbol": symbol,
        "market": market,
        "datatype": datatype,
    })
