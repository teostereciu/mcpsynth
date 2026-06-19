from typing import Any, Dict, Optional

from .stripe_client import stripe_list_all, stripe_request


def products_create(
    name: str,
    *,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    id: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tax_code: Optional[str] = None,
    default_price_data: Optional[Dict[str, Any]] = None,
    images: Optional[list] = None,
    url: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "name": name,
        "active": active,
        "description": description,
        "id": id,
        "metadata": metadata,
        "tax_code": tax_code,
        "default_price_data": default_price_data,
        "images": images,
        "url": url,
    }
    return stripe_request("POST", "/v1/products", params, stripe_account=stripe_account, idempotency_key=idempotency_key)


def products_retrieve(product_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/products/{product_id}", None, stripe_account=stripe_account)


def products_update(
    product_id: str,
    *,
    name: Optional[str] = None,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    default_price: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tax_code: Optional[str] = None,
    images: Optional[list] = None,
    url: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "name": name,
        "active": active,
        "description": description,
        "default_price": default_price,
        "metadata": metadata,
        "tax_code": tax_code,
        "images": images,
        "url": url,
    }
    return stripe_request("POST", f"/v1/products/{product_id}", params, stripe_account=stripe_account)


def products_delete(product_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/products/{product_id}", None, stripe_account=stripe_account)


def products_list(
    *,
    active: Optional[bool] = None,
    ids: Optional[list] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "ids": ids,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/products", params, stripe_account=stripe_account)


def products_list_all(
    *,
    active: Optional[bool] = None,
    ids: Optional[list] = None,
    stripe_account: Optional[str] = None,
    limit: int = 100,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"active": active, "ids": ids}
    return stripe_list_all("/v1/products", params, stripe_account=stripe_account, limit=limit, max_pages=max_pages)
