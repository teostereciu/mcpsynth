from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_product(
    name: str,
    *,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    product_id: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
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
    return stripe_request(
        "POST",
        "/v1/products",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_product(
    product_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request("GET", f"/v1/products/{product_id}", params=params, stripe_account=stripe_account)


def update_product(
    product_id: str,
    *,
    active: Optional[bool] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    default_price: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    tax_code: Optional[str] = None,
    images: Optional[list[str]] = None,
    url: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "name": name,
        "description": description,
        "default_price": default_price,
        "metadata": metadata,
        "tax_code": tax_code,
        "images": images,
        "url": url,
    }
    return stripe_request("POST", f"/v1/products/{product_id}", params=params, stripe_account=stripe_account)


def delete_product(
    product_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/products/{product_id}", stripe_account=stripe_account)


def list_products(
    *,
    active: Optional[bool] = None,
    created: Optional[Dict[str, Any]] = None,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "created": created,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
        "expand": expand,
    }
    return stripe_request("GET", "/v1/products", params=params, stripe_account=stripe_account)
