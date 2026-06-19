"""
Stripe Products tools.
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


def create_product(
    name: str,
    description: str = None,
    active: bool = None,
    images: list = None,
    metadata: dict = None,
    statement_descriptor: str = None,
    unit_label: str = None,
    url: str = None,
) -> dict:
    """Create a Product."""
    data = {"name": name}
    if description:
        data["description"] = description
    if active is not None:
        data["active"] = str(active).lower()
    if images:
        for i, img in enumerate(images):
            data[f"images[{i}]"] = img
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    if unit_label:
        data["unit_label"] = unit_label
    if url:
        data["url"] = url
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/products", data=data, auth=_auth())
    return _handle(resp)


def get_product(product_id: str) -> dict:
    """Retrieve a Product by ID."""
    resp = requests.get(f"{BASE_URL}/products/{product_id}", auth=_auth())
    return _handle(resp)


def update_product(
    product_id: str,
    name: str = None,
    description: str = None,
    active: bool = None,
    metadata: dict = None,
    statement_descriptor: str = None,
    unit_label: str = None,
    url: str = None,
) -> dict:
    """Update a Product."""
    data = {}
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if active is not None:
        data["active"] = str(active).lower()
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    if unit_label:
        data["unit_label"] = unit_label
    if url:
        data["url"] = url
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(
        f"{BASE_URL}/products/{product_id}", data=data, auth=_auth()
    )
    return _handle(resp)


def delete_product(product_id: str) -> dict:
    """Delete a Product."""
    resp = requests.delete(f"{BASE_URL}/products/{product_id}", auth=_auth())
    return _handle(resp)


def list_products(
    active: bool = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
    created_gte: int = None,
    created_lte: int = None,
) -> dict:
    """List Products."""
    params = {}
    if active is not None:
        params["active"] = str(active).lower()
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
    resp = requests.get(f"{BASE_URL}/products", params=params, auth=_auth())
    return _handle(resp)


def search_products(query: str, limit: int = None, page: str = None) -> dict:
    """Search Products using Stripe query syntax."""
    params = {"query": query}
    if limit is not None:
        params["limit"] = limit
    if page:
        params["page"] = page
    resp = requests.get(f"{BASE_URL}/products/search", params=params, auth=_auth())
    return _handle(resp)
