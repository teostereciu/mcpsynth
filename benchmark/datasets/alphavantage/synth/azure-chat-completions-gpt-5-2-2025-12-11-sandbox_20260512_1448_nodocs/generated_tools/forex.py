from typing import Any, Dict, Optional

from .client import AlphaVantageClient, normalize_outputsize, safe_validate


def fx_exchange_rate(from_currency: str, to_currency: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    return c.request("CURRENCY_EXCHANGE_RATE", from_currency=from_currency, to_currency=to_currency)


def fx_daily(
    from_symbol: str,
    to_symbol: str,
    outputsize: str = "compact",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    _, err = safe_validate(normalize_outputsize, outputsize)
    if err:
        return {"error": err}
    return c.request("FX_DAILY", from_symbol=from_symbol, to_symbol=to_symbol, outputsize=outputsize)


def fx_weekly(from_symbol: str, to_symbol: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    return c.request("FX_WEEKLY", from_symbol=from_symbol, to_symbol=to_symbol)


def fx_monthly(from_symbol: str, to_symbol: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    return c.request("FX_MONTHLY", from_symbol=from_symbol, to_symbol=to_symbol)
