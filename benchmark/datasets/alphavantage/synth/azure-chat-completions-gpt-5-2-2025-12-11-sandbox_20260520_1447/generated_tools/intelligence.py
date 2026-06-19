from typing import Any, Dict, Optional, Union

from .client import av_get


def news_sentiment(
    tickers: Optional[str] = None,
    topics: Optional[str] = None,
    time_from: Optional[str] = None,
    time_to: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
    """NEWS_SENTIMENT.

    Doc: docs/api_intelligence.md
    Endpoint: GET /query?function=NEWS_SENTIMENT
    """
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
    return av_get(params)  # type: ignore[return-value]


def earnings_call_transcript(symbol: str, quarter: str) -> Dict[str, Any]:
    """EARNINGS_CALL_TRANSCRIPT.

    Doc: docs/api_intelligence.md
    Endpoint: GET /query?function=EARNINGS_CALL_TRANSCRIPT
    """
    return av_get({"function": "EARNINGS_CALL_TRANSCRIPT", "symbol": symbol, "quarter": quarter})  # type: ignore[return-value]


def top_gainers_losers(entitlement: Optional[str] = None) -> Dict[str, Any]:
    """TOP_GAINERS_LOSERS.

    Doc: docs/api_intelligence.md
    Endpoint: GET /query?function=TOP_GAINERS_LOSERS
    """
    params: Dict[str, Any] = {"function": "TOP_GAINERS_LOSERS"}
    if entitlement:
        params["entitlement"] = entitlement
    return av_get(params)  # type: ignore[return-value]


def insider_transactions(symbol: str, from_date: Optional[str] = None) -> Dict[str, Any]:
    """INSIDER_TRANSACTIONS.

    Doc: docs/api_intelligence.md
    Endpoint: GET /query?function=INSIDER_TRANSACTIONS
    """
    params: Dict[str, Any] = {"function": "INSIDER_TRANSACTIONS", "symbol": symbol}
    if from_date:
        params["from"] = from_date
    return av_get(params)  # type: ignore[return-value]
