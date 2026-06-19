from typing import Any, Dict, Optional

from .client import AlphaVantageClient


def realtime_options(
    symbol: str,
    require_greeks: bool = False,
    contract: Optional[str] = None,
    expiration: Optional[str] = None,
    datatype: str = "json",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Realtime US options chain.

    function=REALTIME_OPTIONS
    """
    c = client or AlphaVantageClient()
    params: Dict[str, Any] = {"function": "REALTIME_OPTIONS", "symbol": symbol, "datatype": datatype}
    if require_greeks:
        params["require_greeks"] = "true"
    if contract:
        params["contract"] = contract
    if expiration:
        params["expiration"] = expiration
    return c.request(params)


def historical_options(
    symbol: str,
    date: Optional[str] = None,
    contract: Optional[str] = None,
    datatype: str = "json",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Historical US options chain for a date.

    function=HISTORICAL_OPTIONS
    """
    c = client or AlphaVantageClient()
    params: Dict[str, Any] = {"function": "HISTORICAL_OPTIONS", "symbol": symbol, "datatype": datatype}
    if date:
        params["date"] = date
    if contract:
        params["contract"] = contract
    return c.request(params)


def realtime_put_call_ratio(symbol: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Realtime put-call ratio.

    function=REALTIME_PUT_CALL_RATIO
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "REALTIME_PUT_CALL_RATIO", "symbol": symbol})


def realtime_volume_open_interest_ratio(symbol: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Realtime volume-to-open-interest ratio.

    function=REALTIME_VOLUME_OPEN_INTEREST_RATIO
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "REALTIME_VOLUME_OPEN_INTEREST_RATIO", "symbol": symbol})
