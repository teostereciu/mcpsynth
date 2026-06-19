import os
import requests

ALPHAVANTAGE_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"

def get_crypto_exchange_rate(from_currency, to_currency):
    """
    Get realtime exchange rate for a pair of cryptocurrencies or fiat currencies.
    Args:
        from_currency (str): Source currency (e.g., BTC, USD).
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


def get_crypto_intraday(symbol, market, interval, outputsize="compact", datatype="json"):
    """
    Get intraday time series for a cryptocurrency.
    Args:
        symbol (str): Crypto symbol (e.g., ETH).
        market (str): Market currency (e.g., USD).
        interval (str): Interval ('1min', '5min', '15min', '30min', '60min').
        outputsize (str): 'compact' or 'full'.
        datatype (str): 'json' or 'csv'.
    Returns:
        dict or str: JSON or CSV data.
    """
    params = {
        "function": "CRYPTO_INTRADAY",
        "symbol": symbol,
        "market": market,
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


def get_crypto_daily(symbol, market, datatype="json"):
    """
    Get daily historical time series for a cryptocurrency.
    Args:
        symbol (str): Crypto symbol (e.g., BTC).
        market (str): Market currency (e.g., EUR).
        datatype (str): 'json' or 'csv'.
    Returns:
        dict or str: JSON or CSV data.
    """
    params = {
        "function": "DIGITAL_CURRENCY_DAILY",
        "symbol": symbol,
        "market": market,
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
