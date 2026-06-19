"""Stripe Subscription Items and Usage Records tools."""
import os
import requests

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", "")
BASE_URL = "https://api.stripe.com/v1"


def _headers():
    return {"Authorization": f"Bearer {STRIPE_API_KEY}"}


def _req(method, path, params=None, data=None):
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


def create_subscription_item(
    subscription: str,
    price: str,
    quantity: int = None,
    proration_behavior: str = None,
    tax_rates: list = None,
    metadata: dict = None,
) -> dict:
    """Add an item to an existing Subscription."""
    data = {"subscription": subscription, "price": price}
    if quantity is not None:
        data["quantity"] = quantity
    if proration_behavior:
        data["proration_behavior"] = proration_behavior
    if tax_rates:
        for i, tr in enumerate(tax_rates):
            data[f"tax_rates[{i}]"] = tr
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/subscription_items", data=data)


def get_subscription_item(item_id: str) -> dict:
    """Retrieve a Subscription Item by ID."""
    return _req("GET", f"/subscription_items/{item_id}")


def update_subscription_item(
    item_id: str,
    price: str = None,
    quantity: int = None,
    proration_behavior: str = None,
    metadata: dict = None,
) -> dict:
    """Update a Subscription Item."""
    data = {}
    if price:
        data["price"] = price
    if quantity is not None:
        data["quantity"] = quantity
    if proration_behavior:
        data["proration_behavior"] = proration_behavior
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/subscription_items/{item_id}", data=data)


def delete_subscription_item(
    item_id: str,
    proration_behavior: str = None,
    clear_usage: bool = None,
) -> dict:
    """Remove a Subscription Item."""
    data = {}
    if proration_behavior:
        data["proration_behavior"] = proration_behavior
    if clear_usage is not None:
        data["clear_usage"] = str(clear_usage).lower()
    return _req("DELETE", f"/subscription_items/{item_id}", data=data)


def list_subscription_items(
    subscription: str,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
) -> dict:
    """List items for a Subscription."""
    params = {"subscription": subscription}
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    return _req("GET", "/subscription_items", params=params)


def create_usage_record(
    subscription_item_id: str,
    quantity: int,
    timestamp: int = None,
    action: str = "increment",
) -> dict:
    """Create a Usage Record for a metered Subscription Item."""
    data = {"quantity": quantity, "action": action}
    if timestamp is not None:
        data["timestamp"] = timestamp
    return _req("POST", f"/subscription_items/{subscription_item_id}/usage_records", data=data)


def list_usage_record_summaries(
    subscription_item_id: str,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
) -> dict:
    """List usage record summaries for a Subscription Item."""
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    return _req("GET", f"/subscription_items/{subscription_item_id}/usage_record_summaries", params=params)
