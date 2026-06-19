import os
import requests

ALPHAVANTAGE_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"

def get_gold_silver_spot(symbol):
    """
    Get live spot price for gold or silver.
    Args:
        symbol (str): 'GOLD', 'XAU', 'SILVER', or 'XAG'.
    Returns:
        dict: JSON result.
    """
    params = {
        "function": "GOLD_SILVER_SPOT",
        "symbol": symbol,
        "apikey": ALPHAVANTAGE_API_KEY,
    }
    try:
        resp = requests.get(BASE_URL, params=params)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_gold_silver_history(symbol, interval, datatype="json"):
    """
    Get historical prices for gold or silver.
    Args:
        symbol (str): 'GOLD', 'XAU', 'SILVER', or 'XAG'.
        interval (str): 'daily', 'weekly', 'monthly'.
        datatype (str): 'json' or 'csv'.
    Returns:
        dict or str: JSON or CSV data.
    """
    params = {
        "function": "GOLD_SILVER_HISTORY",
        "symbol": symbol,
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


def get_wti_crude_oil(interval="monthly", datatype="json"):
    """
    Get West Texas Intermediate (WTI) crude oil prices.
    Args:
        interval (str): 'daily', 'weekly', 'monthly'.
        datatype (str): 'json' or 'csv'.
    Returns:
        dict or str: JSON or CSV data.
    """
    params = {
        "function": "WTI",
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


def get_brent_crude_oil(interval="monthly", datatype="json"):
    """
    Get Brent crude oil prices.
    Args:
        interval (str): 'daily', 'weekly', 'monthly'.
        datatype (str): 'json' or 'csv'.
    Returns:
        dict or str: JSON or CSV data.
    """
    params = {
        "function": "BRENT",
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
