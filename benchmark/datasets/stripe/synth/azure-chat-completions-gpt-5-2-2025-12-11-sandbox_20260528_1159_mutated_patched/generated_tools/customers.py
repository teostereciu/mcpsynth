from typing import Any, Dict, Optional

from .http import stripe_request


def create_customer(
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    tax: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
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
    params: Dict[str, Any] = {
        "email": email,
        "name": name,
        "phone": phone,
        "description": description,
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
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_customer(
    customer_id: str,
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    tax: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    balance: Optional[int] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    preferred_locales: Optional[list[str]] = None,
    source: Optional[str] = None,
    default_source: Optional[str] = None,
    tax_exempt: Optional[str] = None,
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
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_customer(
    customer_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/customers/{customer_id}",
        params=None,
        stripe_account=stripe_account,
    )
