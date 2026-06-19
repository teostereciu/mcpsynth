"""Tools for Stripe Products and Prices API."""
import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.stripe.com"

def _get_headers():
    api_key = os.environ.get("STRIPE_API_KEY", "")
    return {"Authorization": f"Bearer {api_key}"}

def _req(method, path, **kwargs):
    try:
        resp = requests.request(method, f"{BASE_URL}{path}", headers=_get_headers(), **kwargs)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def register_product_price_tools(mcp: FastMCP):

    # ---- Products ----

    @mcp.tool()
    def create_product(
        name: str,
        active: bool = None,
        description: str = None,
        metadata: dict = None,
        tax_code: str = None,
    ) -> dict:
        """Create a new Product.

        Args:
            name: The product's name (displayable to customers).
            active: Whether the product is available for purchase. Defaults to True.
            description: Long-form description of the product.
            metadata: Key-value pairs to attach to the object.
            tax_code: A tax code ID for the product.
        """
        data = {"name": name}
        if active is not None:
            data["active"] = str(active).lower()
        if description:
            data["description"] = description
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        if tax_code:
            data["tax_code"] = tax_code
        return _req("POST", "/v1/products", data=data)

    @mcp.tool()
    def retrieve_product(product_id: str) -> dict:
        """Retrieve a Product by ID.

        Args:
            product_id: The ID of the product (e.g. 'prod_...').
        """
        return _req("GET", f"/v1/products/{product_id}")

    @mcp.tool()
    def update_product(
        product_id: str,
        name: str = None,
        active: bool = None,
        description: str = None,
        default_price: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update an existing Product.

        Args:
            product_id: The ID of the product to update.
            name: The product's name.
            active: Whether the product is available for purchase.
            description: Long-form description of the product.
            default_price: ID of the default Price for this product.
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if name:
            data["name"] = name
        if active is not None:
            data["active"] = str(active).lower()
        if description:
            data["description"] = description
        if default_price:
            data["default_price"] = default_price
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/products/{product_id}", data=data)

    @mcp.tool()
    def delete_product(product_id: str) -> dict:
        """Delete a Product.

        Args:
            product_id: The ID of the product to delete.
        """
        return _req("DELETE", f"/v1/products/{product_id}")

    @mcp.tool()
    def list_products(
        active: bool = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Products.

        Args:
            active: Filter by active status.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if active is not None:
            params["active"] = str(active).lower()
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return _req("GET", "/v1/products", params=params)

    # ---- Prices ----

    @mcp.tool()
    def create_price(
        currency: str,
        unit_amount: int = None,
        product: str = None,
        recurring_interval: str = None,
        recurring_interval_count: int = None,
        nickname: str = None,
        active: bool = None,
        metadata: dict = None,
    ) -> dict:
        """Create a new Price for a Product.

        Args:
            currency: Three-letter ISO currency code (e.g. 'usd').
            unit_amount: Amount in smallest currency unit (e.g. cents).
            product: ID of the product this price belongs to.
            recurring_interval: Billing interval: 'day', 'week', 'month', or 'year'.
            recurring_interval_count: Number of intervals between billings.
            nickname: Brief description of the price (hidden from customers).
            active: Whether the price can be used for new purchases.
            metadata: Key-value pairs to attach to the object.
        """
        data = {"currency": currency}
        if unit_amount is not None:
            data["unit_amount"] = unit_amount
        if product:
            data["product"] = product
        if recurring_interval:
            data["recurring[interval]"] = recurring_interval
        if recurring_interval_count is not None:
            data["recurring[interval_count]"] = recurring_interval_count
        if nickname:
            data["nickname"] = nickname
        if active is not None:
            data["active"] = str(active).lower()
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/prices", data=data)

    @mcp.tool()
    def retrieve_price(price_id: str) -> dict:
        """Retrieve a Price by ID.

        Args:
            price_id: The ID of the price (e.g. 'price_...').
        """
        return _req("GET", f"/v1/prices/{price_id}")

    @mcp.tool()
    def update_price(
        price_id: str,
        active: bool = None,
        nickname: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update an existing Price.

        Args:
            price_id: The ID of the price to update.
            active: Whether the price can be used for new purchases.
            nickname: Brief description of the price.
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if active is not None:
            data["active"] = str(active).lower()
        if nickname:
            data["nickname"] = nickname
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/prices/{price_id}", data=data)

    @mcp.tool()
    def list_prices(
        product: str = None,
        active: bool = None,
        type: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Prices.

        Args:
            product: Filter by product ID.
            active: Filter by active status.
            type: Filter by type: 'one_time' or 'recurring'.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if product:
            params["product"] = product
        if active is not None:
            params["active"] = str(active).lower()
        if type:
            params["type"] = type
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return _req("GET", "/v1/prices", params=params)
