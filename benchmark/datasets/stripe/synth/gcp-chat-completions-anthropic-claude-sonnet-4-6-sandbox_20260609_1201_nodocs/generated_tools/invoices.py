"""
Stripe Invoices tools.
Endpoints covered:
  POST   /v1/invoices
  GET    /v1/invoices/{id}
  POST   /v1/invoices/{id}
  DELETE /v1/invoices/{id}
  POST   /v1/invoices/{id}/finalize
  POST   /v1/invoices/{id}/pay
  POST   /v1/invoices/{id}/send
  POST   /v1/invoices/{id}/void
  POST   /v1/invoices/{id}/mark_uncollectible
  GET    /v1/invoices
  GET    /v1/invoices/upcoming
  POST   /v1/invoiceitems
  GET    /v1/invoiceitems/{id}
  POST   /v1/invoiceitems/{id}
  DELETE /v1/invoiceitems/{id}
  GET    /v1/invoiceitems
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def create_invoice(
        customer: str,
        auto_advance: bool = None,
        collection_method: str = None,
        days_until_due: int = None,
        description: str = None,
        footer: str = None,
        subscription: str = None,
        default_payment_method: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a draft Invoice for a Customer."""
        data = {"customer": customer}
        if auto_advance is not None:
            data["auto_advance"] = str(auto_advance).lower()
        if collection_method:
            data["collection_method"] = collection_method
        if days_until_due is not None:
            data["days_until_due"] = days_until_due
        if description:
            data["description"] = description
        if footer:
            data["footer"] = footer
        if subscription:
            data["subscription"] = subscription
        if default_payment_method:
            data["default_payment_method"] = default_payment_method
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/invoices", data=data)

    @mcp.tool()
    def get_invoice(invoice_id: str) -> dict:
        """Retrieve an Invoice by ID."""
        return stripe_request("GET", f"/v1/invoices/{invoice_id}")

    @mcp.tool()
    def update_invoice(
        invoice_id: str,
        auto_advance: bool = None,
        collection_method: str = None,
        days_until_due: int = None,
        description: str = None,
        footer: str = None,
        default_payment_method: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a draft Invoice."""
        data = {}
        if auto_advance is not None:
            data["auto_advance"] = str(auto_advance).lower()
        if collection_method:
            data["collection_method"] = collection_method
        if days_until_due is not None:
            data["days_until_due"] = days_until_due
        if description:
            data["description"] = description
        if footer:
            data["footer"] = footer
        if default_payment_method:
            data["default_payment_method"] = default_payment_method
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/invoices/{invoice_id}", data=data)

    @mcp.tool()
    def delete_invoice(invoice_id: str) -> dict:
        """Delete a draft Invoice."""
        return stripe_request("DELETE", f"/v1/invoices/{invoice_id}")

    @mcp.tool()
    def finalize_invoice(invoice_id: str, auto_advance: bool = None) -> dict:
        """Finalize a draft Invoice, making it ready to pay."""
        data = {}
        if auto_advance is not None:
            data["auto_advance"] = str(auto_advance).lower()
        return stripe_request("POST", f"/v1/invoices/{invoice_id}/finalize", data=data)

    @mcp.tool()
    def pay_invoice(
        invoice_id: str,
        payment_method: str = None,
        source: str = None,
        paid_out_of_band: bool = None,
        forgive: bool = None,
        off_session: bool = None,
    ) -> dict:
        """Attempt to pay an Invoice."""
        data = {}
        if payment_method:
            data["payment_method"] = payment_method
        if source:
            data["source"] = source
        if paid_out_of_band is not None:
            data["paid_out_of_band"] = str(paid_out_of_band).lower()
        if forgive is not None:
            data["forgive"] = str(forgive).lower()
        if off_session is not None:
            data["off_session"] = str(off_session).lower()
        return stripe_request("POST", f"/v1/invoices/{invoice_id}/pay", data=data)

    @mcp.tool()
    def send_invoice(invoice_id: str) -> dict:
        """Send a finalized Invoice to the customer by email."""
        return stripe_request("POST", f"/v1/invoices/{invoice_id}/send")

    @mcp.tool()
    def void_invoice(invoice_id: str) -> dict:
        """Void a finalized Invoice."""
        return stripe_request("POST", f"/v1/invoices/{invoice_id}/void")

    @mcp.tool()
    def mark_invoice_uncollectible(invoice_id: str) -> dict:
        """Mark a finalized Invoice as uncollectible."""
        return stripe_request("POST", f"/v1/invoices/{invoice_id}/mark_uncollectible")

    @mcp.tool()
    def list_invoices(
        customer: str = None,
        subscription: str = None,
        status: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        due_date_gte: int = None,
        due_date_lte: int = None,
    ) -> dict:
        """List Invoices. status: draft | open | paid | uncollectible | void"""
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
        if due_date_gte is not None:
            params["due_date[gte]"] = due_date_gte
        if due_date_lte is not None:
            params["due_date[lte]"] = due_date_lte
        return stripe_request("GET", "/v1/invoices", params=params)

    @mcp.tool()
    def get_upcoming_invoice(
        customer: str,
        subscription: str = None,
        coupon: str = None,
        subscription_items: list = None,
    ) -> dict:
        """Preview the upcoming Invoice for a Customer."""
        params = {"customer": customer}
        if subscription:
            params["subscription"] = subscription
        if coupon:
            params["coupon"] = coupon
        if subscription_items:
            for i, item in enumerate(subscription_items):
                if "price" in item:
                    params[f"subscription_items[{i}][price]"] = item["price"]
                if "quantity" in item:
                    params[f"subscription_items[{i}][quantity]"] = item["quantity"]
        return stripe_request("GET", "/v1/invoices/upcoming", params=params)

    # ── Invoice Items ──────────────────────────────────────────────────────────

    @mcp.tool()
    def create_invoice_item(
        customer: str,
        amount: int = None,
        currency: str = None,
        price: str = None,
        quantity: int = None,
        description: str = None,
        invoice: str = None,
        subscription: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create an Invoice Item to be included on the next Invoice."""
        data = {"customer": customer}
        if amount is not None:
            data["amount"] = amount
        if currency:
            data["currency"] = currency
        if price:
            data["price"] = price
        if quantity is not None:
            data["quantity"] = quantity
        if description:
            data["description"] = description
        if invoice:
            data["invoice"] = invoice
        if subscription:
            data["subscription"] = subscription
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/invoiceitems", data=data)

    @mcp.tool()
    def get_invoice_item(invoice_item_id: str) -> dict:
        """Retrieve an Invoice Item by ID."""
        return stripe_request("GET", f"/v1/invoiceitems/{invoice_item_id}")

    @mcp.tool()
    def update_invoice_item(
        invoice_item_id: str,
        amount: int = None,
        description: str = None,
        quantity: int = None,
        price: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update an Invoice Item."""
        data = {}
        if amount is not None:
            data["amount"] = amount
        if description:
            data["description"] = description
        if quantity is not None:
            data["quantity"] = quantity
        if price:
            data["price"] = price
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/invoiceitems/{invoice_item_id}", data=data)

    @mcp.tool()
    def delete_invoice_item(invoice_item_id: str) -> dict:
        """Delete an Invoice Item."""
        return stripe_request("DELETE", f"/v1/invoiceitems/{invoice_item_id}")

    @mcp.tool()
    def list_invoice_items(
        customer: str = None,
        invoice: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List Invoice Items."""
        params = {}
        if customer:
            params["customer"] = customer
        if invoice:
            params["invoice"] = invoice
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return stripe_request("GET", "/v1/invoiceitems", params=params)
