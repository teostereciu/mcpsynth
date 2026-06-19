from typing import Any, Dict, Optional

from .client import AlphaVantageClient


def fx_exchange_rate(
    from_currency: str,
    to_currency: str,
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Realtime exchange rate for a pair of currencies.

    function=CURRENCY_EXCHANGE_RATE
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "CURRENCY_EXCHANGE_RATE", "from_currency": from_currency, "to_currency": to_currency})


def fx_intraday(
    from_symbol: str,
    to_symbol: str,
    interval: str,
    outputsize: Optional[str] = None,
    datatype: str = "json",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Intraday FX time series.

    function=FX_INTRADAY
    """
    c = client or AlphaVantageClient()
    params: Dict[str, Any] = {
        "function": "FX_INTRADAY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "interval": interval,
        "datatype": datatype,
    }
    if outputsize:
        params["outputsize"] = outputsize
    return c.request(params)


def fx_daily(
    from_symbol: str,
    to_symbol: str,
    outputsize: Optional[str] = None,
    datatype: str = "json",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Daily FX time series.

    function=FX_DAILY
    """
    c = client or AlphaVantageClient()
    params: Dict[str, Any] = {"function": "FX_DAILY", "from_symbol": from_symbol, "to_symbol": to_symbol, "datatype": datatype}
    if outputsize:
        params["outputsize"] = outputsize
    return c.request(params)


def fx_weekly(
    from_symbol: str,
    to_symbol: str,
    datatype: str = "json",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Weekly FX time series.

    function=FX_WEEKLY
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "FX_WEEKLY", "from_symbol": from_symbol, "to_symbol": to_symbol, "datatype": datatype})


def fx_monthly(
    from_symbol: str,
    to_symbol: str,
    datatype: str = "json",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Monthly FX time series.

    function=FX_MONTHLY
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "FX_MONTHLY", "from_symbol": from_symbol, "to_symbol": to_symbol, "datatype": datatype})
