"""Tools for Stripe Invoices API."""
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


def register_invoice_tools(mcp: FastMCP):

    @mcp.tool()
    def create_invoice(
        customer: str,
        auto_advance: bool = None,
        collection_method: str = None,
        description: str = None,
        days_until_due: int = None,
        metadata: dict = None,
    ) -> dict:
        """Create a draft Invoice for a Customer.

        Args:
            customer: ID of the customer to bill.
            auto_advance: If True, automatically finalize and attempt payment.
            collection_method: 'charge_automatically' or 'send_invoice'.
            description: Arbitrary string attached to the object.
            days_until_due: Days until invoice is due (for send_invoice).
            metadata: Key-value pairs to attach to the object.
        """
        data = {"customer": customer}
        if auto_advance is not None:
            data["auto_advance"] = str(auto_advance).lower()
        if collection_method:
            data["collection_method"] = collection_method
        if description:
            data["description"] = description
        if days_until_due is not None:
            data["days_until_due"] = days_until_due
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/invoices", data=data)

    @mcp.tool()
    def retrieve_invoice(invoice_id: str) -> dict:
        """Retrieve an Invoice by ID.

        Args:
            invoice_id: The ID of the invoice (e.g. 'in_...').
        """
        return _req("GET", f"/v1/invoices/{invoice_id}")

    @mcp.tool()
    def update_invoice(
        invoice_id: str,
        auto_advance: bool = None,
        collection_method: str = None,
        description: str = None,
        days_until_due: int = None,
        metadata: dict = None,
    ) -> dict:
        """Update a draft Invoice.

        Args:
            invoice_id: The ID of the invoice to update.
            auto_advance: If True, automatically finalize and attempt payment.
            collection_method: 'charge_automatically' or 'send_invoice'.
            description: Arbitrary string attached to the object.
            days_until_due: Days until invoice is due.
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if auto_advance is not None:
            data["auto_advance"] = str(auto_advance).lower()
        if collection_method:
            data["collection_method"] = collection_method
        if description:
            data["description"] = description
        if days_until_due is not None:
            data["days_until_due"] = days_until_due
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/invoices/{invoice_id}", data=data)

    @mcp.tool()
    def finalize_invoice(invoice_id: str, auto_advance: bool = None) -> dict:
        """Finalize a draft Invoice, making it open and ready for payment.

        Args:
            invoice_id: The ID of the invoice to finalize.
            auto_advance: Controls automatic collection after finalization.
        """
        data = {}
        if auto_advance is not None:
            data["auto_advance"] = str(auto_advance).lower()
        return _req("POST", f"/v1/invoices/{invoice_id}/finalize", data=data)

    @mcp.tool()
    def pay_invoice(invoice_id: str, payment_method: str = None) -> dict:
        """Attempt to pay an open Invoice.

        Args:
            invoice_id: The ID of the invoice to pay.
            payment_method: ID of the payment method to use.
        """
        data = {}
        if payment_method:
            data["payment_method"] = payment_method
        return _req("POST", f"/v1/invoices/{invoice_id}/pay", data=data)

    @mcp.tool()
    def void_invoice(invoice_id: str) -> dict:
        """Void an open Invoice (marks it as uncollectible).

        Args:
            invoice_id: The ID of the invoice to void.
        """
        return _req("POST", f"/v1/invoices/{invoice_id}/void")

    @mcp.tool()
    def send_invoice(invoice_id: str) -> dict:
        """Send an Invoice to the customer via email.

        Args:
            invoice_id: The ID of the invoice to send.
        """
        return _req("POST", f"/v1/invoices/{invoice_id}/send")

    @mcp.tool()
    def list_invoices(
        customer: str = None,
        subscription: str = None,
        status: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Invoices.

        Args:
            customer: Filter by customer ID.
            subscription: Filter by subscription ID.
            status: Filter by status: 'draft', 'open', 'paid', 'uncollectible', 'void'.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if customer:
            params["customer"] = customer
        if subscription:
            params["subscription"] = subscription
        if status:
            params["status"] = status
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return _req("GET", "/v1/invoices", params=params)

    @mcp.tool()
    def preview_invoice(
        customer: str = None,
        subscription: str = None,
    ) -> dict:
        """Preview an upcoming Invoice for a Customer or Subscription.

        Args:
            customer: ID of the customer to preview invoice for.
            subscription: ID of the subscription to preview invoice for.
        """
        data = {}
        if customer:
            data["customer"] = customer
        if subscription:
            data["subscription"] = subscription
        return _req("POST", "/v1/invoices/create_preview", data=data)
