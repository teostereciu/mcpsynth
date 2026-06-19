from .time_series import make_request

def get_crypto_daily(symbol: str, market: str = "USD") -> dict:
    """Get daily cryptocurrency time series data."""
    return make_request({
        "function": "DIGITAL_CURRENCY_DAILY",
        "symbol": symbol,
        "market": market
    })

def get_crypto_weekly(symbol: str, market: str = "USD") -> dict:
    """Get weekly cryptocurrency time series data."""
    return make_request({
        "function": "DIGITAL_CURRENCY_WEEKLY",
        "symbol": symbol,
        "market": market
    })

def get_crypto_monthly(symbol: str, market: str = "USD") -> dict:
    """Get monthly cryptocurrency time series data."""
    return make_request({
        "function": "DIGITAL_CURRENCY_MONTHLY",
        "symbol": symbol,
        "market": market
    })
