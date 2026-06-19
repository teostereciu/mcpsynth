"""
Stripe Events tools.
Endpoints covered:
  GET    /v1/events/{id}
  GET    /v1/events
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def get_event(event_id: str) -> dict:
        """Retrieve a Stripe Event by ID."""
        return stripe_request("GET", f"/v1/events/{event_id}")

    @mcp.tool()
    def list_events(
        type: str = None,
        types: list = None,
        object_id: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        created_gte: int = None,
        created_lte: int = None,
        delivery_success: bool = None,
    ) -> dict:
        """
        List Events.
        type: filter by a single event type, e.g. 'payment_intent.succeeded'.
        types: filter by multiple event types (list).
        """
        params = {}
        if type:
            params["type"] = type
        if types:
            for i, t in enumerate(types):
                params[f"types[{i}]"] = t
        if object_id:
            params["object_id"] = object_id
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
        if delivery_success is not None:
            params["delivery_success"] = str(delivery_success).lower()
        return stripe_request("GET", "/v1/events", params=params)
