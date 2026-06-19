from typing import Optional

from generated_tools.common import alpha_vantage_get, build_result


def _indicator(function_name: str, **kwargs):
    params = {"function": function_name, **kwargs}
    return build_result(function_name.lower(), params, alpha_vantage_get(params))


def get_sma(symbol: str, interval: str, time_period: int, series_type: str, month: Optional[str] = None, entitlement: Optional[str] = None):
    return _indicator("SMA", symbol=symbol, interval=interval, time_period=time_period, series_type=series_type, month=month, entitlement=entitlement)


def get_ema(symbol: str, interval: str, time_period: int, series_type: str, month: Optional[str] = None, entitlement: Optional[str] = None):
    return _indicator("EMA", symbol=symbol, interval=interval, time_period=time_period, series_type=series_type, month=month, entitlement=entitlement)


def get_rsi(symbol: str, interval: str, time_period: int, series_type: str, month: Optional[str] = None, entitlement: Optional[str] = None):
    return _indicator("RSI", symbol=symbol, interval=interval, time_period=time_period, series_type=series_type, month=month, entitlement=entitlement)


def get_macd(symbol: str, interval: str, series_type: str, month: Optional[str] = None, entitlement: Optional[str] = None):
    return _indicator("MACD", symbol=symbol, interval=interval, series_type=series_type, month=month, entitlement=entitlement)


def get_bbands(symbol: str, interval: str, time_period: int, series_type: str, nbdevup: Optional[int] = None, nbdevdn: Optional[int] = None, matype: Optional[int] = None, month: Optional[str] = None, entitlement: Optional[str] = None):
    return _indicator("BBANDS", symbol=symbol, interval=interval, time_period=time_period, series_type=series_type, nbdevup=nbdevup, nbdevdn=nbdevdn, matype=matype, month=month, entitlement=entitlement)
