import os
import requests

ALPHAVANTAGE_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"

def get_real_gdp(interval="annual", datatype="json"):
    """
    Get US Real GDP (annual or quarterly).
    Args:
        interval (str): 'annual' or 'quarterly'.
        datatype (str): 'json' or 'csv'.
    Returns:
        dict or str: JSON or CSV data.
    """
    params = {
        "function": "REAL_GDP",
        "interval": interval,
        "apikey": ALPHAVANTAGE_API_KEY,
        "datatype": datatype,
    }
    try:
        resp = requests.get(BASE_URL, params=params)
        if datatype == "csv":
            return resp.text
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_real_gdp_per_capita(datatype="json"):
    """
    Get US Real GDP per Capita (quarterly).
    Args:
        datatype (str): 'json' or 'csv'.
    Returns:
        dict or str: JSON or CSV data.
    """
    params = {
        "function": "REAL_GDP_PER_CAPITA",
        "apikey": ALPHAVANTAGE_API_KEY,
        "datatype": datatype,
    }
    try:
        resp = requests.get(BASE_URL, params=params)
        if datatype == "csv":
            return resp.text
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_treasury_yield(interval="monthly", maturity="10year", datatype="json"):
    """
    Get US Treasury Yield for a given interval and maturity.
    Args:
        interval (str): 'daily', 'weekly', 'monthly'.
        maturity (str): '3month', '2year', '5year', '7year', '10year', '30year'.
        datatype (str): 'json' or 'csv'.
    Returns:
        dict or str: JSON or CSV data.
    """
    params = {
        "function": "TREASURY_YIELD",
        "interval": interval,
        "maturity": maturity,
        "apikey": ALPHAVANTAGE_API_KEY,
        "datatype": datatype,
    }
    try:
        resp = requests.get(BASE_URL, params=params)
        if datatype == "csv":
            return resp.text
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_federal_funds_rate(interval="monthly", datatype="json"):
    """
    Get US Federal Funds Rate for a given interval.
    Args:
        interval (str): 'daily', 'weekly', 'monthly'.
        datatype (str): 'json' or 'csv'.
    Returns:
        dict or str: JSON or CSV data.
    """
    params = {
        "function": "FEDERAL_FUNDS_RATE",
        "interval": interval,
        "apikey": ALPHAVANTAGE_API_KEY,
        "datatype": datatype,
    }
    try:
        resp = requests.get(BASE_URL, params=params)
        if datatype == "csv":
            return resp.text
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
