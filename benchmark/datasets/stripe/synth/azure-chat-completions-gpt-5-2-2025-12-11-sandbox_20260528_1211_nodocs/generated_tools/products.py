from typing import Any, Dict, Optional

from .http import stripe_request


def create_product(
    name: str,
    *,
    description: Optional[str] = None,
    active: Optional[bool] = None,
    images: Optional[list[str]] = None,
    metadata: Optional[Dict[str, str]] = None,
    default_price_data: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"name": name}
    if description is not None:
        data["description"] = description
    if active is not None:
        data["active"] = active
    if images is not None:
        data["images"] = images
    if metadata is not None:
        data["metadata"] = metadata
    if default_price_data is not None:
        data["default_price_data"] = default_price_data

    res, err = stripe_request(
        "POST",
        "/v1/products",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def retrieve_product(product_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/products/{product_id}", stripe_account=stripe_account)
    return res if err is None else err


def update_product(
    product_id: str,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    active: Optional[bool] = None,
    images: Optional[list[str]] = None,
    metadata: Optional[Dict[str, str]] = None,
    default_price: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if active is not None:
        data["active"] = active
    if images is not None:
        data["images"] = images
    if metadata is not None:
        data["metadata"] = metadata
    if default_price is not None:
        data["default_price"] = default_price

    res, err = stripe_request("POST", f"/v1/products/{product_id}", data=data, stripe_account=stripe_account)
    return res if err is None else err


def delete_product(product_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("DELETE", f"/v1/products/{product_id}", stripe_account=stripe_account)
    return res if err is None else err


def list_products(
    *,
    active: Optional[bool] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if active is not None:
        query["active"] = active
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before

    res, err = stripe_request("GET", "/v1/products", query=query, stripe_account=stripe_account)
    return res if err is None else err
