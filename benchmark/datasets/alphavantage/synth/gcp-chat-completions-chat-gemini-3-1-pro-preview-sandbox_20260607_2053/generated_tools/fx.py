from .time_series import make_request

def get_exchange_rate(from_currency: str, to_currency: str) -> dict:
    """Get the real-time exchange rate for any pair of digital currency or fiat currency."""
    return make_request({
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": from_currency,
        "to_currency": to_currency
    })

def get_fx_daily(from_symbol: str, to_symbol: str) -> dict:
    """Get daily forex time series data."""
    return make_request({
        "function": "FX_DAILY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol
    })

def get_fx_weekly(from_symbol: str, to_symbol: str) -> dict:
    """Get weekly forex time series data."""
    return make_request({
        "function": "FX_WEEKLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol
    })

def get_fx_monthly(from_symbol: str, to_symbol: str) -> dict:
    """Get monthly forex time series data."""
    return make_request({
        "function": "FX_MONTHLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol
    })
