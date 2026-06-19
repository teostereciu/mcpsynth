from typing import Any, Dict, Optional

from .http import stripe_request


def prices_create(
    currency: str,
    unit_amount: Optional[int] = None,
    unit_amount_decimal: Optional[str] = None,
    product: Optional[str] = None,
    product_data: Optional[Dict[str, Any]] = None,
    recurring: Optional[Dict[str, Any]] = None,
    nickname: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tax_behavior: Optional[str] = None,
    billing_scheme: Optional[str] = None,
    tiers_mode: Optional[str] = None,
    tiers: Optional[list] = None,
    transform_quantity: Optional[Dict[str, Any]] = None,
    lookup_key: Optional[str] = None,
    transfer_lookup_key: Optional[bool] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "currency": currency,
        "unit_amount": unit_amount,
        "unit_amount_decimal": unit_amount_decimal,
        "product": product,
        "product_data": product_data,
        "recurring": recurring,
        "nickname": nickname,
        "active": active,
        "metadata": metadata,
        "tax_behavior": tax_behavior,
        "billing_scheme": billing_scheme,
        "tiers_mode": tiers_mode,
        "tiers": tiers,
        "transform_quantity": transform_quantity,
        "lookup_key": lookup_key,
        "transfer_lookup_key": transfer_lookup_key,
    }
    data, err = stripe_request(
        "POST",
        "/v1/prices",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def prices_retrieve(price_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("GET", f"/v1/prices/{price_id}", stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]


def prices_update(
    price_id: str,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    lookup_key: Optional[str] = None,
    transfer_lookup_key: Optional[bool] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "nickname": nickname,
        "metadata": metadata,
        "lookup_key": lookup_key,
        "transfer_lookup_key": transfer_lookup_key,
    }
    data, err = stripe_request(
        "POST",
        f"/v1/prices/{price_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def prices_list(
    limit: int = 10,
    active: Optional[bool] = None,
    product: Optional[str] = None,
    currency: Optional[str] = None,
    lookup_keys: Optional[list] = None,
    recurring: Optional[Dict[str, Any]] = None,
    created: Optional[Dict[str, Any]] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "limit": limit,
        "active": active,
        "product": product,
        "currency": currency,
        "lookup_keys": lookup_keys,
        "recurring": recurring,
        "created": created,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    data, err = stripe_request("GET", "/v1/prices", params=params, stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]
