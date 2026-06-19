from .time_series import make_request

def get_sma(symbol: str, interval: str, time_period: int, series_type: str) -> dict:
    """Get Simple Moving Average (SMA) values."""
    return make_request({
        "function": "SMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type
    })

def get_ema(symbol: str, interval: str, time_period: int, series_type: str) -> dict:
    """Get Exponential Moving Average (EMA) values."""
    return make_request({
        "function": "EMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type
    })

def get_rsi(symbol: str, interval: str, time_period: int, series_type: str) -> dict:
    """Get Relative Strength Index (RSI) values."""
    return make_request({
        "function": "RSI",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type
    })

def get_macd(symbol: str, interval: str, series_type: str) -> dict:
    """Get Moving Average Convergence/Divergence (MACD) values."""
    return make_request({
        "function": "MACD",
        "symbol": symbol,
        "interval": interval,
        "series_type": series_type
    })

def get_bbands(symbol: str, interval: str, time_period: int, series_type: str) -> dict:
    """Get Bollinger Bands (BBANDS) values."""
    return make_request({
        "function": "BBANDS",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type
    })
