import os
import requests

ALPHAVANTAGE_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"

def get_sma(symbol, interval, time_period, series_type, month=None, datatype="json", entitlement=None):
    """
    Get simple moving average (SMA) values.
    Args:
        symbol (str): Ticker symbol.
        interval (str): Interval ('1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly').
        time_period (int): Number of data points.
        series_type (str): Price type ('close', 'open', 'high', 'low').
        month (str): YYYY-MM for historical month.
        datatype (str): 'json' or 'csv'.
        entitlement (str): 'realtime' or 'delayed'.
    Returns:
        dict or str: JSON or CSV data.
    """
    params = {
        "function": "SMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
        "apikey": ALPHAVANTAGE_API_KEY,
        "datatype": datatype,
    }
    if month:
        params["month"] = month
    if entitlement:
        params["entitlement"] = entitlement
    try:
        resp = requests.get(BASE_URL, params=params)
        if datatype == "csv":
            return resp.text
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_ema(symbol, interval, time_period, series_type, month=None, datatype="json", entitlement=None):
    """
    Get exponential moving average (EMA) values.
    Args:
        symbol (str): Ticker symbol.
        interval (str): Interval ('1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly').
        time_period (int): Number of data points.
        series_type (str): Price type ('close', 'open', 'high', 'low').
        month (str): YYYY-MM for historical month.
        datatype (str): 'json' or 'csv'.
        entitlement (str): 'realtime' or 'delayed'.
    Returns:
        dict or str: JSON or CSV data.
    """
    params = {
        "function": "EMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
        "apikey": ALPHAVANTAGE_API_KEY,
        "datatype": datatype,
    }
    if month:
        params["month"] = month
    if entitlement:
        params["entitlement"] = entitlement
    try:
        resp = requests.get(BASE_URL, params=params)
        if datatype == "csv":
            return resp.text
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
