from typing import Any, Dict, Optional

from .alphavantage_client import call_alpha_vantage


def crypto_intraday(
    ticker: str,
    market: str,
    time_interval: str,
    output_size: Optional[str] = "compact",
    format: Optional[str] = "json",
) -> Dict[str, Any]:
    """CRYPTO_INTRADAY.

    Doc: docs/api_digital_currency.md
    """
    params: Dict[str, Any] = {
        "function": "CRYPTO_INTRADAY",
        "symbol": ticker,
        "market": market,
        "interval": time_interval,
    }
    if output_size:
        params["outputsize"] = output_size
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def digital_currency_daily(ticker: str, market: str, format: Optional[str] = "json") -> Dict[str, Any]:
    """DIGITAL_CURRENCY_DAILY.

    Doc: docs/api_digital_currency.md
    """
    params: Dict[str, Any] = {"function": "DIGITAL_CURRENCY_DAILY", "symbol": ticker, "market": market}
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def digital_currency_weekly(ticker: str, market: str, format: Optional[str] = "json") -> Dict[str, Any]:
    """DIGITAL_CURRENCY_WEEKLY.

    Doc: docs/api_digital_currency.md
    """
    params: Dict[str, Any] = {"function": "DIGITAL_CURRENCY_WEEKLY", "symbol": ticker, "market": market}
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def digital_currency_monthly(ticker: str, market: str, format: Optional[str] = "json") -> Dict[str, Any]:
    """DIGITAL_CURRENCY_MONTHLY.

    Doc: docs/api_digital_currency.md
    """
    params: Dict[str, Any] = {"function": "DIGITAL_CURRENCY_MONTHLY", "symbol": ticker, "market": market}
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)
