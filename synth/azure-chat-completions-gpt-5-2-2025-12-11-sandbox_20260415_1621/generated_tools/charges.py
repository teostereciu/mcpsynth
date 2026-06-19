from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def charges_create(
    *,
    amount: int,
    currency: str,
    source: Optional[str] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    capture: Optional[bool] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"amount": amount, "currency": currency}
    if source is not None:
        data["source"] = source
    if customer is not None:
        data["customer"] = customer
    if description is not None:
        data["description"] = description
    if receipt_email is not None:
        data["receipt_email"] = receipt_email
    if shipping is not None:
        data["shipping"] = shipping
    if metadata is not None:
        data["metadata"] = metadata
    if capture is not None:
        data["capture"] = capture
    if statement_descriptor is not None:
        data["statement_descriptor"] = statement_descriptor
    if statement_descriptor_suffix is not None:
        data["statement_descriptor_suffix"] = statement_descriptor_suffix
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/charges",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def charges_retrieve(*, charge_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/charges/{charge_id}", stripe_account=stripe_account)


def charges_update(
    *,
    charge_id: str,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    fraud_details: Optional[Dict[str, Any]] = None,
    transfer_group: Optional[str] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if customer is not None:
        data["customer"] = customer
    if description is not None:
        data["description"] = description
    if receipt_email is not None:
        data["receipt_email"] = receipt_email
    if shipping is not None:
        data["shipping"] = shipping
    if metadata is not None:
        data["metadata"] = metadata
    if fraud_details is not None:
        data["fraud_details"] = fraud_details
    if transfer_group is not None:
        data["transfer_group"] = transfer_group
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/charges/{charge_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def charges_list(
    *,
    limit: Optional[int] = 10,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_query: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if limit is not None:
        query["limit"] = limit
    if customer is not None:
        query["customer"] = customer
    if payment_intent is not None:
        query["payment_intent"] = payment_intent
    if created is not None:
        query["created"] = created
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if extra_query:
        query.update(extra_query)

    return stripe_request("GET", "/v1/charges", params=query, stripe_account=stripe_account)
