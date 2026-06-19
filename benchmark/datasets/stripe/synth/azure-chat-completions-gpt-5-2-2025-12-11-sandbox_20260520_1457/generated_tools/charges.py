from typing import Any, Dict, Optional

from .http_client import ok_or_error, stripe_request


def create_charge(
    *,
    amount: int,
    currency: str,
    source: Optional[str] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    capture: Optional[bool] = None,
    application_fee_amount: Optional[int] = None,
    on_behalf_of: Optional[str] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    transfer_group: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "source": source,
        "customer": customer,
        "description": description,
        "receipt_email": receipt_email,
        "shipping": shipping,
        "metadata": metadata,
        "capture": capture,
        "application_fee_amount": application_fee_amount,
        "on_behalf_of": on_behalf_of,
        "transfer_data": transfer_data,
        "transfer_group": transfer_group,
    }
    status, payload = stripe_request(
        "POST", "/v1/charges", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def retrieve_charge(*, charge_id: str, stripe_account: Optional[str] = None) -> Any:
    status, payload = stripe_request("GET", f"/v1/charges/{charge_id}", stripe_account=stripe_account)
    return ok_or_error(status, payload)


def update_charge(
    *,
    charge_id: str,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    fraud_details: Optional[Dict[str, Any]] = None,
    transfer_group: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "customer": customer,
        "description": description,
        "receipt_email": receipt_email,
        "shipping": shipping,
        "metadata": metadata,
        "fraud_details": fraud_details,
        "transfer_group": transfer_group,
    }
    status, payload = stripe_request(
        "POST", f"/v1/charges/{charge_id}", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def list_charges(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_intent": payment_intent,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
        "created": created,
    }
    status, payload = stripe_request("GET", "/v1/charges", params=params, stripe_account=stripe_account)
    return ok_or_error(status, payload)
