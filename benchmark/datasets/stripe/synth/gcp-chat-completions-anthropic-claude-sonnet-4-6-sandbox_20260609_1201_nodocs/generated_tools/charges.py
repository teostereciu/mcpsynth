"""
Stripe Charges tools.
Endpoints covered:
  POST   /v1/charges
  GET    /v1/charges/{id}
  POST   /v1/charges/{id}
  POST   /v1/charges/{id}/capture
  GET    /v1/charges
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def create_charge(
        amount: int,
        currency: str,
        source: str = None,
        customer: str = None,
        description: str = None,
        capture: bool = None,
        receipt_email: str = None,
        statement_descriptor: str = None,
        metadata: dict = None,
        application_fee_amount: int = None,
        transfer_data_destination: str = None,
        on_behalf_of: str = None,
    ) -> dict:
        """Create a Charge. amount is in the smallest currency unit."""
        data = {"amount": amount, "currency": currency}
        if source:
            data["source"] = source
        if customer:
            data["customer"] = customer
        if description:
            data["description"] = description
        if capture is not None:
            data["capture"] = str(capture).lower()
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
        return stripe_request("POST", "/v1/charges", data=data)

    @mcp.tool()
    def get_charge(charge_id: str) -> dict:
        """Retrieve a Charge by ID."""
        return stripe_request("GET", f"/v1/charges/{charge_id}")

    @mcp.tool()
    def update_charge(
        charge_id: str,
        description: str = None,
        receipt_email: str = None,
        fraud_details_user_report: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Charge's description, receipt_email, or metadata."""
        data = {}
        if description:
            data["description"] = description
        if receipt_email:
            data["receipt_email"] = receipt_email
        if fraud_details_user_report:
            data["fraud_details[user_report]"] = fraud_details_user_report
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/charges/{charge_id}", data=data)

    @mcp.tool()
    def capture_charge(
        charge_id: str,
        amount: int = None,
        receipt_email: str = None,
        statement_descriptor: str = None,
        application_fee_amount: int = None,
    ) -> dict:
        """Capture an uncaptured Charge."""
        data = {}
        if amount is not None:
            data["amount"] = amount
        if receipt_email:
            data["receipt_email"] = receipt_email
        if statement_descriptor:
            data["statement_descriptor"] = statement_descriptor
        if application_fee_amount is not None:
            data["application_fee_amount"] = application_fee_amount
        return stripe_request("POST", f"/v1/charges/{charge_id}/capture", data=data)

    @mcp.tool()
    def list_charges(
        customer: str = None,
        payment_intent: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        created_gte: int = None,
        created_lte: int = None,
    ) -> dict:
        """List Charges with optional filters."""
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
        if created_gte is not None:
            params["created[gte]"] = created_gte
        if created_lte is not None:
            params["created[lte]"] = created_lte
        return stripe_request("GET", "/v1/charges", params=params)
