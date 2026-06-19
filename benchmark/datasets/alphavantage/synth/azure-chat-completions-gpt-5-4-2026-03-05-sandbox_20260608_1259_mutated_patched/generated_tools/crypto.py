from typing import Optional

from generated_tools.common import call_alpha_vantage


def get_crypto_intraday(
    ticker: str, market: str, time_interval: str, output_size: Optional[str] = None
):
    return call_alpha_vantage(
        {
            "function": "CRYPTO_INTRADAY",
            "symbol": ticker,
            "market": market,
            "interval": time_interval,
            "outputsize": output_size,
        }
    )


def get_digital_currency_daily(ticker: str, market: str):
    return call_alpha_vantage(
        {"function": "DIGITAL_CURRENCY_DAILY", "symbol": ticker, "market": market}
    )


def get_digital_currency_weekly(ticker: str, market: str):
    return call_alpha_vantage(
        {"function": "DIGITAL_CURRENCY_WEEKLY", "symbol": ticker, "market": market}
    )


def get_digital_currency_monthly(ticker: str, market: str):
    return call_alpha_vantage(
        {"function": "DIGITAL_CURRENCY_MONTHLY", "symbol": ticker, "market": market}
    )
