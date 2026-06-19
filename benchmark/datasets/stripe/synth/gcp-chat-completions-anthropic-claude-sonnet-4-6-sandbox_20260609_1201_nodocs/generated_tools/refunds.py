"""
Stripe Refunds tools.
Endpoints covered:
  POST   /v1/refunds
  GET    /v1/refunds/{id}
  POST   /v1/refunds/{id}
  POST   /v1/refunds/{id}/cancel
  GET    /v1/refunds
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def create_refund(
        charge: str = None,
        payment_intent: str = None,
        amount: int = None,
        reason: str = None,
        refund_application_fee: bool = None,
        reverse_transfer: bool = None,
        metadata: dict = None,
    ) -> dict:
        """
        Create a Refund for a Charge or PaymentIntent.
        reason: duplicate | fraudulent | requested_by_customer
        """
        data = {}
        if charge:
            data["charge"] = charge
        if payment_intent:
            data["payment_intent"] = payment_intent
        if amount is not None:
            data["amount"] = amount
        if reason:
            data["reason"] = reason
        if refund_application_fee is not None:
            data["refund_application_fee"] = str(refund_application_fee).lower()
        if reverse_transfer is not None:
            data["reverse_transfer"] = str(reverse_transfer).lower()
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/refunds", data=data)

    @mcp.tool()
    def get_refund(refund_id: str) -> dict:
        """Retrieve a Refund by ID."""
        return stripe_request("GET", f"/v1/refunds/{refund_id}")

    @mcp.tool()
    def update_refund(refund_id: str, metadata: dict = None) -> dict:
        """Update a Refund's metadata."""
        data = {}
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/refunds/{refund_id}", data=data)

    @mcp.tool()
    def cancel_refund(refund_id: str) -> dict:
        """Cancel a Refund (only possible while status=requires_action)."""
        return stripe_request("POST", f"/v1/refunds/{refund_id}/cancel")

    @mcp.tool()
    def list_refunds(
        charge: str = None,
        payment_intent: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List Refunds with optional filters."""
        params = {}
        if charge:
            params["charge"] = charge
        if payment_intent:
            params["payment_intent"] = payment_intent
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return stripe_request("GET", "/v1/refunds", params=params)
