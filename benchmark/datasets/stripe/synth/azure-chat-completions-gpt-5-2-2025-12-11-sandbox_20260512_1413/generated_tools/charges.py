from typing import Any, Dict, Optional

from .stripe_client import stripe_list_all, stripe_request


def charges_create(
    amount: int,
    currency: str,
    *,
    source: Optional[str] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    capture: Optional[bool] = None,
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
        "shipping": shipping,
        "metadata": metadata,
        "capture": capture,
    }
    return stripe_request("POST", "/v1/charges", params, stripe_account=stripe_account, idempotency_key=idempotency_key)


def charges_retrieve(charge_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/charges/{charge_id}", None, stripe_account=stripe_account)


def charges_update(
    charge_id: str,
    *,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    fraud_details: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "description": description,
        "receipt_email": receipt_email,
        "shipping": shipping,
        "metadata": metadata,
        "fraud_details": fraud_details,
    }
    return stripe_request("POST", f"/v1/charges/{charge_id}", params, stripe_account=stripe_account)


def charges_list(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_intent": payment_intent,
        "created": created,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/charges", params, stripe_account=stripe_account)


def charges_list_all(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    limit: int = 100,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"customer": customer, "payment_intent": payment_intent, "created": created}
    return stripe_list_all("/v1/charges", params, stripe_account=stripe_account, limit=limit, max_pages=max_pages)
