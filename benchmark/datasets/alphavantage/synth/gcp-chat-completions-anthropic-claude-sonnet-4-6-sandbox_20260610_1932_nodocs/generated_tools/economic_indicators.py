"""
Alpha Vantage — Economic Indicators tools
Covers: CPI, inflation, GDP (real), unemployment, treasury yields,
        federal funds rate, retail sales, durables orders
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
        if "Information" in data:
            return {"error": data["Information"]}
        if "Note" in data:
            return {"error": data["Note"]}
        return data
    except requests.exceptions.RequestException as exc:
        return {"error": str(exc)}
    except ValueError as exc:
        return {"error": f"JSON decode error: {exc}"}


def get_cpi(interval: str = "monthly") -> dict:
    """
    Fetch the Consumer Price Index (CPI) for the United States.

    The CPI measures the average change over time in the prices paid by
    urban consumers for a market basket of consumer goods and services.

    Args:
        interval: Data frequency. Allowed: 'monthly', 'semiannual'.

    Returns:
        Dict with 'name', 'interval', 'unit', and 'data' (list of date/value pairs).
    """
    return _get({
        "function": "CPI",
        "interval": interval,
    })


def get_inflation() -> dict:
    """
    Fetch the annual inflation rate (%) for the United States.

    Based on the Consumer Price Index for All Urban Consumers (CPI-U).

    Returns:
        Dict with 'name', 'interval', 'unit', and 'data' (list of year/value pairs).
    """
    return _get({
        "function": "INFLATION",
    })


def get_real_gdp(interval: str = "annual") -> dict:
    """
    Fetch the Real GDP of the United States.

    Args:
        interval: Data frequency. Allowed: 'annual', 'quarterly'.

    Returns:
        Dict with 'name', 'interval', 'unit' (billions of dollars), and
        'data' (list of date/value pairs).
    """
    return _get({
        "function": "REAL_GDP",
        "interval": interval,
    })


def get_real_gdp_per_capita() -> dict:
    """
    Fetch the Real GDP per Capita of the United States (quarterly).

    Returns:
        Dict with 'name', 'interval', 'unit' (chained 2012 dollars), and
        'data' (list of date/value pairs).
    """
    return _get({
        "function": "REAL_GDP_PER_CAPITA",
    })


def get_unemployment() -> dict:
    """
    Fetch the monthly US unemployment rate.

    The unemployment rate represents the number of unemployed as a percentage
    of the labor force.

    Returns:
        Dict with 'name', 'interval', 'unit' (percent), and
        'data' (list of date/value pairs).
    """
    return _get({
        "function": "UNEMPLOYMENT",
    })


def get_treasury_yield(interval: str = "monthly", maturity: str = "10year") -> dict:
    """
    Fetch US Treasury yield for a given maturity.

    Args:
        interval: Data frequency. Allowed: 'daily', 'weekly', 'monthly'.
        maturity: Treasury maturity. Allowed: '3month', '2year', '5year',
                  '7year', '10year', '30year'.

    Returns:
        Dict with 'name', 'interval', 'unit' (percent), and
        'data' (list of date/value pairs).
    """
    return _get({
        "function": "TREASURY_YIELD",
        "interval": interval,
        "maturity": maturity,
    })


def get_federal_funds_rate(interval: str = "monthly") -> dict:
    """
    Fetch the US Federal Funds Rate (interest rate).

    The federal funds rate is the interest rate at which depository institutions
    trade federal funds with each other overnight.

    Args:
        interval: Data frequency. Allowed: 'daily', 'weekly', 'monthly'.

    Returns:
        Dict with 'name', 'interval', 'unit' (percent), and
        'data' (list of date/value pairs).
    """
    return _get({
        "function": "FEDERAL_FUNDS_RATE",
        "interval": interval,
    })


def get_retail_sales() -> dict:
    """
    Fetch the monthly US Advance Retail Sales data.

    Retail sales measure the total receipts at stores that sell merchandise
    and related services to final consumers.

    Returns:
        Dict with 'name', 'interval', 'unit' (millions of dollars), and
        'data' (list of date/value pairs).
    """
    return _get({
        "function": "RETAIL_SALES",
    })


def get_durables() -> dict:
    """
    Fetch the monthly US Manufacturers' New Orders for Durable Goods.

    Durable goods orders are a leading economic indicator of manufacturing
    activity and business investment.

    Returns:
        Dict with 'name', 'interval', 'unit' (billions of dollars), and
        'data' (list of date/value pairs).
    """
    return _get({
        "function": "DURABLES",
    })


def get_nonfarm_payroll() -> dict:
    """
    Fetch the monthly US Total Nonfarm Payroll (employment) data.

    Nonfarm payroll measures the number of workers in the US excluding
    farm workers and some other job classifications.

    Returns:
        Dict with 'name', 'interval', 'unit' (thousands of persons), and
        'data' (list of date/value pairs).
    """
    return _get({
        "function": "NONFARM_PAYROLL",
    })
