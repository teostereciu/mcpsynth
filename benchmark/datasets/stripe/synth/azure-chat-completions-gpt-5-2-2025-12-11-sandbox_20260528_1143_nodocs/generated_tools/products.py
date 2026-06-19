from typing import Any, Dict, Optional

from .http import stripe_request


def products_create(
    *,
    name: str,
    description: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, str]] = None,
    images: Optional[list[str]] = None,
    url: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "name": name,
        "description": description,
        "active": active,
        "metadata": metadata,
        "images": images,
        "url": url,
    }
    res, err = stripe_request(
        "POST",
        "/v1/products",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or res  # type: ignore[return-value]


def products_retrieve(*, product_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/products/{product_id}", stripe_account=stripe_account)
    return err or res  # type: ignore[return-value]


def products_update(
    *,
    product_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, str]] = None,
    images: Optional[list[str]] = None,
    url: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "name": name,
        "description": description,
        "active": active,
        "metadata": metadata,
        "images": images,
        "url": url,
    }
    res, err = stripe_request("POST", f"/v1/products/{product_id}", data=data, stripe_account=stripe_account)
    return err or res  # type: ignore[return-value]


def products_delete(*, product_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("DELETE", f"/v1/products/{product_id}", stripe_account=stripe_account)
    return err or res  # type: ignore[return-value]


def products_list(
    *,
    active: Optional[bool] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    res, err = stripe_request("GET", "/v1/products", params=params, stripe_account=stripe_account)
    return err or res  # type: ignore[return-value]
