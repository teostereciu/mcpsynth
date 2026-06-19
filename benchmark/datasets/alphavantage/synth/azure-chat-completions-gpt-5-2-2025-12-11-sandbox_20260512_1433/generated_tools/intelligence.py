from typing import Any, Dict, Optional

from .client import AlphaVantageClient


def news_sentiment(
    tickers: Optional[str] = None,
    topics: Optional[str] = None,
    time_from: Optional[str] = None,
    time_to: Optional[str] = None,
    sort: str = "LATEST",
    limit: int = 50,
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Market news and sentiment.

    function=NEWS_SENTIMENT
    """
    c = client or AlphaVantageClient()
    params: Dict[str, Any] = {"function": "NEWS_SENTIMENT", "sort": sort, "limit": str(limit)}
    if tickers:
        params["tickers"] = tickers
    if topics:
        params["topics"] = topics
    if time_from:
        params["time_from"] = time_from
    if time_to:
        params["time_to"] = time_to
    return c.request(params)


def top_gainers_losers(entitlement: Optional[str] = None, client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    """Top gainers, losers, and most actively traded tickers.

    function=TOP_GAINERS_LOSERS
    """
    c = client or AlphaVantageClient()
    params: Dict[str, Any] = {"function": "TOP_GAINERS_LOSERS"}
    if entitlement:
        params["entitlement"] = entitlement
    return c.request(params)


def insider_transactions(
    symbol: str,
    from_date: Optional[str] = None,
    to_date: Optional[str] = None,
    client: Optional[AlphaVantageClient] = None,
) -> Dict[str, Any]:
    """Insider transactions for a company.

    function=INSIDER_TRANSACTIONS

    Note: API uses query params named 'from' and 'to'.
    """
    c = client or AlphaVantageClient()
    params: Dict[str, Any] = {"function": "INSIDER_TRANSACTIONS", "symbol": symbol}
    if from_date:
        params["from"] = from_date
    if to_date:
        params["to"] = to_date
    return c.request(params)
