from .common import alpha_vantage_get


def get_sma(symbol: str, interval: str, time_period: int, series_type: str = "close"):
    return alpha_vantage_get({
        "function": "SMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    })


def get_ema(symbol: str, interval: str, time_period: int, series_type: str = "close"):
    return alpha_vantage_get({
        "function": "EMA",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    })


def get_rsi(symbol: str, interval: str, time_period: int = 14, series_type: str = "close"):
    return alpha_vantage_get({
        "function": "RSI",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
    })


def get_macd(symbol: str, interval: str, series_type: str = "close", fastperiod: int = 12, slowperiod: int = 26, signalperiod: int = 9):
    return alpha_vantage_get({
        "function": "MACD",
        "symbol": symbol,
        "interval": interval,
        "series_type": series_type,
        "fastperiod": fastperiod,
        "slowperiod": slowperiod,
        "signalperiod": signalperiod,
    })


def get_bbands(symbol: str, interval: str, time_period: int = 20, series_type: str = "close", nbdevup: int = 2, nbdevdn: int = 2):
    return alpha_vantage_get({
        "function": "BBANDS",
        "symbol": symbol,
        "interval": interval,
        "time_period": time_period,
        "series_type": series_type,
        "nbdevup": nbdevup,
        "nbdevdn": nbdevdn,
    })
