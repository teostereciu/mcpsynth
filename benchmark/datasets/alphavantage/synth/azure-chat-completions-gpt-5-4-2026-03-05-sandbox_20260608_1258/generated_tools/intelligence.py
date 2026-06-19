from typing import Optional

from generated_tools.common import alpha_vantage_get, build_result


def get_news_sentiment(tickers: Optional[str] = None, topics: Optional[str] = None, time_from: Optional[str] = None, time_to: Optional[str] = None, sort: Optional[str] = None, limit: Optional[int] = None):
    params = {
        "function": "NEWS_SENTIMENT",
        "tickers": tickers,
        "topics": topics,
        "time_from": time_from,
        "time_to": time_to,
        "sort": sort,
        "limit": limit,
    }
    return build_result("get_news_sentiment", params, alpha_vantage_get(params))


def get_earnings_call_transcript(symbol: str, quarter: str):
    params = {"function": "EARNINGS_CALL_TRANSCRIPT", "symbol": symbol, "quarter": quarter}
    return build_result("get_earnings_call_transcript", params, alpha_vantage_get(params))


def get_top_gainers_losers(entitlement: Optional[str] = None):
    params = {"function": "TOP_GAINERS_LOSERS", "entitlement": entitlement}
    return build_result("get_top_gainers_losers", params, alpha_vantage_get(params))


def get_insider_transactions(symbol: str, from_date: Optional[str] = None):
    params = {"function": "INSIDER_TRANSACTIONS", "symbol": symbol, "from": from_date}
    return build_result("get_insider_transactions", params, alpha_vantage_get(params))
