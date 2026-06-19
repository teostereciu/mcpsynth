"""
Stripe Setup Intents tools.
Endpoints covered:
  POST   /v1/setup_intents
  GET    /v1/setup_intents/{id}
  POST   /v1/setup_intents/{id}
  POST   /v1/setup_intents/{id}/confirm
  POST   /v1/setup_intents/{id}/cancel
  GET    /v1/setup_intents
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def create_setup_intent(
        customer: str = None,
        payment_method: str = None,
        payment_method_types: list = None,
        usage: str = None,
        description: str = None,
        metadata: dict = None,
        confirm: bool = None,
        return_url: str = None,
        on_behalf_of: str = None,
    ) -> dict:
        """
        Create a SetupIntent to save a payment method for future use.
        usage: off_session | on_session
        """
        data = {}
        if customer:
            data["customer"] = customer
        if payment_method:
            data["payment_method"] = payment_method
        if payment_method_types:
            for i, pm in enumerate(payment_method_types):
                data[f"payment_method_types[{i}]"] = pm
        if usage:
            data["usage"] = usage
        if description:
            data["description"] = description
        if confirm is not None:
            data["confirm"] = str(confirm).lower()
        if return_url:
            data["return_url"] = return_url
        if on_behalf_of:
            data["on_behalf_of"] = on_behalf_of
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/setup_intents", data=data)

    @mcp.tool()
    def get_setup_intent(setup_intent_id: str) -> dict:
        """Retrieve a SetupIntent by ID."""
        return stripe_request("GET", f"/v1/setup_intents/{setup_intent_id}")

    @mcp.tool()
    def update_setup_intent(
        setup_intent_id: str,
        customer: str = None,
        payment_method: str = None,
        description: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a SetupIntent."""
        data = {}
        if customer:
            data["customer"] = customer
        if payment_method:
            data["payment_method"] = payment_method
        if description:
            data["description"] = description
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}", data=data)

    @mcp.tool()
    def confirm_setup_intent(
        setup_intent_id: str,
        payment_method: str = None,
        return_url: str = None,
    ) -> dict:
        """Confirm a SetupIntent."""
        data = {}
        if payment_method:
            data["payment_method"] = payment_method
        if return_url:
            data["return_url"] = return_url
        return stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/confirm", data=data)

    @mcp.tool()
    def cancel_setup_intent(
        setup_intent_id: str,
        cancellation_reason: str = None,
    ) -> dict:
        """Cancel a SetupIntent. cancellation_reason: abandoned | requested_by_customer | duplicate"""
        data = {}
        if cancellation_reason:
            data["cancellation_reason"] = cancellation_reason
        return stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/cancel", data=data)

    @mcp.tool()
    def list_setup_intents(
        customer: str = None,
        payment_method: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        created_gte: int = None,
        created_lte: int = None,
    ) -> dict:
        """List SetupIntents."""
        params = {}
        if customer:
            params["customer"] = customer
        if payment_method:
            params["payment_method"] = payment_method
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
        return stripe_request("GET", "/v1/setup_intents", params=params)
