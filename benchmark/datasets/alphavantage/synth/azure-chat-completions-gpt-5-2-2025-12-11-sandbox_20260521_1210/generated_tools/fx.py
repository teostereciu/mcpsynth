from typing import Any, Dict, Optional

from .client import call_alpha_vantage


def fx_exchange_rate(from_currency: str, to_currency: str) -> Dict[str, Any]:
    return call_alpha_vantage(
        {"function": "CURRENCY_EXCHANGE_RATE", "from_currency": from_currency, "to_currency": to_currency}
    )


def fx_intraday(
    from_symbol: str,
    to_symbol: str,
    interval: str,
    outputsize: Optional[str] = None,
    datatype: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "FX_INTRADAY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "interval": interval,
    }
    if outputsize is not None:
        params["outputsize"] = outputsize
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def fx_daily(
    from_symbol: str,
    to_symbol: str,
    outputsize: Optional[str] = None,
    datatype: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "FX_DAILY", "from_symbol": from_symbol, "to_symbol": to_symbol}
    if outputsize is not None:
        params["outputsize"] = outputsize
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def fx_weekly(from_symbol: str, to_symbol: str, datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "FX_WEEKLY", "from_symbol": from_symbol, "to_symbol": to_symbol}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def fx_monthly(from_symbol: str, to_symbol: str, datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "FX_MONTHLY", "from_symbol": from_symbol, "to_symbol": to_symbol}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)
