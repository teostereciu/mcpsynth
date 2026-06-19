"""
Stripe Subscription Items & Usage Records tools.
Endpoints covered:
  POST   /v1/subscription_items
  GET    /v1/subscription_items/{id}
  POST   /v1/subscription_items/{id}
  DELETE /v1/subscription_items/{id}
  GET    /v1/subscription_items
  POST   /v1/subscription_items/{id}/usage_records
  GET    /v1/subscription_items/{id}/usage_record_summaries
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def create_subscription_item(
        subscription: str,
        price: str,
        quantity: int = None,
        proration_behavior: str = None,
        proration_date: int = None,
        metadata: dict = None,
    ) -> dict:
        """Add a Subscription Item to an existing Subscription."""
        data = {"subscription": subscription, "price": price}
        if quantity is not None:
            data["quantity"] = quantity
        if proration_behavior:
            data["proration_behavior"] = proration_behavior
        if proration_date is not None:
            data["proration_date"] = proration_date
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/subscription_items", data=data)

    @mcp.tool()
    def get_subscription_item(subscription_item_id: str) -> dict:
        """Retrieve a Subscription Item by ID."""
        return stripe_request("GET", f"/v1/subscription_items/{subscription_item_id}")

    @mcp.tool()
    def update_subscription_item(
        subscription_item_id: str,
        price: str = None,
        quantity: int = None,
        proration_behavior: str = None,
        proration_date: int = None,
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
        if proration_date is not None:
            data["proration_date"] = proration_date
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/subscription_items/{subscription_item_id}", data=data)

    @mcp.tool()
    def delete_subscription_item(
        subscription_item_id: str,
        proration_behavior: str = None,
        proration_date: int = None,
    ) -> dict:
        """Remove a Subscription Item from a Subscription."""
        data = {}
        if proration_behavior:
            data["proration_behavior"] = proration_behavior
        if proration_date is not None:
            data["proration_date"] = proration_date
        return stripe_request("DELETE", f"/v1/subscription_items/{subscription_item_id}", data=data)

    @mcp.tool()
    def list_subscription_items(
        subscription: str,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List Subscription Items for a Subscription."""
        params = {"subscription": subscription}
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return stripe_request("GET", "/v1/subscription_items", params=params)

    @mcp.tool()
    def create_usage_record(
        subscription_item_id: str,
        quantity: int,
        timestamp: int = None,
        action: str = None,
    ) -> dict:
        """
        Report usage for a metered Subscription Item.
        action: increment | set
        """
        data = {"quantity": quantity}
        if timestamp is not None:
            data["timestamp"] = timestamp
        if action:
            data["action"] = action
        return stripe_request(
            "POST",
            f"/v1/subscription_items/{subscription_item_id}/usage_records",
            data=data,
        )

    @mcp.tool()
    def list_usage_record_summaries(
        subscription_item_id: str,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List usage record summaries for a metered Subscription Item."""
        params = {}
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return stripe_request(
            "GET",
            f"/v1/subscription_items/{subscription_item_id}/usage_record_summaries",
            params=params,
        )
