from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def create_charge(
    amount: int,
    currency: str,
    *,
    source: Optional[str] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    capture: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"amount": amount, "currency": currency}
    if source is not None:
        params["source"] = source
    if customer is not None:
        params["customer"] = customer
    if description is not None:
        params["description"] = description
    if receipt_email is not None:
        params["receipt_email"] = receipt_email
    if metadata is not None:
        params["metadata"] = metadata
    if shipping is not None:
        params["shipping"] = shipping
    if statement_descriptor is not None:
        params["statement_descriptor"] = statement_descriptor
    if statement_descriptor_suffix is not None:
        params["statement_descriptor_suffix"] = statement_descriptor_suffix
    if capture is not None:
        params["capture"] = capture

    return stripe_request(
        "POST",
        "/v1/charges",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_charge(
    charge_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return stripe_request(
        "GET",
        f"/v1/charges/{charge_id}",
        params=params,
        stripe_account=stripe_account,
    )


def update_charge(
    charge_id: str,
    *,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    fraud_details: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if description is not None:
        params["description"] = description
    if receipt_email is not None:
        params["receipt_email"] = receipt_email
    if metadata is not None:
        params["metadata"] = metadata
    if shipping is not None:
        params["shipping"] = shipping
    if fraud_details is not None:
        params["fraud_details"] = fraud_details

    return stripe_request(
        "POST",
        f"/v1/charges/{charge_id}",
        params=params,
        stripe_account=stripe_account,
    )


def capture_charge(
    charge_id: str,
    *,
    amount: Optional[int] = None,
    receipt_email: Optional[str] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if amount is not None:
        params["amount"] = amount
    if receipt_email is not None:
        params["receipt_email"] = receipt_email
    if statement_descriptor is not None:
        params["statement_descriptor"] = statement_descriptor
    if statement_descriptor_suffix is not None:
        params["statement_descriptor_suffix"] = statement_descriptor_suffix

    return stripe_request(
        "POST",
        f"/v1/charges/{charge_id}/capture",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_charges(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if payment_intent is not None:
        params["payment_intent"] = payment_intent
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before
    if created is not None:
        params["created"] = created

    return stripe_request(
        "GET",
        "/v1/charges",
        params=params,
        stripe_account=stripe_account,
    )
