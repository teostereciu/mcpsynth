from typing import Any, Dict, Optional, Union

from .client import av_get


def fx_exchange_rate(from_currency: str, to_currency: str) -> Dict[str, Any]:
    """CURRENCY_EXCHANGE_RATE (FX).

    Doc: docs/api_fx.md
    Endpoint: GET /query?function=CURRENCY_EXCHANGE_RATE
    """
    return av_get(
        {"function": "CURRENCY_EXCHANGE_RATE", "from_currency": from_currency, "to_currency": to_currency}
    )  # type: ignore[return-value]


def fx_intraday(
    from_symbol: str,
    to_symbol: str,
    interval: str,
    outputsize: Optional[str] = None,
    datatype: Optional[str] = None,
) -> Union[Dict[str, Any], str]:
    """FX_INTRADAY.

    Doc: docs/api_fx.md
    Endpoint: GET /query?function=FX_INTRADAY
    """
    params: Dict[str, Any] = {
        "function": "FX_INTRADAY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "interval": interval,
    }
    if outputsize:
        params["outputsize"] = outputsize
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def fx_daily(
    from_symbol: str,
    to_symbol: str,
    outputsize: Optional[str] = None,
    datatype: Optional[str] = None,
) -> Union[Dict[str, Any], str]:
    """FX_DAILY.

    Doc: docs/api_fx.md
    Endpoint: GET /query?function=FX_DAILY
    """
    params: Dict[str, Any] = {"function": "FX_DAILY", "from_symbol": from_symbol, "to_symbol": to_symbol}
    if outputsize:
        params["outputsize"] = outputsize
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def fx_weekly(from_symbol: str, to_symbol: str, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """FX_WEEKLY.

    Doc: docs/api_fx.md
    Endpoint: GET /query?function=FX_WEEKLY
    """
    params: Dict[str, Any] = {"function": "FX_WEEKLY", "from_symbol": from_symbol, "to_symbol": to_symbol}
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def fx_monthly(from_symbol: str, to_symbol: str, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """FX_MONTHLY.

    Doc: docs/api_fx.md
    Endpoint: GET /query?function=FX_MONTHLY
    """
    params: Dict[str, Any] = {"function": "FX_MONTHLY", "from_symbol": from_symbol, "to_symbol": to_symbol}
    if datatype:
        params["datatype"] = datatype
    return av_get(params)
