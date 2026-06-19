from typing import Any, Dict, Optional, Union

from .client import av_get


def realtime_options(
    symbol: str,
    require_greeks: Optional[bool] = None,
    contract: Optional[str] = None,
    expiration: Optional[str] = None,
    datatype: Optional[str] = None,
) -> Union[Dict[str, Any], str]:
    """REALTIME_OPTIONS.

    Doc: docs/api_options.md
    Endpoint: GET /query?function=REALTIME_OPTIONS
    """
    params: Dict[str, Any] = {"function": "REALTIME_OPTIONS", "symbol": symbol}
    if require_greeks is not None:
        params["require_greeks"] = "true" if require_greeks else "false"
    if contract:
        params["contract"] = contract
    if expiration:
        params["expiration"] = expiration
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def realtime_put_call_ratio(symbol: str) -> Dict[str, Any]:
    """REALTIME_PUT_CALL_RATIO.

    Doc: docs/api_options.md
    Endpoint: GET /query?function=REALTIME_PUT_CALL_RATIO
    """
    return av_get({"function": "REALTIME_PUT_CALL_RATIO", "symbol": symbol})  # type: ignore[return-value]


def realtime_volume_open_interest_ratio(symbol: str) -> Dict[str, Any]:
    """REALTIME_VOLUME_OPEN_INTEREST_RATIO.

    Doc: docs/api_options.md
    Endpoint: GET /query?function=REALTIME_VOLUME_OPEN_INTEREST_RATIO
    """
    return av_get({"function": "REALTIME_VOLUME_OPEN_INTEREST_RATIO", "symbol": symbol})  # type: ignore[return-value]


def historical_options(
    symbol: str,
    date: Optional[str] = None,
    contract: Optional[str] = None,
    datatype: Optional[str] = None,
) -> Union[Dict[str, Any], str]:
    """HISTORICAL_OPTIONS.

    Doc: docs/api_options.md
    Endpoint: GET /query?function=HISTORICAL_OPTIONS
    """
    params: Dict[str, Any] = {"function": "HISTORICAL_OPTIONS", "symbol": symbol}
    if date:
        params["date"] = date
    if contract:
        params["contract"] = contract
    if datatype:
        params["datatype"] = datatype
    return av_get(params)
