from typing import Optional

from generated_tools.common import call_alpha_vantage


def get_realtime_options(
    ticker: str,
    require_greeks: Optional[bool] = None,
    contract: Optional[str] = None,
    expiration: Optional[str] = None,
):
    return call_alpha_vantage(
        {
            "function": "REALTIME_OPTIONS",
            "symbol": ticker,
            "require_greeks": str(require_greeks).lower() if require_greeks is not None else None,
            "contract": contract,
            "expiration": expiration,
        }
    )


def get_realtime_put_call_ratio(ticker: str):
    return call_alpha_vantage({"function": "REALTIME_PUT_CALL_RATIO", "symbol": ticker})


def get_realtime_volume_open_interest_ratio(ticker: str):
    return call_alpha_vantage(
        {"function": "REALTIME_VOLUME_OPEN_INTEREST_RATIO", "symbol": ticker}
    )


def get_historical_options(
    ticker: str, date: Optional[str] = None, contract: Optional[str] = None
):
    return call_alpha_vantage(
        {
            "function": "HISTORICAL_OPTIONS",
            "symbol": ticker,
            "date": date,
            "contract": contract,
        }
    )
