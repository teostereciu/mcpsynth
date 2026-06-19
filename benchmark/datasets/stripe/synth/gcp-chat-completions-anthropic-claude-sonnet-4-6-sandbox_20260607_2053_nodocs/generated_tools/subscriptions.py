"""
Stripe Subscriptions tools.
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


def create_subscription(
    customer: str,
    items: list,
    default_payment_method: str = None,
    trial_period_days: int = None,
    trial_end: int = None,
    cancel_at_period_end: bool = None,
    cancel_at: int = None,
    coupon: str = None,
    promotion_code: str = None,
    proration_behavior: str = None,
    billing_cycle_anchor: int = None,
    collection_method: str = None,
    days_until_due: int = None,
    metadata: dict = None,
    payment_behavior: str = None,
) -> dict:
    """
    Create a Subscription.
    items: list of dicts with keys 'price' and optionally 'quantity'.
    """
    data = {"customer": customer}
    for i, item in enumerate(items):
        if "price" in item:
            data[f"items[{i}][price]"] = item["price"]
        if "quantity" in item:
            data[f"items[{i}][quantity]"] = item["quantity"]
    if default_payment_method:
        data["default_payment_method"] = default_payment_method
    if trial_period_days is not None:
        data["trial_period_days"] = trial_period_days
    if trial_end is not None:
        data["trial_end"] = trial_end
    if cancel_at_period_end is not None:
        data["cancel_at_period_end"] = str(cancel_at_period_end).lower()
    if cancel_at is not None:
        data["cancel_at"] = cancel_at
    if coupon:
        data["coupon"] = coupon
    if promotion_code:
        data["promotion_code"] = promotion_code
    if proration_behavior:
        data["proration_behavior"] = proration_behavior
    if billing_cycle_anchor is not None:
        data["billing_cycle_anchor"] = billing_cycle_anchor
    if collection_method:
        data["collection_method"] = collection_method
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    if payment_behavior:
        data["payment_behavior"] = payment_behavior
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/subscriptions", data=data, auth=_auth())
    return _handle(resp)


def get_subscription(subscription_id: str) -> dict:
    """Retrieve a Subscription by ID."""
    resp = requests.get(f"{BASE_URL}/subscriptions/{subscription_id}", auth=_auth())
    return _handle(resp)


def update_subscription(
    subscription_id: str,
    items: list = None,
    default_payment_method: str = None,
    cancel_at_period_end: bool = None,
    cancel_at: int = None,
    coupon: str = None,
    promotion_code: str = None,
    proration_behavior: str = None,
    trial_end: int = None,
    collection_method: str = None,
    days_until_due: int = None,
    metadata: dict = None,
    payment_behavior: str = None,
) -> dict:
    """Update a Subscription."""
    data = {}
    if items:
        for i, item in enumerate(items):
            if "id" in item:
                data[f"items[{i}][id]"] = item["id"]
            if "price" in item:
                data[f"items[{i}][price]"] = item["price"]
            if "quantity" in item:
                data[f"items[{i}][quantity]"] = item["quantity"]
            if item.get("deleted"):
                data[f"items[{i}][deleted]"] = "true"
    if default_payment_method:
        data["default_payment_method"] = default_payment_method
    if cancel_at_period_end is not None:
        data["cancel_at_period_end"] = str(cancel_at_period_end).lower()
    if cancel_at is not None:
        data["cancel_at"] = cancel_at
    if coupon:
        data["coupon"] = coupon
    if promotion_code:
        data["promotion_code"] = promotion_code
    if proration_behavior:
        data["proration_behavior"] = proration_behavior
    if trial_end is not None:
        data["trial_end"] = trial_end
    if collection_method:
        data["collection_method"] = collection_method
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    if payment_behavior:
        data["payment_behavior"] = payment_behavior
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(
        f"{BASE_URL}/subscriptions/{subscription_id}", data=data, auth=_auth()
    )
    return _handle(resp)


def cancel_subscription(
    subscription_id: str,
    invoice_now: bool = None,
    prorate: bool = None,
) -> dict:
    """Cancel a Subscription immediately."""
    data = {}
    if invoice_now is not None:
        data["invoice_now"] = str(invoice_now).lower()
    if prorate is not None:
        data["prorate"] = str(prorate).lower()
    resp = requests.delete(
        f"{BASE_URL}/subscriptions/{subscription_id}", data=data, auth=_auth()
    )
    return _handle(resp)


def list_subscriptions(
    customer: str = None,
    price: str = None,
    status: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
    created_gte: int = None,
    created_lte: int = None,
) -> dict:
    """List Subscriptions."""
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
    if created_gte is not None:
        params["created[gte]"] = created_gte
    if created_lte is not None:
        params["created[lte]"] = created_lte
    resp = requests.get(f"{BASE_URL}/subscriptions", params=params, auth=_auth())
    return _handle(resp)


def search_subscriptions(query: str, limit: int = None, page: str = None) -> dict:
    """Search Subscriptions using Stripe query syntax."""
    params = {"query": query}
    if limit is not None:
        params["limit"] = limit
    if page:
        params["page"] = page
    resp = requests.get(
        f"{BASE_URL}/subscriptions/search", params=params, auth=_auth()
    )
    return _handle(resp)


# ── Subscription Items ──────────────────────────────────────────────────────

def create_subscription_item(
    subscription: str,
    price: str,
    quantity: int = None,
    proration_behavior: str = None,
    metadata: dict = None,
) -> dict:
    """Add an item to an existing Subscription."""
    data = {"subscription": subscription, "price": price}
    if quantity is not None:
        data["quantity"] = quantity
    if proration_behavior:
        data["proration_behavior"] = proration_behavior
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/subscription_items", data=data, auth=_auth())
    return _handle(resp)


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
    resp = requests.post(
        f"{BASE_URL}/subscription_items/{item_id}", data=data, auth=_auth()
    )
    return _handle(resp)


def delete_subscription_item(
    item_id: str, proration_behavior: str = None
) -> dict:
    """Delete a Subscription Item."""
    data = {}
    if proration_behavior:
        data["proration_behavior"] = proration_behavior
    resp = requests.delete(
        f"{BASE_URL}/subscription_items/{item_id}", data=data, auth=_auth()
    )
    return _handle(resp)


def list_subscription_items(
    subscription: str, limit: int = None, starting_after: str = None
) -> dict:
    """List items of a Subscription."""
    params = {"subscription": subscription}
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    resp = requests.get(
        f"{BASE_URL}/subscription_items", params=params, auth=_auth()
    )
    return _handle(resp)
