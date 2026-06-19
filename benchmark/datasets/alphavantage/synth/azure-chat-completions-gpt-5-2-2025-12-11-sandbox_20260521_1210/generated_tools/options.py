from typing import Any, Dict, Optional

from .client import call_alpha_vantage


def realtime_options(
    symbol: str,
    require_greeks: Optional[bool] = None,
    contract: Optional[str] = None,
    expiration: Optional[str] = None,
    datatype: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "REALTIME_OPTIONS", "symbol": symbol}
    if require_greeks is not None:
        params["require_greeks"] = "true" if require_greeks else "false"
    if contract is not None:
        params["contract"] = contract
    if expiration is not None:
        params["expiration"] = expiration
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def realtime_put_call_ratio(symbol: str) -> Dict[str, Any]:
    return call_alpha_vantage({"function": "REALTIME_PUT_CALL_RATIO", "symbol": symbol})


def realtime_volume_open_interest_ratio(symbol: str) -> Dict[str, Any]:
    return call_alpha_vantage({"function": "REALTIME_VOLUME_OPEN_INTEREST_RATIO", "symbol": symbol})


def historical_options(
    symbol: str,
    date: Optional[str] = None,
    contract: Optional[str] = None,
    datatype: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "HISTORICAL_OPTIONS", "symbol": symbol}
    if date is not None:
        params["date"] = date
    if contract is not None:
        params["contract"] = contract
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)
