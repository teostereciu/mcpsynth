from typing import Any, Dict, Optional

from .client import call_alpha_vantage


def crypto_intraday(
    symbol: str,
    market: str,
    interval: str,
    outputsize: Optional[str] = None,
    datatype: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "CRYPTO_INTRADAY",
        "symbol": symbol,
        "market": market,
        "interval": interval,
    }
    if outputsize is not None:
        params["outputsize"] = outputsize
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def digital_currency_daily(symbol: str, market: str, datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "DIGITAL_CURRENCY_DAILY", "symbol": symbol, "market": market}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def digital_currency_weekly(symbol: str, market: str, datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "DIGITAL_CURRENCY_WEEKLY", "symbol": symbol, "market": market}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def digital_currency_monthly(symbol: str, market: str, datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "DIGITAL_CURRENCY_MONTHLY", "symbol": symbol, "market": market}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)
