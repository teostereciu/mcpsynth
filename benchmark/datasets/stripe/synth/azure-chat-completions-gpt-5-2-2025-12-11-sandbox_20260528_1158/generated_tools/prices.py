from typing import Any, Dict, Optional

from .stripe_client import stripe_request


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
    custom_unit_amount: Optional[Dict[str, Any]] = None,
    lookup_key: Optional[str] = None,
    transfer_lookup_key: Optional[bool] = None,
    tiers: Optional[list[Dict[str, Any]]] = None,
    tiers_mode: Optional[str] = None,
    transform_quantity: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"currency": currency}
    if unit_amount is not None:
        params["unit_amount"] = unit_amount
    if unit_amount_decimal is not None:
        params["unit_amount_decimal"] = unit_amount_decimal
    if product is not None:
        params["product"] = product
    if product_data is not None:
        params["product_data"] = product_data
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
    if transfer_lookup_key is not None:
        params["transfer_lookup_key"] = transfer_lookup_key
    if tiers is not None:
        params["tiers"] = tiers
    if tiers_mode is not None:
        params["tiers_mode"] = tiers_mode
    if transform_quantity is not None:
        params["transform_quantity"] = transform_quantity

    return stripe_request("POST", "/v1/prices", params=params)


def retrieve_price(price_id: str, *, expand: Optional[list[str]] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return stripe_request("GET", f"/v1/prices/{price_id}", params=params)


def update_price(
    price_id: str,
    *,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tax_behavior: Optional[str] = None,
    lookup_key: Optional[str] = None,
    transfer_lookup_key: Optional[bool] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if active is not None:
        params["active"] = active
    if nickname is not None:
        params["nickname"] = nickname
    if metadata is not None:
        params["metadata"] = metadata
    if tax_behavior is not None:
        params["tax_behavior"] = tax_behavior
    if lookup_key is not None:
        params["lookup_key"] = lookup_key
    if transfer_lookup_key is not None:
        params["transfer_lookup_key"] = transfer_lookup_key

    return stripe_request("POST", f"/v1/prices/{price_id}", params=params)


def list_prices(
    *,
    active: Optional[bool] = None,
    product: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    lookup_keys: Optional[list[str]] = None,
    recurring: Optional[Dict[str, Any]] = None,
    type: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if active is not None:
        params["active"] = active
    if product is not None:
        params["product"] = product
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before
    if lookup_keys is not None:
        params["lookup_keys"] = lookup_keys
    if recurring is not None:
        params["recurring"] = recurring
    if type is not None:
        params["type"] = type

    return stripe_request("GET", "/v1/prices", params=params)
