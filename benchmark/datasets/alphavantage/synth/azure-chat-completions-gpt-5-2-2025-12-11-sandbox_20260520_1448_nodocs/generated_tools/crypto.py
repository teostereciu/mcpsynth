from typing import Any, Dict

from .client import call_alpha_vantage


def crypto_exchange_rate(from_currency: str, to_currency: str) -> Dict[str, Any]:
    return call_alpha_vantage({
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": from_currency,
        "to_currency": to_currency,
    })


def crypto_daily(symbol: str, market: str = "USD") -> Dict[str, Any]:
    return call_alpha_vantage({
        "function": "DIGITAL_CURRENCY_DAILY",
        "symbol": symbol,
        "market": market,
    })


def crypto_weekly(symbol: str, market: str = "USD") -> Dict[str, Any]:
    return call_alpha_vantage({
        "function": "DIGITAL_CURRENCY_WEEKLY",
        "symbol": symbol,
        "market": market,
    })


def crypto_monthly(symbol: str, market: str = "USD") -> Dict[str, Any]:
    return call_alpha_vantage({
        "function": "DIGITAL_CURRENCY_MONTHLY",
        "symbol": symbol,
        "market": market,
    })
