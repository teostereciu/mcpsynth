from typing import Any, Dict, Optional

from .http import stripe_request


def products_create(
    name: str,
    description: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    images: Optional[list] = None,
    url: Optional[str] = None,
    shippable: Optional[bool] = None,
    statement_descriptor: Optional[str] = None,
    unit_label: Optional[str] = None,
    tax_code: Optional[str] = None,
    default_price_data: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "name": name,
        "description": description,
        "active": active,
        "metadata": metadata,
        "images": images,
        "url": url,
        "shippable": shippable,
        "statement_descriptor": statement_descriptor,
        "unit_label": unit_label,
        "tax_code": tax_code,
        "default_price_data": default_price_data,
    }
    data, err = stripe_request(
        "POST",
        "/v1/products",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def products_retrieve(product_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("GET", f"/v1/products/{product_id}", stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]


def products_update(
    product_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    images: Optional[list] = None,
    url: Optional[str] = None,
    shippable: Optional[bool] = None,
    statement_descriptor: Optional[str] = None,
    unit_label: Optional[str] = None,
    tax_code: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "name": name,
        "description": description,
        "active": active,
        "metadata": metadata,
        "images": images,
        "url": url,
        "shippable": shippable,
        "statement_descriptor": statement_descriptor,
        "unit_label": unit_label,
        "tax_code": tax_code,
    }
    data, err = stripe_request(
        "POST",
        f"/v1/products/{product_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def products_delete(product_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("DELETE", f"/v1/products/{product_id}", stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]


def products_list(
    limit: int = 10,
    active: Optional[bool] = None,
    created: Optional[Dict[str, Any]] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "limit": limit,
        "active": active,
        "created": created,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    data, err = stripe_request("GET", "/v1/products", params=params, stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]
