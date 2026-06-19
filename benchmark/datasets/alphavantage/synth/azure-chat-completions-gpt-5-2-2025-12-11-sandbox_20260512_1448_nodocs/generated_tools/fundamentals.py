from typing import Any, Dict, Optional

from .client import AlphaVantageClient


def company_overview(symbol: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    return c.request("OVERVIEW", symbol=symbol)


def income_statement(symbol: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    return c.request("INCOME_STATEMENT", symbol=symbol)


def balance_sheet(symbol: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    return c.request("BALANCE_SHEET", symbol=symbol)


def earnings(symbol: str, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    return c.request("EARNINGS", symbol=symbol)
