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
    images: Optional[list] = None,
    marketing_features: Optional[list] = None,
    package_dimensions: Optional[Dict[str, Any]] = None,
    shippable: Optional[bool] = None,
    statement_descriptor: Optional[str] = None,
    unit_label: Optional[str] = None,
    url: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/products"""
    params: Dict[str, Any] = {"name": name}
    if active is not None:
        params["active"] = active
    if description is not None:
        params["description"] = description
    if product_id is not None:
        params["id"] = product_id
    if metadata is not None:
        params["metadata"] = metadata
    if tax_code is not None:
        params["tax_code"] = tax_code
    if default_price_data is not None:
        params["default_price_data"] = default_price_data
    if images is not None:
        params["images"] = images
    if marketing_features is not None:
        params["marketing_features"] = marketing_features
    if package_dimensions is not None:
        params["package_dimensions"] = package_dimensions
    if shippable is not None:
        params["shippable"] = shippable
    if statement_descriptor is not None:
        params["statement_descriptor"] = statement_descriptor
    if unit_label is not None:
        params["unit_label"] = unit_label
    if url is not None:
        params["url"] = url

    data, err = stripe_request(
        "POST",
        "/v1/products",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def update_product(
    product_id: str,
    *,
    name: Optional[str] = None,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    default_price: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tax_code: Optional[str] = None,
    images: Optional[list] = None,
    marketing_features: Optional[list] = None,
    package_dimensions: Optional[Dict[str, Any]] = None,
    shippable: Optional[bool] = None,
    statement_descriptor: Optional[str] = None,
    unit_label: Optional[str] = None,
    url: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/products/{id}"""
    params: Dict[str, Any] = {}
    if name is not None:
        params["name"] = name
    if active is not None:
        params["active"] = active
    if description is not None:
        params["description"] = description
    if default_price is not None:
        params["default_price"] = default_price
    if metadata is not None:
        params["metadata"] = metadata
    if tax_code is not None:
        params["tax_code"] = tax_code
    if images is not None:
        params["images"] = images
    if marketing_features is not None:
        params["marketing_features"] = marketing_features
    if package_dimensions is not None:
        params["package_dimensions"] = package_dimensions
    if shippable is not None:
        params["shippable"] = shippable
    if statement_descriptor is not None:
        params["statement_descriptor"] = statement_descriptor
    if unit_label is not None:
        params["unit_label"] = unit_label
    if url is not None:
        params["url"] = url

    data, err = stripe_request(
        "POST",
        f"/v1/products/{product_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def retrieve_product(
    product_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/products/{id}"""
    data, err = stripe_request(
        "GET",
        f"/v1/products/{product_id}",
        params=None,
        stripe_account=stripe_account,
    )
    return data if err is None else err
