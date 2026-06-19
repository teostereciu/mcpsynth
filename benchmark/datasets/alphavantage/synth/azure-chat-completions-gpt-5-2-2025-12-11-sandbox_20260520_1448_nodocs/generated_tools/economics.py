from typing import Any, Dict, Optional

from .client import call_alpha_vantage


def cpi(interval: str = "monthly") -> Dict[str, Any]:
    return call_alpha_vantage({"function": "CPI", "interval": interval})


def inflation() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "INFLATION"})


def gdp(interval: str = "quarterly") -> Dict[str, Any]:
    return call_alpha_vantage({"function": "REAL_GDP", "interval": interval})


def unemployment() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "UNEMPLOYMENT"})


def treasury_yield(interval: str = "monthly", maturity: str = "10year") -> Dict[str, Any]:
    return call_alpha_vantage({"function": "TREASURY_YIELD", "interval": interval, "maturity": maturity})


def federal_funds_rate(interval: str = "monthly") -> Dict[str, Any]:
    return call_alpha_vantage({"function": "FEDERAL_FUNDS_RATE", "interval": interval})


def retail_sales() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "RETAIL_SALES"})


def durables() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "DURABLES"})


def nonfarm_payroll() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "NONFARM_PAYROLL"})


def real_gdp_per_capita() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "REAL_GDP_PER_CAPITA"})


def treasury_yield_spread(interval: str = "monthly", maturity1: str = "10year", maturity2: str = "2year") -> Dict[str, Any]:
    return call_alpha_vantage({
        "function": "TREASURY_YIELD_SPREAD",
        "interval": interval,
        "maturity1": maturity1,
        "maturity2": maturity2,
    })


def consumer_sentiment() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "CONSUMER_SENTIMENT"})


def wti() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "WTI"})


def brent() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "BRENT"})


def natural_gas() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "NATURAL_GAS"})


def copper() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "COPPER"})


def aluminum() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "ALUMINUM"})


def wheat() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "WHEAT"})


def corn() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "CORN"})


def cotton() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "COTTON"})


def sugar() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "SUGAR"})


def coffee() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "COFFEE"})


def all_commodities() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "ALL_COMMODITIES"})
