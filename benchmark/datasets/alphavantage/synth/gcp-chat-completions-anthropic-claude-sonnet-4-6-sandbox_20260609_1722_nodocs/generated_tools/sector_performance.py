"""
Alpha Vantage – Sector Performance tools
Covers: real-time and historical sector performance across the S&P 500
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


def get_sector_performance() -> dict:
    """
    Return real-time and historical sector performance data across the S&P 500.

    Returns performance metrics for 11 GICS sectors over multiple time horizons:
    real-time, 1-day, 5-day, 1-month, 3-month, year-to-date, 1-year, 3-year,
    5-year, and 10-year.
    """
    return _get({"function": "SECTOR"})
