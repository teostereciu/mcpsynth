from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_product(
    name: str,
    *,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    product_id: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tax_code: Optional[str] = None,
    default_price_data: Optional[Dict[str, Any]] = None,
    images: Optional[list[str]] = None,
    url: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "name": name,
        "active": active,
        "description": description,
        "id": product_id,
        "metadata": metadata,
        "tax_code": tax_code,
        "default_price_data": default_price_data,
        "images": images,
        "url": url,
    }
    _, data = stripe_request(
        "POST",
        "/v1/products",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data


def retrieve_product(
    product_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    _, data = stripe_request(
        "GET",
        f"/v1/products/{product_id}",
        stripe_account=stripe_account,
    )
    return data


def update_product(
    product_id: str,
    *,
    name: Optional[str] = None,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    default_price: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tax_code: Optional[str] = None,
    images: Optional[list[str]] = None,
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
    _, data = stripe_request(
        "POST",
        f"/v1/products/{product_id}",
        params=params,
        stripe_account=stripe_account,
    )
    return data


def delete_product(
    product_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    _, data = stripe_request(
        "DELETE",
        f"/v1/products/{product_id}",
        stripe_account=stripe_account,
    )
    return data


def list_products(
    *,
    active: Optional[bool] = None,
    ids: Optional[list[str]] = None,
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
    _, data = stripe_request(
        "GET",
        "/v1/products",
        params=params,
        stripe_account=stripe_account,
    )
    return data
