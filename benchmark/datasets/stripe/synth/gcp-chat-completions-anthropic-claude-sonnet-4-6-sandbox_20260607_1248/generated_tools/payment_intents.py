"""Tools for Stripe Payment Intents API."""
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


def register_payment_intent_tools(mcp: FastMCP):

    @mcp.tool()
    def create_payment_intent(
        amount: int,
        currency: str,
        customer: str = None,
        description: str = None,
        payment_method: str = None,
        receipt_email: str = None,
        setup_future_usage: str = None,
        confirm: bool = None,
        statement_descriptor: str = None,
        statement_descriptor_suffix: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a PaymentIntent to collect a payment from a customer.

        Args:
            amount: Amount in smallest currency unit (e.g. cents).
            currency: Three-letter ISO currency code (e.g. 'usd').
            customer: ID of the Customer this PaymentIntent belongs to.
            description: Arbitrary string attached to the object.
            payment_method: ID of the payment method to attach.
            receipt_email: Email address to send the receipt to.
            setup_future_usage: 'off_session' or 'on_session'.
            confirm: Set True to confirm immediately upon creation.
            statement_descriptor: Statement descriptor for non-card charges.
            statement_descriptor_suffix: Suffix for card charges.
            metadata: Key-value pairs to attach to the object.
        """
        data = {"amount": amount, "currency": currency}
        if customer: data["customer"] = customer
        if description: data["description"] = description
        if payment_method: data["payment_method"] = payment_method
        if receipt_email: data["receipt_email"] = receipt_email
        if setup_future_usage: data["setup_future_usage"] = setup_future_usage
        if confirm is not None: data["confirm"] = str(confirm).lower()
        if statement_descriptor: data["statement_descriptor"] = statement_descriptor
        if statement_descriptor_suffix: data["statement_descriptor_suffix"] = statement_descriptor_suffix
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/payment_intents", data=data)

    @mcp.tool()
    def retrieve_payment_intent(payment_intent_id: str) -> dict:
        """Retrieve a PaymentIntent by ID.

        Args:
            payment_intent_id: The ID of the PaymentIntent.
        """
        return _req("GET", f"/v1/payment_intents/{payment_intent_id}")

    @mcp.tool()
    def update_payment_intent(
        payment_intent_id: str,
        amount: int = None,
        currency: str = None,
        customer: str = None,
        description: str = None,
        payment_method: str = None,
        receipt_email: str = None,
        setup_future_usage: str = None,
        statement_descriptor: str = None,
        statement_descriptor_suffix: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a PaymentIntent.

        Args:
            payment_intent_id: The ID of the PaymentIntent to update.
            amount: New amount in smallest currency unit.
            currency: New currency code.
            customer: New customer ID.
            description: New description.
            payment_method: New payment method ID.
            receipt_email: New receipt email.
            setup_future_usage: 'off_session' or 'on_session'.
            statement_descriptor: New statement descriptor.
            statement_descriptor_suffix: New statement descriptor suffix.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if amount is not None: data["amount"] = amount
        if currency: data["currency"] = currency
        if customer: data["customer"] = customer
        if description: data["description"] = description
        if payment_method: data["payment_method"] = payment_method
        if receipt_email: data["receipt_email"] = receipt_email
        if setup_future_usage: data["setup_future_usage"] = setup_future_usage
        if statement_descriptor: data["statement_descriptor"] = statement_descriptor
        if statement_descriptor_suffix: data["statement_descriptor_suffix"] = statement_descriptor_suffix
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/payment_intents/{payment_intent_id}", data=data)

    @mcp.tool()
    def confirm_payment_intent(
        payment_intent_id: str,
        payment_method: str = None,
        return_url: str = None,
    ) -> dict:
        """Confirm a PaymentIntent to attempt payment collection.

        Args:
            payment_intent_id: The ID of the PaymentIntent to confirm.
            payment_method: ID of the payment method to use.
            return_url: URL to redirect after confirmation.
        """
        data = {}
        if payment_method: data["payment_method"] = payment_method
        if return_url: data["return_url"] = return_url
        return _req("POST", f"/v1/payment_intents/{payment_intent_id}/confirm", data=data)

    @mcp.tool()
    def cancel_payment_intent(
        payment_intent_id: str,
        cancellation_reason: str = None,
    ) -> dict:
        """Cancel a PaymentIntent.

        Args:
            payment_intent_id: The ID of the PaymentIntent to cancel.
            cancellation_reason: Reason for cancellation: 'duplicate', 'fraudulent',
                'requested_by_customer', or 'abandoned'.
        """
        data = {}
        if cancellation_reason: data["cancellation_reason"] = cancellation_reason
        return _req("POST", f"/v1/payment_intents/{payment_intent_id}/cancel", data=data)

    @mcp.tool()
    def capture_payment_intent(
        payment_intent_id: str,
        amount_to_capture: int = None,
    ) -> dict:
        """Capture a PaymentIntent that requires capture.

        Args:
            payment_intent_id: The ID of the PaymentIntent to capture.
            amount_to_capture: Amount to capture (defaults to full amount).
        """
        data = {}
        if amount_to_capture is not None: data["amount_to_capture"] = amount_to_capture
        return _req("POST", f"/v1/payment_intents/{payment_intent_id}/capture", data=data)

    @mcp.tool()
    def list_payment_intents(
        customer: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List PaymentIntents, optionally filtered by customer.

        Args:
            customer: Filter by customer ID.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if customer: params["customer"] = customer
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/payment_intents", params=params)
