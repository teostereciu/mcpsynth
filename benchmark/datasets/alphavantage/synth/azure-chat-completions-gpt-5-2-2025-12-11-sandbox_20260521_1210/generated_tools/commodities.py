from typing import Any, Dict, Optional

from .client import call_alpha_vantage


def gold_silver_spot(symbol: str) -> Dict[str, Any]:
    return call_alpha_vantage({"function": "GOLD_SILVER_SPOT", "symbol": symbol})


def gold_silver_history(symbol: str, interval: str) -> Dict[str, Any]:
    return call_alpha_vantage({"function": "GOLD_SILVER_HISTORY", "symbol": symbol, "interval": interval})


def wti(interval: str = "monthly", datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "WTI", "interval": interval}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def brent(interval: str = "monthly", datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "BRENT", "interval": interval}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def natural_gas(interval: str = "monthly", datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "NATURAL_GAS", "interval": interval}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def copper(interval: str = "monthly", datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "COPPER", "interval": interval}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def aluminum(interval: str = "monthly", datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "ALUMINUM", "interval": interval}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def wheat(interval: str = "monthly", datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "WHEAT", "interval": interval}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def corn(interval: str = "monthly", datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "CORN", "interval": interval}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def cotton(interval: str = "monthly", datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "COTTON", "interval": interval}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def sugar(interval: str = "monthly", datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "SUGAR", "interval": interval}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def coffee(interval: str = "monthly", datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "COFFEE", "interval": interval}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def all_commodities(interval: str = "monthly", datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "ALL_COMMODITIES", "interval": interval}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)
