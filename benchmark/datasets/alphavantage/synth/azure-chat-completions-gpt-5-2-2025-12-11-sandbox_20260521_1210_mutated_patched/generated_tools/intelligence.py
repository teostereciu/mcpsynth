from typing import Any, Dict, Optional

from .client import av_get


def news_sentiment(
    tickers: Optional[str] = None,
    topics: Optional[str] = None,
    time_from: Optional[str] = None,
    time_to: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "NEWS_SENTIMENT"}
    if tickers:
        params["tickers"] = tickers
    if topics:
        params["topics"] = topics
    if time_from:
        params["time_from"] = time_from
    if time_to:
        params["time_to"] = time_to
    if sort:
        params["sort"] = sort
    if limit is not None:
        params["limit"] = limit
    return av_get(params)


def earnings_call_transcript(ticker: str, quarter: str) -> Dict[str, Any]:
    return av_get({"function": "EARNINGS_CALL_TRANSCRIPT", "symbol": ticker, "quarter": quarter})


def top_gainers_losers(entitlement: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "TOP_GAINERS_LOSERS"}
    if entitlement:
        params["entitlement"] = entitlement
    return av_get(params)


def insider_transactions(ticker: str, from_date: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"function": "INSIDER_TRANSACTIONS", "symbol": ticker}
    if from_date:
        params["from"] = from_date
    return av_get(params)
