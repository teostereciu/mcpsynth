from typing import Optional

from generated_tools.common import call_alpha_vantage


def get_gold_silver_spot(ticker: str):
    return call_alpha_vantage({"function": "GOLD_SILVER_SPOT", "symbol": ticker})


def get_gold_silver_history(ticker: str, time_interval: str):
    return call_alpha_vantage(
        {"function": "GOLD_SILVER_HISTORY", "symbol": ticker, "interval": time_interval}
    )


def _commodity(function_name: str, time_interval: Optional[str] = None):
    return call_alpha_vantage(
        {"function": function_name, "interval": time_interval}
    )


def get_wti(time_interval: Optional[str] = None):
    return _commodity("WTI", time_interval)


def get_brent(time_interval: Optional[str] = None):
    return _commodity("BRENT", time_interval)


def get_natural_gas(time_interval: Optional[str] = None):
    return _commodity("NATURAL_GAS", time_interval)


def get_copper(time_interval: Optional[str] = None):
    return _commodity("COPPER", time_interval)


def get_aluminum(time_interval: Optional[str] = None):
    return _commodity("ALUMINUM", time_interval)


def get_wheat(time_interval: Optional[str] = None):
    return _commodity("WHEAT", time_interval)


def get_corn(time_interval: Optional[str] = None):
    return _commodity("CORN", time_interval)


def get_cotton(time_interval: Optional[str] = None):
    return _commodity("COTTON", time_interval)


def get_sugar(time_interval: Optional[str] = None):
    return _commodity("SUGAR", time_interval)


def get_coffee(time_interval: Optional[str] = None):
    return _commodity("COFFEE", time_interval)
