from typing import Any, Dict, Optional

from .http_client import stripe_request


# POST /v1/prices
# GET /v1/prices/{price}
# POST /v1/prices/{price}
# GET /v1/prices


def create_price(
    currency: str,
    *,
    unit_amount: Optional[int] = None,
    product: Optional[str] = None,
    product_data: Optional[Dict[str, Any]] = None,
    recurring: Optional[Dict[str, Any]] = None,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    tax_behavior: Optional[str] = None,
    lookup_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "currency": currency,
        "unit_amount": unit_amount,
        "product": product,
        "product_data": product_data,
        "recurring": recurring,
        "active": active,
        "nickname": nickname,
        "metadata": metadata,
        "tax_behavior": tax_behavior,
        "lookup_key": lookup_key,
    }
    params.update(kwargs)
    return stripe_request(
        "POST",
        "/v1/prices",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_price(price_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/prices/{price_id}", stripe_account=stripe_account)


def update_price(
    price_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/prices/{price_id}",
        params=params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_prices(
    *,
    product: Optional[str] = None,
    active: Optional[bool] = None,
    currency: Optional[str] = None,
    type: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "product": product,
        "active": active,
        "currency": currency,
        "type": type,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/prices", params=params, stripe_account=stripe_account)
