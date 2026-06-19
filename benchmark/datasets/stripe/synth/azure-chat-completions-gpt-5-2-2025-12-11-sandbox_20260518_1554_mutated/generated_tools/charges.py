from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_charge(
    amount: int,
    currency: str,
    *,
    source: Optional[str] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "source": source,
        "customer": customer,
        "description": description,
        "metadata": metadata,
        "receipt_email": receipt_email,
        "shipping": shipping,
        "statement_descriptor": statement_descriptor,
        "statement_descriptor_suffix": statement_descriptor_suffix,
    }
    return stripe_request(
        "POST",
        "/v1/charges",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
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
        params=params or None,
        stripe_account=stripe_account,
    )


def update_charge(
    charge_id: str,
    *,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "description": description,
        "metadata": metadata,
        "receipt_email": receipt_email,
        "shipping": shipping,
    }
    return stripe_request(
        "POST",
        f"/v1/charges/{charge_id}",
        params=params,
        stripe_account=stripe_account,
    )


def list_charges(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_intent": payment_intent,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
        "created": created,
    }
    return stripe_request(
        "GET",
        "/v1/charges",
        params=params,
        stripe_account=stripe_account,
    )
