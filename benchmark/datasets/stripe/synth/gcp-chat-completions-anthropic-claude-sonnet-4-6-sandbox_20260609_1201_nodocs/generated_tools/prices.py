"""
Stripe Prices tools.
Endpoints covered:
  POST   /v1/prices
  GET    /v1/prices/{id}
  POST   /v1/prices/{id}
  GET    /v1/prices
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def create_price(
        currency: str,
        product: str = None,
        product_data_name: str = None,
        unit_amount: int = None,
        unit_amount_decimal: str = None,
        recurring_interval: str = None,
        recurring_interval_count: int = None,
        recurring_usage_type: str = None,
        billing_scheme: str = None,
        nickname: str = None,
        active: bool = None,
        metadata: dict = None,
        tax_behavior: str = None,
        lookup_key: str = None,
        transfer_lookup_key: bool = None,
    ) -> dict:
        """
        Create a Price for a Product.
        recurring_interval: day | week | month | year
        billing_scheme: per_unit | tiered
        tax_behavior: exclusive | inclusive | unspecified
        """
        data = {"currency": currency}
        if product:
            data["product"] = product
        if product_data_name:
            data["product_data[name]"] = product_data_name
        if unit_amount is not None:
            data["unit_amount"] = unit_amount
        if unit_amount_decimal:
            data["unit_amount_decimal"] = unit_amount_decimal
        if recurring_interval:
            data["recurring[interval]"] = recurring_interval
        if recurring_interval_count is not None:
            data["recurring[interval_count]"] = recurring_interval_count
        if recurring_usage_type:
            data["recurring[usage_type]"] = recurring_usage_type
        if billing_scheme:
            data["billing_scheme"] = billing_scheme
        if nickname:
            data["nickname"] = nickname
        if active is not None:
            data["active"] = str(active).lower()
        if tax_behavior:
            data["tax_behavior"] = tax_behavior
        if lookup_key:
            data["lookup_key"] = lookup_key
        if transfer_lookup_key is not None:
            data["transfer_lookup_key"] = str(transfer_lookup_key).lower()
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/prices", data=data)

    @mcp.tool()
    def get_price(price_id: str) -> dict:
        """Retrieve a Price by ID."""
        return stripe_request("GET", f"/v1/prices/{price_id}")

    @mcp.tool()
    def update_price(
        price_id: str,
        active: bool = None,
        nickname: str = None,
        metadata: dict = None,
        tax_behavior: str = None,
        lookup_key: str = None,
        transfer_lookup_key: bool = None,
    ) -> dict:
        """Update a Price (only mutable fields: active, nickname, metadata, etc.)."""
        data = {}
        if active is not None:
            data["active"] = str(active).lower()
        if nickname:
            data["nickname"] = nickname
        if tax_behavior:
            data["tax_behavior"] = tax_behavior
        if lookup_key:
            data["lookup_key"] = lookup_key
        if transfer_lookup_key is not None:
            data["transfer_lookup_key"] = str(transfer_lookup_key).lower()
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/prices/{price_id}", data=data)

    @mcp.tool()
    def list_prices(
        product: str = None,
        active: bool = None,
        currency: str = None,
        type: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        lookup_keys: list = None,
    ) -> dict:
        """List Prices with optional filters. type: one_time | recurring"""
        params = {}
        if product:
            params["product"] = product
        if active is not None:
            params["active"] = str(active).lower()
        if currency:
            params["currency"] = currency
        if type:
            params["type"] = type
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        if lookup_keys:
            for i, lk in enumerate(lookup_keys):
                params[f"lookup_keys[{i}]"] = lk
        return stripe_request("GET", "/v1/prices", params=params)
