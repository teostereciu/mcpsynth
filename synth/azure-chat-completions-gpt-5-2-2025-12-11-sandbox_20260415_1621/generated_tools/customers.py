from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def customers_create(
    *,
    name: Optional[str] = None,
    email: Optional[str] = None,
    description: Optional[str] = None,
    phone: Optional[str] = None,
    payment_method: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    tax: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if name is not None:
        data["name"] = name
    if email is not None:
        data["email"] = email
    if description is not None:
        data["description"] = description
    if phone is not None:
        data["phone"] = phone
    if payment_method is not None:
        data["payment_method"] = payment_method
    if metadata is not None:
        data["metadata"] = metadata
    if address is not None:
        data["address"] = address
    if shipping is not None:
        data["shipping"] = shipping
    if tax is not None:
        data["tax"] = tax
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/customers",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def customers_retrieve(*, customer_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/customers/{customer_id}", stripe_account=stripe_account)


def customers_update(
    *,
    customer_id: str,
    name: Optional[str] = None,
    email: Optional[str] = None,
    description: Optional[str] = None,
    phone: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    tax: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if name is not None:
        data["name"] = name
    if email is not None:
        data["email"] = email
    if description is not None:
        data["description"] = description
    if phone is not None:
        data["phone"] = phone
    if metadata is not None:
        data["metadata"] = metadata
    if address is not None:
        data["address"] = address
    if shipping is not None:
        data["shipping"] = shipping
    if tax is not None:
        data["tax"] = tax
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/customers/{customer_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def customers_delete(*, customer_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/customers/{customer_id}", stripe_account=stripe_account)


def customers_list(
    *,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    email: Optional[str] = None,
    extra_query: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if email is not None:
        query["email"] = email
    if extra_query:
        query.update(extra_query)

    return stripe_request("GET", "/v1/customers", params=query, stripe_account=stripe_account)
