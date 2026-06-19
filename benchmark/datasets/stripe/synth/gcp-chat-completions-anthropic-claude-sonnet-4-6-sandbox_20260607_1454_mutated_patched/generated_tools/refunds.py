"""Tools for Stripe Refunds API."""
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


def register_refund_tools(mcp: FastMCP):

    @mcp.tool()
    def create_refund(
        charge: str = None,
        payment_intent: str = None,
        amount: int = None,
        reason: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a Refund for a Charge or PaymentIntent.

        Args:
            charge: ID of the charge to refund.
            payment_intent: ID of the PaymentIntent to refund.
            amount: Amount to refund in smallest currency unit (partial refund).
            reason: Reason: 'duplicate', 'fraudulent', or 'requested_by_customer'.
            metadata: Key-value pairs to attach to the object.
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
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/refunds", data=data)

    @mcp.tool()
    def retrieve_refund(refund_id: str) -> dict:
        """Retrieve a Refund by ID.

        Args:
            refund_id: The ID of the refund (e.g. 're_...').
        """
        return _req("GET", f"/v1/refunds/{refund_id}")

    @mcp.tool()
    def update_refund(refund_id: str, metadata: dict = None) -> dict:
        """Update a Refund's metadata.

        Args:
            refund_id: The ID of the refund to update.
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/refunds/{refund_id}", data=data)

    @mcp.tool()
    def list_refunds(
        charge: str = None,
        payment_intent: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Refunds.

        Args:
            charge: Filter by charge ID.
            payment_intent: Filter by PaymentIntent ID.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
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
        return _req("GET", "/v1/refunds", params=params)
