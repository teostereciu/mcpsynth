from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def prices_create(
    *,
    currency: str,
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
    custom_unit_amount: Optional[Dict[str, Any]] = None,
    tiers: Optional[Any] = None,
    tiers_mode: Optional[str] = None,
    transform_quantity: Optional[Dict[str, Any]] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    transfer_lookup_key: Optional[bool] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"currency": currency}
    if unit_amount is not None:
        data["unit_amount"] = unit_amount
    if unit_amount_decimal is not None:
        data["unit_amount_decimal"] = unit_amount_decimal
    if product is not None:
        data["product"] = product
    if product_data is not None:
        data["product_data"] = product_data
    if recurring is not None:
        data["recurring"] = recurring
    if active is not None:
        data["active"] = active
    if nickname is not None:
        data["nickname"] = nickname
    if lookup_key is not None:
        data["lookup_key"] = lookup_key
    if tax_behavior is not None:
        data["tax_behavior"] = tax_behavior
    if metadata is not None:
        data["metadata"] = metadata
    if billing_scheme is not None:
        data["billing_scheme"] = billing_scheme
    if custom_unit_amount is not None:
        data["custom_unit_amount"] = custom_unit_amount
    if tiers is not None:
        data["tiers"] = tiers
    if tiers_mode is not None:
        data["tiers_mode"] = tiers_mode
    if transform_quantity is not None:
        data["transform_quantity"] = transform_quantity
    if currency_options is not None:
        data["currency_options"] = currency_options
    if transfer_lookup_key is not None:
        data["transfer_lookup_key"] = transfer_lookup_key
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/prices",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def prices_retrieve(*, price_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/prices/{price_id}", stripe_account=stripe_account)


def prices_update(
    *,
    price_id: str,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    lookup_key: Optional[str] = None,
    tax_behavior: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    transfer_lookup_key: Optional[bool] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if active is not None:
        data["active"] = active
    if nickname is not None:
        data["nickname"] = nickname
    if lookup_key is not None:
        data["lookup_key"] = lookup_key
    if tax_behavior is not None:
        data["tax_behavior"] = tax_behavior
    if metadata is not None:
        data["metadata"] = metadata
    if currency_options is not None:
        data["currency_options"] = currency_options
    if transfer_lookup_key is not None:
        data["transfer_lookup_key"] = transfer_lookup_key
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/prices/{price_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def prices_list(
    *,
    limit: Optional[int] = 10,
    active: Optional[bool] = None,
    product: Optional[str] = None,
    recurring: Optional[Dict[str, Any]] = None,
    lookup_keys: Optional[Any] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_query: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if limit is not None:
        query["limit"] = limit
    if active is not None:
        query["active"] = active
    if product is not None:
        query["product"] = product
    if recurring is not None:
        query["recurring"] = recurring
    if lookup_keys is not None:
        query["lookup_keys"] = lookup_keys
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if extra_query:
        query.update(extra_query)

    return stripe_request("GET", "/v1/prices", params=query, stripe_account=stripe_account)
