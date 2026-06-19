from typing import Any, Dict, Optional

from .client import call_alpha_vantage


def news_sentiment(
    tickers: Optional[str] = None,
    topics: Optional[str] = None,
    time_from: Optional[str] = None,
    time_to: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "NEWS_SENTIMENT"}
    if tickers is not None:
        params["tickers"] = tickers
    if topics is not None:
        params["topics"] = topics
    if time_from is not None:
        params["time_from"] = time_from
    if time_to is not None:
        params["time_to"] = time_to
    if sort is not None:
        params["sort"] = sort
    if limit is not None:
        params["limit"] = limit
    return call_alpha_vantage(params)


def earnings_call_transcript(symbol: str, quarter: str) -> Dict[str, Any]:
    return call_alpha_vantage({"function": "EARNINGS_CALL_TRANSCRIPT", "symbol": symbol, "quarter": quarter})


def top_gainers_losers(entitlement: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "TOP_GAINERS_LOSERS"}
    if entitlement is not None:
        params["entitlement"] = entitlement
    return call_alpha_vantage(params)


def insider_transactions(symbol: str, from_date: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "INSIDER_TRANSACTIONS", "symbol": symbol}
    if from_date is not None:
        params["from"] = from_date
    return call_alpha_vantage(params)
