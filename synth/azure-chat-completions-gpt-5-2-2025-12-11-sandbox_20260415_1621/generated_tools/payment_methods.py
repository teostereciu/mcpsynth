from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def payment_methods_create(
    *,
    type: str,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    allow_redisplay: Optional[str] = None,
    details: Optional[Dict[str, Any]] = None,
    radar_options: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    # `details` should be a dict keyed by payment method type, e.g. {"card": {...}} or {"us_bank_account": {...}}
    data: Dict[str, Any] = {"type": type}
    if billing_details is not None:
        data["billing_details"] = billing_details
    if metadata is not None:
        data["metadata"] = metadata
    if allow_redisplay is not None:
        data["allow_redisplay"] = allow_redisplay
    if radar_options is not None:
        data["radar_options"] = radar_options
    if details:
        data.update(details)
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/payment_methods",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payment_methods_retrieve(*, payment_method_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payment_methods/{payment_method_id}", stripe_account=stripe_account)


def payment_methods_update(
    *,
    payment_method_id: str,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    allow_redisplay: Optional[str] = None,
    card: Optional[Dict[str, Any]] = None,
    us_bank_account: Optional[Dict[str, Any]] = None,
    payto: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if billing_details is not None:
        data["billing_details"] = billing_details
    if metadata is not None:
        data["metadata"] = metadata
    if allow_redisplay is not None:
        data["allow_redisplay"] = allow_redisplay
    if card is not None:
        data["card"] = card
    if us_bank_account is not None:
        data["us_bank_account"] = us_bank_account
    if payto is not None:
        data["payto"] = payto
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/payment_methods/{payment_method_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payment_methods_attach(
    *,
    payment_method_id: str,
    customer: str,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"customer": customer}
    if extra:
        data.update(extra)
    return stripe_request(
        "POST",
        f"/v1/payment_methods/{payment_method_id}/attach",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payment_methods_detach(
    *,
    payment_method_id: str,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payment_methods/{payment_method_id}/detach",
        data={},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def customers_payment_methods_retrieve(
    *,
    customer_id: str,
    payment_method_id: str,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/customers/{customer_id}/payment_methods/{payment_method_id}",
        stripe_account=stripe_account,
    )


def customers_payment_methods_list(
    *,
    customer_id: str,
    type: str,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_query: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {"type": type}
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if extra_query:
        query.update(extra_query)

    return stripe_request(
        "GET",
        f"/v1/customers/{customer_id}/payment_methods",
        params=query,
        stripe_account=stripe_account,
    )
