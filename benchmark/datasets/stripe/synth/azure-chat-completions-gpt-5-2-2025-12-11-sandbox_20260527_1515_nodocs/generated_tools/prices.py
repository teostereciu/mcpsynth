from typing import Any, Dict, Optional

from ._client import stripe_request


def prices_create(
    *,
    currency: str,
    product: Optional[str] = None,
    unit_amount: Optional[int] = None,
    unit_amount_decimal: Optional[str] = None,
    recurring: Optional[Dict[str, Any]] = None,
    nickname: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    lookup_key: Optional[str] = None,
    transfer_lookup_key: Optional[bool] = None,
    tax_behavior: Optional[str] = None,
    billing_scheme: Optional[str] = None,
    tiers: Optional[list[Dict[str, Any]]] = None,
    tiers_mode: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "currency": currency,
        "product": product,
        "unit_amount": unit_amount,
        "unit_amount_decimal": unit_amount_decimal,
        "recurring": recurring,
        "nickname": nickname,
        "active": active,
        "metadata": metadata,
        "lookup_key": lookup_key,
        "transfer_lookup_key": transfer_lookup_key,
        "tax_behavior": tax_behavior,
        "billing_scheme": billing_scheme,
        "tiers": tiers,
        "tiers_mode": tiers_mode,
    }
    data, err = stripe_request(
        "POST",
        "/v1/prices",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or data  # type: ignore[return-value]


def prices_retrieve(*, price_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("GET", f"/v1/prices/{price_id}", stripe_account=stripe_account)
    return err or data  # type: ignore[return-value]


def prices_update(
    *,
    price_id: str,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    nickname: Optional[str] = None,
    lookup_key: Optional[str] = None,
    transfer_lookup_key: Optional[bool] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "metadata": metadata,
        "nickname": nickname,
        "lookup_key": lookup_key,
        "transfer_lookup_key": transfer_lookup_key,
    }
    data, err = stripe_request("POST", f"/v1/prices/{price_id}", params=params, stripe_account=stripe_account)
    return err or data  # type: ignore[return-value]


def prices_list(
    *,
    active: Optional[bool] = None,
    product: Optional[str] = None,
    lookup_keys: Optional[list[str]] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "product": product,
        "lookup_keys": lookup_keys,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
        "created": created,
    }
    data, err = stripe_request("GET", "/v1/prices", params=params, stripe_account=stripe_account)
    return err or data  # type: ignore[return-value]
