from typing import Any, Dict, Optional

from .http import stripe_request


def create_price(
    *,
    currency: str,
    unit_amount: Optional[int] = None,
    unit_amount_decimal: Optional[str] = None,
    product: Optional[str] = None,
    product_data: Optional[Dict[str, Any]] = None,
    recurring: Optional[Dict[str, Any]] = None,
    nickname: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, str]] = None,
    tax_behavior: Optional[str] = None,
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
    if nickname is not None:
        data["nickname"] = nickname
    if active is not None:
        data["active"] = active
    if metadata is not None:
        data["metadata"] = metadata
    if tax_behavior is not None:
        data["tax_behavior"] = tax_behavior

    res, err = stripe_request(
        "POST",
        "/v1/prices",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def retrieve_price(price_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/prices/{price_id}", stripe_account=stripe_account)
    return res if err is None else err


def update_price(
    price_id: str,
    *,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if active is not None:
        data["active"] = active
    if nickname is not None:
        data["nickname"] = nickname
    if metadata is not None:
        data["metadata"] = metadata

    res, err = stripe_request("POST", f"/v1/prices/{price_id}", data=data, stripe_account=stripe_account)
    return res if err is None else err


def list_prices(
    *,
    product: Optional[str] = None,
    active: Optional[bool] = None,
    currency: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if product is not None:
        query["product"] = product
    if active is not None:
        query["active"] = active
    if currency is not None:
        query["currency"] = currency
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before

    res, err = stripe_request("GET", "/v1/prices", query=query, stripe_account=stripe_account)
    return res if err is None else err
