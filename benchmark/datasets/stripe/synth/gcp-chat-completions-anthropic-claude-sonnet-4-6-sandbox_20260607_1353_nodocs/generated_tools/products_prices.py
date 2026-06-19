"""Stripe Products and Prices tools."""
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


# ── Products ──────────────────────────────────────────────────────────────────

def create_product(
    name: str,
    description: str = None,
    active: bool = None,
    images: list = None,
    metadata: dict = None,
    unit_label: str = None,
    url: str = None,
):
    """Create a Product."""
    data = {"name": name}
    if description:
        data["description"] = description
    if active is not None:
        data["active"] = str(active).lower()
    if images:
        for i, img in enumerate(images):
            data[f"images[{i}]"] = img
    if unit_label:
        data["unit_label"] = unit_label
    if url:
        data["url"] = url
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/products", data=data)


def get_product(product_id: str):
    """Retrieve a Product by ID."""
    return _req("GET", f"/products/{product_id}")


def update_product(
    product_id: str,
    name: str = None,
    description: str = None,
    active: bool = None,
    metadata: dict = None,
):
    """Update a Product."""
    data = {}
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if active is not None:
        data["active"] = str(active).lower()
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/products/{product_id}", data=data)


def delete_product(product_id: str):
    """Delete a Product."""
    return _req("DELETE", f"/products/{product_id}")


def list_products(
    active: bool = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
):
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
    return _req("GET", "/products", params=params)


def search_products(query: str, limit: int = None):
    """Search Products using Stripe query syntax."""
    params = {"query": query}
    if limit is not None:
        params["limit"] = limit
    return _req("GET", "/products/search", params=params)


# ── Prices ────────────────────────────────────────────────────────────────────

def create_price(
    currency: str,
    product: str = None,
    unit_amount: int = None,
    recurring_interval: str = None,
    recurring_interval_count: int = None,
    billing_scheme: str = None,
    nickname: str = None,
    active: bool = None,
    metadata: dict = None,
):
    """Create a Price. Use recurring_interval ('day','week','month','year') for subscription prices."""
    data = {"currency": currency}
    if product:
        data["product"] = product
    if unit_amount is not None:
        data["unit_amount"] = unit_amount
    if recurring_interval:
        data["recurring[interval]"] = recurring_interval
    if recurring_interval_count is not None:
        data["recurring[interval_count]"] = recurring_interval_count
    if billing_scheme:
        data["billing_scheme"] = billing_scheme
    if nickname:
        data["nickname"] = nickname
    if active is not None:
        data["active"] = str(active).lower()
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/prices", data=data)


def get_price(price_id: str):
    """Retrieve a Price by ID."""
    return _req("GET", f"/prices/{price_id}")


def update_price(
    price_id: str,
    active: bool = None,
    nickname: str = None,
    metadata: dict = None,
):
    """Update a Price."""
    data = {}
    if active is not None:
        data["active"] = str(active).lower()
    if nickname:
        data["nickname"] = nickname
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/prices/{price_id}", data=data)


def list_prices(
    product: str = None,
    active: bool = None,
    currency: str = None,
    limit: int = None,
    starting_after: str = None,
):
    """List Prices."""
    params = {}
    if product:
        params["product"] = product
    if active is not None:
        params["active"] = str(active).lower()
    if currency:
        params["currency"] = currency
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    return _req("GET", "/prices", params=params)


def search_prices(query: str, limit: int = None):
    """Search Prices using Stripe query syntax."""
    params = {"query": query}
    if limit is not None:
        params["limit"] = limit
    return _req("GET", "/prices/search", params=params)
