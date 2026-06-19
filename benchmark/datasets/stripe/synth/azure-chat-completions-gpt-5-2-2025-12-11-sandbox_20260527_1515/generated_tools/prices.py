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
    tax_behavior: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    lookup_key: Optional[str] = None,
    billing_scheme: Optional[str] = None,
    tiers: Optional[list[Dict[str, Any]]] = None,
    tiers_mode: Optional[str] = None,
    unit_amount_decimal: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "currency": currency,
        "unit_amount": unit_amount,
        "product": product,
        "product_data": product_data,
        "recurring": recurring,
        "active": active,
        "nickname": nickname,
        "tax_behavior": tax_behavior,
        "metadata": metadata,
        "lookup_key": lookup_key,
        "billing_scheme": billing_scheme,
        "tiers": tiers,
        "tiers_mode": tiers_mode,
        "unit_amount_decimal": unit_amount_decimal,
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
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request("GET", f"/v1/prices/{price_id}", params=params, stripe_account=stripe_account)


def update_price(
    price_id: str,
    *,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    tax_behavior: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    lookup_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "nickname": nickname,
        "tax_behavior": tax_behavior,
        "metadata": metadata,
        "lookup_key": lookup_key,
    }
    return stripe_request("POST", f"/v1/prices/{price_id}", params=params, stripe_account=stripe_account)


def list_prices(
    *,
    active: Optional[bool] = None,
    currency: Optional[str] = None,
    product: Optional[str] = None,
    type: Optional[str] = None,
    lookup_keys: Optional[list[str]] = None,
    recurring: Optional[Dict[str, Any]] = None,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "currency": currency,
        "product": product,
        "type": type,
        "lookup_keys": lookup_keys,
        "recurring": recurring,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
        "expand": expand,
    }
    return stripe_request("GET", "/v1/prices", params=params, stripe_account=stripe_account)
