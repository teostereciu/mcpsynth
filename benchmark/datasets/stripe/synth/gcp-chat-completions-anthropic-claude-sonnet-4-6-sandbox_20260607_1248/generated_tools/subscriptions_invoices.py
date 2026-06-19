"""Tools for Stripe Subscriptions and Invoices APIs."""
import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.stripe.com"

def _get_headers():
    api_key = os.environ.get("STRIPE_API_KEY", "")
    return {"Authorization": f"Bearer {api_key}"}

def _req(method, path, params=None, data=None):
    url = f"{BASE_URL}{path}"
    try:
        resp = requests.request(
            method, url,
            headers=_get_headers(),
            params=params,
            data=data,
            timeout=30,
        )
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def register_subscription_invoice_tools(mcp: FastMCP):

    # ── Subscriptions ──────────────────────────────────────────────────────

    @mcp.tool()
    def create_subscription(
        customer: str,
        items: list,
        default_payment_method: str = None,
        description: str = None,
        currency: str = None,
        trial_period_days: int = None,
        cancel_at_period_end: bool = None,
        collection_method: str = None,
        days_until_due: int = None,
        metadata: dict = None,
    ) -> dict:
        """Create a new Subscription for a customer.

        Args:
            customer: ID of the customer to subscribe.
            items: List of dicts with 'price' (and optionally 'quantity') keys.
                   e.g. [{"price": "price_xxx", "quantity": 1}]
            default_payment_method: ID of the default payment method.
            description: Description of the subscription.
            currency: Three-letter ISO currency code.
            trial_period_days: Number of trial period days.
            cancel_at_period_end: If True, cancel at end of current period.
            collection_method: 'charge_automatically' or 'send_invoice'.
            days_until_due: Days until invoice is due (for send_invoice).
            metadata: Key-value pairs to attach.
        """
        data = {"customer": customer}
        for i, item in enumerate(items):
            for k, v in item.items():
                data[f"items[{i}][{k}]"] = v
        if default_payment_method: data["default_payment_method"] = default_payment_method
        if description: data["description"] = description
        if currency: data["currency"] = currency
        if trial_period_days is not None: data["trial_period_days"] = trial_period_days
        if cancel_at_period_end is not None: data["cancel_at_period_end"] = str(cancel_at_period_end).lower()
        if collection_method: data["collection_method"] = collection_method
        if days_until_due is not None: data["days_until_due"] = days_until_due
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/subscriptions", data=data)

    @mcp.tool()
    def retrieve_subscription(subscription_id: str) -> dict:
        """Retrieve a Subscription by ID.

        Args:
            subscription_id: The ID of the subscription to retrieve.
        """
        return _req("GET", f"/v1/subscriptions/{subscription_id}")

    @mcp.tool()
    def update_subscription(
        subscription_id: str,
        default_payment_method: str = None,
        description: str = None,
        cancel_at_period_end: bool = None,
        collection_method: str = None,
        days_until_due: int = None,
        trial_end: str = None,
        proration_behavior: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update an existing Subscription.

        Args:
            subscription_id: The ID of the subscription to update.
            default_payment_method: New default payment method ID.
            description: New description.
            cancel_at_period_end: If True, cancel at end of current period.
            collection_method: 'charge_automatically' or 'send_invoice'.
            days_until_due: Days until invoice is due.
            trial_end: Unix timestamp or 'now' to end trial.
            proration_behavior: 'create_prorations', 'none', or 'always_invoice'.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if default_payment_method: data["default_payment_method"] = default_payment_method
        if description: data["description"] = description
        if cancel_at_period_end is not None: data["cancel_at_period_end"] = str(cancel_at_period_end).lower()
        if collection_method: data["collection_method"] = collection_method
        if days_until_due is not None: data["days_until_due"] = days_until_due
        if trial_end: data["trial_end"] = trial_end
        if proration_behavior: data["proration_behavior"] = proration_behavior
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/subscriptions/{subscription_id}", data=data)

    @mcp.tool()
    def cancel_subscription(
        subscription_id: str,
        cancel_at_period_end: bool = None,
    ) -> dict:
        """Cancel a Subscription immediately or at period end.

        Args:
            subscription_id: The ID of the subscription to cancel.
            cancel_at_period_end: If True, cancel at end of current period instead of immediately.
        """
        if cancel_at_period_end:
            data = {"cancel_at_period_end": "true"}
            return _req("POST", f"/v1/subscriptions/{subscription_id}", data=data)
        return _req("DELETE", f"/v1/subscriptions/{subscription_id}")

    @mcp.tool()
    def list_subscriptions(
        customer: str = None,
        status: str = None,
        price: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Subscriptions.

        Args:
            customer: Filter by customer ID.
            status: Filter by status: 'active', 'past_due', 'canceled', etc.
            price: Filter by price ID.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if customer: params["customer"] = customer
        if status: params["status"] = status
        if price: params["price"] = price
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/subscriptions", params=params)

    # ── Invoices ───────────────────────────────────────────────────────────

    @mcp.tool()
    def create_invoice(
        customer: str,
        description: str = None,
        collection_method: str = None,
        days_until_due: int = None,
        auto_advance: bool = None,
        metadata: dict = None,
    ) -> dict:
        """Create a new Invoice for a customer.

        Args:
            customer: ID of the customer to invoice.
            description: Description for the invoice.
            collection_method: 'charge_automatically' or 'send_invoice'.
            days_until_due: Days until invoice is due (for send_invoice).
            auto_advance: Whether to auto-finalize the invoice.
            metadata: Key-value pairs to attach.
        """
        data = {"customer": customer}
        if description: data["description"] = description
        if collection_method: data["collection_method"] = collection_method
        if days_until_due is not None: data["days_until_due"] = days_until_due
        if auto_advance is not None: data["auto_advance"] = str(auto_advance).lower()
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/invoices", data=data)

    @mcp.tool()
    def retrieve_invoice(invoice_id: str) -> dict:
        """Retrieve an Invoice by ID.

        Args:
            invoice_id: The ID of the invoice to retrieve.
        """
        return _req("GET", f"/v1/invoices/{invoice_id}")

    @mcp.tool()
    def update_invoice(
        invoice_id: str,
        description: str = None,
        auto_advance: bool = None,
        collection_method: str = None,
        days_until_due: int = None,
        metadata: dict = None,
    ) -> dict:
        """Update an Invoice.

        Args:
            invoice_id: The ID of the invoice to update.
            description: New description.
            auto_advance: Whether to auto-finalize the invoice.
            collection_method: 'charge_automatically' or 'send_invoice'.
            days_until_due: Days until invoice is due.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if description: data["description"] = description
        if auto_advance is not None: data["auto_advance"] = str(auto_advance).lower()
        if collection_method: data["collection_method"] = collection_method
        if days_until_due is not None: data["days_until_due"] = days_until_due
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/invoices/{invoice_id}", data=data)

    @mcp.tool()
    def finalize_invoice(invoice_id: str) -> dict:
        """Finalize a draft Invoice, making it ready for payment.

        Args:
            invoice_id: The ID of the invoice to finalize.
        """
        return _req("POST", f"/v1/invoices/{invoice_id}/finalize")

    @mcp.tool()
    def pay_invoice(
        invoice_id: str,
        payment_method: str = None,
        source: str = None,
    ) -> dict:
        """Attempt to pay an Invoice.

        Args:
            invoice_id: The ID of the invoice to pay.
            payment_method: ID of the payment method to use.
            source: ID of the source to use.
        """
        data = {}
        if payment_method: data["payment_method"] = payment_method
        if source: data["source"] = source
        return _req("POST", f"/v1/invoices/{invoice_id}/pay", data=data)

    @mcp.tool()
    def void_invoice(invoice_id: str) -> dict:
        """Void an Invoice.

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
        if customer: params["customer"] = customer
        if subscription: params["subscription"] = subscription
        if status: params["status"] = status
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/invoices", params=params)

    @mcp.tool()
    def preview_invoice(
        customer: str = None,
        subscription: str = None,
    ) -> dict:
        """Preview an upcoming Invoice for a customer or subscription.

        Args:
            customer: ID of the customer to preview invoice for.
            subscription: ID of the subscription to preview invoice for.
        """
        data = {}
        if customer: data["customer"] = customer
        if subscription: data["subscription"] = subscription
        return _req("POST", "/v1/invoices/create_preview", data=data)
