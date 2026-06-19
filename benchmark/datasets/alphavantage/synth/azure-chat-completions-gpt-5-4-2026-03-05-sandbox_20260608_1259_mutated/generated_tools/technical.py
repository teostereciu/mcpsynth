from typing import Optional

from generated_tools.common import call_alpha_vantage


def _indicator(
    function_name: str,
    ticker: str,
    time_interval: str,
    month: Optional[str] = None,
    time_period: Optional[int] = None,
    price_type: Optional[str] = None,
    entitlement: Optional[str] = None,
    **extra,
):
    params = {
        "function": function_name,
        "ticker": ticker,
        "time_interval": time_interval,
        "month": month,
        "time_period": time_period,
        "price_type": price_type,
        "entitlement": entitlement,
    }
    params.update(extra)
    return call_alpha_vantage(params)


def get_sma(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
    entitlement: Optional[str] = None,
):
    return _indicator("SMA", ticker, time_interval, month, time_period, price_type, entitlement)


def get_ema(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
    entitlement: Optional[str] = None,
):
    return _indicator("EMA", ticker, time_interval, month, time_period, price_type, entitlement)


def get_rsi(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
    entitlement: Optional[str] = None,
):
    return _indicator("RSI", ticker, time_interval, month, time_period, price_type, entitlement)


def get_macd(
    ticker: str,
    time_interval: str,
    price_type: str,
    month: Optional[str] = None,
    entitlement: Optional[str] = None,
    fastperiod: Optional[int] = None,
    slowperiod: Optional[int] = None,
    signalperiod: Optional[int] = None,
):
    return _indicator(
        "MACD",
        ticker,
        time_interval,
        month,
        None,
        price_type,
        entitlement,
        fastperiod=fastperiod,
        slowperiod=slowperiod,
        signalperiod=signalperiod,
    )


def get_bbands(
    ticker: str,
    time_interval: str,
    time_period: int,
    price_type: str,
    month: Optional[str] = None,
    entitlement: Optional[str] = None,
    nbdevup: Optional[int] = None,
    nbdevdn: Optional[int] = None,
    matype: Optional[int] = None,
):
    return _indicator(
        "BBANDS",
        ticker,
        time_interval,
        month,
        time_period,
        price_type,
        entitlement,
        nbdevup=nbdevup,
        nbdevdn=nbdevdn,
        matype=matype,
    )
