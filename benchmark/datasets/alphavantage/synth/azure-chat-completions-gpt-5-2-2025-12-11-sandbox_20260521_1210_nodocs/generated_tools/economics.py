from typing import Any, Dict, Optional

from .client import av_get


def cpi(interval: str = "monthly") -> Dict[str, Any]:
    return av_get({"function": "CPI", "interval": interval})


def inflation() -> Dict[str, Any]:
    return av_get({"function": "INFLATION"})


def gdp(interval: str = "quarterly") -> Dict[str, Any]:
    return av_get({"function": "REAL_GDP", "interval": interval})


def unemployment() -> Dict[str, Any]:
    return av_get({"function": "UNEMPLOYMENT"})


def treasury_yield(interval: str = "monthly", maturity: str = "10year") -> Dict[str, Any]:
    return av_get({"function": "TREASURY_YIELD", "interval": interval, "maturity": maturity})
