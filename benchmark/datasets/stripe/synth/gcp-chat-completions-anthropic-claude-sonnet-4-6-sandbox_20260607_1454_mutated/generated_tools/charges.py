"""Tools for Stripe Charges API."""
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


def register_charge_tools(mcp: FastMCP):

    @mcp.tool()
    def create_charge(
        amount: int,
        currency: str,
        source: str = None,
        customer: str = None,
        description: str = None,
        receipt_email: str = None,
        statement_descriptor: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a Charge (legacy). Prefer PaymentIntents for new integrations.

        Args:
            amount: Amount in smallest currency unit (e.g. cents for USD).
            currency: Three-letter ISO currency code (e.g. 'usd').
            source: Payment source ID (card token, bank account, etc.).
            customer: ID of an existing customer to charge.
            description: Arbitrary string attached to the object.
            receipt_email: Email to send receipt to.
            statement_descriptor: Statement descriptor (max 22 chars).
            metadata: Key-value pairs to attach to the object.
        """
        data = {"amount": amount, "currency": currency}
        if source:
            data["source"] = source
        if customer:
            data["customer"] = customer
        if description:
            data["description"] = description
        if receipt_email:
            data["receipt_email"] = receipt_email
        if statement_descriptor:
            data["statement_descriptor"] = statement_descriptor
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/charges", data=data)

    @mcp.tool()
    def retrieve_charge(charge_id: str) -> dict:
        """Retrieve a Charge by ID.

        Args:
            charge_id: The ID of the charge (e.g. 'ch_...').
        """
        return _req("GET", f"/v1/charges/{charge_id}")

    @mcp.tool()
    def update_charge(
        charge_id: str,
        customer: str = None,
        description: str = None,
        receipt_email: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Charge.

        Args:
            charge_id: The ID of the charge to update.
            customer: ID of an existing customer to associate.
            description: Arbitrary string attached to the object.
            receipt_email: Email to send receipt to.
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if customer:
            data["customer"] = customer
        if description:
            data["description"] = description
        if receipt_email:
            data["receipt_email"] = receipt_email
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/charges/{charge_id}", data=data)

    @mcp.tool()
    def list_charges(
        customer: str = None,
        payment_intent: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Charges.

        Args:
            customer: Filter by customer ID.
            payment_intent: Filter by PaymentIntent ID.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if customer:
            params["customer"] = customer
        if payment_intent:
            params["payment_intent"] = payment_intent
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return _req("GET", "/v1/charges", params=params)

    @mcp.tool()
    def capture_charge(charge_id: str, amount: int = None) -> dict:
        """Capture an uncaptured Charge.

        Args:
            charge_id: The ID of the charge to capture.
            amount: Amount to capture (defaults to full amount).
        """
        data = {}
        if amount is not None:
            data["amount"] = amount
        return _req("POST", f"/v1/charges/{charge_id}/capture", data=data)
