from typing import Any, Dict, Optional

from .client import av_get


def realtime_options(
    ticker: str,
    require_greeks: Optional[bool] = None,
    contract: Optional[str] = None,
    expiration: Optional[str] = None,
    format: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "REALTIME_OPTIONS", "symbol": ticker}
    if require_greeks is not None:
        params["require_greeks"] = "true" if require_greeks else "false"
    if contract:
        params["contract"] = contract
    if expiration:
        params["expiration"] = expiration
    if format:
        params["datatype"] = format
    return av_get(params)


def realtime_put_call_ratio(ticker: str) -> Dict[str, Any]:
    return av_get({"function": "REALTIME_PUT_CALL_RATIO", "symbol": ticker})


def realtime_volume_open_interest_ratio(ticker: str) -> Dict[str, Any]:
    return av_get({"function": "REALTIME_VOLUME_OPEN_INTEREST_RATIO", "symbol": ticker})


def historical_options(
    ticker: str,
    date: Optional[str] = None,
    contract: Optional[str] = None,
    format: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "HISTORICAL_OPTIONS", "symbol": ticker}
    if date:
        params["date"] = date
    if contract:
        params["contract"] = contract
    if format:
        params["datatype"] = format
    return av_get(params)
