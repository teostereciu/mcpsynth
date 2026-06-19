from typing import Any, Dict, Optional

from .client import AlphaVantageClient


def crypto_exchange_rate(from_currency: str, to_currency: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    return c.request("CURRENCY_EXCHANGE_RATE", from_currency=from_currency, to_currency=to_currency)


def digital_currency_daily(symbol: str, market: str = "USD", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    return c.request("DIGITAL_CURRENCY_DAILY", symbol=symbol, market=market)


def digital_currency_weekly(symbol: str, market: str = "USD", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    return c.request("DIGITAL_CURRENCY_WEEKLY", symbol=symbol, market=market)


def digital_currency_monthly(symbol: str, market: str = "USD", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    return c.request("DIGITAL_CURRENCY_MONTHLY", symbol=symbol, market=market)
