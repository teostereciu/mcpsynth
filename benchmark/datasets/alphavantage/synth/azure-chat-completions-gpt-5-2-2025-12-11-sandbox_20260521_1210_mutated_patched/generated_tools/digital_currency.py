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
        "symbol": ticker,
        "market": market,
        "interval": time_interval,
    }
    if output_size:
        params["outputsize"] = output_size
    if format:
        params["datatype"] = format
    return av_get(params)


def digital_currency_daily(ticker: str, market: str, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "DIGITAL_CURRENCY_DAILY", "symbol": ticker, "market": market}
    if format:
        params["datatype"] = format
    return av_get(params)


def digital_currency_weekly(ticker: str, market: str, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "DIGITAL_CURRENCY_WEEKLY", "symbol": ticker, "market": market}
    if format:
        params["datatype"] = format
    return av_get(params)


def digital_currency_monthly(ticker: str, market: str, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "DIGITAL_CURRENCY_MONTHLY", "symbol": ticker, "market": market}
    if format:
        params["datatype"] = format
    return av_get(params)
