"""
Stripe Application Fees & Fee Refunds tools (Connect).
Endpoints covered:
  GET    /v1/application_fees/{id}
  GET    /v1/application_fees
  POST   /v1/application_fees/{id}/refunds
  GET    /v1/application_fees/{id}/refunds/{refund_id}
  POST   /v1/application_fees/{id}/refunds/{refund_id}
  GET    /v1/application_fees/{id}/refunds
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def get_application_fee(application_fee_id: str) -> dict:
        """Retrieve an Application Fee by ID."""
        return stripe_request("GET", f"/v1/application_fees/{application_fee_id}")

    @mcp.tool()
    def list_application_fees(
        charge: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        created_gte: int = None,
        created_lte: int = None,
    ) -> dict:
        """List Application Fees."""
        params = {}
        if charge:
            params["charge"] = charge
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
        return stripe_request("GET", "/v1/application_fees", params=params)

    @mcp.tool()
    def create_application_fee_refund(
        application_fee_id: str,
        amount: int = None,
        metadata: dict = None,
    ) -> dict:
        """Refund an Application Fee."""
        data = {}
        if amount is not None:
            data["amount"] = amount
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request(
            "POST",
            f"/v1/application_fees/{application_fee_id}/refunds",
            data=data,
        )

    @mcp.tool()
    def get_application_fee_refund(application_fee_id: str, refund_id: str) -> dict:
        """Retrieve an Application Fee Refund."""
        return stripe_request(
            "GET",
            f"/v1/application_fees/{application_fee_id}/refunds/{refund_id}",
        )

    @mcp.tool()
    def update_application_fee_refund(
        application_fee_id: str,
        refund_id: str,
        metadata: dict = None,
    ) -> dict:
        """Update an Application Fee Refund's metadata."""
        data = {}
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request(
            "POST",
            f"/v1/application_fees/{application_fee_id}/refunds/{refund_id}",
            data=data,
        )

    @mcp.tool()
    def list_application_fee_refunds(
        application_fee_id: str,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List refunds for an Application Fee."""
        params = {}
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return stripe_request(
            "GET",
            f"/v1/application_fees/{application_fee_id}/refunds",
            params=params,
        )
