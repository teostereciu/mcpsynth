from typing import Any, Dict, Optional

from .http_client import stripe_request


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
    billing_scheme: Optional[str] = None,
    lookup_key: Optional[str] = None,
    unit_amount_decimal: Optional[str] = None,
    custom_unit_amount: Optional[Dict[str, Any]] = None,
    tiers: Optional[list[Dict[str, Any]]] = None,
    tiers_mode: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
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
        "billing_scheme": billing_scheme,
        "lookup_key": lookup_key,
        "unit_amount_decimal": unit_amount_decimal,
        "custom_unit_amount": custom_unit_amount,
        "tiers": tiers,
        "tiers_mode": tiers_mode,
    }
    return stripe_request(
        "POST",
        "/v1/prices",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )


def retrieve_price(
    price_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return stripe_request(
        "GET",
        f"/v1/prices/{price_id}",
        params=params or None,
        stripe_account=stripe_account,
    )


def update_price(
    price_id: str,
    *,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    tax_behavior: Optional[str] = None,
    lookup_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "nickname": nickname,
        "metadata": metadata,
        "tax_behavior": tax_behavior,
        "lookup_key": lookup_key,
    }
    return stripe_request(
        "POST",
        f"/v1/prices/{price_id}",
        params=params,
        stripe_account=stripe_account,
    )


def list_prices(
    *,
    product: Optional[str] = None,
    active: Optional[bool] = None,
    currency: Optional[str] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "product": product,
        "active": active,
        "currency": currency,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request(
        "GET",
        "/v1/prices",
        params=params,
        stripe_account=stripe_account,
    )
