from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def create_subscription(
    customer: str,
    items: list,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/subscriptions"""
    body: Dict[str, Any] = {"customer": customer, "items": items}
    if params:
        body.update(params)
    return stripe_request(
        "POST",
        "/v1/subscriptions",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_subscription(
    subscription_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/subscriptions/{id}"""
    return stripe_request("GET", f"/v1/subscriptions/{subscription_id}", None, stripe_account=stripe_account)


def update_subscription(
    subscription_id: str,
    *,
    params: Dict[str, Any],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/subscriptions/{id}"""
    return stripe_request(
        "POST",
        f"/v1/subscriptions/{subscription_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def cancel_subscription(
    subscription_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """DELETE /v1/subscriptions/{id}"""
    return stripe_request(
        "DELETE",
        f"/v1/subscriptions/{subscription_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_subscriptions(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/subscriptions"""
    return stripe_request("GET", "/v1/subscriptions", params, stripe_account=stripe_account)
