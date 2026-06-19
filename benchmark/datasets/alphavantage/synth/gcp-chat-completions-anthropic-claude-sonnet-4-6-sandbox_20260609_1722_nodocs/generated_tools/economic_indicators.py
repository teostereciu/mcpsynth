"""
Alpha Vantage – Economic Indicators tools
Covers: Real GDP, Real GDP per Capita, Treasury Yield, Federal Funds Rate,
        CPI, Inflation, Retail Sales, Durables, Unemployment, Nonfarm Payroll
"""

import os
import requests

BASE_URL = "https://www.alphavantage.co/query"


def _get(params: dict) -> dict:
    params["apikey"] = os.environ.get("ALPHAVANTAGE_API_KEY", "")
    try:
        resp = requests.get(BASE_URL, params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        if "Error Message" in data:
            return {"error": data["Error Message"]}
        if "Note" in data:
            return {"error": "API rate limit reached", "note": data["Note"]}
        if "Information" in data:
            return {"error": "API limit / info", "information": data["Information"]}
        return data
    except requests.RequestException as exc:
        return {"error": str(exc)}


def get_real_gdp(interval: str = "annual") -> dict:
    """
    Return annual or quarterly Real GDP of the United States.

    :param interval: "annual" or "quarterly".
    """
    return _get({"function": "REAL_GDP", "interval": interval})


def get_real_gdp_per_capita() -> dict:
    """
    Return quarterly Real GDP per Capita of the United States.
    """
    return _get({"function": "REAL_GDP_PER_CAPITA"})


def get_treasury_yield(
    interval: str = "monthly",
    maturity: str = "10year",
) -> dict:
    """
    Return daily, weekly, or monthly US Treasury yield for a given maturity.

    :param interval: "daily" | "weekly" | "monthly".
    :param maturity: "3month" | "2year" | "5year" | "7year" | "10year" | "30year".
    """
    return _get({
        "function": "TREASURY_YIELD",
        "interval": interval,
        "maturity": maturity,
    })


def get_federal_funds_rate(interval: str = "monthly") -> dict:
    """
    Return daily, weekly, or monthly US Federal Funds Rate (interest rate).

    :param interval: "daily" | "weekly" | "monthly".
    """
    return _get({"function": "FEDERAL_FUNDS_RATE", "interval": interval})


def get_cpi(interval: str = "monthly") -> dict:
    """
    Return monthly or semiannual Consumer Price Index (CPI) for the United States.

    :param interval: "monthly" or "semiannual".
    """
    return _get({"function": "CPI", "interval": interval})


def get_inflation() -> dict:
    """
    Return annual inflation rates (YoY CPI change) for the United States.
    """
    return _get({"function": "INFLATION"})


def get_retail_sales() -> dict:
    """
    Return monthly Advance Retail Sales data for the United States.
    """
    return _get({"function": "RETAIL_SALES"})


def get_durables() -> dict:
    """
    Return monthly manufacturers' new orders for durable goods in the United States.
    """
    return _get({"function": "DURABLES"})


def get_unemployment() -> dict:
    """
    Return monthly US unemployment rate.
    """
    return _get({"function": "UNEMPLOYMENT"})


def get_nonfarm_payroll() -> dict:
    """
    Return monthly US Total Nonfarm Employees (nonfarm payroll).
    """
    return _get({"function": "NONFARM_PAYROLL"})
