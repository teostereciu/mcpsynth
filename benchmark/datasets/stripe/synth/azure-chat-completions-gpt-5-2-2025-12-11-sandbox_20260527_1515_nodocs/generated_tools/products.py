from typing import Any, Dict, Optional

from ._client import stripe_request


def products_create(
    *,
    name: str,
    description: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    images: Optional[list[str]] = None,
    shippable: Optional[bool] = None,
    statement_descriptor: Optional[str] = None,
    unit_label: Optional[str] = None,
    url: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "name": name,
        "description": description,
        "active": active,
        "metadata": metadata,
        "images": images,
        "shippable": shippable,
        "statement_descriptor": statement_descriptor,
        "unit_label": unit_label,
        "url": url,
    }
    data, err = stripe_request(
        "POST",
        "/v1/products",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or data  # type: ignore[return-value]


def products_retrieve(*, product_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("GET", f"/v1/products/{product_id}", stripe_account=stripe_account)
    return err or data  # type: ignore[return-value]


def products_update(
    *,
    product_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    images: Optional[list[str]] = None,
    shippable: Optional[bool] = None,
    statement_descriptor: Optional[str] = None,
    unit_label: Optional[str] = None,
    url: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "name": name,
        "description": description,
        "active": active,
        "metadata": metadata,
        "images": images,
        "shippable": shippable,
        "statement_descriptor": statement_descriptor,
        "unit_label": unit_label,
        "url": url,
    }
    data, err = stripe_request("POST", f"/v1/products/{product_id}", params=params, stripe_account=stripe_account)
    return err or data  # type: ignore[return-value]


def products_delete(*, product_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("DELETE", f"/v1/products/{product_id}", stripe_account=stripe_account)
    return err or data  # type: ignore[return-value]


def products_list(
    *,
    active: Optional[bool] = None,
    ids: Optional[list[str]] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "ids": ids,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
        "created": created,
    }
    data, err = stripe_request("GET", "/v1/products", params=params, stripe_account=stripe_account)
    return err or data  # type: ignore[return-value]
