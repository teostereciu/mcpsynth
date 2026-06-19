from typing import Any, Dict, Optional

from .client import call_alpha_vantage


def real_gdp(interval: str = "annual", datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "REAL_GDP", "interval": interval}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def real_gdp_per_capita(datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "REAL_GDP_PER_CAPITA"}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def treasury_yield(
    interval: str = "monthly",
    maturity: str = "10year",
    datatype: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "TREASURY_YIELD", "interval": interval, "maturity": maturity}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def federal_funds_rate(interval: str = "monthly", datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "FEDERAL_FUNDS_RATE", "interval": interval}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def cpi(interval: str = "monthly", datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "CPI", "interval": interval}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def inflation(datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "INFLATION"}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def unemployment(datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "UNEMPLOYMENT"}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def retail_sales(datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "RETAIL_SALES"}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def durables(datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "DURABLES"}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)


def nonfarm_payroll(datatype: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "NONFARM_PAYROLL"}
    if datatype is not None:
        params["datatype"] = datatype
    return call_alpha_vantage(params)
