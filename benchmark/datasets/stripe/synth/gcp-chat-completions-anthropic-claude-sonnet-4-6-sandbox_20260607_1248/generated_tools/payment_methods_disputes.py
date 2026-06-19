"""Tools for Stripe Payment Methods and Disputes APIs."""
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


def register_payment_method_dispute_tools(mcp: FastMCP):

    # ── Payment Methods ────────────────────────────────────────────────────

    @mcp.tool()
    def create_payment_method(
        type: str,
        billing_details_name: str = None,
        billing_details_email: str = None,
        billing_details_phone: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a PaymentMethod object.

        Args:
            type: Type of payment method (e.g. 'card', 'us_bank_account', 'sepa_debit').
            billing_details_name: Billing name.
            billing_details_email: Billing email.
            billing_details_phone: Billing phone.
            metadata: Key-value pairs to attach.
        """
        data = {"type": type}
        if billing_details_name: data["billing_details[name]"] = billing_details_name
        if billing_details_email: data["billing_details[email]"] = billing_details_email
        if billing_details_phone: data["billing_details[phone]"] = billing_details_phone
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/payment_methods", data=data)

    @mcp.tool()
    def retrieve_payment_method(payment_method_id: str) -> dict:
        """Retrieve a PaymentMethod by ID.

        Args:
            payment_method_id: The ID of the payment method to retrieve.
        """
        return _req("GET", f"/v1/payment_methods/{payment_method_id}")

    @mcp.tool()
    def update_payment_method(
        payment_method_id: str,
        billing_details_name: str = None,
        billing_details_email: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a PaymentMethod.

        Args:
            payment_method_id: The ID of the payment method to update.
            billing_details_name: New billing name.
            billing_details_email: New billing email.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if billing_details_name: data["billing_details[name]"] = billing_details_name
        if billing_details_email: data["billing_details[email]"] = billing_details_email
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/payment_methods/{payment_method_id}", data=data)

    @mcp.tool()
    def attach_payment_method(
        payment_method_id: str,
        customer: str,
    ) -> dict:
        """Attach a PaymentMethod to a Customer.

        Args:
            payment_method_id: The ID of the payment method to attach.
            customer: The ID of the customer to attach the payment method to.
        """
        data = {"customer": customer}
        return _req("POST", f"/v1/payment_methods/{payment_method_id}/attach", data=data)

    @mcp.tool()
    def detach_payment_method(payment_method_id: str) -> dict:
        """Detach a PaymentMethod from its Customer.

        Args:
            payment_method_id: The ID of the payment method to detach.
        """
        return _req("POST", f"/v1/payment_methods/{payment_method_id}/detach")

    @mcp.tool()
    def list_payment_methods(
        customer: str = None,
        type: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List PaymentMethods for a customer or all payment methods.

        Args:
            customer: Filter by customer ID.
            type: Filter by type (e.g. 'card', 'us_bank_account').
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if customer: params["customer"] = customer
        if type: params["type"] = type
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/payment_methods", params=params)

    @mcp.tool()
    def retrieve_customer_payment_method(
        customer_id: str,
        payment_method_id: str,
    ) -> dict:
        """Retrieve a specific PaymentMethod for a Customer.

        Args:
            customer_id: The ID of the customer.
            payment_method_id: The ID of the payment method.
        """
        return _req("GET", f"/v1/customers/{customer_id}/payment_methods/{payment_method_id}")

    @mcp.tool()
    def list_customer_payment_methods(
        customer_id: str,
        type: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all PaymentMethods for a specific Customer.

        Args:
            customer_id: The ID of the customer.
            type: Filter by payment method type (e.g. 'card').
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if type: params["type"] = type
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", f"/v1/customers/{customer_id}/payment_methods", params=params)

    # ── Disputes ───────────────────────────────────────────────────────────

    @mcp.tool()
    def retrieve_dispute(dispute_id: str) -> dict:
        """Retrieve a Dispute by ID.

        Args:
            dispute_id: The ID of the dispute to retrieve.
        """
        return _req("GET", f"/v1/disputes/{dispute_id}")

    @mcp.tool()
    def update_dispute(
        dispute_id: str,
        submit: bool = None,
        evidence_customer_email_address: str = None,
        evidence_customer_name: str = None,
        evidence_product_description: str = None,
        evidence_uncategorized_text: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Dispute with evidence to contest it.

        Args:
            dispute_id: The ID of the dispute to update.
            submit: If True, immediately submit evidence to the bank.
            evidence_customer_email_address: Customer's email address.
            evidence_customer_name: Customer's name.
            evidence_product_description: Description of the product/service.
            evidence_uncategorized_text: Any additional evidence text.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if submit is not None: data["submit"] = str(submit).lower()
        if evidence_customer_email_address:
            data["evidence[customer_email_address]"] = evidence_customer_email_address
        if evidence_customer_name:
            data["evidence[customer_name]"] = evidence_customer_name
        if evidence_product_description:
            data["evidence[product_description]"] = evidence_product_description
        if evidence_uncategorized_text:
            data["evidence[uncategorized_text]"] = evidence_uncategorized_text
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/disputes/{dispute_id}", data=data)

    @mcp.tool()
    def list_disputes(
        charge: str = None,
        payment_intent: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Disputes.

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
        return _req("GET", "/v1/disputes", params=params)
