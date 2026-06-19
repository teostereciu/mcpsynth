"""Tools for Stripe billing extras: Subscription Items, Invoice Items, Credit Notes, Tax Rates."""
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


def register_billing_extra_tools(mcp: FastMCP):

    # ---- Subscription Items ----

    @mcp.tool()
    def create_subscription_item(
        subscription: str,
        price: str,
        quantity: int = None,
        proration_behavior: str = None,
        metadata: dict = None,
    ) -> dict:
        """Add a new item to an existing Subscription.

        Args:
            subscription: ID of the subscription to modify.
            price: ID of the price to add.
            quantity: Quantity of the plan.
            proration_behavior: 'create_prorations', 'none', or 'always_invoice'.
            metadata: Key-value pairs to attach to the object.
        """
        data = {"subscription": subscription, "price": price}
        if quantity is not None:
            data["quantity"] = quantity
        if proration_behavior:
            data["proration_behavior"] = proration_behavior
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/subscription_items", data=data)

    @mcp.tool()
    def retrieve_subscription_item(item_id: str) -> dict:
        """Retrieve a Subscription Item by ID.

        Args:
            item_id: The ID of the subscription item (e.g. 'si_...').
        """
        return _req("GET", f"/v1/subscription_items/{item_id}")

    @mcp.tool()
    def update_subscription_item(
        item_id: str,
        price: str = None,
        quantity: int = None,
        proration_behavior: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Subscription Item.

        Args:
            item_id: The ID of the subscription item to update.
            price: ID of the new price.
            quantity: New quantity.
            proration_behavior: 'create_prorations', 'none', or 'always_invoice'.
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if price:
            data["price"] = price
        if quantity is not None:
            data["quantity"] = quantity
        if proration_behavior:
            data["proration_behavior"] = proration_behavior
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/subscription_items/{item_id}", data=data)

    @mcp.tool()
    def delete_subscription_item(item_id: str, proration_behavior: str = None) -> dict:
        """Delete a Subscription Item.

        Args:
            item_id: The ID of the subscription item to delete.
            proration_behavior: 'create_prorations', 'none', or 'always_invoice'.
        """
        data = {}
        if proration_behavior:
            data["proration_behavior"] = proration_behavior
        return _req("DELETE", f"/v1/subscription_items/{item_id}", data=data)

    @mcp.tool()
    def list_subscription_items(
        subscription: str,
        limit: int = None,
        starting_after: str = None,
    ) -> dict:
        """List all items for a Subscription.

        Args:
            subscription: ID of the subscription to list items for.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
        """
        params = {"subscription": subscription}
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        return _req("GET", "/v1/subscription_items", params=params)

    # ---- Invoice Items ----

    @mcp.tool()
    def create_invoice_item(
        customer: str,
        amount: int = None,
        currency: str = None,
        description: str = None,
        invoice: str = None,
        price: str = None,
        quantity: int = None,
        metadata: dict = None,
    ) -> dict:
        """Create an Invoice Item to be added to a draft invoice.

        Args:
            customer: ID of the customer to bill.
            amount: Amount in smallest currency unit (e.g. cents).
            currency: Three-letter ISO currency code.
            description: Arbitrary string attached to the object.
            invoice: ID of the invoice to attach this item to.
            price: ID of the price to use.
            quantity: Quantity of the item.
            metadata: Key-value pairs to attach to the object.
        """
        data = {"customer": customer}
        if amount is not None:
            data["amount"] = amount
        if currency:
            data["currency"] = currency
        if description:
            data["description"] = description
        if invoice:
            data["invoice"] = invoice
        if price:
            data["pricing[price]"] = price
        if quantity is not None:
            data["quantity"] = quantity
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/invoiceitems", data=data)

    @mcp.tool()
    def retrieve_invoice_item(invoice_item_id: str) -> dict:
        """Retrieve an Invoice Item by ID.

        Args:
            invoice_item_id: The ID of the invoice item (e.g. 'ii_...').
        """
        return _req("GET", f"/v1/invoiceitems/{invoice_item_id}")

    @mcp.tool()
    def update_invoice_item(
        invoice_item_id: str,
        amount: int = None,
        description: str = None,
        quantity: int = None,
        metadata: dict = None,
    ) -> dict:
        """Update an Invoice Item.

        Args:
            invoice_item_id: The ID of the invoice item to update.
            amount: New amount in smallest currency unit.
            description: Arbitrary string attached to the object.
            quantity: New quantity.
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if amount is not None:
            data["amount"] = amount
        if description:
            data["description"] = description
        if quantity is not None:
            data["quantity"] = quantity
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/invoiceitems/{invoice_item_id}", data=data)

    @mcp.tool()
    def delete_invoice_item(invoice_item_id: str) -> dict:
        """Delete an Invoice Item.

        Args:
            invoice_item_id: The ID of the invoice item to delete.
        """
        return _req("DELETE", f"/v1/invoiceitems/{invoice_item_id}")

    @mcp.tool()
    def list_invoice_items(
        customer: str = None,
        invoice: str = None,
        limit: int = None,
        starting_after: str = None,
    ) -> dict:
        """List all Invoice Items.

        Args:
            customer: Filter by customer ID.
            invoice: Filter by invoice ID.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
        """
        params = {}
        if customer:
            params["customer"] = customer
        if invoice:
            params["invoice"] = invoice
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        return _req("GET", "/v1/invoiceitems", params=params)

    # ---- Tax Rates ----

    @mcp.tool()
    def create_tax_rate(
        display_name: str,
        inclusive: bool,
        percentage: float,
        description: str = None,
        jurisdiction: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a Tax Rate.

        Args:
            display_name: Name of the tax rate shown to customers.
            inclusive: If True, tax is included in the price (inclusive). If False, tax is added on top (exclusive).
            percentage: Tax rate percentage (e.g. 7.5 for 7.5%).
            description: Internal description of the tax rate.
            jurisdiction: Jurisdiction for the tax rate (e.g. 'CA').
            metadata: Key-value pairs to attach to the object.
        """
        data = {
            "display_name": display_name,
            "inclusive": str(inclusive).lower(),
            "percentage": percentage,
        }
        if description:
            data["description"] = description
        if jurisdiction:
            data["jurisdiction"] = jurisdiction
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/tax_rates", data=data)

    @mcp.tool()
    def retrieve_tax_rate(tax_rate_id: str) -> dict:
        """Retrieve a Tax Rate by ID.

        Args:
            tax_rate_id: The ID of the tax rate (e.g. 'txr_...').
        """
        return _req("GET", f"/v1/tax_rates/{tax_rate_id}")

    @mcp.tool()
    def list_tax_rates(
        active: bool = None,
        inclusive: bool = None,
        limit: int = None,
    ) -> dict:
        """List all Tax Rates.

        Args:
            active: Filter by active status.
            inclusive: Filter by inclusive/exclusive.
            limit: Number of objects to return (1-100).
        """
        params = {}
        if active is not None:
            params["active"] = str(active).lower()
        if inclusive is not None:
            params["inclusive"] = str(inclusive).lower()
        if limit is not None:
            params["limit"] = limit
        return _req("GET", "/v1/tax_rates", params=params)
