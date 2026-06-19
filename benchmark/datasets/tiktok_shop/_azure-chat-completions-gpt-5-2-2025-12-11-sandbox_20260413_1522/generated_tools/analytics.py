from __future__ import annotations

from datetime import date, timedelta
from typing import Any, Dict, Optional

from .http import safe_call


def get_shop_performance(
    start_date_ge: str,
    end_date_lt: str,
    granularity: str = "ALL",
    currency: str = "LOCAL",
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /analytics/202509/shop/performance"""
    params: Dict[str, Any] = {
        "start_date_ge": start_date_ge,
        "end_date_lt": end_date_lt,
        "granularity": granularity,
        "currency": currency,
    }
    if shop_cipher:
        params["shop_cipher"] = shop_cipher
    return safe_call("GET", "/analytics/202509/shop/performance", params=params)


def get_shop_performance_last_7_days(shop_cipher: Optional[str] = None) -> Dict[str, Any]:
    """Convenience wrapper for scenarios/tests."""
    today = date.today()
    start = today - timedelta(days=7)
    return get_shop_performance(start.isoformat(), today.isoformat(), shop_cipher=shop_cipher)
