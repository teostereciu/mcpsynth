import os
import requests

ALPHAVANTAGE_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"

def get_company_overview(symbol):
    """
    Get company overview and key metrics for a stock symbol.
    Args:
        symbol (str): Stock ticker symbol.
    Returns:
        dict: JSON result.
    """
    params = {
        "function": "OVERVIEW",
        "symbol": symbol,
        "apikey": ALPHAVANTAGE_API_KEY,
    }
    try:
        resp = requests.get(BASE_URL, params=params)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_etf_profile(symbol):
    """
    Get ETF profile and holdings for a symbol.
    Args:
        symbol (str): ETF ticker symbol.
    Returns:
        dict: JSON result.
    """
    params = {
        "function": "ETF_PROFILE",
        "symbol": symbol,
        "apikey": ALPHAVANTAGE_API_KEY,
    }
    try:
        resp = requests.get(BASE_URL, params=params)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_dividends(symbol, datatype="json"):
    """
    Get dividend history for a stock symbol.
    Args:
        symbol (str): Stock ticker symbol.
        datatype (str): 'json' or 'csv'.
    Returns:
        dict or str: JSON or CSV data.
    """
    params = {
        "function": "DIVIDENDS",
        "symbol": symbol,
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


def get_splits(symbol, datatype="json"):
    """
    Get split history for a stock symbol.
    Args:
        symbol (str): Stock ticker symbol.
        datatype (str): 'json' or 'csv'.
    Returns:
        dict or str: JSON or CSV data.
    """
    params = {
        "function": "SPLITS",
        "symbol": symbol,
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
