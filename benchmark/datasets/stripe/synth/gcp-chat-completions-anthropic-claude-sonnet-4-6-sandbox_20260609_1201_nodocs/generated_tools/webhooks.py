"""
Stripe Webhook Endpoints tools.
Endpoints covered:
  POST   /v1/webhook_endpoints
  GET    /v1/webhook_endpoints/{id}
  POST   /v1/webhook_endpoints/{id}
  DELETE /v1/webhook_endpoints/{id}
  GET    /v1/webhook_endpoints
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def create_webhook_endpoint(
        url: str,
        enabled_events: list,
        description: str = None,
        api_version: str = None,
        connect: bool = None,
        metadata: dict = None,
    ) -> dict:
        """
        Create a Webhook Endpoint.
        enabled_events: list of event types, e.g. ['payment_intent.succeeded', 'charge.failed'].
        Use ['*'] to receive all events.
        """
        data = {"url": url}
        for i, event in enumerate(enabled_events):
            data[f"enabled_events[{i}]"] = event
        if description:
            data["description"] = description
        if api_version:
            data["api_version"] = api_version
        if connect is not None:
            data["connect"] = str(connect).lower()
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/webhook_endpoints", data=data)

    @mcp.tool()
    def get_webhook_endpoint(webhook_endpoint_id: str) -> dict:
        """Retrieve a Webhook Endpoint by ID."""
        return stripe_request("GET", f"/v1/webhook_endpoints/{webhook_endpoint_id}")

    @mcp.tool()
    def update_webhook_endpoint(
        webhook_endpoint_id: str,
        url: str = None,
        enabled_events: list = None,
        description: str = None,
        disabled: bool = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Webhook Endpoint."""
        data = {}
        if url:
            data["url"] = url
        if enabled_events:
            for i, event in enumerate(enabled_events):
                data[f"enabled_events[{i}]"] = event
        if description:
            data["description"] = description
        if disabled is not None:
            data["disabled"] = str(disabled).lower()
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/webhook_endpoints/{webhook_endpoint_id}", data=data)

    @mcp.tool()
    def delete_webhook_endpoint(webhook_endpoint_id: str) -> dict:
        """Delete a Webhook Endpoint."""
        return stripe_request("DELETE", f"/v1/webhook_endpoints/{webhook_endpoint_id}")

    @mcp.tool()
    def list_webhook_endpoints(
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List Webhook Endpoints."""
        params = {}
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return stripe_request("GET", "/v1/webhook_endpoints", params=params)
