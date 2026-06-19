from typing import Any, Dict, Optional

from .http import stripe_request


def create_payment_method(
    type: str,
    *,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    **type_details: Any,
) -> Dict[str, Any]:
    # Pass type-specific details via **type_details (e.g. card={...}, us_bank_account={...}).
    body: Dict[str, Any] = {"type": type, "billing_details": billing_details, "metadata": metadata}
    body.update(type_details)
    return stripe_request("POST", "/v1/payment_methods", body, stripe_account=stripe_account)


def update_payment_method(
    payment_method_id: str,
    *,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    **params: Any,
) -> Dict[str, Any]:
    body: Dict[str, Any] = {"billing_details": billing_details, "metadata": metadata}
    body.update(params)
    return stripe_request("POST", f"/v1/payment_methods/{payment_method_id}", body, stripe_account=stripe_account)


def retrieve_payment_method(payment_method_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payment_methods/{payment_method_id}", None, stripe_account=stripe_account)


def retrieve_customer_payment_method(
    customer_id: str,
    payment_method_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/customers/{customer_id}/payment_methods/{payment_method_id}",
        None,
        stripe_account=stripe_account,
    )


def list_customer_payment_methods(
    customer_id: str,
    *,
    type: str = "card",
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"type": type, "limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    return stripe_request("GET", f"/v1/customers/{customer_id}/payment_methods", params, stripe_account=stripe_account)
