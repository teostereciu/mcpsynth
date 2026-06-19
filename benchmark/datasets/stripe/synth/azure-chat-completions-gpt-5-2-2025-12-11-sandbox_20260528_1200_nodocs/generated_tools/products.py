from typing import Any, Dict, Optional

from .http import stripe_delete, stripe_get, stripe_post


def products_create(
    *,
    name: str,
    description: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    images: Optional[list] = None,
    shippable: Optional[bool] = None,
    statement_descriptor: Optional[str] = None,
    unit_label: Optional[str] = None,
    url: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {
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
    res, err = stripe_post(
        "/v1/products",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def products_retrieve(*, product_id: str, stripe_account: Optional[str] = None):
    res, err = stripe_get(f"/v1/products/{product_id}", stripe_account=stripe_account)
    return err or res


def products_update(
    *,
    product_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    images: Optional[list] = None,
    shippable: Optional[bool] = None,
    statement_descriptor: Optional[str] = None,
    unit_label: Optional[str] = None,
    url: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {
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
    res, err = stripe_post(f"/v1/products/{product_id}", data=data, stripe_account=stripe_account)
    return err or res


def products_delete(*, product_id: str, stripe_account: Optional[str] = None):
    res, err = stripe_delete(f"/v1/products/{product_id}", stripe_account=stripe_account)
    return err or res


def products_list(
    *,
    active: Optional[bool] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    params: Dict[str, Any] = {
        "active": active,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    res, err = stripe_get("/v1/products", params=params, stripe_account=stripe_account)
    return err or res
