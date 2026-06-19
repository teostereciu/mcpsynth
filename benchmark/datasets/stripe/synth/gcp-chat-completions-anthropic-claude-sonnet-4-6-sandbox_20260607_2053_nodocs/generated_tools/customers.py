"""
Stripe Customers tools.
"""
import os
import requests

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", "")
BASE_URL = "https://api.stripe.com/v1"


def _auth():
    return (STRIPE_API_KEY, "")


def _handle(resp: requests.Response) -> dict:
    try:
        return resp.json()
    except Exception:
        return {"error": resp.text}


def create_customer(
    email: str = None,
    name: str = None,
    phone: str = None,
    description: str = None,
    payment_method: str = None,
    source: str = None,
    metadata: dict = None,
    address_line1: str = None,
    address_city: str = None,
    address_state: str = None,
    address_postal_code: str = None,
    address_country: str = None,
) -> dict:
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
    if source:
        data["source"] = source
    if address_line1:
        data["address[line1]"] = address_line1
    if address_city:
        data["address[city]"] = address_city
    if address_state:
        data["address[state]"] = address_state
    if address_postal_code:
        data["address[postal_code]"] = address_postal_code
    if address_country:
        data["address[country]"] = address_country
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/customers", data=data, auth=_auth())
    return _handle(resp)


def get_customer(customer_id: str) -> dict:
    """Retrieve a Customer by ID."""
    resp = requests.get(f"{BASE_URL}/customers/{customer_id}", auth=_auth())
    return _handle(resp)


def update_customer(
    customer_id: str,
    email: str = None,
    name: str = None,
    phone: str = None,
    description: str = None,
    payment_method: str = None,
    source: str = None,
    metadata: dict = None,
    address_line1: str = None,
    address_city: str = None,
    address_state: str = None,
    address_postal_code: str = None,
    address_country: str = None,
) -> dict:
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
    if payment_method:
        data["payment_method"] = payment_method
    if source:
        data["source"] = source
    if address_line1:
        data["address[line1]"] = address_line1
    if address_city:
        data["address[city]"] = address_city
    if address_state:
        data["address[state]"] = address_state
    if address_postal_code:
        data["address[postal_code]"] = address_postal_code
    if address_country:
        data["address[country]"] = address_country
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(
        f"{BASE_URL}/customers/{customer_id}", data=data, auth=_auth()
    )
    return _handle(resp)


def delete_customer(customer_id: str) -> dict:
    """Delete a Customer."""
    resp = requests.delete(f"{BASE_URL}/customers/{customer_id}", auth=_auth())
    return _handle(resp)


def list_customers(
    email: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
    created_gte: int = None,
    created_lte: int = None,
) -> dict:
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
    if created_gte is not None:
        params["created[gte]"] = created_gte
    if created_lte is not None:
        params["created[lte]"] = created_lte
    resp = requests.get(f"{BASE_URL}/customers", params=params, auth=_auth())
    return _handle(resp)


def search_customers(query: str, limit: int = None, page: str = None) -> dict:
    """Search Customers using Stripe query syntax."""
    params = {"query": query}
    if limit is not None:
        params["limit"] = limit
    if page:
        params["page"] = page
    resp = requests.get(f"{BASE_URL}/customers/search", params=params, auth=_auth())
    return _handle(resp)


def list_customer_payment_methods(
    customer_id: str, type: str = None, limit: int = None
) -> dict:
    """List PaymentMethods attached to a Customer."""
    params = {}
    if type:
        params["type"] = type
    if limit is not None:
        params["limit"] = limit
    resp = requests.get(
        f"{BASE_URL}/customers/{customer_id}/payment_methods",
        params=params,
        auth=_auth(),
    )
    return _handle(resp)
