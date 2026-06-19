from typing import Any, Dict, Optional, Union

from .client import av_get


def crypto_intraday(
    symbol: str,
    market: str,
    interval: str,
    outputsize: Optional[str] = None,
    datatype: Optional[str] = None,
) -> Union[Dict[str, Any], str]:
    """CRYPTO_INTRADAY.

    Doc: docs/api_digital_currency.md
    Endpoint: GET /query?function=CRYPTO_INTRADAY
    """
    params: Dict[str, Any] = {
        "function": "CRYPTO_INTRADAY",
        "symbol": symbol,
        "market": market,
        "interval": interval,
    }
    if outputsize:
        params["outputsize"] = outputsize
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def digital_currency_daily(symbol: str, market: str, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """DIGITAL_CURRENCY_DAILY.

    Doc: docs/api_digital_currency.md
    Endpoint: GET /query?function=DIGITAL_CURRENCY_DAILY
    """
    params: Dict[str, Any] = {"function": "DIGITAL_CURRENCY_DAILY", "symbol": symbol, "market": market}
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def digital_currency_weekly(symbol: str, market: str, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """DIGITAL_CURRENCY_WEEKLY.

    Doc: docs/api_digital_currency.md
    Endpoint: GET /query?function=DIGITAL_CURRENCY_WEEKLY
    """
    params: Dict[str, Any] = {"function": "DIGITAL_CURRENCY_WEEKLY", "symbol": symbol, "market": market}
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def digital_currency_monthly(symbol: str, market: str, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """DIGITAL_CURRENCY_MONTHLY.

    Doc: docs/api_digital_currency.md
    Endpoint: GET /query?function=DIGITAL_CURRENCY_MONTHLY
    """
    params: Dict[str, Any] = {"function": "DIGITAL_CURRENCY_MONTHLY", "symbol": symbol, "market": market}
    if datatype:
        params["datatype"] = datatype
    return av_get(params)
