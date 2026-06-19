from typing import Any, Dict, Optional

from .alphavantage_client import call_alpha_vantage


def real_gdp(time_interval: Optional[str] = "annual", format: Optional[str] = "json") -> Dict[str, Any]:
    """REAL_GDP.

    Doc: docs/api_economic_indicators.md
    """
    params: Dict[str, Any] = {"function": "REAL_GDP"}
    if time_interval:
        params["time_interval"] = time_interval
    if format:
        params["format"] = format
    return call_alpha_vantage(params)


def real_gdp_per_capita(format: Optional[str] = "json") -> Dict[str, Any]:
    """REAL_GDP_PER_CAPITA.

    Doc: docs/api_economic_indicators.md
    """
    params: Dict[str, Any] = {"function": "REAL_GDP_PER_CAPITA"}
    if format:
        params["format"] = format
    return call_alpha_vantage(params)


def treasury_yield(
    time_interval: Optional[str] = "monthly",
    maturity: Optional[str] = "10year",
    format: Optional[str] = "json",
) -> Dict[str, Any]:
    """TREASURY_YIELD.

    Doc: docs/api_economic_indicators.md
    """
    params: Dict[str, Any] = {"function": "TREASURY_YIELD"}
    if time_interval:
        params["time_interval"] = time_interval
    if maturity:
        params["maturity"] = maturity
    if format:
        params["format"] = format
    return call_alpha_vantage(params)


def federal_funds_rate(time_interval: Optional[str] = "monthly", format: Optional[str] = "json") -> Dict[str, Any]:
    """FEDERAL_FUNDS_RATE.

    Doc: docs/api_economic_indicators.md
    """
    params: Dict[str, Any] = {"function": "FEDERAL_FUNDS_RATE"}
    if time_interval:
        params["time_interval"] = time_interval
    if format:
        params["format"] = format
    return call_alpha_vantage(params)


def cpi(time_interval: Optional[str] = "monthly", format: Optional[str] = "json") -> Dict[str, Any]:
    """CPI.

    Doc: docs/api_economic_indicators.md
    """
    params: Dict[str, Any] = {"function": "CPI"}
    if time_interval:
        params["time_interval"] = time_interval
    if format:
        params["format"] = format
    return call_alpha_vantage(params)


def inflation(format: Optional[str] = "json") -> Dict[str, Any]:
    """INFLATION.

    Doc: docs/api_economic_indicators.md
    """
    params: Dict[str, Any] = {"function": "INFLATION"}
    if format:
        params["format"] = format
    return call_alpha_vantage(params)


def unemployment(format: Optional[str] = "json") -> Dict[str, Any]:
    """UNEMPLOYMENT.

    Doc: docs/api_economic_indicators.md
    """
    params: Dict[str, Any] = {"function": "UNEMPLOYMENT"}
    if format:
        params["format"] = format
    return call_alpha_vantage(params)
