"""
Stripe Payment Links tools.
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


def create_payment_link(
    line_items: list,
    allow_promotion_codes: bool = None,
    billing_address_collection: str = None,
    after_completion_type: str = None,
    after_completion_redirect_url: str = None,
    metadata: dict = None,
    payment_method_types: list = None,
    currency: str = None,
    customer_creation: str = None,
    shipping_address_collection_allowed_countries: list = None,
    subscription_data_trial_period_days: int = None,
) -> dict:
    """
    Create a Payment Link.
    line_items: list of dicts with 'price' and 'quantity'.
    """
    data = {}
    for i, item in enumerate(line_items):
        if "price" in item:
            data[f"line_items[{i}][price]"] = item["price"]
        if "quantity" in item:
            data[f"line_items[{i}][quantity]"] = item["quantity"]
    if allow_promotion_codes is not None:
        data["allow_promotion_codes"] = str(allow_promotion_codes).lower()
    if billing_address_collection:
        data["billing_address_collection"] = billing_address_collection
    if after_completion_type:
        data["after_completion[type]"] = after_completion_type
    if after_completion_redirect_url:
        data["after_completion[redirect][url]"] = after_completion_redirect_url
    if payment_method_types:
        for i, pm in enumerate(payment_method_types):
            data[f"payment_method_types[{i}]"] = pm
    if currency:
        data["currency"] = currency
    if customer_creation:
        data["customer_creation"] = customer_creation
    if shipping_address_collection_allowed_countries:
        for i, c in enumerate(shipping_address_collection_allowed_countries):
            data[f"shipping_address_collection[allowed_countries][{i}]"] = c
    if subscription_data_trial_period_days is not None:
        data["subscription_data[trial_period_days]"] = subscription_data_trial_period_days
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/payment_links", data=data, auth=_auth())
    return _handle(resp)


def get_payment_link(payment_link_id: str) -> dict:
    """Retrieve a Payment Link by ID."""
    resp = requests.get(f"{BASE_URL}/payment_links/{payment_link_id}", auth=_auth())
    return _handle(resp)


def update_payment_link(
    payment_link_id: str,
    active: bool = None,
    allow_promotion_codes: bool = None,
    metadata: dict = None,
    payment_method_types: list = None,
    after_completion_type: str = None,
    after_completion_redirect_url: str = None,
) -> dict:
    """Update a Payment Link."""
    data = {}
    if active is not None:
        data["active"] = str(active).lower()
    if allow_promotion_codes is not None:
        data["allow_promotion_codes"] = str(allow_promotion_codes).lower()
    if after_completion_type:
        data["after_completion[type]"] = after_completion_type
    if after_completion_redirect_url:
        data["after_completion[redirect][url]"] = after_completion_redirect_url
    if payment_method_types:
        for i, pm in enumerate(payment_method_types):
            data[f"payment_method_types[{i}]"] = pm
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(
        f"{BASE_URL}/payment_links/{payment_link_id}", data=data, auth=_auth()
    )
    return _handle(resp)


def list_payment_links(
    active: bool = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
) -> dict:
    """List Payment Links."""
    params = {}
    if active is not None:
        params["active"] = str(active).lower()
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    resp = requests.get(f"{BASE_URL}/payment_links", params=params, auth=_auth())
    return _handle(resp)


def list_payment_link_line_items(
    payment_link_id: str, limit: int = None, starting_after: str = None
) -> dict:
    """List line items for a Payment Link."""
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    resp = requests.get(
        f"{BASE_URL}/payment_links/{payment_link_id}/line_items",
        params=params,
        auth=_auth(),
    )
    return _handle(resp)
