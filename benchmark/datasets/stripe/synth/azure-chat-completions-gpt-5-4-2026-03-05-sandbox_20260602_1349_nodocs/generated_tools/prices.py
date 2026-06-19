from typing import Any, Dict, Optional

from generated_tools.stripe_common import stripe_request


def create_price(
    currency: str,
    unit_amount: int,
    product: str,
    recurring_interval: Optional[str] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Any:
    params = {
        "currency": currency,
        "unit_amount": unit_amount,
        "product": product,
        "nickname": nickname,
        "metadata": metadata,
    }
    if recurring_interval:
        params["recurring[interval]"] = recurring_interval
    return stripe_request("POST", "/v1/prices", params)


def retrieve_price(price_id: str) -> Any:
    return stripe_request("GET", f"/v1/prices/{price_id}")


def update_price(price_id: str, metadata: Optional[Dict[str, Any]] = None, active: Optional[bool] = None) -> Any:
    return stripe_request("POST", f"/v1/prices/{price_id}", {"metadata": metadata, "active": active})


def list_prices(product: Optional[str] = None, active: Optional[bool] = None, limit: Optional[int] = 10) -> Any:
    return stripe_request("GET", "/v1/prices", {"product": product, "active": active, "limit": limit})


def search_prices(query: str, limit: Optional[int] = 10) -> Any:
    return stripe_request("GET", "/v1/prices/search", {"query": query, "limit": limit})
