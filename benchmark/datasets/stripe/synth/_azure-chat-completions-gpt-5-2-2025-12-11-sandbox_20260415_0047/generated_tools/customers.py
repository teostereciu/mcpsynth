"""Customer and PaymentMethod management."""

from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import stripe_request


@mcp.tool()
def customers_create(
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    payment_method: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a customer (/v1/customers)."""

    data: Dict[str, Any] = {}
    if email is not None:
        data["email"] = email
    if name is not None:
        data["name"] = name
    if phone is not None:
        data["phone"] = phone
    if description is not None:
        data["description"] = description
    if address is not None:
        data["address"] = address
    if shipping is not None:
        data["shipping"] = shipping
    if metadata is not None:
        data["metadata"] = metadata
    if invoice_settings is not None:
        data["invoice_settings"] = invoice_settings
    if payment_method is not None:
        data["payment_method"] = payment_method
    return stripe_request("POST", "/v1/customers", data=data)


@mcp.tool()
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
    invoice_settings: Optional[Dict[str, Any]] = None,
    default_source: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a customer (/v1/customers/{id})."""

    data: Dict[str, Any] = {}
    if email is not None:
        data["email"] = email
    if name is not None:
        data["name"] = name
    if phone is not None:
        data["phone"] = phone
    if description is not None:
        data["description"] = description
    if address is not None:
        data["address"] = address
    if shipping is not None:
        data["shipping"] = shipping
    if metadata is not None:
        data["metadata"] = metadata
    if invoice_settings is not None:
        data["invoice_settings"] = invoice_settings
    if default_source is not None:
        data["default_source"] = default_source
    return stripe_request("POST", f"/v1/customers/{customer_id}", data=data)


@mcp.tool()
def customers_retrieve(customer_id: str) -> Dict[str, Any]:
    """Retrieve a customer (/v1/customers/{id})."""

    return stripe_request("GET", f"/v1/customers/{customer_id}")


# Payment Methods
@mcp.tool()
def payment_methods_attach(payment_method_id: str, *, customer: str) -> Dict[str, Any]:
    """Attach a PaymentMethod to a customer (/v1/payment_methods/{id}/attach)."""

    return stripe_request(
        "POST",
        f"/v1/payment_methods/{payment_method_id}/attach",
        data={"customer": customer},
    )


@mcp.tool()
def payment_methods_list(
    *,
    customer: str,
    type: str = "card",
    limit: int = 10,
) -> Dict[str, Any]:
    """List a customer's payment methods (/v1/payment_methods)."""

    return stripe_request(
        "GET",
        "/v1/payment_methods",
        query={"customer": customer, "type": type, "limit": limit},
    )
