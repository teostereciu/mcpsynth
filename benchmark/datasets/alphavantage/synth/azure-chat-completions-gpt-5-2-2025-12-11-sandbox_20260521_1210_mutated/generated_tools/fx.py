from typing import Any, Dict, Optional

from .client import av_get


def fx_exchange_rate(from_currency: str, to_currency: str) -> Dict[str, Any]:
    return av_get(
        {
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": from_currency,
            "to_currency": to_currency,
        }
    )


def fx_intraday(
    from_symbol: str,
    to_symbol: str,
    time_interval: str,
    output_size: Optional[str] = None,
    format: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "function": "FX_INTRADAY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "time_interval": time_interval,
    }
    if output_size:
        params["output_size"] = output_size
    if format:
        params["format"] = format
    return av_get(params)


def fx_daily(
    from_symbol: str,
    to_symbol: str,
    output_size: Optional[str] = None,
    format: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "FX_DAILY", "from_symbol": from_symbol, "to_symbol": to_symbol}
    if output_size:
        params["output_size"] = output_size
    if format:
        params["format"] = format
    return av_get(params)


def fx_weekly(from_symbol: str, to_symbol: str, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "FX_WEEKLY", "from_symbol": from_symbol, "to_symbol": to_symbol}
    if format:
        params["format"] = format
    return av_get(params)


def fx_monthly(from_symbol: str, to_symbol: str, format: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "FX_MONTHLY", "from_symbol": from_symbol, "to_symbol": to_symbol}
    if format:
        params["format"] = format
    return av_get(params)
