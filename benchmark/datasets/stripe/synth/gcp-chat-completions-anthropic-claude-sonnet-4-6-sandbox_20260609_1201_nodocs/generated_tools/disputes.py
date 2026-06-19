"""
Stripe Disputes tools.
Endpoints covered:
  GET    /v1/disputes/{id}
  POST   /v1/disputes/{id}
  POST   /v1/disputes/{id}/close
  GET    /v1/disputes
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def get_dispute(dispute_id: str) -> dict:
        """Retrieve a Dispute by ID."""
        return stripe_request("GET", f"/v1/disputes/{dispute_id}")

    @mcp.tool()
    def update_dispute(
        dispute_id: str,
        evidence_customer_email_address: str = None,
        evidence_customer_name: str = None,
        evidence_product_description: str = None,
        evidence_uncategorized_text: str = None,
        evidence_shipping_tracking_number: str = None,
        evidence_receipt: str = None,
        submit: bool = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Dispute with evidence. Set submit=True to submit to the bank."""
        data = {}
        if evidence_customer_email_address:
            data["evidence[customer_email_address]"] = evidence_customer_email_address
        if evidence_customer_name:
            data["evidence[customer_name]"] = evidence_customer_name
        if evidence_product_description:
            data["evidence[product_description]"] = evidence_product_description
        if evidence_uncategorized_text:
            data["evidence[uncategorized_text]"] = evidence_uncategorized_text
        if evidence_shipping_tracking_number:
            data["evidence[shipping_tracking_number]"] = evidence_shipping_tracking_number
        if evidence_receipt:
            data["evidence[receipt]"] = evidence_receipt
        if submit is not None:
            data["submit"] = str(submit).lower()
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/disputes/{dispute_id}", data=data)

    @mcp.tool()
    def close_dispute(dispute_id: str) -> dict:
        """Close a Dispute (accept the dispute, forfeiting the funds)."""
        return stripe_request("POST", f"/v1/disputes/{dispute_id}/close")

    @mcp.tool()
    def list_disputes(
        charge: str = None,
        payment_intent: str = None,
        status: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        created_gte: int = None,
        created_lte: int = None,
    ) -> dict:
        """List Disputes. status: needs_response | under_review | charge_refunded | won | lost | warning_*"""
        params = {}
        if charge:
            params["charge"] = charge
        if payment_intent:
            params["payment_intent"] = payment_intent
        if status:
            params["status"] = status
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
        return stripe_request("GET", "/v1/disputes", params=params)
