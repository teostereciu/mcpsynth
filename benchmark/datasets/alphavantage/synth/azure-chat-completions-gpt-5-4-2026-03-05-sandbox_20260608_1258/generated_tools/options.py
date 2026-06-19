from typing import Optional

from generated_tools.common import alpha_vantage_get, build_result


def get_realtime_options(symbol: str, require_greeks: Optional[bool] = None, contract: Optional[str] = None, expiration: Optional[str] = None):
    params = {
        "function": "REALTIME_OPTIONS",
        "symbol": symbol,
        "require_greeks": str(require_greeks).lower() if require_greeks is not None else None,
        "contract": contract,
        "expiration": expiration,
    }
    return build_result("get_realtime_options", params, alpha_vantage_get(params))


def get_realtime_put_call_ratio(symbol: str):
    params = {"function": "REALTIME_PUT_CALL_RATIO", "symbol": symbol}
    return build_result("get_realtime_put_call_ratio", params, alpha_vantage_get(params))


def get_realtime_volume_open_interest_ratio(symbol: str):
    params = {"function": "REALTIME_VOLUME_OPEN_INTEREST_RATIO", "symbol": symbol}
    return build_result("get_realtime_volume_open_interest_ratio", params, alpha_vantage_get(params))


def get_historical_options(symbol: str, date: Optional[str] = None, contract: Optional[str] = None):
    params = {"function": "HISTORICAL_OPTIONS", "symbol": symbol, "date": date, "contract": contract}
    return build_result("get_historical_options", params, alpha_vantage_get(params))
