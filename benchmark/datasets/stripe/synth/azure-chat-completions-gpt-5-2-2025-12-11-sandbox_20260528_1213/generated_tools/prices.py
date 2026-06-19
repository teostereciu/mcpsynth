from typing import Any, Dict, Optional

from .http_client import stripe_request


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
    custom_unit_amount: Optional[Dict[str, Any]] = None,
    lookup_key: Optional[str] = None,
    tiers: Optional[list] = None,
    tiers_mode: Optional[str] = None,
    transfer_lookup_key: Optional[bool] = None,
    transform_quantity: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/prices"""
    params: Dict[str, Any] = {"currency": currency}
    if product is not None:
        params["product"] = product
    if product_data is not None:
        params["product_data"] = product_data
    if unit_amount is not None:
        params["unit_amount"] = unit_amount
    if unit_amount_decimal is not None:
        params["unit_amount_decimal"] = unit_amount_decimal
    if recurring is not None:
        params["recurring"] = recurring
    if active is not None:
        params["active"] = active
    if nickname is not None:
        params["nickname"] = nickname
    if metadata is not None:
        params["metadata"] = metadata
    if tax_behavior is not None:
        params["tax_behavior"] = tax_behavior
    if billing_scheme is not None:
        params["billing_scheme"] = billing_scheme
    if custom_unit_amount is not None:
        params["custom_unit_amount"] = custom_unit_amount
    if lookup_key is not None:
        params["lookup_key"] = lookup_key
    if tiers is not None:
        params["tiers"] = tiers
    if tiers_mode is not None:
        params["tiers_mode"] = tiers_mode
    if transfer_lookup_key is not None:
        params["transfer_lookup_key"] = transfer_lookup_key
    if transform_quantity is not None:
        params["transform_quantity"] = transform_quantity

    if product is None and product_data is None:
        return {"error": "invalid_request", "message": "Must provide either product or product_data"}

    data, err = stripe_request(
        "POST",
        "/v1/prices",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


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
    """POST /v1/prices/{id}"""
    params: Dict[str, Any] = {}
    if active is not None:
        params["active"] = active
    if nickname is not None:
        params["nickname"] = nickname
    if metadata is not None:
        params["metadata"] = metadata
    if tax_behavior is not None:
        params["tax_behavior"] = tax_behavior
    if currency_options is not None:
        params["currency_options"] = currency_options
    if lookup_key is not None:
        params["lookup_key"] = lookup_key
    if transfer_lookup_key is not None:
        params["transfer_lookup_key"] = transfer_lookup_key

    data, err = stripe_request(
        "POST",
        f"/v1/prices/{price_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def retrieve_price(
    price_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/prices/{id}"""
    data, err = stripe_request(
        "GET",
        f"/v1/prices/{price_id}",
        params=None,
        stripe_account=stripe_account,
    )
    return data if err is None else err
