from typing import Any, Dict, Optional

from ._client import stripe_request


def charges_retrieve(*, charge_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("GET", f"/v1/charges/{charge_id}", stripe_account=stripe_account)
    return err or data  # type: ignore[return-value]


def charges_list(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    limit: int = 10,
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
    data, err = stripe_request("GET", "/v1/charges", params=params, stripe_account=stripe_account)
    return err or data  # type: ignore[return-value]


def charges_update(
    *,
    charge_id: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    fraud_details: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "description": description,
        "metadata": metadata,
        "receipt_email": receipt_email,
        "shipping": shipping,
        "fraud_details": fraud_details,
    }
    data, err = stripe_request("POST", f"/v1/charges/{charge_id}", params=params, stripe_account=stripe_account)
    return err or data  # type: ignore[return-value]


def charges_capture(
    *,
    charge_id: str,
    amount: Optional[int] = None,
    application_fee_amount: Optional[int] = None,
    receipt_email: Optional[str] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "amount": amount,
        "application_fee_amount": application_fee_amount,
        "receipt_email": receipt_email,
        "statement_descriptor": statement_descriptor,
        "statement_descriptor_suffix": statement_descriptor_suffix,
        "transfer_data": transfer_data,
    }
    data, err = stripe_request("POST", f"/v1/charges/{charge_id}/capture", params=params, stripe_account=stripe_account)
    return err or data  # type: ignore[return-value]
