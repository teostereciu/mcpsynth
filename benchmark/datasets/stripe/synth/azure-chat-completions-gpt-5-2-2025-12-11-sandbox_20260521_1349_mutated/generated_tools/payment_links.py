from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def create_payment_link(
    line_items: list,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_links"""
    body: Dict[str, Any] = {"line_items": line_items}
    if params:
        body.update(params)
    return stripe_request(
        "POST",
        "/v1/payment_links",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payment_link(
    payment_link_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payment_links/{id}"""
    return stripe_request("GET", f"/v1/payment_links/{payment_link_id}", None, stripe_account=stripe_account)


def update_payment_link(
    payment_link_id: str,
    *,
    params: Dict[str, Any],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_links/{id}"""
    return stripe_request(
        "POST",
        f"/v1/payment_links/{payment_link_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_payment_links(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payment_links"""
    return stripe_request("GET", "/v1/payment_links", params, stripe_account=stripe_account)


def list_payment_link_line_items(
    payment_link_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payment_links/{id}/line_items"""
    return stripe_request(
        "GET",
        f"/v1/payment_links/{payment_link_id}/line_items",
        params,
        stripe_account=stripe_account,
    )
