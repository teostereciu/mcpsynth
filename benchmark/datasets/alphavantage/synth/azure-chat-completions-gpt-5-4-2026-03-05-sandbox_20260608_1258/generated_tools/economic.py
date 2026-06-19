from typing import Optional

from generated_tools.common import alpha_vantage_get, build_result


def get_real_gdp(interval: Optional[str] = None):
    params = {"function": "REAL_GDP", "interval": interval}
    return build_result("get_real_gdp", params, alpha_vantage_get(params))


def get_real_gdp_per_capita():
    params = {"function": "REAL_GDP_PER_CAPITA"}
    return build_result("get_real_gdp_per_capita", params, alpha_vantage_get(params))


def get_treasury_yield(interval: Optional[str] = None, maturity: Optional[str] = None):
    params = {"function": "TREASURY_YIELD", "interval": interval, "maturity": maturity}
    return build_result("get_treasury_yield", params, alpha_vantage_get(params))


def get_federal_funds_rate(interval: Optional[str] = None):
    params = {"function": "FEDERAL_FUNDS_RATE", "interval": interval}
    return build_result("get_federal_funds_rate", params, alpha_vantage_get(params))


def get_cpi(interval: Optional[str] = None):
    params = {"function": "CPI", "interval": interval}
    return build_result("get_cpi", params, alpha_vantage_get(params))


def get_inflation():
    params = {"function": "INFLATION"}
    return build_result("get_inflation", params, alpha_vantage_get(params))


def get_unemployment():
    params = {"function": "UNEMPLOYMENT"}
    return build_result("get_unemployment", params, alpha_vantage_get(params))
