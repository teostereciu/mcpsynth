"""
Stripe Tax Rates tools.
Endpoints covered:
  POST   /v1/tax_rates
  GET    /v1/tax_rates/{id}
  POST   /v1/tax_rates/{id}
  GET    /v1/tax_rates
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def create_tax_rate(
        display_name: str,
        inclusive: bool,
        percentage: float,
        active: bool = None,
        country: str = None,
        description: str = None,
        jurisdiction: str = None,
        state: str = None,
        tax_type: str = None,
        metadata: dict = None,
    ) -> dict:
        """
        Create a Tax Rate.
        inclusive: True if the tax is included in the price, False if added on top.
        tax_type: vat | sales_tax | gst | hst | pst | qst | igst | jct | lease_tax | rst
        """
        data = {
            "display_name": display_name,
            "inclusive": str(inclusive).lower(),
            "percentage": percentage,
        }
        if active is not None:
            data["active"] = str(active).lower()
        if country:
            data["country"] = country
        if description:
            data["description"] = description
        if jurisdiction:
            data["jurisdiction"] = jurisdiction
        if state:
            data["state"] = state
        if tax_type:
            data["tax_type"] = tax_type
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/tax_rates", data=data)

    @mcp.tool()
    def get_tax_rate(tax_rate_id: str) -> dict:
        """Retrieve a Tax Rate by ID."""
        return stripe_request("GET", f"/v1/tax_rates/{tax_rate_id}")

    @mcp.tool()
    def update_tax_rate(
        tax_rate_id: str,
        active: bool = None,
        display_name: str = None,
        description: str = None,
        jurisdiction: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Tax Rate."""
        data = {}
        if active is not None:
            data["active"] = str(active).lower()
        if display_name:
            data["display_name"] = display_name
        if description:
            data["description"] = description
        if jurisdiction:
            data["jurisdiction"] = jurisdiction
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/tax_rates/{tax_rate_id}", data=data)

    @mcp.tool()
    def list_tax_rates(
        active: bool = None,
        inclusive: bool = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        created_gte: int = None,
        created_lte: int = None,
    ) -> dict:
        """List Tax Rates."""
        params = {}
        if active is not None:
            params["active"] = str(active).lower()
        if inclusive is not None:
            params["inclusive"] = str(inclusive).lower()
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
        return stripe_request("GET", "/v1/tax_rates", params=params)
