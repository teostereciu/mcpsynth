from typing import Any, Dict, Optional

from .alphavantage_client import call_alpha_vantage


def fx_exchange_rate(from_currency: str, to_currency: str) -> Dict[str, Any]:
    """CURRENCY_EXCHANGE_RATE.

    Doc: docs/api_fx.md
    """
    return call_alpha_vantage(
        {"function": "CURRENCY_EXCHANGE_RATE", "from_currency": from_currency, "to_currency": to_currency}
    )


def fx_intraday(
    from_symbol: str,
    to_symbol: str,
    time_interval: str,
    output_size: Optional[str] = "compact",
    format: Optional[str] = "json",
) -> Dict[str, Any]:
    """FX_INTRADAY.

    Doc: docs/api_fx.md
    """
    params: Dict[str, Any] = {
        "function": "FX_INTRADAY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "interval": time_interval,
    }
    if output_size:
        params["outputsize"] = output_size
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def fx_daily(
    from_symbol: str,
    to_symbol: str,
    output_size: Optional[str] = "compact",
    format: Optional[str] = "json",
) -> Dict[str, Any]:
    """FX_DAILY.

    Doc: docs/api_fx.md
    """
    params: Dict[str, Any] = {"function": "FX_DAILY", "from_symbol": from_symbol, "to_symbol": to_symbol}
    if output_size:
        params["outputsize"] = output_size
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def fx_weekly(from_symbol: str, to_symbol: str, format: Optional[str] = "json") -> Dict[str, Any]:
    """FX_WEEKLY.

    Doc: docs/api_fx.md
    """
    params: Dict[str, Any] = {"function": "FX_WEEKLY", "from_symbol": from_symbol, "to_symbol": to_symbol}
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)


def fx_monthly(from_symbol: str, to_symbol: str, format: Optional[str] = "json") -> Dict[str, Any]:
    """FX_MONTHLY.

    Doc: docs/api_fx.md
    """
    params: Dict[str, Any] = {"function": "FX_MONTHLY", "from_symbol": from_symbol, "to_symbol": to_symbol}
    if format:
        params["datatype"] = format
    return call_alpha_vantage(params)
