from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_charge(
    amount: int,
    currency: str,
    *,
    source: Optional[str] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    capture: Optional[bool] = None,
    application_fee_amount: Optional[int] = None,
    on_behalf_of: Optional[str] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    transfer_group: Optional[str] = None,
    radar_options: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/charges

    Doc: docs/charges.md (Create a charge - Deprecated)
    """
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "source": source,
        "customer": customer,
        "description": description,
        "receipt_email": receipt_email,
        "metadata": metadata,
        "shipping": shipping,
        "capture": capture,
        "application_fee_amount": application_fee_amount,
        "on_behalf_of": on_behalf_of,
        "transfer_data": transfer_data,
        "transfer_group": transfer_group,
        "radar_options": radar_options,
    }
    return stripe_request(
        "POST",
        "/v1/charges",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_charge(
    charge_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/charges/{charge_id}

    Doc: docs/charges.md (Retrieve a charge)
    """
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request(
        "GET",
        f"/v1/charges/{charge_id}",
        params,
        stripe_account=stripe_account,
    )


def update_charge(
    charge_id: str,
    *,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    fraud_details: Optional[Dict[str, Any]] = None,
    transfer_group: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/charges/{charge_id}

    Doc: docs/charges.md (Update a charge)
    """
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
        params,
        stripe_account=stripe_account,
    )


def list_charges(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/charges

    Doc: docs/charges.md (List all charges)
    """
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_intent": payment_intent,
        "created": created,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
        "expand": expand,
    }
    return stripe_request(
        "GET",
        "/v1/charges",
        params,
        stripe_account=stripe_account,
    )
