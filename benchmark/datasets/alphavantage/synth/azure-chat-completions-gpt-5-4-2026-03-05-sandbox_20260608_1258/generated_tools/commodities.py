from typing import Optional

from generated_tools.common import alpha_vantage_get, build_result


def get_gold_silver_spot(symbol: str):
    params = {"function": "GOLD_SILVER_SPOT", "symbol": symbol}
    return build_result("get_gold_silver_spot", params, alpha_vantage_get(params))


def get_gold_silver_history(symbol: str, interval: str):
    params = {"function": "GOLD_SILVER_HISTORY", "symbol": symbol, "interval": interval}
    return build_result("get_gold_silver_history", params, alpha_vantage_get(params))


def get_wti(interval: Optional[str] = None):
    params = {"function": "WTI", "interval": interval}
    return build_result("get_wti", params, alpha_vantage_get(params))


def get_brent(interval: Optional[str] = None):
    params = {"function": "BRENT", "interval": interval}
    return build_result("get_brent", params, alpha_vantage_get(params))


def get_natural_gas(interval: Optional[str] = None):
    params = {"function": "NATURAL_GAS", "interval": interval}
    return build_result("get_natural_gas", params, alpha_vantage_get(params))


def get_copper(interval: Optional[str] = None):
    params = {"function": "COPPER", "interval": interval}
    return build_result("get_copper", params, alpha_vantage_get(params))


def get_aluminum(interval: Optional[str] = None):
    params = {"function": "ALUMINUM", "interval": interval}
    return build_result("get_aluminum", params, alpha_vantage_get(params))


def get_wheat(interval: Optional[str] = None):
    params = {"function": "WHEAT", "interval": interval}
    return build_result("get_wheat", params, alpha_vantage_get(params))


def get_corn(interval: Optional[str] = None):
    params = {"function": "CORN", "interval": interval}
    return build_result("get_corn", params, alpha_vantage_get(params))


def get_cotton(interval: Optional[str] = None):
    params = {"function": "COTTON", "interval": interval}
    return build_result("get_cotton", params, alpha_vantage_get(params))


def get_sugar(interval: Optional[str] = None):
    params = {"function": "SUGAR", "interval": interval}
    return build_result("get_sugar", params, alpha_vantage_get(params))


def get_coffee(interval: Optional[str] = None):
    params = {"function": "COFFEE", "interval": interval}
    return build_result("get_coffee", params, alpha_vantage_get(params))
