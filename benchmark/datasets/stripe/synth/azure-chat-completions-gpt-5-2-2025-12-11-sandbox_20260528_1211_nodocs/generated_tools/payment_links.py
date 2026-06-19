from typing import Any, Dict, Optional

from .http import stripe_request


def create_payment_link(
    *,
    line_items: list[Dict[str, Any]],
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    currency: Optional[str] = None,
    customer_creation: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"line_items": line_items}
    if after_completion is not None:
        data["after_completion"] = after_completion
    if allow_promotion_codes is not None:
        data["allow_promotion_codes"] = allow_promotion_codes
    if automatic_tax is not None:
        data["automatic_tax"] = automatic_tax
    if billing_address_collection is not None:
        data["billing_address_collection"] = billing_address_collection
    if currency is not None:
        data["currency"] = currency
    if customer_creation is not None:
        data["customer_creation"] = customer_creation
    if metadata is not None:
        data["metadata"] = metadata
    if restrictions is not None:
        data["restrictions"] = restrictions
    if subscription_data is not None:
        data["subscription_data"] = subscription_data

    res, err = stripe_request(
        "POST",
        "/v1/payment_links",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def retrieve_payment_link(payment_link_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/payment_links/{payment_link_id}", stripe_account=stripe_account)
    return res if err is None else err


def update_payment_link(
    payment_link_id: str,
    *,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, str]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if active is not None:
        data["active"] = active
    if metadata is not None:
        data["metadata"] = metadata
    if restrictions is not None:
        data["restrictions"] = restrictions

    res, err = stripe_request("POST", f"/v1/payment_links/{payment_link_id}", data=data, stripe_account=stripe_account)
    return res if err is None else err


def list_payment_links(
    *,
    active: Optional[bool] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if active is not None:
        query["active"] = active
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before

    res, err = stripe_request("GET", "/v1/payment_links", query=query, stripe_account=stripe_account)
    return res if err is None else err
