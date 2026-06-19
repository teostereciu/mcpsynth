from typing import Any, Dict, Optional

from .client import AlphaVantageClient


def crypto_intraday(
    symbol: str,
    market: str,
    interval: str,
    outputsize: Optional[str] = None,
    datatype: str = "json",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Intraday crypto time series.

    function=CRYPTO_INTRADAY
    """
    c = client or AlphaVantageClient()
    params: Dict[str, Any] = {
        "function": "CRYPTO_INTRADAY",
        "symbol": symbol,
        "market": market,
        "interval": interval,
        "datatype": datatype,
    }
    if outputsize:
        params["outputsize"] = outputsize
    return c.request(params)


def digital_currency_daily(
    symbol: str,
    market: str,
    datatype: str = "json",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Daily crypto historical time series.

    function=DIGITAL_CURRENCY_DAILY
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "DIGITAL_CURRENCY_DAILY", "symbol": symbol, "market": market, "datatype": datatype})


def digital_currency_weekly(
    symbol: str,
    market: str,
    datatype: str = "json",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Weekly crypto historical time series.

    function=DIGITAL_CURRENCY_WEEKLY
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "DIGITAL_CURRENCY_WEEKLY", "symbol": symbol, "market": market, "datatype": datatype})


def digital_currency_monthly(
    symbol: str,
    market: str,
    datatype: str = "json",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Monthly crypto historical time series.

    function=DIGITAL_CURRENCY_MONTHLY
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "DIGITAL_CURRENCY_MONTHLY", "symbol": symbol, "market": market, "datatype": datatype})
