"""Tools for Stripe Webhook Endpoints and Credit Notes APIs."""
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


def register_webhook_credit_note_tools(mcp: FastMCP):

    # ---- Webhook Endpoints ----

    @mcp.tool()
    def create_webhook_endpoint(
        url: str,
        enabled_events: list,
        description: str = None,
        api_version: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a Webhook Endpoint to receive Stripe events.

        Args:
            url: The URL of the webhook endpoint.
            enabled_events: List of event types to enable (e.g. ['charge.succeeded']).
                            Use ['*'] to enable all events.
            description: Optional description of the webhook.
            api_version: Stripe API version for events sent to this endpoint.
            metadata: Key-value pairs to attach to the object.
        """
        data = {"url": url}
        for i, event in enumerate(enabled_events):
            data[f"enabled_events[{i}]"] = event
        if description:
            data["description"] = description
        if api_version:
            data["api_version"] = api_version
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/webhook_endpoints", data=data)

    @mcp.tool()
    def retrieve_webhook_endpoint(webhook_endpoint_id: str) -> dict:
        """Retrieve a Webhook Endpoint by ID.

        Args:
            webhook_endpoint_id: The ID of the webhook endpoint (e.g. 'we_...').
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
            url: New URL for the webhook endpoint.
            enabled_events: New list of event types to enable.
            description: Optional description of the webhook.
            disabled: If True, disable the webhook endpoint.
            metadata: Key-value pairs to attach to the object.
        """
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
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return _req("GET", "/v1/webhook_endpoints", params=params)

    # ---- Credit Notes ----

    @mcp.tool()
    def create_credit_note(
        invoice: str,
        amount: int = None,
        memo: str = None,
        reason: str = None,
        refund_amount: int = None,
        metadata: dict = None,
    ) -> dict:
        """Create a Credit Note to adjust a finalized Invoice.

        Args:
            invoice: ID of the invoice to credit.
            amount: Amount to credit in smallest currency unit.
            memo: Customer-facing text on the credit note PDF.
            reason: 'duplicate', 'fraudulent', 'order_change', or 'product_unsatisfactory'.
            refund_amount: Amount to refund to the customer.
            metadata: Key-value pairs to attach to the object.
        """
        data = {"invoice": invoice}
        if amount is not None:
            data["amount"] = amount
        if memo:
            data["memo"] = memo
        if reason:
            data["reason"] = reason
        if refund_amount is not None:
            data["refund_amount"] = refund_amount
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/credit_notes", data=data)

    @mcp.tool()
    def retrieve_credit_note(credit_note_id: str) -> dict:
        """Retrieve a Credit Note by ID.

        Args:
            credit_note_id: The ID of the credit note (e.g. 'cn_...').
        """
        return _req("GET", f"/v1/credit_notes/{credit_note_id}")

    @mcp.tool()
    def update_credit_note(
        credit_note_id: str,
        memo: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Credit Note.

        Args:
            credit_note_id: The ID of the credit note to update.
            memo: Customer-facing text on the credit note PDF.
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if memo:
            data["memo"] = memo
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/credit_notes/{credit_note_id}", data=data)

    @mcp.tool()
    def void_credit_note(credit_note_id: str) -> dict:
        """Void a Credit Note.

        Args:
            credit_note_id: The ID of the credit note to void.
        """
        return _req("POST", f"/v1/credit_notes/{credit_note_id}/void")

    @mcp.tool()
    def list_credit_notes(
        invoice: str = None,
        limit: int = None,
        starting_after: str = None,
    ) -> dict:
        """List all Credit Notes.

        Args:
            invoice: Filter by invoice ID.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
        """
        params = {}
        if invoice:
            params["invoice"] = invoice
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        return _req("GET", "/v1/credit_notes", params=params)
