from typing import Any, Dict, Optional

from .client import AlphaVantageClient


def gold_silver_spot(symbol: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Live spot prices of gold or silver.

    function=GOLD_SILVER_SPOT
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "GOLD_SILVER_SPOT", "symbol": symbol})


def gold_silver_history(symbol: str, interval: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Historical gold/silver prices.

    function=GOLD_SILVER_HISTORY
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "GOLD_SILVER_HISTORY", "symbol": symbol, "interval": interval})


def wti(interval: str = "monthly", datatype: str = "json", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """WTI crude oil prices.

    function=WTI
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "WTI", "interval": interval, "datatype": datatype})


def brent(interval: str = "monthly", datatype: str = "json", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Brent crude oil prices.

    function=BRENT
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "BRENT", "interval": interval, "datatype": datatype})


def natural_gas(interval: str = "monthly", datatype: str = "json", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Natural gas prices.

    function=NATURAL_GAS
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "NATURAL_GAS", "interval": interval, "datatype": datatype})


def copper(interval: str = "monthly", datatype: str = "json", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Global price of copper.

    function=COPPER
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "COPPER", "interval": interval, "datatype": datatype})


def aluminum(interval: str = "monthly", datatype: str = "json", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Global price of aluminum.

    function=ALUMINUM
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "ALUMINUM", "interval": interval, "datatype": datatype})


def wheat(interval: str = "monthly", datatype: str = "json", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Global price of wheat.

    function=WHEAT
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "WHEAT", "interval": interval, "datatype": datatype})


def corn(interval: str = "monthly", datatype: str = "json", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Global price of corn.

    function=CORN
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "CORN", "interval": interval, "datatype": datatype})


def cotton(interval: str = "monthly", datatype: str = "json", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Global price of cotton.

    function=COTTON
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "COTTON", "interval": interval, "datatype": datatype})


def sugar(interval: str = "monthly", datatype: str = "json", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Global price of sugar.

    function=SUGAR
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "SUGAR", "interval": interval, "datatype": datatype})


def coffee(interval: str = "monthly", datatype: str = "json", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Global price of coffee.

    function=COFFEE
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "COFFEE", "interval": interval, "datatype": datatype})


def all_commodities(interval: str = "monthly", datatype: str = "json", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Global price index of all commodities.

    function=ALL_COMMODITIES
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "ALL_COMMODITIES", "interval": interval, "datatype": datatype})
