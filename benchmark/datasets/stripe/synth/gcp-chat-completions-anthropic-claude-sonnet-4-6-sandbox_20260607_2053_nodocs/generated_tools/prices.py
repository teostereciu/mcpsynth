"""
Stripe Prices tools.
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


def create_price(
    currency: str,
    product: str = None,
    product_data_name: str = None,
    unit_amount: int = None,
    unit_amount_decimal: str = None,
    recurring_interval: str = None,
    recurring_interval_count: int = None,
    recurring_usage_type: str = None,
    billing_scheme: str = None,
    nickname: str = None,
    active: bool = None,
    metadata: dict = None,
    lookup_key: str = None,
    tax_behavior: str = None,
) -> dict:
    """Create a Price. Provide either product or product_data_name."""
    data = {"currency": currency}
    if product:
        data["product"] = product
    if product_data_name:
        data["product_data[name]"] = product_data_name
    if unit_amount is not None:
        data["unit_amount"] = unit_amount
    if unit_amount_decimal:
        data["unit_amount_decimal"] = unit_amount_decimal
    if recurring_interval:
        data["recurring[interval]"] = recurring_interval
    if recurring_interval_count is not None:
        data["recurring[interval_count]"] = recurring_interval_count
    if recurring_usage_type:
        data["recurring[usage_type]"] = recurring_usage_type
    if billing_scheme:
        data["billing_scheme"] = billing_scheme
    if nickname:
        data["nickname"] = nickname
    if active is not None:
        data["active"] = str(active).lower()
    if lookup_key:
        data["lookup_key"] = lookup_key
    if tax_behavior:
        data["tax_behavior"] = tax_behavior
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/prices", data=data, auth=_auth())
    return _handle(resp)


def get_price(price_id: str) -> dict:
    """Retrieve a Price by ID."""
    resp = requests.get(f"{BASE_URL}/prices/{price_id}", auth=_auth())
    return _handle(resp)


def update_price(
    price_id: str,
    active: bool = None,
    nickname: str = None,
    metadata: dict = None,
    lookup_key: str = None,
    tax_behavior: str = None,
) -> dict:
    """Update a Price."""
    data = {}
    if active is not None:
        data["active"] = str(active).lower()
    if nickname:
        data["nickname"] = nickname
    if lookup_key:
        data["lookup_key"] = lookup_key
    if tax_behavior:
        data["tax_behavior"] = tax_behavior
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/prices/{price_id}", data=data, auth=_auth())
    return _handle(resp)


def list_prices(
    product: str = None,
    active: bool = None,
    currency: str = None,
    type: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
    lookup_keys: list = None,
) -> dict:
    """List Prices."""
    params = {}
    if product:
        params["product"] = product
    if active is not None:
        params["active"] = str(active).lower()
    if currency:
        params["currency"] = currency
    if type:
        params["type"] = type
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if lookup_keys:
        for i, lk in enumerate(lookup_keys):
            params[f"lookup_keys[{i}]"] = lk
    resp = requests.get(f"{BASE_URL}/prices", params=params, auth=_auth())
    return _handle(resp)


def search_prices(query: str, limit: int = None, page: str = None) -> dict:
    """Search Prices using Stripe query syntax."""
    params = {"query": query}
    if limit is not None:
        params["limit"] = limit
    if page:
        params["page"] = page
    resp = requests.get(f"{BASE_URL}/prices/search", params=params, auth=_auth())
    return _handle(resp)
