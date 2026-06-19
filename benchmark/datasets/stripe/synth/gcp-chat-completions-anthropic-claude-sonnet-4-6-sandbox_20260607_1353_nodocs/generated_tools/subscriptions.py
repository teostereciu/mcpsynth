"""Stripe Subscriptions tools."""
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


# ── Subscriptions ─────────────────────────────────────────────────────────────

def create_subscription(
    customer: str,
    items: list,
    default_payment_method: str = None,
    trial_period_days: int = None,
    cancel_at_period_end: bool = None,
    coupon: str = None,
    promotion_code: str = None,
    metadata: dict = None,
):
    """Create a Subscription. items is a list of dicts with 'price' (and optionally 'quantity')."""
    data = {"customer": customer}
    for i, item in enumerate(items):
        for k, v in item.items():
            data[f"items[{i}][{k}]"] = v
    if default_payment_method:
        data["default_payment_method"] = default_payment_method
    if trial_period_days is not None:
        data["trial_period_days"] = trial_period_days
    if cancel_at_period_end is not None:
        data["cancel_at_period_end"] = str(cancel_at_period_end).lower()
    if coupon:
        data["coupon"] = coupon
    if promotion_code:
        data["promotion_code"] = promotion_code
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/subscriptions", data=data)


def get_subscription(subscription_id: str):
    """Retrieve a Subscription by ID."""
    return _req("GET", f"/subscriptions/{subscription_id}")


def update_subscription(
    subscription_id: str,
    items: list = None,
    default_payment_method: str = None,
    cancel_at_period_end: bool = None,
    coupon: str = None,
    promotion_code: str = None,
    trial_end: str = None,
    metadata: dict = None,
):
    """Update a Subscription."""
    data = {}
    if items:
        for i, item in enumerate(items):
            for k, v in item.items():
                data[f"items[{i}][{k}]"] = v
    if default_payment_method:
        data["default_payment_method"] = default_payment_method
    if cancel_at_period_end is not None:
        data["cancel_at_period_end"] = str(cancel_at_period_end).lower()
    if coupon:
        data["coupon"] = coupon
    if promotion_code:
        data["promotion_code"] = promotion_code
    if trial_end:
        data["trial_end"] = trial_end
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/subscriptions/{subscription_id}", data=data)


def cancel_subscription(subscription_id: str, invoice_now: bool = None, prorate: bool = None):
    """Cancel a Subscription immediately."""
    data = {}
    if invoice_now is not None:
        data["invoice_now"] = str(invoice_now).lower()
    if prorate is not None:
        data["prorate"] = str(prorate).lower()
    return _req("DELETE", f"/subscriptions/{subscription_id}")


def list_subscriptions(
    customer: str = None,
    price: str = None,
    status: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
):
    """List Subscriptions. status can be 'active','past_due','canceled', etc."""
    params = {}
    if customer:
        params["customer"] = customer
    if price:
        params["price"] = price
    if status:
        params["status"] = status
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    return _req("GET", "/subscriptions", params=params)


def search_subscriptions(query: str, limit: int = None):
    """Search Subscriptions using Stripe query syntax."""
    params = {"query": query}
    if limit is not None:
        params["limit"] = limit
    return _req("GET", "/subscriptions/search", params=params)


# ── Subscription Items ────────────────────────────────────────────────────────

def create_subscription_item(
    subscription: str,
    price: str,
    quantity: int = None,
    metadata: dict = None,
):
    """Add an item to an existing Subscription."""
    data = {"subscription": subscription, "price": price}
    if quantity is not None:
        data["quantity"] = quantity
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/subscription_items", data=data)


def update_subscription_item(
    subscription_item_id: str,
    price: str = None,
    quantity: int = None,
    metadata: dict = None,
):
    """Update a Subscription Item."""
    data = {}
    if price:
        data["price"] = price
    if quantity is not None:
        data["quantity"] = quantity
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/subscription_items/{subscription_item_id}", data=data)


def delete_subscription_item(subscription_item_id: str):
    """Remove an item from a Subscription."""
    return _req("DELETE", f"/subscription_items/{subscription_item_id}")


def list_subscription_items(subscription: str, limit: int = None):
    """List items belonging to a Subscription."""
    params = {"subscription": subscription}
    if limit is not None:
        params["limit"] = limit
    return _req("GET", "/subscription_items", params=params)
