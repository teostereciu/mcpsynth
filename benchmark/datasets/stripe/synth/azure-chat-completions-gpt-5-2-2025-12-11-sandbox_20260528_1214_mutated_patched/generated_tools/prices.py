from typing import Any, Dict, Optional

from .http import stripe_request


# Docs: docs/prices.md

def create_price(
    currency: str,
    *,
    unit_amount: Optional[int] = None,
    unit_amount_decimal: Optional[str] = None,
    product: Optional[str] = None,
    product_data: Optional[Dict[str, Any]] = None,
    recurring: Optional[Dict[str, Any]] = None,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tax_behavior: Optional[str] = None,
    billing_scheme: Optional[str] = None,
    lookup_key: Optional[str] = None,
    tiers: Optional[list[Dict[str, Any]]] = None,
    tiers_mode: Optional[str] = None,
    transform_quantity: Optional[Dict[str, Any]] = None,
    custom_unit_amount: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "currency": currency,
        "unit_amount": unit_amount,
        "unit_amount_decimal": unit_amount_decimal,
        "product": product,
        "product_data": product_data,
        "recurring": recurring,
        "active": active,
        "nickname": nickname,
        "metadata": metadata,
        "tax_behavior": tax_behavior,
        "billing_scheme": billing_scheme,
        "lookup_key": lookup_key,
        "tiers": tiers,
        "tiers_mode": tiers_mode,
        "transform_quantity": transform_quantity,
        "custom_unit_amount": custom_unit_amount,
    }
    return stripe_request(
        "POST",
        "/v1/prices",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_price(
    price_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/prices/{price_id}",
        params={"expand": expand},
        stripe_account=stripe_account,
    )


def update_price(
    price_id: str,
    *,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tax_behavior: Optional[str] = None,
    lookup_key: Optional[str] = None,
    transfer_lookup_key: Optional[bool] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "nickname": nickname,
        "metadata": metadata,
        "tax_behavior": tax_behavior,
        "lookup_key": lookup_key,
        "transfer_lookup_key": transfer_lookup_key,
        "currency_options": currency_options,
    }
    return stripe_request(
        "POST",
        f"/v1/prices/{price_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_prices(
    *,
    active: Optional[bool] = None,
    product: Optional[str] = None,
    currency: Optional[str] = None,
    type: Optional[str] = None,
    recurring: Optional[Dict[str, Any]] = None,
    lookup_keys: Optional[list[str]] = None,
    created: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "product": product,
        "currency": currency,
        "type": type,
        "recurring": recurring,
        "lookup_keys": lookup_keys,
        "created": created,
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
