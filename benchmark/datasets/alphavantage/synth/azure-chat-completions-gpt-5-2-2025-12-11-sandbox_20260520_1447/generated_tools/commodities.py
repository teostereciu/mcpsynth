from typing import Any, Dict, Optional, Union

from .client import av_get


def gold_silver_spot(symbol: str) -> Dict[str, Any]:
    """GOLD_SILVER_SPOT.

    Doc: docs/api_commodities.md
    Endpoint: GET /query?function=GOLD_SILVER_SPOT
    """
    return av_get({"function": "GOLD_SILVER_SPOT", "symbol": symbol})  # type: ignore[return-value]


def gold_silver_history(symbol: str, interval: str) -> Dict[str, Any]:
    """GOLD_SILVER_HISTORY.

    Doc: docs/api_commodities.md
    Endpoint: GET /query?function=GOLD_SILVER_HISTORY
    """
    return av_get({"function": "GOLD_SILVER_HISTORY", "symbol": symbol, "interval": interval})  # type: ignore[return-value]


def wti(interval: Optional[str] = None, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """WTI crude oil.

    Doc: docs/api_commodities.md
    Endpoint: GET /query?function=WTI
    """
    params: Dict[str, Any] = {"function": "WTI"}
    if interval:
        params["interval"] = interval
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def brent(interval: Optional[str] = None, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """BRENT crude oil.

    Doc: docs/api_commodities.md
    Endpoint: GET /query?function=BRENT
    """
    params: Dict[str, Any] = {"function": "BRENT"}
    if interval:
        params["interval"] = interval
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def natural_gas(interval: Optional[str] = None, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """NATURAL_GAS.

    Doc: docs/api_commodities.md
    Endpoint: GET /query?function=NATURAL_GAS
    """
    params: Dict[str, Any] = {"function": "NATURAL_GAS"}
    if interval:
        params["interval"] = interval
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def copper(interval: Optional[str] = None, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """COPPER.

    Doc: docs/api_commodities.md
    Endpoint: GET /query?function=COPPER
    """
    params: Dict[str, Any] = {"function": "COPPER"}
    if interval:
        params["interval"] = interval
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def aluminum(interval: Optional[str] = None, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """ALUMINUM.

    Doc: docs/api_commodities.md
    Endpoint: GET /query?function=ALUMINUM
    """
    params: Dict[str, Any] = {"function": "ALUMINUM"}
    if interval:
        params["interval"] = interval
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def wheat(interval: Optional[str] = None, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """WHEAT.

    Doc: docs/api_commodities.md
    Endpoint: GET /query?function=WHEAT
    """
    params: Dict[str, Any] = {"function": "WHEAT"}
    if interval:
        params["interval"] = interval
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def corn(interval: Optional[str] = None, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """CORN.

    Doc: docs/api_commodities.md
    Endpoint: GET /query?function=CORN
    """
    params: Dict[str, Any] = {"function": "CORN"}
    if interval:
        params["interval"] = interval
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def cotton(interval: Optional[str] = None, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """COTTON.

    Doc: docs/api_commodities.md
    Endpoint: GET /query?function=COTTON
    """
    params: Dict[str, Any] = {"function": "COTTON"}
    if interval:
        params["interval"] = interval
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def sugar(interval: Optional[str] = None, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """SUGAR.

    Doc: docs/api_commodities.md
    Endpoint: GET /query?function=SUGAR
    """
    params: Dict[str, Any] = {"function": "SUGAR"}
    if interval:
        params["interval"] = interval
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def coffee(interval: Optional[str] = None, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """COFFEE.

    Doc: docs/api_commodities.md
    Endpoint: GET /query?function=COFFEE
    """
    params: Dict[str, Any] = {"function": "COFFEE"}
    if interval:
        params["interval"] = interval
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def all_commodities(interval: Optional[str] = None, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """ALL_COMMODITIES.

    Doc: docs/api_commodities.md
    Endpoint: GET /query?function=ALL_COMMODITIES
    """
    params: Dict[str, Any] = {"function": "ALL_COMMODITIES"}
    if interval:
        params["interval"] = interval
    if datatype:
        params["datatype"] = datatype
    return av_get(params)
