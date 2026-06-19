from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_customer(
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    phone: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    tax: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    balance: Optional[int] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    preferred_locales: Optional[list[str]] = None,
    source: Optional[str] = None,
    tax_exempt: Optional[str] = None,
    test_clock: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/customers

    Doc: docs/customers.md (Create a customer)
    """
    params: Dict[str, Any] = {
        "email": email,
        "name": name,
        "description": description,
        "phone": phone,
        "address": address,
        "shipping": shipping,
        "tax": tax,
        "metadata": metadata,
        "payment_method": payment_method,
        "balance": balance,
        "invoice_settings": invoice_settings,
        "preferred_locales": preferred_locales,
        "source": source,
        "tax_exempt": tax_exempt,
        "test_clock": test_clock,
    }
    return stripe_request(
        "POST",
        "/v1/customers",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_customer(
    customer_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/customers/{customer_id}

    Doc: docs/customers.md (Retrieve a customer)
    """
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request(
        "GET",
        f"/v1/customers/{customer_id}",
        params,
        stripe_account=stripe_account,
    )


def update_customer(
    customer_id: str,
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    phone: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    tax: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    balance: Optional[int] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    preferred_locales: Optional[list[str]] = None,
    source: Optional[str] = None,
    default_source: Optional[str] = None,
    tax_exempt: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/customers/{customer_id}

    Doc: docs/customers.md (Update a customer)
    """
    params: Dict[str, Any] = {
        "email": email,
        "name": name,
        "description": description,
        "phone": phone,
        "address": address,
        "shipping": shipping,
        "tax": tax,
        "metadata": metadata,
        "balance": balance,
        "invoice_settings": invoice_settings,
        "preferred_locales": preferred_locales,
        "source": source,
        "default_source": default_source,
        "tax_exempt": tax_exempt,
    }
    return stripe_request(
        "POST",
        f"/v1/customers/{customer_id}",
        params,
        stripe_account=stripe_account,
    )


def delete_customer(
    customer_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """DELETE /v1/customers/{customer_id}

    Doc: docs/customers.md (Delete a customer)
    """
    return stripe_request(
        "DELETE",
        f"/v1/customers/{customer_id}",
        None,
        stripe_account=stripe_account,
    )


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
    """GET /v1/customers

    Doc: docs/customers.md (List all customers)
    """
    params: Dict[str, Any] = {
        "email": email,
        "created": created,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
        "expand": expand,
    }
    return stripe_request(
        "GET",
        "/v1/customers",
        params,
        stripe_account=stripe_account,
    )
