from typing import Any, Dict, Optional

from .stripe_client import stripe_request


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


def retrieve_customer(
    customer_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/customers/{customer}"""
    return stripe_request("GET", f"/v1/customers/{customer_id}", None, stripe_account=stripe_account)


def update_customer(
    customer_id: str,
    *,
    params: Dict[str, Any],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/customers/{customer}"""
    return stripe_request(
        "POST",
        f"/v1/customers/{customer_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def delete_customer(
    customer_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """DELETE /v1/customers/{customer}"""
    return stripe_request("DELETE", f"/v1/customers/{customer_id}", None, stripe_account=stripe_account)


def list_customers(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/customers"""
    return stripe_request("GET", "/v1/customers", params, stripe_account=stripe_account)
