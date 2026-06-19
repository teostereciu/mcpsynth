from .common import alpha_vantage_get


def get_digital_currency_daily(symbol: str, market: str = "USD"):
    return alpha_vantage_get({
        "function": "DIGITAL_CURRENCY_DAILY",
        "symbol": symbol,
        "market": market,
    })


def get_digital_currency_weekly(symbol: str, market: str = "USD"):
    return alpha_vantage_get({
        "function": "DIGITAL_CURRENCY_WEEKLY",
        "symbol": symbol,
        "market": market,
    })


def get_digital_currency_monthly(symbol: str, market: str = "USD"):
    return alpha_vantage_get({
        "function": "DIGITAL_CURRENCY_MONTHLY",
        "symbol": symbol,
        "market": market,
    })
