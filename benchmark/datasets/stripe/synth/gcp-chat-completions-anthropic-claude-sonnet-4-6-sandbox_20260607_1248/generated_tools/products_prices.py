"""Tools for Stripe Products and Prices APIs."""
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


def register_product_price_tools(mcp: FastMCP):

    # ── Products ───────────────────────────────────────────────────────────

    @mcp.tool()
    def create_product(
        name: str,
        description: str = None,
        active: bool = None,
        tax_code: str = None,
        url: str = None,
        statement_descriptor: str = None,
        unit_label: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a new Product.

        Args:
            name: The product's name, meant to be displayable to the customer.
            description: Product description for display purposes.
            active: Whether the product is currently available for purchase.
            tax_code: A tax code ID for the product.
            url: A URL of a publicly-accessible webpage for this product.
            statement_descriptor: Extra information about the product for the customer's credit card statement.
            unit_label: A label that represents units of this product.
            metadata: Key-value pairs to attach.
        """
        data = {"name": name}
        if description: data["description"] = description
        if active is not None: data["active"] = str(active).lower()
        if tax_code: data["tax_code"] = tax_code
        if url: data["url"] = url
        if statement_descriptor: data["statement_descriptor"] = statement_descriptor
        if unit_label: data["unit_label"] = unit_label
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/products", data=data)

    @mcp.tool()
    def retrieve_product(product_id: str) -> dict:
        """Retrieve a Product by ID.

        Args:
            product_id: The ID of the product to retrieve.
        """
        return _req("GET", f"/v1/products/{product_id}")

    @mcp.tool()
    def update_product(
        product_id: str,
        name: str = None,
        description: str = None,
        active: bool = None,
        default_price: str = None,
        tax_code: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update an existing Product.

        Args:
            product_id: The ID of the product to update.
            name: New product name.
            description: New product description.
            active: Whether the product is available for purchase.
            default_price: ID of the default Price for this product.
            tax_code: New tax code ID.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if name: data["name"] = name
        if description: data["description"] = description
        if active is not None: data["active"] = str(active).lower()
        if default_price: data["default_price"] = default_price
        if tax_code: data["tax_code"] = tax_code
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
        if active is not None: params["active"] = str(active).lower()
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/products", params=params)

    # ── Prices ─────────────────────────────────────────────────────────────

    @mcp.tool()
    def create_price(
        currency: str,
        unit_amount: int = None,
        product: str = None,
        recurring_interval: str = None,
        recurring_interval_count: int = None,
        nickname: str = None,
        active: bool = None,
        tax_behavior: str = None,
        lookup_key: str = None,
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
            tax_behavior: 'inclusive', 'exclusive', or 'unspecified'.
            lookup_key: A lookup key for the price.
            metadata: Key-value pairs to attach.
        """
        data = {"currency": currency}
        if unit_amount is not None: data["unit_amount"] = unit_amount
        if product: data["product"] = product
        if recurring_interval:
            data["recurring[interval]"] = recurring_interval
            if recurring_interval_count is not None:
                data["recurring[interval_count]"] = recurring_interval_count
        if nickname: data["nickname"] = nickname
        if active is not None: data["active"] = str(active).lower()
        if tax_behavior: data["tax_behavior"] = tax_behavior
        if lookup_key: data["lookup_key"] = lookup_key
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/prices", data=data)

    @mcp.tool()
    def retrieve_price(price_id: str) -> dict:
        """Retrieve a Price by ID.

        Args:
            price_id: The ID of the price to retrieve.
        """
        return _req("GET", f"/v1/prices/{price_id}")

    @mcp.tool()
    def update_price(
        price_id: str,
        active: bool = None,
        nickname: str = None,
        tax_behavior: str = None,
        lookup_key: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update an existing Price.

        Args:
            price_id: The ID of the price to update.
            active: Whether the price can be used for new purchases.
            nickname: New brief description.
            tax_behavior: 'inclusive', 'exclusive', or 'unspecified'.
            lookup_key: New lookup key.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if active is not None: data["active"] = str(active).lower()
        if nickname: data["nickname"] = nickname
        if tax_behavior: data["tax_behavior"] = tax_behavior
        if lookup_key: data["lookup_key"] = lookup_key
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/prices/{price_id}", data=data)

    @mcp.tool()
    def list_prices(
        product: str = None,
        active: bool = None,
        currency: str = None,
        type: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Prices.

        Args:
            product: Filter by product ID.
            active: Filter by active status.
            currency: Filter by currency code.
            type: Filter by type: 'one_time' or 'recurring'.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if product: params["product"] = product
        if active is not None: params["active"] = str(active).lower()
        if currency: params["currency"] = currency
        if type: params["type"] = type
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/prices", params=params)
