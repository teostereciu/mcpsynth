from typing import Any, Dict, List, Optional

from .http_client import stripe_request, _maybe_expand


def create_product(
    name: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/products"""
    body = {"name": name}
    body.update(params or {})
    return stripe_request(
        "POST",
        "/v1/products",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_product(
    product_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/products/{product}"""
    return stripe_request(
        "POST",
        f"/v1/products/{product_id}",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_product(
    product_id: str,
    *,
    expand: Optional[List[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/products/{product}"""
    return stripe_request(
        "GET",
        f"/v1/products/{product_id}",
        _maybe_expand({}, expand),
        stripe_account=stripe_account,
    )


def delete_product(
    product_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """DELETE /v1/products/{product}"""
    return stripe_request(
        "DELETE",
        f"/v1/products/{product_id}",
        {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_products(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/products"""
    return stripe_request("GET", "/v1/products", params or {}, stripe_account=stripe_account)


def search_products(
    query: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/products/search"""
    p = {"query": query}
    p.update(params or {})
    return stripe_request("GET", "/v1/products/search", p, stripe_account=stripe_account)
