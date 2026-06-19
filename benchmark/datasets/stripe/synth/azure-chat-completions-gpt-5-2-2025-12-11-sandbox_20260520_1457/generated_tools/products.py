from typing import Any, Dict, Optional, List

from .http_client import ok_or_error, stripe_request


def create_product(
    *,
    name: str,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    product_id: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    tax_code: Optional[str] = None,
    default_price_data: Optional[Dict[str, Any]] = None,
    images: Optional[List[str]] = None,
    marketing_features: Optional[List[Dict[str, Any]]] = None,
    package_dimensions: Optional[Dict[str, Any]] = None,
    shippable: Optional[bool] = None,
    statement_descriptor: Optional[str] = None,
    unit_label: Optional[str] = None,
    url: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "name": name,
        "active": active,
        "description": description,
        "id": product_id,
        "metadata": metadata,
        "tax_code": tax_code,
        "default_price_data": default_price_data,
        "images": images,
        "marketing_features": marketing_features,
        "package_dimensions": package_dimensions,
        "shippable": shippable,
        "statement_descriptor": statement_descriptor,
        "unit_label": unit_label,
        "url": url,
    }
    status, payload = stripe_request(
        "POST", "/v1/products", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def update_product(
    *,
    product_id: str,
    name: Optional[str] = None,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    default_price: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    tax_code: Optional[str] = None,
    images: Optional[List[str]] = None,
    marketing_features: Optional[List[Dict[str, Any]]] = None,
    package_dimensions: Optional[Dict[str, Any]] = None,
    shippable: Optional[bool] = None,
    statement_descriptor: Optional[str] = None,
    unit_label: Optional[str] = None,
    url: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "name": name,
        "active": active,
        "description": description,
        "default_price": default_price,
        "metadata": metadata,
        "tax_code": tax_code,
        "images": images,
        "marketing_features": marketing_features,
        "package_dimensions": package_dimensions,
        "shippable": shippable,
        "statement_descriptor": statement_descriptor,
        "unit_label": unit_label,
        "url": url,
    }
    status, payload = stripe_request(
        "POST", f"/v1/products/{product_id}", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def retrieve_product(*, product_id: str, stripe_account: Optional[str] = None) -> Any:
    status, payload = stripe_request("GET", f"/v1/products/{product_id}", stripe_account=stripe_account)
    return ok_or_error(status, payload)


def list_products(
    *,
    active: Optional[bool] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "active": active,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    status, payload = stripe_request("GET", "/v1/products", params=params, stripe_account=stripe_account)
    return ok_or_error(status, payload)
