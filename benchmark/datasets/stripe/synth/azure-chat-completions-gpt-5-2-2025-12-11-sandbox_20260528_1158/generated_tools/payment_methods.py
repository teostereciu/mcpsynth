from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def create_payment_method(
    type: str,
    *,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    allow_redisplay: Optional[str] = None,
    card: Optional[Dict[str, Any]] = None,
    us_bank_account: Optional[Dict[str, Any]] = None,
    sepa_debit: Optional[Dict[str, Any]] = None,
    au_becs_debit: Optional[Dict[str, Any]] = None,
    bacs_debit: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"type": type}
    if billing_details is not None:
        params["billing_details"] = billing_details
    if metadata is not None:
        params["metadata"] = metadata
    if allow_redisplay is not None:
        params["allow_redisplay"] = allow_redisplay
    if card is not None:
        params["card"] = card
    if us_bank_account is not None:
        params["us_bank_account"] = us_bank_account
    if sepa_debit is not None:
        params["sepa_debit"] = sepa_debit
    if au_becs_debit is not None:
        params["au_becs_debit"] = au_becs_debit
    if bacs_debit is not None:
        params["bacs_debit"] = bacs_debit

    return stripe_request("POST", "/v1/payment_methods", params=params)


def retrieve_payment_method(
    payment_method_id: str,
    *,
    expand: Optional[list[str]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return stripe_request("GET", f"/v1/payment_methods/{payment_method_id}", params=params)


def update_payment_method(
    payment_method_id: str,
    *,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    allow_redisplay: Optional[str] = None,
    card: Optional[Dict[str, Any]] = None,
    us_bank_account: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if billing_details is not None:
        params["billing_details"] = billing_details
    if metadata is not None:
        params["metadata"] = metadata
    if allow_redisplay is not None:
        params["allow_redisplay"] = allow_redisplay
    if card is not None:
        params["card"] = card
    if us_bank_account is not None:
        params["us_bank_account"] = us_bank_account

    return stripe_request("POST", f"/v1/payment_methods/{payment_method_id}", params=params)


def attach_payment_method(
    payment_method_id: str,
    customer: str,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payment_methods/{payment_method_id}/attach",
        params={"customer": customer},
    )


def detach_payment_method(payment_method_id: str) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/payment_methods/{payment_method_id}/detach", params={})


def list_payment_methods(
    customer: str,
    type: str,
    *,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"customer": customer, "type": type}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before
    return stripe_request("GET", "/v1/payment_methods", params=params)


def retrieve_customer_payment_method(
    customer_id: str,
    payment_method_id: str,
    *,
    expand: Optional[list[str]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return stripe_request(
        "GET",
        f"/v1/customers/{customer_id}/payment_methods/{payment_method_id}",
        params=params,
    )
