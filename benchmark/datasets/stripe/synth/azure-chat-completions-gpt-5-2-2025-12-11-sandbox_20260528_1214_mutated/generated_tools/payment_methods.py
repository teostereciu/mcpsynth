from typing import Any, Dict, Optional

from .http import stripe_request


# Docs: docs/payment_methods.md

def create_payment_method(
    type: str,
    *,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    card: Optional[Dict[str, Any]] = None,
    us_bank_account: Optional[Dict[str, Any]] = None,
    sepa_debit: Optional[Dict[str, Any]] = None,
    au_becs_debit: Optional[Dict[str, Any]] = None,
    bacs_debit: Optional[Dict[str, Any]] = None,
    link: Optional[Dict[str, Any]] = None,
    paypal: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **type_data: Any,
) -> Dict[str, Any]:
    # type-specific payload can be passed via **type_data (e.g. ideal={...})
    params: Dict[str, Any] = {
        "type": type,
        "billing_details": billing_details,
        "metadata": metadata,
        "card": card,
        "us_bank_account": us_bank_account,
        "sepa_debit": sepa_debit,
        "au_becs_debit": au_becs_debit,
        "bacs_debit": bacs_debit,
        "link": link,
        "paypal": paypal,
    }
    params.update(type_data)
    return stripe_request(
        "POST",
        "/v1/payment_methods",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payment_method(
    payment_method_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/payment_methods/{payment_method_id}",
        params={"expand": expand},
        stripe_account=stripe_account,
    )


def update_payment_method(
    payment_method_id: str,
    *,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    allow_redisplay: Optional[str] = None,
    card: Optional[Dict[str, Any]] = None,
    us_bank_account: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "billing_details": billing_details,
        "metadata": metadata,
        "allow_redisplay": allow_redisplay,
        "card": card,
        "us_bank_account": us_bank_account,
    }
    return stripe_request(
        "POST",
        f"/v1/payment_methods/{payment_method_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def attach_payment_method(
    payment_method_id: str,
    customer: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payment_methods/{payment_method_id}/attach",
        params={"customer": customer},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def detach_payment_method(
    payment_method_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payment_methods/{payment_method_id}/detach",
        params={},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_payment_methods(
    customer: str,
    *,
    type: str,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "customer": customer,
        "type": type,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request(
        "GET",
        "/v1/payment_methods",
        params=params,
        stripe_account=stripe_account,
    )


def retrieve_customer_payment_method(
    customer_id: str,
    payment_method_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/customers/{customer_id}/payment_methods/{payment_method_id}",
        params=None,
        stripe_account=stripe_account,
    )
