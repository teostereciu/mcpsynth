from typing import Any, Dict, Optional, Union

from .client import av_get


def real_gdp(interval: Optional[str] = None, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """REAL_GDP.

    Doc: docs/api_economic_indicators.md
    Endpoint: GET /query?function=REAL_GDP
    """
    params: Dict[str, Any] = {"function": "REAL_GDP"}
    if interval:
        params["interval"] = interval
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def real_gdp_per_capita(datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """REAL_GDP_PER_CAPITA.

    Doc: docs/api_economic_indicators.md
    Endpoint: GET /query?function=REAL_GDP_PER_CAPITA
    """
    params: Dict[str, Any] = {"function": "REAL_GDP_PER_CAPITA"}
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def treasury_yield(
    interval: Optional[str] = None,
    maturity: Optional[str] = None,
    datatype: Optional[str] = None,
) -> Union[Dict[str, Any], str]:
    """TREASURY_YIELD.

    Doc: docs/api_economic_indicators.md
    Endpoint: GET /query?function=TREASURY_YIELD
    """
    params: Dict[str, Any] = {"function": "TREASURY_YIELD"}
    if interval:
        params["interval"] = interval
    if maturity:
        params["maturity"] = maturity
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def federal_funds_rate(interval: Optional[str] = None, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """FEDERAL_FUNDS_RATE.

    Doc: docs/api_economic_indicators.md
    Endpoint: GET /query?function=FEDERAL_FUNDS_RATE
    """
    params: Dict[str, Any] = {"function": "FEDERAL_FUNDS_RATE"}
    if interval:
        params["interval"] = interval
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def cpi(interval: Optional[str] = None, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """CPI.

    Doc: docs/api_economic_indicators.md
    Endpoint: GET /query?function=CPI
    """
    params: Dict[str, Any] = {"function": "CPI"}
    if interval:
        params["interval"] = interval
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def inflation(datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """INFLATION.

    Doc: docs/api_economic_indicators.md
    Endpoint: GET /query?function=INFLATION
    """
    params: Dict[str, Any] = {"function": "INFLATION"}
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def unemployment(datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """UNEMPLOYMENT.

    Doc: docs/api_economic_indicators.md
    Endpoint: GET /query?function=UNEMPLOYMENT
    """
    params: Dict[str, Any] = {"function": "UNEMPLOYMENT"}
    if datatype:
        params["datatype"] = datatype
    return av_get(params)
