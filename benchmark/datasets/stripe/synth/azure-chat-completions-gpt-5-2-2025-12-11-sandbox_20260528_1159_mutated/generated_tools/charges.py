from typing import Any, Dict, Optional

from .http import stripe_request


def create_charge(
    amount: int,
    currency: str,
    source: Optional[str] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    capture: Optional[bool] = None,
    application_fee_amount: Optional[int] = None,
    on_behalf_of: Optional[str] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    transfer_group: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "source": source,
        "customer": customer,
        "description": description,
        "receipt_email": receipt_email,
        "metadata": metadata,
        "shipping": shipping,
        "statement_descriptor": statement_descriptor,
        "statement_descriptor_suffix": statement_descriptor_suffix,
        "capture": capture,
        "application_fee_amount": application_fee_amount,
        "on_behalf_of": on_behalf_of,
        "transfer_data": transfer_data,
        "transfer_group": transfer_group,
    }
    return stripe_request(
        "POST",
        "/v1/charges",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_charge(
    charge_id: str,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    fraud_details: Optional[Dict[str, Any]] = None,
    transfer_group: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "description": description,
        "receipt_email": receipt_email,
        "metadata": metadata,
        "shipping": shipping,
        "fraud_details": fraud_details,
        "transfer_group": transfer_group,
    }
    return stripe_request(
        "POST",
        f"/v1/charges/{charge_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
