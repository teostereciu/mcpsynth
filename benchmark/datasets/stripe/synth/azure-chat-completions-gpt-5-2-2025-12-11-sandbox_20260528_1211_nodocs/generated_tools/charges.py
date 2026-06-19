from typing import Any, Dict, Optional

from .http import stripe_request


def retrieve_charge(charge_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/charges/{charge_id}", stripe_account=stripe_account)
    return res if err is None else err


def update_charge(
    charge_id: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    if receipt_email is not None:
        data["receipt_email"] = receipt_email
    if shipping is not None:
        data["shipping"] = shipping

    res, err = stripe_request("POST", f"/v1/charges/{charge_id}", data=data, stripe_account=stripe_account)
    return res if err is None else err


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
    query: Dict[str, Any] = {}
    if customer is not None:
        query["customer"] = customer
    if payment_intent is not None:
        query["payment_intent"] = payment_intent
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if created is not None:
        query["created"] = created

    res, err = stripe_request("GET", "/v1/charges", query=query, stripe_account=stripe_account)
    return res if err is None else err


def capture_charge(
    charge_id: str,
    *,
    amount: Optional[int] = None,
    application_fee_amount: Optional[int] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if amount is not None:
        data["amount"] = amount
    if application_fee_amount is not None:
        data["application_fee_amount"] = application_fee_amount

    res, err = stripe_request(
        "POST",
        f"/v1/charges/{charge_id}/capture",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err
