from typing import Optional

from .common import alpha_vantage_get


def get_cpi(interval: str = "monthly"):
    return alpha_vantage_get({"function": "CPI", "interval": interval})


def get_inflation():
    return alpha_vantage_get({"function": "INFLATION"})


def get_real_gdp(interval: str = "annual"):
    return alpha_vantage_get({"function": "REAL_GDP", "interval": interval})


def get_unemployment():
    return alpha_vantage_get({"function": "UNEMPLOYMENT"})


def get_treasury_yield(interval: str = "monthly", maturity: str = "10year"):
    return alpha_vantage_get({"function": "TREASURY_YIELD", "interval": interval, "maturity": maturity})


def get_federal_funds_rate(interval: str = "monthly"):
    return alpha_vantage_get({"function": "FEDERAL_FUNDS_RATE", "interval": interval})


def get_retail_sales(interval: str = "monthly"):
    return alpha_vantage_get({"function": "RETAIL_SALES", "interval": interval})


def get_durables(interval: str = "monthly"):
    return alpha_vantage_get({"function": "DURABLES", "interval": interval})


def get_nonfarm_payroll():
    return alpha_vantage_get({"function": "NONFARM_PAYROLL"})


def get_real_gdp_per_capita():
    return alpha_vantage_get({"function": "REAL_GDP_PER_CAPITA"})
