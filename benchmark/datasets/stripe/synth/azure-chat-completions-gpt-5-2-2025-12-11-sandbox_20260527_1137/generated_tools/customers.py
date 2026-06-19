from typing import Any, Dict, List, Optional

from .http_client import stripe_request, _maybe_expand


def create_customer(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/customers"""
    return stripe_request(
        "POST",
        "/v1/customers",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_customer(
    customer_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/customers/{customer}"""
    return stripe_request(
        "POST",
        f"/v1/customers/{customer_id}",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_customer(
    customer_id: str,
    *,
    expand: Optional[List[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/customers/{customer}"""
    return stripe_request(
        "GET",
        f"/v1/customers/{customer_id}",
        _maybe_expand({}, expand),
        stripe_account=stripe_account,
    )


def delete_customer(
    customer_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """DELETE /v1/customers/{customer}"""
    return stripe_request(
        "DELETE",
        f"/v1/customers/{customer_id}",
        {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_customers(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/customers"""
    return stripe_request("GET", "/v1/customers", params or {}, stripe_account=stripe_account)


def search_customers(
    query: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/customers/search"""
    p = {"query": query}
    p.update(params or {})
    return stripe_request("GET", "/v1/customers/search", p, stripe_account=stripe_account)
