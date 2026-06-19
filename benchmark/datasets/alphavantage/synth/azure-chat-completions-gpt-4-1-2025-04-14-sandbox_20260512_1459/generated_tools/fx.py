import os
import requests

ALPHAVANTAGE_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"

def get_currency_exchange_rate(from_currency, to_currency):
    """
    Get realtime exchange rate for a pair of fiat or crypto currencies.
    Args:
        from_currency (str): Source currency (e.g., USD, BTC).
        to_currency (str): Target currency (e.g., EUR, USD).
    Returns:
        dict: JSON result.
    """
    params = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": from_currency,
        "to_currency": to_currency,
        "apikey": ALPHAVANTAGE_API_KEY,
    }
    try:
        resp = requests.get(BASE_URL, params=params)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_fx_intraday(from_symbol, to_symbol, interval, outputsize="compact", datatype="json"):
    """
    Get intraday FX time series for a currency pair.
    Args:
        from_symbol (str): Source currency (e.g., EUR).
        to_symbol (str): Target currency (e.g., USD).
        interval (str): Interval ('1min', '5min', '15min', '30min', '60min').
        outputsize (str): 'compact' or 'full'.
        datatype (str): 'json' or 'csv'.
    Returns:
        dict or str: JSON or CSV data.
    """
    params = {
        "function": "FX_INTRADAY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "interval": interval,
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


def get_fx_daily(from_symbol, to_symbol, outputsize="compact", datatype="json"):
    """
    Get daily FX time series for a currency pair.
    Args:
        from_symbol (str): Source currency (e.g., EUR).
        to_symbol (str): Target currency (e.g., USD).
        outputsize (str): 'compact' or 'full'.
        datatype (str): 'json' or 'csv'.
    Returns:
        dict or str: JSON or CSV data.
    """
    params = {
        "function": "FX_DAILY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
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
