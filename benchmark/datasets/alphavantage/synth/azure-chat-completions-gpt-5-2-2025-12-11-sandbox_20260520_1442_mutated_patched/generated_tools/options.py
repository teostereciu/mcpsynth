from typing import Any, Dict, Optional

from .alphavantage_client import call_alpha_vantage


def realtime_options(
    ticker: str,
    require_greeks: Optional[bool] = False,
    contract: Optional[str] = None,
    expiration: Optional[str] = None,
    format: Optional[str] = "json",
) -> Dict[str, Any]:
    """REALTIME_OPTIONS.

    Doc: docs/api_options.md
    """
    params: Dict[str, Any] = {"function": "REALTIME_OPTIONS", "symbol": ticker}
    if require_greeks is not None:
        params["require_greeks"] = "true" if require_greeks else "false"
    if contract:
        params["contract"] = contract
    if expiration:
        params["expiration"] = expiration
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def realtime_put_call_ratio(ticker: str) -> Dict[str, Any]:
    """REALTIME_PUT_CALL_RATIO.

    Doc: docs/api_options.md
    """
    return call_alpha_vantage({"function": "REALTIME_PUT_CALL_RATIO", "symbol": ticker})


def realtime_volume_open_interest_ratio(ticker: str) -> Dict[str, Any]:
    """REALTIME_VOLUME_OPEN_INTEREST_RATIO.

    Doc: docs/api_options.md
    """
    return call_alpha_vantage({"function": "REALTIME_VOLUME_OPEN_INTEREST_RATIO", "symbol": ticker})


def historical_options(
    ticker: str,
    date: Optional[str] = None,
    contract: Optional[str] = None,
    format: Optional[str] = "json",
) -> Dict[str, Any]:
    """HISTORICAL_OPTIONS.

    Doc: docs/api_options.md
    """
    params: Dict[str, Any] = {"function": "HISTORICAL_OPTIONS", "symbol": ticker}
    if date:
        params["date"] = date
    if contract:
        params["contract"] = contract
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)
