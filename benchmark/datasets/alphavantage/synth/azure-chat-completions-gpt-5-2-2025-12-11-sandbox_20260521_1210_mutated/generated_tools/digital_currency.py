from typing import Any, Dict, Optional

from .client import av_get


def crypto_intraday(
    ticker: str,
    market: str,
    time_interval: str,
    output_size: Optional[str] = None,
    format: Optional[str] = None,
) -> Dict[str, Any]:
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
    return av_get(params)


def digital_currency_daily(ticker: str, market: str, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "DIGITAL_CURRENCY_DAILY", "ticker": ticker, "market": market}
    if format:
        params["format"] = format
    return av_get(params)


def digital_currency_weekly(ticker: str, market: str, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "DIGITAL_CURRENCY_WEEKLY", "ticker": ticker, "market": market}
    if format:
        params["format"] = format
    return av_get(params)


def digital_currency_monthly(ticker: str, market: str, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "DIGITAL_CURRENCY_MONTHLY", "ticker": ticker, "market": market}
    if format:
        params["format"] = format
    return av_get(params)
