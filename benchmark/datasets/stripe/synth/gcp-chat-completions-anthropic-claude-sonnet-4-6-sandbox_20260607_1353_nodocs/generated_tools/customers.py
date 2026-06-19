"""Stripe Customers tools."""
import os
import requests

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", "")
BASE_URL = "https://api.stripe.com/v1"


def _headers():
    return {"Authorization": f"Bearer {STRIPE_API_KEY}"}


def _req(method: str, path: str, params: dict = None, data: dict = None):
    url = f"{BASE_URL}{path}"
    try:
        resp = requests.request(
            method,
            url,
            headers=_headers(),
            params=params if method == "GET" else None,
            data=data if method != "GET" else None,
            timeout=30,
        )
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


# ── Customers ─────────────────────────────────────────────────────────────────

def create_customer(
    email: str = None,
    name: str = None,
    phone: str = None,
    description: str = None,
    payment_method: str = None,
    metadata: dict = None,
):
    """Create a Customer."""
    data = {}
    if email:
        data["email"] = email
    if name:
        data["name"] = name
    if phone:
        data["phone"] = phone
    if description:
        data["description"] = description
    if payment_method:
        data["payment_method"] = payment_method
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/customers", data=data)


def get_customer(customer_id: str):
    """Retrieve a Customer by ID."""
    return _req("GET", f"/customers/{customer_id}")


def update_customer(
    customer_id: str,
    email: str = None,
    name: str = None,
    phone: str = None,
    description: str = None,
    default_source: str = None,
    metadata: dict = None,
):
    """Update a Customer."""
    data = {}
    if email:
        data["email"] = email
    if name:
        data["name"] = name
    if phone:
        data["phone"] = phone
    if description:
        data["description"] = description
    if default_source:
        data["default_source"] = default_source
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/customers/{customer_id}", data=data)


def delete_customer(customer_id: str):
    """Delete a Customer."""
    return _req("DELETE", f"/customers/{customer_id}")


def list_customers(
    email: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
):
    """List Customers."""
    params = {}
    if email:
        params["email"] = email
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    return _req("GET", "/customers", params=params)


def search_customers(query: str, limit: int = None):
    """Search Customers using Stripe query syntax."""
    params = {"query": query}
    if limit is not None:
        params["limit"] = limit
    return _req("GET", "/customers/search", params=params)


# ── Payment Methods ───────────────────────────────────────────────────────────

def attach_payment_method(payment_method_id: str, customer: str):
    """Attach a PaymentMethod to a Customer."""
    return _req("POST", f"/payment_methods/{payment_method_id}/attach", data={"customer": customer})


def detach_payment_method(payment_method_id: str):
    """Detach a PaymentMethod from a Customer."""
    return _req("POST", f"/payment_methods/{payment_method_id}/detach")


def list_customer_payment_methods(customer_id: str, type: str = None, limit: int = None):
    """List PaymentMethods for a Customer."""
    params = {"customer": customer_id}
    if type:
        params["type"] = type
    if limit is not None:
        params["limit"] = limit
    return _req("GET", "/payment_methods", params=params)


def get_payment_method(payment_method_id: str):
    """Retrieve a PaymentMethod by ID."""
    return _req("GET", f"/payment_methods/{payment_method_id}")
