from typing import Any, Dict, Optional

from .http import stripe_request


def create_price(
    currency: str,
    *,
    product: Optional[str] = None,
    product_data: Optional[Dict[str, Any]] = None,
    unit_amount: Optional[int] = None,
    unit_amount_decimal: Optional[str] = None,
    recurring: Optional[Dict[str, Any]] = None,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tax_behavior: Optional[str] = None,
    billing_scheme: Optional[str] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    custom_unit_amount: Optional[Dict[str, Any]] = None,
    lookup_key: Optional[str] = None,
    tiers: Optional[list[Dict[str, Any]]] = None,
    tiers_mode: Optional[str] = None,
    transfer_lookup_key: Optional[bool] = None,
    transform_quantity: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "currency": currency,
        "product": product,
        "product_data": product_data,
        "unit_amount": unit_amount,
        "unit_amount_decimal": unit_amount_decimal,
        "recurring": recurring,
        "active": active,
        "nickname": nickname,
        "metadata": metadata,
        "tax_behavior": tax_behavior,
        "billing_scheme": billing_scheme,
        "currency_options": currency_options,
        "custom_unit_amount": custom_unit_amount,
        "lookup_key": lookup_key,
        "tiers": tiers,
        "tiers_mode": tiers_mode,
        "transfer_lookup_key": transfer_lookup_key,
        "transform_quantity": transform_quantity,
    }
    return stripe_request(
        "POST",
        "/v1/prices",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_price(
    price_id: str,
    *,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tax_behavior: Optional[str] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    lookup_key: Optional[str] = None,
    transfer_lookup_key: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "nickname": nickname,
        "metadata": metadata,
        "tax_behavior": tax_behavior,
        "currency_options": currency_options,
        "lookup_key": lookup_key,
        "transfer_lookup_key": transfer_lookup_key,
    }
    return stripe_request(
        "POST",
        f"/v1/prices/{price_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_price(
    price_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/prices/{price_id}",
        params=None,
        stripe_account=stripe_account,
    )
