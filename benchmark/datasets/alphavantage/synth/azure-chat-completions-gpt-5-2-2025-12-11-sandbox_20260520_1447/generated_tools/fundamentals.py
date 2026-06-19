from typing import Any, Dict, Optional, Union

from .client import av_get


def company_overview(symbol: str) -> Dict[str, Any]:
    """OVERVIEW.

    Doc: docs/api_fundamentals.md
    Endpoint: GET /query?function=OVERVIEW
    """
    return av_get({"function": "OVERVIEW", "symbol": symbol})  # type: ignore[return-value]


def etf_profile(symbol: str) -> Dict[str, Any]:
    """ETF_PROFILE.

    Doc: docs/api_fundamentals.md
    Endpoint: GET /query?function=ETF_PROFILE
    """
    return av_get({"function": "ETF_PROFILE", "symbol": symbol})  # type: ignore[return-value]


def dividends(symbol: str, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """DIVIDENDS.

    Doc: docs/api_fundamentals.md
    Endpoint: GET /query?function=DIVIDENDS
    """
    params: Dict[str, Any] = {"function": "DIVIDENDS", "symbol": symbol}
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def splits(symbol: str, datatype: Optional[str] = None) -> Union[Dict[str, Any], str]:
    """SPLITS.

    Doc: docs/api_fundamentals.md
    Endpoint: GET /query?function=SPLITS
    """
    params: Dict[str, Any] = {"function": "SPLITS", "symbol": symbol}
    if datatype:
        params["datatype"] = datatype
    return av_get(params)


def income_statement(symbol: str) -> Dict[str, Any]:
    """INCOME_STATEMENT.

    Doc: docs/api_fundamentals.md
    Endpoint: GET /query?function=INCOME_STATEMENT
    """
    return av_get({"function": "INCOME_STATEMENT", "symbol": symbol})  # type: ignore[return-value]


def balance_sheet(symbol: str) -> Dict[str, Any]:
    """BALANCE_SHEET.

    Doc: docs/api_fundamentals.md
    Endpoint: GET /query?function=BALANCE_SHEET
    """
    return av_get({"function": "BALANCE_SHEET", "symbol": symbol})  # type: ignore[return-value]


def cash_flow(symbol: str) -> Dict[str, Any]:
    """CASH_FLOW.

    Doc: docs/api_fundamentals.md
    Endpoint: GET /query?function=CASH_FLOW
    """
    return av_get({"function": "CASH_FLOW", "symbol": symbol})  # type: ignore[return-value]


def earnings(symbol: str) -> Dict[str, Any]:
    """EARNINGS.

    Doc: docs/api_fundamentals.md
    Endpoint: GET /query?function=EARNINGS
    """
    return av_get({"function": "EARNINGS", "symbol": symbol})  # type: ignore[return-value]
