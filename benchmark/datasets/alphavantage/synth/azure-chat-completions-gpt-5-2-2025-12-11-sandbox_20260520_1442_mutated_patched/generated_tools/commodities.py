from typing import Any, Dict, Optional

from .alphavantage_client import call_alpha_vantage


def gold_silver_spot(ticker: str) -> Dict[str, Any]:
    """GOLD_SILVER_SPOT.

    Doc: docs/api_commodities.md
    """
    return call_alpha_vantage({"function": "GOLD_SILVER_SPOT", "symbol": ticker})


def gold_silver_history(ticker: str, time_interval: str) -> Dict[str, Any]:
    """GOLD_SILVER_HISTORY.

    Doc: docs/api_commodities.md
    """
    return call_alpha_vantage({"function": "GOLD_SILVER_HISTORY", "symbol": ticker, "interval": time_interval})


def wti(time_interval: Optional[str] = "monthly", format: Optional[str] = "json") -> Dict[str, Any]:
    """WTI.

    Doc: docs/api_commodities.md
    """
    params: Dict[str, Any] = {"function": "WTI"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def brent(time_interval: Optional[str] = "monthly", format: Optional[str] = "json") -> Dict[str, Any]:
    """BRENT.

    Doc: docs/api_commodities.md
    """
    params: Dict[str, Any] = {"function": "BRENT"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def natural_gas(time_interval: Optional[str] = "monthly", format: Optional[str] = "json") -> Dict[str, Any]:
    """NATURAL_GAS.

    Doc: docs/api_commodities.md
    """
    params: Dict[str, Any] = {"function": "NATURAL_GAS"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def copper(time_interval: Optional[str] = "monthly", format: Optional[str] = "json") -> Dict[str, Any]:
    """COPPER.

    Doc: docs/api_commodities.md
    """
    params: Dict[str, Any] = {"function": "COPPER"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def aluminum(time_interval: Optional[str] = "monthly", format: Optional[str] = "json") -> Dict[str, Any]:
    """ALUMINUM.

    Doc: docs/api_commodities.md
    """
    params: Dict[str, Any] = {"function": "ALUMINUM"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def wheat(time_interval: Optional[str] = "monthly", format: Optional[str] = "json") -> Dict[str, Any]:
    """WHEAT.

    Doc: docs/api_commodities.md
    """
    params: Dict[str, Any] = {"function": "WHEAT"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def corn(time_interval: Optional[str] = "monthly", format: Optional[str] = "json") -> Dict[str, Any]:
    """CORN.

    Doc: docs/api_commodities.md
    """
    params: Dict[str, Any] = {"function": "CORN"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def cotton(time_interval: Optional[str] = "monthly", format: Optional[str] = "json") -> Dict[str, Any]:
    """COTTON.

    Doc: docs/api_commodities.md
    """
    params: Dict[str, Any] = {"function": "COTTON"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def sugar(time_interval: Optional[str] = "monthly", format: Optional[str] = "json") -> Dict[str, Any]:
    """SUGAR.

    Doc: docs/api_commodities.md
    """
    params: Dict[str, Any] = {"function": "SUGAR"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def coffee(time_interval: Optional[str] = "monthly", format: Optional[str] = "json") -> Dict[str, Any]:
    """COFFEE.

    Doc: docs/api_commodities.md
    """
    params: Dict[str, Any] = {"function": "COFFEE"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def all_commodities(time_interval: Optional[str] = "monthly", format: Optional[str] = "json") -> Dict[str, Any]:
    """ALL_COMMODITIES.

    Doc: docs/api_commodities.md
    """
    params: Dict[str, Any] = {"function": "ALL_COMMODITIES"}
    if time_interval:
        params["interval"] = time_interval
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)
