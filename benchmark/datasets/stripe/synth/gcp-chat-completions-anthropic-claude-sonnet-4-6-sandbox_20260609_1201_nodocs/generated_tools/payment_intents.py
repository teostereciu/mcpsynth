"""
Stripe Payment Intents tools.
Endpoints covered:
  POST   /v1/payment_intents
  GET    /v1/payment_intents/{id}
  POST   /v1/payment_intents/{id}
  POST   /v1/payment_intents/{id}/confirm
  POST   /v1/payment_intents/{id}/capture
  POST   /v1/payment_intents/{id}/cancel
  GET    /v1/payment_intents
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request

def register(mcp: FastMCP):

    @mcp.tool()
    def create_payment_intent(
        amount: int,
        currency: str,
        customer: str = None,
        description: str = None,
        payment_method: str = None,
        payment_method_types: list = None,
        confirm: bool = None,
        capture_method: str = None,
        setup_future_usage: str = None,
        metadata: dict = None,
        receipt_email: str = None,
        statement_descriptor: str = None,
        application_fee_amount: int = None,
        transfer_data_destination: str = None,
        on_behalf_of: str = None,
    ) -> dict:
        """Create a PaymentIntent. amount is in the smallest currency unit (e.g. cents)."""
        data = {"amount": amount, "currency": currency}
        if customer:
            data["customer"] = customer
        if description:
            data["description"] = description
        if payment_method:
            data["payment_method"] = payment_method
        if payment_method_types:
            for i, pm in enumerate(payment_method_types):
                data[f"payment_method_types[{i}]"] = pm
        if confirm is not None:
            data["confirm"] = str(confirm).lower()
        if capture_method:
            data["capture_method"] = capture_method
        if setup_future_usage:
            data["setup_future_usage"] = setup_future_usage
        if receipt_email:
            data["receipt_email"] = receipt_email
        if statement_descriptor:
            data["statement_descriptor"] = statement_descriptor
        if application_fee_amount is not None:
            data["application_fee_amount"] = application_fee_amount
        if transfer_data_destination:
            data["transfer_data[destination]"] = transfer_data_destination
        if on_behalf_of:
            data["on_behalf_of"] = on_behalf_of
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/payment_intents", data=data)

    @mcp.tool()
    def get_payment_intent(payment_intent_id: str) -> dict:
        """Retrieve a PaymentIntent by ID."""
        return stripe_request("GET", f"/v1/payment_intents/{payment_intent_id}")

    @mcp.tool()
    def update_payment_intent(
        payment_intent_id: str,
        amount: int = None,
        currency: str = None,
        customer: str = None,
        description: str = None,
        payment_method: str = None,
        receipt_email: str = None,
        statement_descriptor: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a PaymentIntent."""
        data = {}
        if amount is not None:
            data["amount"] = amount
        if currency:
            data["currency"] = currency
        if customer:
            data["customer"] = customer
        if description:
            data["description"] = description
        if payment_method:
            data["payment_method"] = payment_method
        if receipt_email:
            data["receipt_email"] = receipt_email
        if statement_descriptor:
            data["statement_descriptor"] = statement_descriptor
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}", data=data)

    @mcp.tool()
    def confirm_payment_intent(
        payment_intent_id: str,
        payment_method: str = None,
        return_url: str = None,
    ) -> dict:
        """Confirm a PaymentIntent."""
        data = {}
        if payment_method:
            data["payment_method"] = payment_method
        if return_url:
            data["return_url"] = return_url
        return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/confirm", data=data)

    @mcp.tool()
    def capture_payment_intent(
        payment_intent_id: str,
        amount_to_capture: int = None,
        application_fee_amount: int = None,
    ) -> dict:
        """Capture funds for a PaymentIntent that requires manual capture."""
        data = {}
        if amount_to_capture is not None:
            data["amount_to_capture"] = amount_to_capture
        if application_fee_amount is not None:
            data["application_fee_amount"] = application_fee_amount
        return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/capture", data=data)

    @mcp.tool()
    def cancel_payment_intent(
        payment_intent_id: str,
        cancellation_reason: str = None,
    ) -> dict:
        """Cancel a PaymentIntent. cancellation_reason: duplicate, fraudulent, requested_by_customer, abandoned."""
        data = {}
        if cancellation_reason:
            data["cancellation_reason"] = cancellation_reason
        return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/cancel", data=data)

    @mcp.tool()
    def list_payment_intents(
        customer: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        created_gte: int = None,
        created_lte: int = None,
    ) -> dict:
        """List PaymentIntents, optionally filtered by customer."""
        params = {}
        if customer:
            params["customer"] = customer
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        if created_gte is not None:
            params["created[gte]"] = created_gte
        if created_lte is not None:
            params["created[lte]"] = created_lte
        return stripe_request("GET", "/v1/payment_intents", params=params)
