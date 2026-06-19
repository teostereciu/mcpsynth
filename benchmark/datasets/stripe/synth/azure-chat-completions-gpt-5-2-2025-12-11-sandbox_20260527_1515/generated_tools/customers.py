from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_customer(
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    payment_method: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
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
        "payment_method": payment_method,
        "metadata": metadata,
        "invoice_settings": invoice_settings,
    }
    return stripe_request(
        "POST",
        "/v1/customers",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_customer(
    customer_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request("GET", f"/v1/customers/{customer_id}", params=params, stripe_account=stripe_account)


def update_customer(
    customer_id: str,
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    default_source: Optional[str] = None,
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
        "invoice_settings": invoice_settings,
        "default_source": default_source,
    }
    return stripe_request("POST", f"/v1/customers/{customer_id}", params=params, stripe_account=stripe_account)


def delete_customer(
    customer_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/customers/{customer_id}", stripe_account=stripe_account)


def list_customers(
    *,
    email: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "email": email,
        "created": created,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
        "expand": expand,
    }
    return stripe_request("GET", "/v1/customers", params=params, stripe_account=stripe_account)
