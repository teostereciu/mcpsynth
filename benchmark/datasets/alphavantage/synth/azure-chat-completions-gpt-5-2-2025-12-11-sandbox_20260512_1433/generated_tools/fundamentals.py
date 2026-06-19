from typing import Any, Dict, Optional

from .client import AlphaVantageClient


def company_overview(symbol: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Company overview and key metrics.

    function=OVERVIEW
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "OVERVIEW", "symbol": symbol})


def income_statement(symbol: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Annual and quarterly income statements.

    function=INCOME_STATEMENT
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "INCOME_STATEMENT", "symbol": symbol})


def balance_sheet(symbol: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Annual and quarterly balance sheets.

    function=BALANCE_SHEET
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "BALANCE_SHEET", "symbol": symbol})


def cash_flow(symbol: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Annual and quarterly cash flow statements.

    function=CASH_FLOW
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "CASH_FLOW", "symbol": symbol})


def earnings(symbol: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Annual and quarterly earnings.

    function=EARNINGS
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "EARNINGS", "symbol": symbol})


def earnings_estimates(symbol: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Earnings estimates.

    function=EARNINGS_ESTIMATES
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "EARNINGS_ESTIMATES", "symbol": symbol})


def earnings_calendar(
    horizon: str = "3month",
    symbol: Optional[str] = None,
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Earnings calendar (CSV response).

    function=EARNINGS_CALENDAR
    """
    c = client or AlphaVantageClient()
    params: Dict[str, Any] = {"function": "EARNINGS_CALENDAR", "horizon": horizon}
    if symbol:
        params["symbol"] = symbol
    # This endpoint returns CSV by default
    params["datatype"] = "csv"
    return c.request(params)


def etf_profile(symbol: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """ETF profile and holdings.

    function=ETF_PROFILE
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "ETF_PROFILE", "symbol": symbol})


def dividends(symbol: str, datatype: str = "json", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Dividend distributions.

    function=DIVIDENDS
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "DIVIDENDS", "symbol": symbol, "datatype": datatype})


def splits(symbol: str, datatype: str = "json", client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Split events.

    function=SPLITS
    """
    c = client or AlphaVantageClient()
    return c.request({"function": "SPLITS", "symbol": symbol, "datatype": datatype})
