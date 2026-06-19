from typing import Optional

from generated_tools.common import call_alpha_vantage


def get_news_sentiment(
    tickers: Optional[str] = None,
    topics: Optional[str] = None,
    time_from: Optional[str] = None,
    time_to: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
):
    return call_alpha_vantage(
        {
            "function": "NEWS_SENTIMENT",
            "tickers": tickers,
            "topics": topics,
            "time_from": time_from,
            "time_to": time_to,
            "sort": sort,
            "limit": limit,
        }
    )


def get_earnings_call_transcript(ticker: str, quarter: str):
    return call_alpha_vantage(
        {"function": "EARNINGS_CALL_TRANSCRIPT", "ticker": ticker, "quarter": quarter}
    )


def get_top_gainers_losers(entitlement: Optional[str] = None):
    return call_alpha_vantage({"function": "TOP_GAINERS_LOSERS", "entitlement": entitlement})


def get_insider_transactions(ticker: str, from_date: Optional[str] = None):
    return call_alpha_vantage(
        {"function": "INSIDER_TRANSACTIONS", "ticker": ticker, "from": from_date}
    )
