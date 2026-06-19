from typing import Any, Dict, Optional

from .http_client import stripe_request


def update_charge(
    charge_id: str,
    *,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    fraud_details: Optional[Dict[str, Any]] = None,
    transfer_group: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/charges/{charge}"""
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if receipt_email is not None:
        params["receipt_email"] = receipt_email
    if shipping is not None:
        params["shipping"] = shipping
    if fraud_details is not None:
        params["fraud_details"] = fraud_details
    if transfer_group is not None:
        params["transfer_group"] = transfer_group

    data, err = stripe_request(
        "POST",
        f"/v1/charges/{charge_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def retrieve_charge(
    charge_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/charges/{charge}"""
    data, err = stripe_request(
        "GET",
        f"/v1/charges/{charge_id}",
        params=None,
        stripe_account=stripe_account,
    )
    return data if err is None else err


def list_charges(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/charges"""
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if payment_intent is not None:
        params["payment_intent"] = payment_intent
    if created is not None:
        params["created"] = created
    if ending_before is not None:
        params["ending_before"] = ending_before
    if starting_after is not None:
        params["starting_after"] = starting_after
    if limit is not None:
        params["limit"] = limit

    data, err = stripe_request(
        "GET",
        "/v1/charges",
        params=params,
        stripe_account=stripe_account,
    )
    return data if err is None else err
