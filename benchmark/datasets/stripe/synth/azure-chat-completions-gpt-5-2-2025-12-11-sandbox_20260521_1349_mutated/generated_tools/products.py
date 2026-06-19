from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def create_product(
    name: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/products"""
    body: Dict[str, Any] = {"name": name}
    if params:
        body.update(params)
    return stripe_request(
        "POST",
        "/v1/products",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_product(
    product_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/products/{id}"""
    return stripe_request("GET", f"/v1/products/{product_id}", None, stripe_account=stripe_account)


def update_product(
    product_id: str,
    *,
    params: Dict[str, Any],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/products/{id}"""
    return stripe_request(
        "POST",
        f"/v1/products/{product_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def delete_product(
    product_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """DELETE /v1/products/{id}"""
    return stripe_request("DELETE", f"/v1/products/{product_id}", None, stripe_account=stripe_account)


def list_products(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/products"""
    return stripe_request("GET", "/v1/products", params, stripe_account=stripe_account)
