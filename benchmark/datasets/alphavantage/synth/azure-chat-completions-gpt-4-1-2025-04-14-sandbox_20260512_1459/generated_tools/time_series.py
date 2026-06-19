import os
import requests

ALPHAVANTAGE_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"

def get_intraday_time_series(symbol, interval, adjusted=True, extended_hours=True, month=None, outputsize="compact", datatype="json", entitlement=None):
    """
    Get intraday OHLCV time series for a stock symbol.
    Args:
        symbol (str): Stock ticker symbol.
        interval (str): Interval between data points ('1min', '5min', '15min', '30min', '60min').
        adjusted (bool): Adjusted for splits/dividends (default True).
        extended_hours (bool): Include pre/post-market (default True).
        month (str): YYYY-MM for historical month.
        outputsize (str): 'compact' or 'full'.
        datatype (str): 'json' or 'csv'.
        entitlement (str): 'realtime' or 'delayed'.
    Returns:
        dict or str: JSON or CSV data.
    """
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "apikey": ALPHAVANTAGE_API_KEY,
        "outputsize": outputsize,
        "datatype": datatype,
        "adjusted": str(adjusted).lower(),
        "extended_hours": str(extended_hours).lower(),
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

def get_daily_time_series(symbol, outputsize="compact", datatype="json"):
    """
    Get daily OHLCV time series for a stock symbol.
    Args:
        symbol (str): Stock ticker symbol.
        outputsize (str): 'compact' or 'full'.
        datatype (str): 'json' or 'csv'.
    Returns:
        dict or str: JSON or CSV data.
    """
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": ALPHAVANTAGE_API_KEY,
        "outputsize": outputsize,
        "datatype": datatype,
    }
    try:
        resp = requests.get(BASE_URL, params=params)
        if datatype == "csv":
            return resp.text
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_daily_adjusted_time_series(symbol, outputsize="compact", datatype="json", entitlement=None):
    """
    Get daily adjusted OHLCV time series for a stock symbol (includes splits/dividends).
    Args:
        symbol (str): Stock ticker symbol.
        outputsize (str): 'compact' or 'full'.
        datatype (str): 'json' or 'csv'.
        entitlement (str): 'realtime' or 'delayed'.
    Returns:
        dict or str: JSON or CSV data.
    """
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": symbol,
        "apikey": ALPHAVANTAGE_API_KEY,
        "outputsize": outputsize,
        "datatype": datatype,
    }
    if entitlement:
        params["entitlement"] = entitlement
    try:
        resp = requests.get(BASE_URL, params=params)
        if datatype == "csv":
            return resp.text
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
