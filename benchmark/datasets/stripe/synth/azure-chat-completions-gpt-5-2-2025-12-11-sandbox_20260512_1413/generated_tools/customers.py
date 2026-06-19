from typing import Any, Dict, Optional

from .stripe_client import stripe_list_all, stripe_request


def customers_create(
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_method: Optional[str] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    tax: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "email": email,
        "name": name,
        "phone": phone,
        "description": description,
        "address": address,
        "shipping": shipping,
        "metadata": metadata,
        "payment_method": payment_method,
        "invoice_settings": invoice_settings,
        "tax": tax,
    }
    return stripe_request("POST", "/v1/customers", params, stripe_account=stripe_account, idempotency_key=idempotency_key)


def customers_retrieve(customer_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/customers/{customer_id}", None, stripe_account=stripe_account)


def customers_update(
    customer_id: str,
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    default_source: Optional[str] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    tax: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "email": email,
        "name": name,
        "phone": phone,
        "description": description,
        "address": address,
        "shipping": shipping,
        "metadata": metadata,
        "default_source": default_source,
        "invoice_settings": invoice_settings,
        "tax": tax,
    }
    return stripe_request("POST", f"/v1/customers/{customer_id}", params, stripe_account=stripe_account)


def customers_delete(customer_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/customers/{customer_id}", None, stripe_account=stripe_account)


def customers_list(
    *,
    email: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "email": email,
        "created": created,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/customers", params, stripe_account=stripe_account)


def customers_list_all(
    *,
    email: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    limit: int = 100,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"email": email, "created": created}
    return stripe_list_all("/v1/customers", params, stripe_account=stripe_account, limit=limit, max_pages=max_pages)
