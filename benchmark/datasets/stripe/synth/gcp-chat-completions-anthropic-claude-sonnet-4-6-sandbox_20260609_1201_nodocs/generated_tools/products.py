"""
Stripe Products tools.
Endpoints covered:
  POST   /v1/products
  GET    /v1/products/{id}
  POST   /v1/products/{id}
  DELETE /v1/products/{id}
  GET    /v1/products
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def create_product(
        name: str,
        description: str = None,
        active: bool = None,
        images: list = None,
        metadata: dict = None,
        statement_descriptor: str = None,
        unit_label: str = None,
        url: str = None,
    ) -> dict:
        """Create a new Product."""
        data = {"name": name}
        if description:
            data["description"] = description
        if active is not None:
            data["active"] = str(active).lower()
        if images:
            for i, img in enumerate(images):
                data[f"images[{i}]"] = img
        if statement_descriptor:
            data["statement_descriptor"] = statement_descriptor
        if unit_label:
            data["unit_label"] = unit_label
        if url:
            data["url"] = url
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/products", data=data)

    @mcp.tool()
    def get_product(product_id: str) -> dict:
        """Retrieve a Product by ID."""
        return stripe_request("GET", f"/v1/products/{product_id}")

    @mcp.tool()
    def update_product(
        product_id: str,
        name: str = None,
        description: str = None,
        active: bool = None,
        images: list = None,
        metadata: dict = None,
        statement_descriptor: str = None,
        unit_label: str = None,
        url: str = None,
    ) -> dict:
        """Update an existing Product."""
        data = {}
        if name:
            data["name"] = name
        if description:
            data["description"] = description
        if active is not None:
            data["active"] = str(active).lower()
        if images:
            for i, img in enumerate(images):
                data[f"images[{i}]"] = img
        if statement_descriptor:
            data["statement_descriptor"] = statement_descriptor
        if unit_label:
            data["unit_label"] = unit_label
        if url:
            data["url"] = url
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/products/{product_id}", data=data)

    @mcp.tool()
    def delete_product(product_id: str) -> dict:
        """Delete a Product by ID."""
        return stripe_request("DELETE", f"/v1/products/{product_id}")

    @mcp.tool()
    def list_products(
        active: bool = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        created_gte: int = None,
        created_lte: int = None,
    ) -> dict:
        """List Products with optional filters."""
        params = {}
        if active is not None:
            params["active"] = str(active).lower()
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
        return stripe_request("GET", "/v1/products", params=params)
