from typing import Any, Dict, List, Optional

from .http_client import stripe_request, _maybe_expand


def create_subscription(
    customer: str,
    items: List[Dict[str, Any]],
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/subscriptions"""
    body: Dict[str, Any] = {"customer": customer, "items": items}
    body.update(params or {})
    return stripe_request(
        "POST",
        "/v1/subscriptions",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_subscription(
    subscription_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/subscriptions/{subscription}"""
    return stripe_request(
        "POST",
        f"/v1/subscriptions/{subscription_id}",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_subscription(
    subscription_id: str,
    *,
    expand: Optional[List[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/subscriptions/{subscription}"""
    return stripe_request(
        "GET",
        f"/v1/subscriptions/{subscription_id}",
        _maybe_expand({}, expand),
        stripe_account=stripe_account,
    )


def cancel_subscription(
    subscription_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """DELETE /v1/subscriptions/{subscription}"""
    return stripe_request(
        "DELETE",
        f"/v1/subscriptions/{subscription_id}",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_subscriptions(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/subscriptions"""
    return stripe_request("GET", "/v1/subscriptions", params or {}, stripe_account=stripe_account)


def search_subscriptions(
    query: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/subscriptions/search"""
    p = {"query": query}
    p.update(params or {})
    return stripe_request("GET", "/v1/subscriptions/search", p, stripe_account=stripe_account)
