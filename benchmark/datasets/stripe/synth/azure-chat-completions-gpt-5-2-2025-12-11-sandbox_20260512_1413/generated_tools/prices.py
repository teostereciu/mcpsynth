from typing import Any, Dict, Optional

from .stripe_client import stripe_list_all, stripe_request


def prices_create(
    currency: str,
    *,
    unit_amount: Optional[int] = None,
    unit_amount_decimal: Optional[str] = None,
    product: Optional[str] = None,
    product_data: Optional[Dict[str, Any]] = None,
    recurring: Optional[Dict[str, Any]] = None,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    lookup_key: Optional[str] = None,
    tax_behavior: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    billing_scheme: Optional[str] = None,
    tiers: Optional[list] = None,
    tiers_mode: Optional[str] = None,
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
        "lookup_key": lookup_key,
        "tax_behavior": tax_behavior,
        "metadata": metadata,
        "billing_scheme": billing_scheme,
        "tiers": tiers,
        "tiers_mode": tiers_mode,
        "custom_unit_amount": custom_unit_amount,
    }
    return stripe_request("POST", "/v1/prices", params, stripe_account=stripe_account, idempotency_key=idempotency_key)


def prices_retrieve(price_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/prices/{price_id}", None, stripe_account=stripe_account)


def prices_update(
    price_id: str,
    *,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    lookup_key: Optional[str] = None,
    tax_behavior: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    transfer_lookup_key: Optional[bool] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "nickname": nickname,
        "lookup_key": lookup_key,
        "tax_behavior": tax_behavior,
        "metadata": metadata,
        "currency_options": currency_options,
        "transfer_lookup_key": transfer_lookup_key,
    }
    return stripe_request("POST", f"/v1/prices/{price_id}", params, stripe_account=stripe_account)


def prices_list(
    *,
    active: Optional[bool] = None,
    product: Optional[str] = None,
    type: Optional[str] = None,
    lookup_keys: Optional[list] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "product": product,
        "type": type,
        "lookup_keys": lookup_keys,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/prices", params, stripe_account=stripe_account)


def prices_list_all(
    *,
    active: Optional[bool] = None,
    product: Optional[str] = None,
    type: Optional[str] = None,
    lookup_keys: Optional[list] = None,
    stripe_account: Optional[str] = None,
    limit: int = 100,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"active": active, "product": product, "type": type, "lookup_keys": lookup_keys}
    return stripe_list_all("/v1/prices", params, stripe_account=stripe_account, limit=limit, max_pages=max_pages)
