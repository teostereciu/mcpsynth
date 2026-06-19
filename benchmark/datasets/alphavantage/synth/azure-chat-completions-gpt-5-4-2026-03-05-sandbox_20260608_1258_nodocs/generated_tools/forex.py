from .common import alpha_vantage_get


def get_currency_exchange_rate(from_currency: str, to_currency: str):
    return alpha_vantage_get({
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": from_currency,
        "to_currency": to_currency,
    })


def get_fx_daily(from_symbol: str, to_symbol: str, outputsize: str = "compact"):
    return alpha_vantage_get({
        "function": "FX_DAILY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "outputsize": outputsize,
    })


def get_fx_weekly(from_symbol: str, to_symbol: str):
    return alpha_vantage_get({
        "function": "FX_WEEKLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
    })


def get_fx_monthly(from_symbol: str, to_symbol: str):
    return alpha_vantage_get({
        "function": "FX_MONTHLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
    })
