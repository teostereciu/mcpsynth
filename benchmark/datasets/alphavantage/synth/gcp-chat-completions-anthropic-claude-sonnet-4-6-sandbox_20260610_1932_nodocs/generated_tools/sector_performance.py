"""
Alpha Vantage — Sector Performance tools
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
        if "Information" in data:
            return {"error": data["Information"]}
        if "Note" in data:
            return {"error": data["Note"]}
        return data
    except requests.exceptions.RequestException as exc:
        return {"error": str(exc)}
    except ValueError as exc:
        return {"error": f"JSON decode error: {exc}"}


def get_sector_performance() -> dict:
    """
    Fetch real-time and historical sector performance data for the S&P 500.

    Returns performance rankings across 11 GICS sectors for multiple time
    horizons: real-time (1 day), 5 days, 1 month, 3 months, year-to-date,
    1 year, 3 years, 5 years, and 10 years.

    Sectors covered:
        Information Technology, Health Care, Financials, Consumer Discretionary,
        Communication Services, Industrials, Consumer Staples, Energy, Utilities,
        Real Estate, Materials.

    Returns:
        Dict with metadata and sector performance percentages for each time horizon.
    """
    return _get({
        "function": "SECTOR",
    })
