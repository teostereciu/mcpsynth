from typing import Optional

from generated_tools.common import alpha_vantage_get, build_result


def get_currency_exchange_rate(from_currency: str, to_currency: str):
    params = {"function": "CURRENCY_EXCHANGE_RATE", "from_currency": from_currency, "to_currency": to_currency}
    return build_result("get_currency_exchange_rate", params, alpha_vantage_get(params))


def get_fx_intraday(from_symbol: str, to_symbol: str, interval: str, outputsize: Optional[str] = None):
    params = {
        "function": "FX_INTRADAY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "interval": interval,
        "outputsize": outputsize,
    }
    return build_result("get_fx_intraday", params, alpha_vantage_get(params))


def get_fx_daily(from_symbol: str, to_symbol: str, outputsize: Optional[str] = None):
    params = {"function": "FX_DAILY", "from_symbol": from_symbol, "to_symbol": to_symbol, "outputsize": outputsize}
    return build_result("get_fx_daily", params, alpha_vantage_get(params))


def get_fx_weekly(from_symbol: str, to_symbol: str):
    params = {"function": "FX_WEEKLY", "from_symbol": from_symbol, "to_symbol": to_symbol}
    return build_result("get_fx_weekly", params, alpha_vantage_get(params))


def get_fx_monthly(from_symbol: str, to_symbol: str):
    params = {"function": "FX_MONTHLY", "from_symbol": from_symbol, "to_symbol": to_symbol}
    return build_result("get_fx_monthly", params, alpha_vantage_get(params))
