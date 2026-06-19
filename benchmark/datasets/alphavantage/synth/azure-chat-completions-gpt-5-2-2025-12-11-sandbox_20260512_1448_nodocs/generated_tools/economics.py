from typing import Any, Dict, Optional

from .client import AlphaVantageClient


def cpi(interval: str = "monthly", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    return c.request("CPI", interval=interval)


def inflation(client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    return c.request("INFLATION")


def gdp(interval: str = "quarterly", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    return c.request("REAL_GDP", interval=interval)


def unemployment(client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    return c.request("UNEMPLOYMENT")


def treasury_yield(interval: str = "monthly", maturity: str = "10year", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    return c.request("TREASURY_YIELD", interval=interval, maturity=maturity)
