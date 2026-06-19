"""Tools for Stripe Subscription Items and Webhook Endpoints APIs."""
import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.stripe.com"

def _get_headers():
    api_key = os.environ.get("STRIPE_API_KEY", "")
    return {"Authorization": f"Bearer {api_key}"}

def _req(method, path, params=None, data=None):
    url = f"{BASE_URL}{path}"
    try:
        resp = requests.request(
            method, url,
            headers=_get_headers(),
            params=params,
            data=data,
            timeout=30,
        )
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def register_subscription_item_webhook_tools(mcp: FastMCP):

    # ── Subscription Items ─────────────────────────────────────────────────

    @mcp.tool()
    def create_subscription_item(
        subscription: str,
        price: str = None,
        quantity: int = None,
        proration_behavior: str = None,
        metadata: dict = None,
    ) -> dict:
        """Add a new item to an existing Subscription.

        Args:
            subscription: ID of the subscription to modify.
            price: ID of the price object to add.
            quantity: Quantity for the subscription item.
            proration_behavior: 'create_prorations', 'none', or 'always_invoice'.
            metadata: Key-value pairs to attach.
        """
        data = {"subscription": subscription}
        if price: data["price"] = price
        if quantity is not None: data["quantity"] = quantity
        if proration_behavior: data["proration_behavior"] = proration_behavior
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/subscription_items", data=data)

    @mcp.tool()
    def retrieve_subscription_item(item_id: str) -> dict:
        """Retrieve a Subscription Item by ID.

        Args:
            item_id: The ID of the subscription item to retrieve.
        """
        return _req("GET", f"/v1/subscription_items/{item_id}")

    @mcp.tool()
    def update_subscription_item(
        item_id: str,
        price: str = None,
        quantity: int = None,
        proration_behavior: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Subscription Item (e.g. change price or quantity).

        Args:
            item_id: The ID of the subscription item to update.
            price: New price ID.
            quantity: New quantity.
            proration_behavior: 'create_prorations', 'none', or 'always_invoice'.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if price: data["price"] = price
        if quantity is not None: data["quantity"] = quantity
        if proration_behavior: data["proration_behavior"] = proration_behavior
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/subscription_items/{item_id}", data=data)

    @mcp.tool()
    def delete_subscription_item(
        item_id: str,
        proration_behavior: str = None,
    ) -> dict:
        """Remove a Subscription Item from a subscription.

        Args:
            item_id: The ID of the subscription item to delete.
            proration_behavior: 'create_prorations', 'none', or 'always_invoice'.
        """
        data = {}
        if proration_behavior: data["proration_behavior"] = proration_behavior
        return _req("DELETE", f"/v1/subscription_items/{item_id}", data=data)

    @mcp.tool()
    def list_subscription_items(
        subscription: str,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all items for a Subscription.

        Args:
            subscription: ID of the subscription to list items for.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {"subscription": subscription}
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/subscription_items", params=params)

    # ── Webhook Endpoints ──────────────────────────────────────────────────

    @mcp.tool()
    def create_webhook_endpoint(
        url: str,
        enabled_events: list,
        description: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a Webhook Endpoint to receive event notifications.

        Args:
            url: The URL of the webhook endpoint.
            enabled_events: List of event types to enable (e.g. ['charge.succeeded']).
                            Use ['*'] to enable all events.
            description: Optional description of the webhook.
            metadata: Key-value pairs to attach.
        """
        data = {"url": url}
        for i, event in enumerate(enabled_events):
            data[f"enabled_events[{i}]"] = event
        if description: data["description"] = description
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/webhook_endpoints", data=data)

    @mcp.tool()
    def retrieve_webhook_endpoint(webhook_endpoint_id: str) -> dict:
        """Retrieve a Webhook Endpoint by ID.

        Args:
            webhook_endpoint_id: The ID of the webhook endpoint to retrieve.
        """
        return _req("GET", f"/v1/webhook_endpoints/{webhook_endpoint_id}")

    @mcp.tool()
    def update_webhook_endpoint(
        webhook_endpoint_id: str,
        url: str = None,
        enabled_events: list = None,
        description: str = None,
        disabled: bool = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Webhook Endpoint.

        Args:
            webhook_endpoint_id: The ID of the webhook endpoint to update.
            url: New URL for the webhook.
            enabled_events: New list of event types to enable.
            description: New description.
            disabled: Set True to disable the webhook.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if url: data["url"] = url
        if enabled_events:
            for i, event in enumerate(enabled_events):
                data[f"enabled_events[{i}]"] = event
        if description: data["description"] = description
        if disabled is not None: data["disabled"] = str(disabled).lower()
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/webhook_endpoints/{webhook_endpoint_id}", data=data)

    @mcp.tool()
    def delete_webhook_endpoint(webhook_endpoint_id: str) -> dict:
        """Delete a Webhook Endpoint.

        Args:
            webhook_endpoint_id: The ID of the webhook endpoint to delete.
        """
        return _req("DELETE", f"/v1/webhook_endpoints/{webhook_endpoint_id}")

    @mcp.tool()
    def list_webhook_endpoints(
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Webhook Endpoints.

        Args:
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/webhook_endpoints", params=params)
