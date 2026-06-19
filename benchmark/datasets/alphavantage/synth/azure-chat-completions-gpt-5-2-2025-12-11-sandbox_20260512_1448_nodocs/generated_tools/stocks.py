from typing import Any, Dict, Optional

from .client import AlphaVantageClient, safe_validate, normalize_interval, normalize_outputsize


def quote(symbol: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Get latest quote for a stock symbol."""
    c = client or AlphaVantageClient()
    return c.request("GLOBAL_QUOTE", symbol=symbol)


def search_keywords(keywords: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Search for symbols by keywords."""
    c = client or AlphaVantageClient()
    return c.request("SYMBOL_SEARCH", keywords=keywords)


def time_series_intraday(
    symbol: str,
    interval: str = "5min",
    adjusted: bool = True,
    outputsize: str = "compact",
    extended_hours: bool = True,
    month: Optional[str] = None,
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Intraday OHLCV. month is optional (YYYY-MM) for intraday extended history."""
    c = client or AlphaVantageClient()

    _, err = safe_validate(normalize_interval, interval)
    if err:
        return {"error": err}
    _, err = safe_validate(normalize_outputsize, outputsize)
    if err:
        return {"error": err}

    fn = "TIME_SERIES_INTRADAY" if not adjusted else "TIME_SERIES_INTRADAY_ADJUSTED"
    return c.request(
        fn,
        symbol=symbol,
        interval=interval,
        outputsize=outputsize,
        extended_hours="true" if extended_hours else "false",
        month=month,
    )


def time_series_daily(
    symbol: str,
    adjusted: bool = True,
    outputsize: str = "compact",
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    _, err = safe_validate(normalize_outputsize, outputsize)
    if err:
        return {"error": err}
    fn = "TIME_SERIES_DAILY_ADJUSTED" if adjusted else "TIME_SERIES_DAILY"
    return c.request(fn, symbol=symbol, outputsize=outputsize)


def time_series_weekly(symbol: str, adjusted: bool = True, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    fn = "TIME_SERIES_WEEKLY_ADJUSTED" if adjusted else "TIME_SERIES_WEEKLY"
    return c.request(fn, symbol=symbol)


def time_series_monthly(symbol: str, adjusted: bool = True, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    fn = "TIME_SERIES_MONTHLY_ADJUSTED" if adjusted else "TIME_SERIES_MONTHLY"
    return c.request(fn, symbol=symbol)
