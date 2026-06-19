from typing import Any, Dict, Optional

from .client import AlphaVantageClient


def real_gdp(interval: str = "annual", datatype: str = "json", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """US real GDP (annual or quarterly).

    function=REAL_GDP
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "REAL_GDP", "interval": interval, "datatype": datatype})


def real_gdp_per_capita(datatype: str = "json", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """US real GDP per capita (quarterly).

    function=REAL_GDP_PER_CAPITA
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "REAL_GDP_PER_CAPITA", "datatype": datatype})


def treasury_yield(
    interval: str = "monthly",
    maturity: str = "10year",
    datatype: str = "json",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """US treasury yield.

    function=TREASURY_YIELD
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "TREASURY_YIELD", "interval": interval, "maturity": maturity, "datatype": datatype})


def cpi(interval: str = "monthly", datatype: str = "json", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """US consumer price index.

    function=CPI
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "CPI", "interval": interval, "datatype": datatype})


def inflation(datatype: str = "json", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """US inflation rate.

    function=INFLATION
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "INFLATION", "datatype": datatype})


def unemployment(datatype: str = "json", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """US unemployment rate.

    function=UNEMPLOYMENT
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "UNEMPLOYMENT", "datatype": datatype})
