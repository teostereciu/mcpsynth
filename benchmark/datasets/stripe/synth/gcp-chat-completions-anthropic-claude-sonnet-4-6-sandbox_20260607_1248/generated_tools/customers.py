"""Tools for Stripe Customers, Charges, and Refunds APIs."""
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


def register_customer_tools(mcp: FastMCP):

    # ── Customers ──────────────────────────────────────────────────────────

    @mcp.tool()
    def create_customer(
        name: str = None,
        email: str = None,
        phone: str = None,
        description: str = None,
        payment_method: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a new Stripe Customer.

        Args:
            name: The customer's full name or business name.
            email: The customer's email address.
            phone: The customer's phone number.
            description: Arbitrary string attached to the object.
            payment_method: ID of the PaymentMethod to attach.
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if name: data["name"] = name
        if email: data["email"] = email
        if phone: data["phone"] = phone
        if description: data["description"] = description
        if payment_method: data["payment_method"] = payment_method
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/customers", data=data)

    @mcp.tool()
    def retrieve_customer(customer_id: str) -> dict:
        """Retrieve a Customer by ID.

        Args:
            customer_id: The ID of the customer to retrieve.
        """
        return _req("GET", f"/v1/customers/{customer_id}")

    @mcp.tool()
    def update_customer(
        customer_id: str,
        name: str = None,
        email: str = None,
        phone: str = None,
        description: str = None,
        default_source: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update an existing Customer.

        Args:
            customer_id: The ID of the customer to update.
            name: New full name or business name.
            email: New email address.
            phone: New phone number.
            description: New description.
            default_source: ID of the default payment source.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if name: data["name"] = name
        if email: data["email"] = email
        if phone: data["phone"] = phone
        if description: data["description"] = description
        if default_source: data["default_source"] = default_source
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/customers/{customer_id}", data=data)

    @mcp.tool()
    def delete_customer(customer_id: str) -> dict:
        """Permanently delete a Customer.

        Args:
            customer_id: The ID of the customer to delete.
        """
        return _req("DELETE", f"/v1/customers/{customer_id}")

    @mcp.tool()
    def list_customers(
        email: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Customers, optionally filtered by email.

        Args:
            email: Filter customers by email address.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if email: params["email"] = email
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/customers", params=params)

    # ── Charges ────────────────────────────────────────────────────────────

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
        """Create a charge (legacy). Prefer Payment Intents for new integrations.

        Args:
            amount: Amount in smallest currency unit (e.g. cents).
            currency: Three-letter ISO currency code (e.g. 'usd').
            source: Payment source ID (card, token, etc.).
            customer: ID of an existing customer to charge.
            description: Arbitrary string attached to the charge.
            receipt_email: Email to send the receipt to.
            statement_descriptor: Statement descriptor text.
            metadata: Key-value pairs to attach.
        """
        data = {"amount": amount, "currency": currency}
        if source: data["source"] = source
        if customer: data["customer"] = customer
        if description: data["description"] = description
        if receipt_email: data["receipt_email"] = receipt_email
        if statement_descriptor: data["statement_descriptor"] = statement_descriptor
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/charges", data=data)

    @mcp.tool()
    def retrieve_charge(charge_id: str) -> dict:
        """Retrieve a Charge by ID.

        Args:
            charge_id: The ID of the charge to retrieve.
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
            customer: Associate an existing customer with this charge.
            description: New description.
            receipt_email: New receipt email.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if customer: data["customer"] = customer
        if description: data["description"] = description
        if receipt_email: data["receipt_email"] = receipt_email
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
        if customer: params["customer"] = customer
        if payment_intent: params["payment_intent"] = payment_intent
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/charges", params=params)

    # ── Refunds ────────────────────────────────────────────────────────────

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
            metadata: Key-value pairs to attach.
        """
        data = {}
        if charge: data["charge"] = charge
        if payment_intent: data["payment_intent"] = payment_intent
        if amount is not None: data["amount"] = amount
        if reason: data["reason"] = reason
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/refunds", data=data)

    @mcp.tool()
    def retrieve_refund(refund_id: str) -> dict:
        """Retrieve a Refund by ID.

        Args:
            refund_id: The ID of the refund to retrieve.
        """
        return _req("GET", f"/v1/refunds/{refund_id}")

    @mcp.tool()
    def update_refund(
        refund_id: str,
        metadata: dict = None,
    ) -> dict:
        """Update a Refund's metadata.

        Args:
            refund_id: The ID of the refund to update.
            metadata: Key-value pairs to attach.
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
        if charge: params["charge"] = charge
        if payment_intent: params["payment_intent"] = payment_intent
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/refunds", params=params)
