from typing import Optional

from generated_tools.common import call_alpha_vantage


def get_real_gdp(time_interval: Optional[str] = None):
    return call_alpha_vantage({"function": "REAL_GDP", "time_interval": time_interval})


def get_real_gdp_per_capita():
    return call_alpha_vantage({"function": "REAL_GDP_PER_CAPITA"})


def get_treasury_yield(
    time_interval: Optional[str] = None, maturity: Optional[str] = None
):
    return call_alpha_vantage(
        {"function": "TREASURY_YIELD", "time_interval": time_interval, "maturity": maturity}
    )


def get_federal_funds_rate(time_interval: Optional[str] = None):
    return call_alpha_vantage({"function": "FEDERAL_FUNDS_RATE", "time_interval": time_interval})


def get_cpi(time_interval: Optional[str] = None):
    return call_alpha_vantage({"function": "CPI", "time_interval": time_interval})


def get_inflation():
    return call_alpha_vantage({"function": "INFLATION"})


def get_retail_sales():
    return call_alpha_vantage({"function": "RETAIL_SALES"})


def get_durables():
    return call_alpha_vantage({"function": "DURABLES"})


def get_unemployment():
    return call_alpha_vantage({"function": "UNEMPLOYMENT"})


def get_nonfarm_payroll():
    return call_alpha_vantage({"function": "NONFARM_PAYROLL"})
