from typing import Optional

from generated_tools.common import call_alpha_vantage


def get_currency_exchange_rate(from_currency: str, to_currency: str):
    return call_alpha_vantage(
        {
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": from_currency,
            "to_currency": to_currency,
        }
    )


def get_fx_intraday(
    from_symbol: str, to_symbol: str, time_interval: str, output_size: Optional[str] = None
):
    return call_alpha_vantage(
        {
            "function": "FX_INTRADAY",
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
            "time_interval": time_interval,
            "output_size": output_size,
        }
    )


def get_fx_daily(from_symbol: str, to_symbol: str, output_size: Optional[str] = None):
    return call_alpha_vantage(
        {
            "function": "FX_DAILY",
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
            "output_size": output_size,
        }
    )


def get_fx_weekly(from_symbol: str, to_symbol: str):
    return call_alpha_vantage(
        {"function": "FX_WEEKLY", "from_symbol": from_symbol, "to_symbol": to_symbol}
    )


def get_fx_monthly(from_symbol: str, to_symbol: str):
    return call_alpha_vantage(
        {"function": "FX_MONTHLY", "from_symbol": from_symbol, "to_symbol": to_symbol}
    )
