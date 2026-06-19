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
        "ticker": ticker,
        "market": market,
        "time_interval": time_interval,
    }
    if output_size:
        params["output_size"] = output_size
    if format:
        params["format"] = format
    return call_alpha_vantage(params)


def digital_currency_daily(ticker: str, market: str, format: Optional[str] = "json") -> Dict[str, Any]:
    """DIGITAL_CURRENCY_DAILY.

    Doc: docs/api_digital_currency.md
    """
    params: Dict[str, Any] = {"function": "DIGITAL_CURRENCY_DAILY", "ticker": ticker, "market": market}
    if format:
        params["format"] = format
    return call_alpha_vantage(params)


def digital_currency_weekly(ticker: str, market: str, format: Optional[str] = "json") -> Dict[str, Any]:
    """DIGITAL_CURRENCY_WEEKLY.

    Doc: docs/api_digital_currency.md
    """
    params: Dict[str, Any] = {"function": "DIGITAL_CURRENCY_WEEKLY", "ticker": ticker, "market": market}
    if format:
        params["format"] = format
    return call_alpha_vantage(params)


def digital_currency_monthly(ticker: str, market: str, format: Optional[str] = "json") -> Dict[str, Any]:
    """DIGITAL_CURRENCY_MONTHLY.

    Doc: docs/api_digital_currency.md
    """
    params: Dict[str, Any] = {"function": "DIGITAL_CURRENCY_MONTHLY", "ticker": ticker, "market": market}
    if format:
        params["format"] = format
    return call_alpha_vantage(params)
