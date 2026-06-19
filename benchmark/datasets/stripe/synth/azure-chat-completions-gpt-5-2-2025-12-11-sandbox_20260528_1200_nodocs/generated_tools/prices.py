from typing import Any, Dict, Optional

from .http import stripe_get, stripe_post


def prices_create(
    *,
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
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {
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
    }
    res, err = stripe_post(
        "/v1/prices",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def prices_retrieve(*, price_id: str, stripe_account: Optional[str] = None):
    res, err = stripe_get(f"/v1/prices/{price_id}", stripe_account=stripe_account)
    return err or res


def prices_update(
    *,
    price_id: str,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    nickname: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {"active": active, "metadata": metadata, "nickname": nickname}
    res, err = stripe_post(f"/v1/prices/{price_id}", data=data, stripe_account=stripe_account)
    return err or res


def prices_list(
    *,
    product: Optional[str] = None,
    active: Optional[bool] = None,
    currency: Optional[str] = None,
    type: Optional[str] = None,
    recurring: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    params: Dict[str, Any] = {
        "product": product,
        "active": active,
        "currency": currency,
        "type": type,
        "recurring": recurring,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    res, err = stripe_get("/v1/prices", params=params, stripe_account=stripe_account)
    return err or res
