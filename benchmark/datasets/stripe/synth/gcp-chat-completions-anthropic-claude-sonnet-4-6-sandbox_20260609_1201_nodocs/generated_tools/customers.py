"""
Stripe Customers tools.
Endpoints covered:
  POST   /v1/customers
  GET    /v1/customers/{id}
  POST   /v1/customers/{id}
  DELETE /v1/customers/{id}
  GET    /v1/customers
  GET    /v1/customers/{id}/payment_methods
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def create_customer(
        email: str = None,
        name: str = None,
        phone: str = None,
        description: str = None,
        payment_method: str = None,
        source: str = None,
        address_line1: str = None,
        address_line2: str = None,
        address_city: str = None,
        address_state: str = None,
        address_postal_code: str = None,
        address_country: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a new Customer."""
        data = {}
        if email:
            data["email"] = email
        if name:
            data["name"] = name
        if phone:
            data["phone"] = phone
        if description:
            data["description"] = description
        if payment_method:
            data["payment_method"] = payment_method
        if source:
            data["source"] = source
        if address_line1:
            data["address[line1]"] = address_line1
        if address_line2:
            data["address[line2]"] = address_line2
        if address_city:
            data["address[city]"] = address_city
        if address_state:
            data["address[state]"] = address_state
        if address_postal_code:
            data["address[postal_code]"] = address_postal_code
        if address_country:
            data["address[country]"] = address_country
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/customers", data=data)

    @mcp.tool()
    def get_customer(customer_id: str) -> dict:
        """Retrieve a Customer by ID."""
        return stripe_request("GET", f"/v1/customers/{customer_id}")

    @mcp.tool()
    def update_customer(
        customer_id: str,
        email: str = None,
        name: str = None,
        phone: str = None,
        description: str = None,
        payment_method: str = None,
        source: str = None,
        address_line1: str = None,
        address_line2: str = None,
        address_city: str = None,
        address_state: str = None,
        address_postal_code: str = None,
        address_country: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update an existing Customer."""
        data = {}
        if email:
            data["email"] = email
        if name:
            data["name"] = name
        if phone:
            data["phone"] = phone
        if description:
            data["description"] = description
        if payment_method:
            data["payment_method"] = payment_method
        if source:
            data["source"] = source
        if address_line1:
            data["address[line1]"] = address_line1
        if address_line2:
            data["address[line2]"] = address_line2
        if address_city:
            data["address[city]"] = address_city
        if address_state:
            data["address[state]"] = address_state
        if address_postal_code:
            data["address[postal_code]"] = address_postal_code
        if address_country:
            data["address[country]"] = address_country
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/customers/{customer_id}", data=data)

    @mcp.tool()
    def delete_customer(customer_id: str) -> dict:
        """Permanently delete a Customer."""
        return stripe_request("DELETE", f"/v1/customers/{customer_id}")

    @mcp.tool()
    def list_customers(
        email: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        created_gte: int = None,
        created_lte: int = None,
    ) -> dict:
        """List Customers with optional filters."""
        params = {}
        if email:
            params["email"] = email
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
        return stripe_request("GET", "/v1/customers", params=params)

    @mcp.tool()
    def list_customer_payment_methods(
        customer_id: str,
        type: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List PaymentMethods attached to a Customer."""
        params = {}
        if type:
            params["type"] = type
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return stripe_request("GET", f"/v1/customers/{customer_id}/payment_methods", params=params)
