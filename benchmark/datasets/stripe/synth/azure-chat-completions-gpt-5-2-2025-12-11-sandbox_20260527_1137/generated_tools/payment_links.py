from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_payment_link(
    line_items: list,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_links"""
    body: Dict[str, Any] = {"line_items": line_items}
    body.update(params or {})
    return stripe_request(
        "POST",
        "/v1/payment_links",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_payment_link(
    payment_link_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_links/{payment_link}"""
    return stripe_request(
        "POST",
        f"/v1/payment_links/{payment_link_id}",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payment_link(
    payment_link_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payment_links/{payment_link}"""
    return stripe_request("GET", f"/v1/payment_links/{payment_link_id}", {}, stripe_account=stripe_account)


def list_payment_links(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payment_links"""
    return stripe_request("GET", "/v1/payment_links", params or {}, stripe_account=stripe_account)


def list_payment_link_line_items(
    payment_link_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payment_links/{payment_link}/line_items"""
    return stripe_request(
        "GET",
        f"/v1/payment_links/{payment_link_id}/line_items",
        params or {},
        stripe_account=stripe_account,
    )
