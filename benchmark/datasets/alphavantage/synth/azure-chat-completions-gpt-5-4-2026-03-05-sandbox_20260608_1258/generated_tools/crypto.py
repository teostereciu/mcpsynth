from typing import Optional

from generated_tools.common import alpha_vantage_get, build_result


def get_crypto_exchange_rate(from_currency: str, to_currency: str):
    params = {"function": "CURRENCY_EXCHANGE_RATE", "from_currency": from_currency, "to_currency": to_currency}
    return build_result("get_crypto_exchange_rate", params, alpha_vantage_get(params))


def get_crypto_intraday(symbol: str, market: str, interval: str, outputsize: Optional[str] = None):
    params = {
        "function": "CRYPTO_INTRADAY",
        "symbol": symbol,
        "market": market,
        "interval": interval,
        "outputsize": outputsize,
    }
    return build_result("get_crypto_intraday", params, alpha_vantage_get(params))


def get_crypto_daily(symbol: str, market: str):
    params = {"function": "DIGITAL_CURRENCY_DAILY", "symbol": symbol, "market": market}
    return build_result("get_crypto_daily", params, alpha_vantage_get(params))


def get_crypto_weekly(symbol: str, market: str):
    params = {"function": "DIGITAL_CURRENCY_WEEKLY", "symbol": symbol, "market": market}
    return build_result("get_crypto_weekly", params, alpha_vantage_get(params))


def get_crypto_monthly(symbol: str, market: str):
    params = {"function": "DIGITAL_CURRENCY_MONTHLY", "symbol": symbol, "market": market}
    return build_result("get_crypto_monthly", params, alpha_vantage_get(params))
