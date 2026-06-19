"""Tools for Stripe Subscriptions API."""
import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.stripe.com"

def _get_headers():
    api_key = os.environ.get("STRIPE_API_KEY", "")
    return {"Authorization": f"Bearer {api_key}"}

def _req(method, path, **kwargs):
    try:
        resp = requests.request(method, f"{BASE_URL}{path}", headers=_get_headers(), **kwargs)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def register_subscription_tools(mcp: FastMCP):

    @mcp.tool()
    def create_subscription(
        customer: str,
        items: list,
        currency: str = None,
        default_payment_method: str = None,
        description: str = None,
        trial_period_days: int = None,
        cancel_at_period_end: bool = None,
        collection_method: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a new Subscription for a Customer.

        Args:
            customer: ID of the customer to subscribe.
            items: List of dicts with 'price' key (and optionally 'quantity').
                   e.g. [{"price": "price_xxx", "quantity": 1}]
            currency: Three-letter ISO currency code.
            default_payment_method: ID of the default payment method.
            description: Description of the subscription.
            trial_period_days: Number of trial days before billing starts.
            cancel_at_period_end: If True, cancel at end of current period.
            collection_method: 'charge_automatically' or 'send_invoice'.
            metadata: Key-value pairs to attach to the object.
        """
        data = {"customer": customer}
        for i, item in enumerate(items):
            for k, v in item.items():
                data[f"items[{i}][{k}]"] = v
        if currency:
            data["currency"] = currency
        if default_payment_method:
            data["default_payment_method"] = default_payment_method
        if description:
            data["description"] = description
        if trial_period_days is not None:
            data["trial_period_days"] = trial_period_days
        if cancel_at_period_end is not None:
            data["cancel_at_period_end"] = str(cancel_at_period_end).lower()
        if collection_method:
            data["collection_method"] = collection_method
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/subscriptions", data=data)

    @mcp.tool()
    def retrieve_subscription(subscription_id: str) -> dict:
        """Retrieve a Subscription by ID.

        Args:
            subscription_id: The ID of the subscription (e.g. 'sub_...').
        """
        return _req("GET", f"/v1/subscriptions/{subscription_id}")

    @mcp.tool()
    def update_subscription(
        subscription_id: str,
        default_payment_method: str = None,
        description: str = None,
        cancel_at_period_end: bool = None,
        trial_end: str = None,
        proration_behavior: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update an existing Subscription.

        Args:
            subscription_id: The ID of the subscription to update.
            default_payment_method: ID of the default payment method.
            description: Description of the subscription.
            cancel_at_period_end: If True, cancel at end of current period.
            trial_end: Unix timestamp or 'now' to end trial.
            proration_behavior: 'create_prorations', 'none', or 'always_invoice'.
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if default_payment_method:
            data["default_payment_method"] = default_payment_method
        if description:
            data["description"] = description
        if cancel_at_period_end is not None:
            data["cancel_at_period_end"] = str(cancel_at_period_end).lower()
        if trial_end:
            data["trial_end"] = trial_end
        if proration_behavior:
            data["proration_behavior"] = proration_behavior
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/subscriptions/{subscription_id}", data=data)

    @mcp.tool()
    def cancel_subscription(
        subscription_id: str,
        cancel_at_period_end: bool = None,
    ) -> dict:
        """Cancel a Subscription immediately or at period end.

        Args:
            subscription_id: The ID of the subscription to cancel.
            cancel_at_period_end: If True, cancel at end of current period instead of immediately.
        """
        if cancel_at_period_end:
            data = {"cancel_at_period_end": "true"}
            return _req("POST", f"/v1/subscriptions/{subscription_id}", data=data)
        return _req("DELETE", f"/v1/subscriptions/{subscription_id}")

    @mcp.tool()
    def list_subscriptions(
        customer: str = None,
        status: str = None,
        price: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Subscriptions.

        Args:
            customer: Filter by customer ID.
            status: Filter by status: 'active', 'past_due', 'canceled', etc.
            price: Filter by price ID.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if customer:
            params["customer"] = customer
        if status:
            params["status"] = status
        if price:
            params["price"] = price
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return _req("GET", "/v1/subscriptions", params=params)
