from typing import Any, Dict, List, Optional

from .stripe_client import stripe_request


def products_create(
    *,
    name: str,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    product_id: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tax_code: Optional[str] = None,
    default_price_data: Optional[Dict[str, Any]] = None,
    images: Optional[List[str]] = None,
    marketing_features: Optional[List[Dict[str, Any]]] = None,
    package_dimensions: Optional[Dict[str, Any]] = None,
    shippable: Optional[bool] = None,
    statement_descriptor: Optional[str] = None,
    unit_label: Optional[str] = None,
    url: Optional[str] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"name": name}
    if active is not None:
        data["active"] = active
    if description is not None:
        data["description"] = description
    if product_id is not None:
        data["id"] = product_id
    if metadata is not None:
        data["metadata"] = metadata
    if tax_code is not None:
        data["tax_code"] = tax_code
    if default_price_data is not None:
        data["default_price_data"] = default_price_data
    if images is not None:
        data["images"] = images
    if marketing_features is not None:
        data["marketing_features"] = marketing_features
    if package_dimensions is not None:
        data["package_dimensions"] = package_dimensions
    if shippable is not None:
        data["shippable"] = shippable
    if statement_descriptor is not None:
        data["statement_descriptor"] = statement_descriptor
    if unit_label is not None:
        data["unit_label"] = unit_label
    if url is not None:
        data["url"] = url
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/products",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def products_retrieve(*, product_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/products/{product_id}", stripe_account=stripe_account)


def products_update(
    *,
    product_id: str,
    name: Optional[str] = None,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    default_price: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tax_code: Optional[str] = None,
    images: Optional[List[str]] = None,
    marketing_features: Optional[List[Dict[str, Any]]] = None,
    package_dimensions: Optional[Dict[str, Any]] = None,
    shippable: Optional[bool] = None,
    statement_descriptor: Optional[str] = None,
    unit_label: Optional[str] = None,
    url: Optional[str] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if name is not None:
        data["name"] = name
    if active is not None:
        data["active"] = active
    if description is not None:
        data["description"] = description
    if default_price is not None:
        data["default_price"] = default_price
    if metadata is not None:
        data["metadata"] = metadata
    if tax_code is not None:
        data["tax_code"] = tax_code
    if images is not None:
        data["images"] = images
    if marketing_features is not None:
        data["marketing_features"] = marketing_features
    if package_dimensions is not None:
        data["package_dimensions"] = package_dimensions
    if shippable is not None:
        data["shippable"] = shippable
    if statement_descriptor is not None:
        data["statement_descriptor"] = statement_descriptor
    if unit_label is not None:
        data["unit_label"] = unit_label
    if url is not None:
        data["url"] = url
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/products/{product_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def products_delete(*, product_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/products/{product_id}", stripe_account=stripe_account)


def products_list(
    *,
    limit: Optional[int] = 10,
    active: Optional[bool] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    ids: Optional[List[str]] = None,
    extra_query: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if limit is not None:
        query["limit"] = limit
    if active is not None:
        query["active"] = active
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if ids is not None:
        query["ids"] = ids
    if extra_query:
        query.update(extra_query)

    return stripe_request("GET", "/v1/products", params=query, stripe_account=stripe_account)
